# command: uvicorn main:app --reload
# main: the file main.py (the Python "module").
# app: the object created inside of main.py with the line app = FastAPI().
# --reload: make the server restart after code changes. Only do this for development.

import json

import numpy
from typing import List
from fastapi import FastAPI, Query, HTTPException

import utils

# Init
app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "COSMO, a REST API for the BlueTides3 Cosmology Simulation Data"}

# Get the list of PIG folders available for querying
@app.get("/pig/")
async def read_pig():
    pig_list = []
    subdirectories = utils.get_pig_folders()
    for subdir in subdirectories:
        pig_dict = {}
        pig_id = subdir.replace("PIG_", "")
        pig_dict["id"] = pig_id
        pig_dict["name"] = subdir
        pig_dict["num_halos"] = int(utils.get_pig_numhalo(subdir))
        pig_dict["time"] = float(utils.get_pig_redshift(subdir))
        pig_list.append(pig_dict)
    return {"LIST": pig_list}



@app.get("/pig/{id}")
async def read_snapshot_info(id: int):
    utils.check_pig_id(pig_id=id)
    pig = utils.get_pig_data(id)
    total_part = pig['Header'].attrs['NumPartInGroupTotal']
    num_part = numpy.array(total_part)
    return {'subdirs':['fofgroup','gas','dm','star','bh'],\
            'num_gas':num_part[0],'num_dm':num_part[1],\
            'num_star':num_part[4],'num_bh':num_part[5]}


@app.get("/pig/{id}/{ptype}")
async def read_snapshot_type_info(id: int, ptype: str):
    subfields = utils.get_part_subfield(pig_id = id,ptype = ptype)
    return {'type':ptype, 'subdirs':subfields}


@app.get("/pig/{id}/fofgroup")
async def read_snapshot_fof_info(id: int, ptype: str):
    subfields = utils.get_fof_subfield(pig_id = id)
    return {'fof_subdirs':subfields}    



# Route
# Get the first n lengthByType data in a particular pig folder.
@app.get("/pig/{id}/lengthbytype/n={num}")
async def read_lbt_file(id: int, num: int):
    # Data
    utils.check_pig_id(pig_id=id)
    pig = utils.get_pig_data(id)
    utils.check_halo_id_range(pig=pig, halo_id=num - 1)
    nhalo = num  # only read from the first n halos

    # lbt: number of particles in each Fof halo
    # Read data from the first n halos
    lbt = pig.open('FOFGroups/LengthByType')[:nhalo]

    # serialize lbt numpy array into json
    numpy_array_data = numpy.array(lbt)
    encoded_numpy_data = json.dumps(numpy_array_data, cls=utils.NumpyArrayEncoder)
    return {"length_by_type": encoded_numpy_data}


# Get the number of all gas type particles in the nth halo of a particular pig folder
@app.get("/pig/{id}/lengthbytype/{halo_id}/")
async def read_lbh(id: int, halo_id: int):
    utils.check_pig_id(pig_id=id)
    pig = utils.get_pig_data(id)
    utils.check_halo_id_range(pig=pig, halo_id=halo_id)
    nhalo = pig.open('FOFGroups/LengthByType')[halo_id]
    numpy_array_type_data = numpy.array(nhalo)
    encoded_numpy_type_data = json.dumps(numpy_array_type_data, cls=utils.NumpyArrayEncoder)
    return {"halo_id": halo_id, "type_length": encoded_numpy_type_data}


# Get the number of a specific gas type particles in the nth halo of a particular pig folder
@app.get("/pig/{id}/lengthbytype/{halo_id}/{type_id}")
async def read_lbht(id: int, halo_id: int, type_id: int):
    utils.check_pig_id(pig_id=id)
    pig = utils.get_pig_data(id)
    utils.check_halo_id_range(pig=pig, halo_id=halo_id)
    utils.check_type_id_range(type_id=type_id)
    nhalo = pig.open('FOFGroups/LengthByType')[halo_id]
    length = nhalo[type_id]
    numpy_array_len_data = numpy.array(length)
    encoded_numpy_len_data = json.dumps(numpy_array_len_data, cls=utils.NumpyArrayEncoder)
    return {"halo_id": halo_id, "type_id": type_id, "length": encoded_numpy_len_data}


# Get the beginning and the ending index of a particular group and pig folder.
@app.get("/pig/{id}/offsetbytype/{halo_id}/")
async def read_obh(id: int, halo_id: int):
    utils.check_pig_id(pig_id=id)
    pig = utils.get_pig_data(id)
    utils.check_halo_id_range(pig=pig, halo_id=halo_id)
    lbt = pig.open('FOFGroups/LengthByType')[:halo_id + 1]
    obt = numpy.cumsum(lbt, axis=0).astype(int)
    if halo_id == 0:
        begin = [0] * 6
    else:
        begin = obt[halo_id - 1]
    end = obt[halo_id]
    numpy_array_begin_data = numpy.array(begin)
    encoded_numpy_begin_data = json.dumps(numpy_array_begin_data, cls=utils.NumpyArrayEncoder)
    numpy_array_end_data = numpy.array(end)
    encoded_numpy_end_data = json.dumps(numpy_array_end_data, cls=utils.NumpyArrayEncoder)
    return {"halo_id": halo_id, "beginning_index": encoded_numpy_begin_data, "ending_index": encoded_numpy_end_data}


###################################################################
#                        FoF Group Queries                        #
###################################################################
# Regular query for particle data in a Group={group_id} of type={ptype}
@app.get("/pig/{id}/fofgroup/{feature}/{group_id}")
async def read_fofgroup_data(id: int, group_id: int, feature: str):
    data = utils.get_fofgroup_data(pig_id=id, group_id=group_id, feature=feature)
    return {('fofgroup'+'_'+feature.lower()): data}


###################################################################
#                        Particle Queries                         #
###################################################################
# Regular query for particle data in a Group={group_id} of type={ptype}
@app.get("/pig/{id}/{ptype}/{feature}/{group_id}")
async def read_particle_data_by_groupid(id: int, group_id: int,ptype: str, feature:str):
    data = utils.get_particle_data(pig_id=id, group_id=group_id, ptype = ptype, feature=feature)
    return {(ptype+'_'+feature.lower()): data}

@app.get("/pig/{id}/{ptype}/{feature}/")
async def read_particle_data_by_groupid_list(id: int, ptype: str, feature: str, groupid_list: List[int] = Query(None)):
    data = {}
    if groupid_list is None:
        raise HTTPException(status_code=404, detail="GroupID is needed. Please input a valid one.")
    for group_id in groupid_list:
        data[group_id] = utils.get_particle_data(pig_id=id, group_id=group_id, ptype = ptype, feature=feature)
    return {(ptype+'_'+feature.lower()): data}

###################################################################
#                     Search by Criterion Queries                 #
###################################################################



