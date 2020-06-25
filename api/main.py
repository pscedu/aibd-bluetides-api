# command: uvicorn main:app --reload
# main: the file main.py (the Python "module").
# app: the object created inside of main.py with the line app = FastAPI().
# --reload: make the server restart after code changes. Only do this for development.

import json
from json import JSONEncoder

import numpy
from bigfile import BigFile
from fastapi import FastAPI, HTTPException

# Init
app = FastAPI()


# Json serializer
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


# Data Directory
pig_dir = '/pylon5/as5pi3p/yueying/BT3/PIG_251/'
pig = BigFile(pig_dir)


# Route
# Get the first n lengthByType data
@app.get("/lengthbytype/n={num}")
async def read_lbt_file(num: int):
    # Data
    nhalo = num #only read from the first n halos

    # lbt: number of particles in each Fof halo
    # Read data from the first n halos
    lbt = pig.open('FOFGroups/LengthByType')[:nhalo]

    # serialize lbt numpy array into json
    numpyArrayData = numpy.array(lbt)
    encodedNumpyData = json.dumps(numpyArrayData, cls=NumpyArrayEncoder)
    return {"length_by_type": encodedNumpyData}


# Get the number of all gas type particles in the nth halo
@app.get("/lengthbytype/{halo_id}/")
async def read_lbh(halo_id: int):
    nhalo = pig.open('FOFGroups/LengthByType')[halo_id]
    numpyArrayTypeData = numpy.array(nhalo)
    encodedNumpyTypeData = json.dumps(numpyArrayTypeData, cls=NumpyArrayEncoder)
    return {"halo_id": halo_id, "type_length": encodedNumpyTypeData}

