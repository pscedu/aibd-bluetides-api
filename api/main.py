# command: uvicorn main:app --reload
# main: the file main.py (the Python "module").
# app: the object created inside of main.py with the line app = FastAPI().
# --reload: make the server restart after code changes. Only do this for development.

import json
import os
from json import JSONEncoder

import bigfile
import numpy
from fastapi import FastAPI
from fastapi import HTTPException

# Init
app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "COSMO, a REST API for the BlueTides3 Cosmology Simulation Data"}


# Json serializer
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


# Route
# Get the first n lengthByType data in a particular pig folder.
@app.get("/pig/{id}/lengthbytype/n={num}")
async def read_lbt_file(id: int, num: int):
    # Data
    check_pig_id(id)
    pig = get_pig_data(id)
    check_halo_id_range(pig, num - 1)
    nhalo = num  # only read from the first n halos

    # lbt: number of particles in each Fof halo
    # Read data from the first n halos
    lbt = pig.open('FOFGroups/LengthByType')[:nhalo]

    # serialize lbt numpy array into json
    numpyArrayData = numpy.array(lbt)
    encodedNumpyData = json.dumps(numpyArrayData, cls=NumpyArrayEncoder)
    return {"length_by_type": encodedNumpyData}


# Get the number of all gas type particles in the nth halo of a particular pig folder
@app.get("/pig/{id}/lengthbytype/{halo_id}/")
async def read_lbh(id: int, halo_id: int):
    check_pig_id(id)
    pig = get_pig_data(id)
    check_halo_id_range(pig, halo_id)
    nhalo = pig.open('FOFGroups/LengthByType')[halo_id]
    numpyArrayTypeData = numpy.array(nhalo)
    encodedNumpyTypeData = json.dumps(numpyArrayTypeData, cls=NumpyArrayEncoder)
    return {"halo_id": halo_id, "type_length": encodedNumpyTypeData}


# Get the number of a specific gas type particles in the nth halo of a particular pig folder
@app.get("/pig/{id}/lengthbytype/{halo_id}/{type_id}")
async def read_lbht(id: int, halo_id: int, type_id: int):
    check_pig_id(id)
    pig = get_pig_data(id)
    check_halo_id_range(pig, halo_id)
    check_type_id_range(type_id)
    nhalo = pig.open('FOFGroups/LengthByType')[halo_id]
    length = nhalo[type_id]
    numpyArrayLenData = numpy.array(length)
    encodedNumpyLenData = json.dumps(numpyArrayLenData, cls=NumpyArrayEncoder)
    return {"halo_id": halo_id, "type_id": type_id, "length": encodedNumpyLenData}


# Get the beginning and the ending index of a particular group and pig folder.
@app.get("/pig/{id}/offsetbytype/{halo_id}/")
async def read_obh(id: int, halo_id: int):
    check_pig_id(id)
    pig = get_pig_data(id)
    check_halo_id_range(pig, halo_id)
    lbt = pig.open('FOFGroups/LengthByType')[:halo_id + 1]
    obt = numpy.cumsum(lbt, axis=0).astype(int)
    if halo_id == 0:
        begin = [0] * 6
    else:
        begin = obt[halo_id - 1]
    end = obt[halo_id]
    numpyArrayBeginData = numpy.array(begin)
    encodedNumpyBeginData = json.dumps(numpyArrayBeginData, cls=NumpyArrayEncoder)
    numpyArrayEndData = numpy.array(end)
    encodedNumpyEndData = json.dumps(numpyArrayEndData, cls=NumpyArrayEncoder)
    return {"halo_id": halo_id, "beginning_index": encodedNumpyBeginData, "ending_index": encodedNumpyEndData}


# Get the list of PIG folders available for querying
@app.get("/pig/")
async def read_pig():
    pig_list = []
    subdirectories = get_pig_folders()
    for subdir in subdirectories:
        pig_dict = {}
        pig_id = subdir.replace("PIG_", "")
        pig_dict["id"] = pig_id
        pig_dict["name"] = subdir
        pig_dict["num_halos"] = int(get_pig_numhalo(subdir))
        pig_dict["time"] = float(get_pig_redshift(subdir))
        pig_list.append(pig_dict)
    return {"LIST": pig_list}


# Get the position of each particle in a particular group and pig folder
@app.get("/pig/{id}/gas/position/{group_id}")
async def read_gas_position(id: int, group_id: int):
    position = get_gas_data(id, group_id, "Position")
    return {"gas_position": position}


