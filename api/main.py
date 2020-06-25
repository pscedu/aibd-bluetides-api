#command: uvicorn main:app --reload
# main: the file main.py (the Python "module").
# app: the object created inside of main.py with the line app = FastAPI().
# --reload: make the server restart after code changes. Only do this for development.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bigfile import BigFile
import glob,os,struct
import json
from json import JSONEncoder
import numpy

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

# Get the number of a specific gas type particles in the nth halo
@app.get("/lengthbytype/{halo_id}/{type_id}")
async def read_lbht(halo_id: int, type_id: int):
    total_halo = pig.open('FOFGroups/LengthByType').size
    if halo_id < 0 or halo_id >= total_halo:
        raise HTTPException(status_code=400, detail="halo_id out of range, should be [0,{})".format(total_halo))
    if type_id < 0 or type_id >= 6:
        raise HTTPException(status_code=400, detail="type_id out of range, should be [0,6)")
    nhalo = pig.open('FOFGroups/LengthByType')[halo_id]
    length = nhalo[type_id]
    numpyArrayLenData = numpy.array(length)
    encodedNumpyLenData = json.dumps(numpyArrayLenData, cls=NumpyArrayEncoder)
    return {"halo_id": halo_id, "type_id": type_id, "length": encodedNumpyLenData}