# Get the number of free electrons at the particle position in a particular group and pig folder
@app.get("/pig/{id}/gas/electron/{group_id}")
async def read_gas_electron(id: int, group_id: int):
    electron = get_gas_data(id, group_id, "ElectronAbundance")
    return {"gas_electron_abundance": electron}


# Get the fraction of hydrogen molecules in a particular group and pig folder
@app.get("/pig/{id}/gas/h2fraction/{group_id}")
async def read_gas_h2fraction(id: int, group_id: int):
    h2fraction = get_gas_data(id, group_id, "H2Fraction")
    return {"gas_h2fraction": h2fraction}


# Get the fraction of hydrogen molecules in a particular group and pig folder
@app.get("/pig/{id}/gas/internalenergy/{group_id}")
async def read_gas_internal_energy(id: int, group_id: int):
    internal_energy = get_gas_data(id, group_id, "InternalEnergy")
    return {"gas_internal_energy": internal_energy}


# Get the list of PIG folders
def get_pig_folders():
    path = '/pylon5/as5pi3p/yueying/BT3/'
    subdirectories = []
    directory_contents = os.listdir(path)
    for item in directory_contents:
        if item.startswith("PIG_"):
            subdirectories.append(item)
    return subdirectories


def get_pig_numhalo(sub_dir: str):
    path = '/pylon5/as5pi3p/yueying/BT3/'
    pig_dir = path + sub_dir + '/'
    pig = bigfile.File(pig_dir)
    Nhalo = pig['Header'].attrs['NumFOFGroupsTotal'][0]
    return Nhalo


def get_pig_redshift(sub_dir: str):
    path = '/pylon5/as5pi3p/yueying/BT3/'
    pig_dir = path + sub_dir + '/'
    pig = bigfile.File(pig_dir)
    scalefactor = pig['Header'].attrs['Time'][0]
    redshift = 1. / scalefactor - 1.
    return redshift


# Get a particular pig folder data in bigfile format
def get_pig_data(id: int):
    # data directory
    pig_base_dir = '/pylon5/as5pi3p/yueying/BT3/'
    pig_dir = pig_base_dir + "PIG_" + str(id) + "/"
    pig = bigfile.File(pig_dir)
    return pig


def get_obt(id: int, group_id: int):
    check_pig_id(id)
    pig = get_pig_data(id)
    check_group_id_range(pig, group_id)
    lbt = pig.open('FOFGroups/LengthByType')[:group_id]
    obt = numpy.cumsum(lbt, axis=0).astype(int)
    return obt


def get_gas_data(id: int, group_id: int, feature: str):
    check_pig_id(id)
    pig = get_pig_data(id)
    check_group_id_range(pig, group_id)
    lbt = pig.open('FOFGroups/LengthByType')[:group_id]
    obt = numpy.cumsum(lbt, axis=0).astype(int)
    obt = get_obt(id, group_id)
    path = '0/' + feature
    if group_id == 1:
        gas_data = pig.open(path)[:obt[0][0]]
    else:
        gas_data = pig.open(path)[obt[-2][0]:obt[-1][0]]
    numpyArrayGasData = numpy.array(gas_data)
    encodedNumpyGasData = json.dumps(numpyArrayGasData, cls=NumpyArrayEncoder)
    return encodedNumpyGasData


def check_halo_id_range(pig, halo_id: int):
    total_halo = pig.open('FOFGroups/LengthByType').size
    if halo_id < 0 or halo_id >= total_halo:
        raise HTTPException(status_code=400, detail="halo_id out of range, should be [0,{})".format(total_halo))


def check_group_id_range(pig, group_id: int):
    total_group = pig.open('FOFGroups/LengthByType').size
    if group_id <= 0 or group_id > total_group:
        raise HTTPException(status_code=400, detail="group_id out of range, should be [1,{}]".format(total_group))


def check_type_id_range(type_id: int):
    if type_id < 0 or type_id >= 6:
        raise HTTPException(status_code=400, detail="type_id out of range, should be [0,6)")


def check_pig_id(pig_id: int):
    subdirectories = get_pig_folders()
    pig_folder = "PIG_" + str(pig_id)
    if pig_folder not in subdirectories:
        raise HTTPException(status_code=404, detail="PIG folder does not exist, should in {}".format(subdirectories))
