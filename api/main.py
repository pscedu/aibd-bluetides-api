# command: uvicorn main:app --reload
# main: the file main.py (the Python "module").
# app: the object created inside of main.py with the line app = FastAPI().
# --reload: make the server restart after code changes. Only do this for development.

import json

import numpy
from typing import List, Optional
from fastapi import FastAPI, Query, Path, Body, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

import utils
import constants


# Init
app = FastAPI(
    title="COSMO",
    description="A REST API for the BlueTides3 Cosmology Simulation Data. You can find out more about COSMO at [{}]({}).".format(constants.WEB_URL,constants.WEB_URL),
    openapi_tags=constants.tags_metadata,
    )


class Snapshot(BaseModel):
    id: int
    subdirs: list
    num_gas: int
    num_dm: int
    num_star: int
    num_bh: int


class SnapshotFoFGroup(BaseModel):
    id: int
    fof_subdirs: list


class SnapshotParticle(BaseModel):
    id: int
    ptype: str
    subdirs: list

class LengthbytypeN(BaseModel):
    id: int
    num: int
    length_by_type: list

class LengthbytypeHaloID(BaseModel):
    id: int
    halo_id: int
    type_length: list

# class LengthbytypeHaloList(BaseModel):
#     id: int

class LengthbytypeHaloIDTypeID(BaseModel):
    id: int
    halo_id: int
    type_id: int
    length: int

class Offsetbytype(BaseModel):
    id: int
    halo_id: int
    beginning_index: list
    ending_index: list

@app.get("/")
async def read_main():
    return {"msg": "COSMO, a REST API for the BlueTides3 Cosmology Simulation Data"}


@app.get(
    "/pig/",
    tags=["pig"],
    responses={
            200: constants.response_200["read_pig"],
        },
    )
async def read_pig():
    """
    Get the list of PIG folders available for querying along with their halo numbers and redshifts.
    """
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


@app.get("/pig/{id}",
    tags=["pig"],
    response_model=Snapshot,
    responses={
        404: constants.response_404["read_snapshot_info"],
        200: constants.response_200["read_snapshot_info"],
        },
    )
async def read_snapshot_info(id: int= Path(..., description="ID of a PIG folder")):
    """
    Get the snapshot info of a PIG folder with all the information:

    - **id**: ID of a PIG folder. It should be in [208, 230, 237, 216, 265, 244, 271, 258, 222, 251, 184, 197].
    """
    utils.check_pig_id(pig_id=id)
    pig = utils.get_pig_data(id)
    total_part = pig['Header'].attrs['NumPartInGroupTotal']
    num_part = numpy.array(total_part)
    return {'id': id,
            'subdirs': ['fofgroup', 'gas', 'dm', 'star', 'bh'],
            'num_gas': json.dumps(num_part[0], cls=utils.NumpyArrayEncoder),
            'num_dm': json.dumps(num_part[1], cls=utils.NumpyArrayEncoder),
            'num_star': json.dumps(num_part[4], cls=utils.NumpyArrayEncoder),
            'num_bh': json.dumps(num_part[5], cls=utils.NumpyArrayEncoder)}


@app.get(
    "/pig/{id}/fofgroup", 
    tags=["pig"],
    response_model=SnapshotFoFGroup,
    responses={
        404: constants.response_404["read_snapshot_info"],
        200: constants.response_200["read_snapshot_fof_info"],
        },)
async def read_snapshot_fof_info(id: int = Path(..., description="ID of a PIG folder")):
    """
    Get the FoFGroup info of a PIG folder with all the information:

    - **id**: ID of a PIG folder. It should be in [208, 230, 237, 216, 265, 244, 271, 258, 222, 251, 184, 197].
    """
    subfields = utils.get_fof_subfield(pig_id=id)
    return {'id':id, 'fof_subdirs': subfields}


@app.get(
    "/pig/{id}/{ptype}", 
    tags=["pig"],
    response_model=SnapshotParticle,
    responses={
        404: constants.response_404["read_snapshot_type_info"],
        200: constants.response_200["read_snapshot_type_info"]
        },)
async def read_snapshot_type_info(id: int = Path(..., description="ID of a PIG folder"), ptype: str = Path(..., description="Particle type")):
    """
    Get the particle feature info of a PIG folder with all the information:

    - **id**: ID of a PIG folder. It should be in [208, 230, 237, 216, 265, 244, 271, 258, 222, 251, 184, 197].
    - **ptype**: Type of particle. It should be in ['gas', 'dm', 'star', 'bh'].
    """
    subfields = utils.get_part_subfield(pig_id=id, ptype=ptype)
    return {'id': id, 'ptype': ptype, 'subdirs': subfields}


# Route
# Get the first n lengthByType data in a particular PIG folder.
@app.get(
    "/pig/{id}/lengthbytype/n={num}", 
    tags=["lengthbytype"],
    response_model=LengthbytypeN,
    responses={
    404: constants.response_404["read_lbt_file"],
    200: constants.response_200["read_lbt_file"]
    },)
async def read_lbt_file(id: int = Path(..., description="ID of a PIG folder"), num: int = Path(..., description="Number of halos")):
    """
    Get the length info of the first n halos in a PIG folder with all the information:

    - **id**: ID of a PIG folder. It should be in [208, 230, 237, 216, 265, 244, 271, 258, 222, 251, 184, 197].
    - **num**: Number of halos. It should be between 1 to the max halo size.
    """
    # Data
    utils.check_pig_id(pig_id=id)
    pig = utils.get_pig_data(id)
    utils.check_group_id_range(pig=pig, group_id=num)
    nhalo = num  # only read from the first n halos

    # lbt: number of particles in each Fof halo
    # Read data from the first n halos
    lbt = pig.open('FOFGroups/LengthByType')[:nhalo]

    # serialize lbt numpy array into json
    numpy_array_data = numpy.array(lbt)
    # encoded_numpy_data = json.dumps(numpy_array_data, cls=utils.NumpyArrayEncoder)
    return {"id": id, "num": num, "length_by_type": numpy_array_data.tolist()}


# Get the number of all gas type particles in the nth halo of a particular PIG folder
@app.get(
    "/pig/{id}/lengthbytype/{halo_id}/", 
    tags=["lengthbytype"],
    response_model=LengthbytypeHaloID,
    responses={
    404: constants.response_404["read_lbt_by_haloid"],
    200: constants.response_200["read_lbt_by_haloid"]
    },)
async def read_lbt_by_haloid(id: int = Path(..., description="ID of a PIG folder"), halo_id: int = Path(..., description="ID of a halo")):
    """
    Get the number of all type particles for the nth halo in a PIG folder with all the information:

    - **id**: ID of a PIG folder. It should be in [208, 230, 237, 216, 265, 244, 271, 258, 222, 251, 184, 197].
    - **halo_id**: ID of a halo. ID of a halo. It should be between 0 to the max halo ID.
    """
    data = utils.get_lbt_by_haloid(pig_id=id, halo_id=halo_id)
    return {"id": id, "halo_id": halo_id, "type_length": data}


# Get the number of all type particles in a halo list of a particular PIG folder
@app.get(
    "/pig/{id}/lengthbytype/", 
    tags=["lengthbytype"],
    responses={
    404: constants.response_404["read_lbt_by_haloid_list"],
    # 200: constants.response_200["read_lbt_by_haloid_list"]
    },)
async def read_lbt_by_haloid_list(id: int = Path(..., description="ID of a PIG folder"), haloid_list: List[int] = Query(None, description="A list of group IDs")):
    """
    Get the number of all type particles for a halo list in a PIG folder with all the information:

    - **id**: ID of a PIG folder. It should be in [208, 230, 237, 216, 265, 244, 271, 258, 222, 251, 184, 197].
    - **haloid_list**: A list of group IDs. It should be a list and be passed as a query parameter.
    """
    data = {} 
    utils.check_query_list(haloid_list)
    for halo_id in haloid_list:
        data[halo_id] = utils.get_lbt_by_haloid(pig_id=id, halo_id=halo_id)
    return data


# Get the number of a specific type particles in the nth halo of a particular PIG folder
@app.get(
    "/pig/{id}/lengthbytype/{halo_id}/{type_id}", 
    tags=["lengthbytype"],
    responses={
    404: constants.response_404["read_lbht"],
    # 200: constants.response_200["read_lbht"]
    },)
async def read_lbht(id: int = Path(..., description="ID of a PIG folder"), halo_id: int = Path(..., description="ID of a halo"), type_id: int = Path(..., description="ID of a particle type")):
    """
    Get the number of a specific type particles for the nth halo in a PIG folder with all the information:

    - **id**: ID of a PIG folder. It should be in [208, 230, 237, 216, 265, 244, 271, 258, 222, 251, 184, 197].
    - **haloid_list**: A list of group IDs. It should be a list and be passed as a query parameter.
    """
    utils.check_pig_id(pig_id=id)
    pig = utils.get_pig_data(id)
    utils.check_halo_id_range(pig=pig, halo_id=halo_id)
    utils.check_type_id_range(type_id=type_id)
    nhalo = pig.open('FOFGroups/LengthByType')[halo_id]
    length = nhalo[type_id]
    numpy_array_len_data = numpy.array(length)
    encoded_numpy_len_data = json.dumps(numpy_array_len_data, cls=utils.NumpyArrayEncoder)
    return {"halo_id": halo_id, "type_id": type_id, "length": encoded_numpy_len_data}


# Get the beginning and the ending index of a particular group and PIG folder.
@app.get(
    "/pig/{id}/offsetbytype/{halo_id}/", 
    tags=["lengthbytype"],
    responses={
    404: constants.response_404["read_obh"],
    # 200: constants.response_200["read_obh"]
    },)
async def read_obh(id: int = Path(..., description="ID of a PIG folder"), halo_id: int = Path(..., description="ID of a halo")):
    """
    Get the beginning and the ending index of the nth halo group in a PIG folder with all the information:

    - **id**: ID of a PIG folder. It should be in [208, 230, 237, 216, 265, 244, 271, 258, 222, 251, 184, 197].
    - **halo_id**: ID of a halo. It should be between 0 to the max halo ID.
    """
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
#                     Search by Criterion Queries                 #
###################################################################
@app.get(
    "/pig/{id}/search_id/{ptype}/{feature}", 
    tags=["advanced"],
    responses={
    404: constants.response_404["read_haloid_by_criterion"],
    # 200: constants.response_200["read_haloid_by_criterion"]
    },)
async def read_haloid_by_criterion(id: int = Path(..., description="ID of a PIG folder"), feature: str = Path(..., description="Feature of FoFGroup"), 
    ptype: str = Path(..., description="Name of particle type"), min_range: Optional[float] = Query(None, description="Min range of a searching criterion"), 
    max_range: Optional[float] = Query(None, description="Min range of a searching criterion")):
    utils.check_pig_id(pig_id=id)
    """
    Get all halo IDs of particles matching some searching criterion in a PIG folder with all the information:

    - **id**: ID of a PIG folder. It should be in [208, 230, 237, 216, 265, 244, 271, 258, 222, 251, 184, 197].
    - **ptype**: Name of pariticle type. It should be in ['gas', 'dm', 'star', 'bh'].
    - **feature**: Feature of FoFGroup.
    """
    # utils.check_feature(pig_id = id, ptype = ptype, feature = feature)
    type_ind = {'gas': 0, 'dm': 1, 'star': 4, 'bh': 5}
    ind = type_ind[ptype]
    pig = utils.get_pig_data(id)
    data = pig.open('FOFGroups/' + feature)[:][:, ind]
    if min_range and max_range:
        res = numpy.where((data <= max_range) & (data >= min_range))
    elif min_range:
        res = numpy.where(data >= min_range)
    elif max_range:
        res = numpy.where(data <= max_range)
    else:
        res = data

    encoded_numpy_data = json.dumps(res, cls=utils.NumpyArrayEncoder)
    return {"IDlist": encoded_numpy_data}


@app.get(
    "/pig/{id}/search/{ptype}/{feature}/{criterion}", 
    tags=["advanced"],
    responses={
    404: constants.response_404["read_particle_data_by_criterion"],
    # 200: constants.response_200["read_particle_data_by_criterion"]
    },)
async def read_particle_data_by_criterion(id: int = Path(..., description="ID of a PIG folder"), ptype: str = Path(..., description="Name of particle type"), 
    feature: str  = Path(..., description="Feature of the particle"), criterion: str = Path(..., description="Searching Criterion"), 
    min_range: Optional[float] = Query(None, description="Min range of a searching criterion"), max_range: Optional[float] = Query(None, description="Min range of a searching criterion")):
    """
    Get a dictionary of {groupid:data} for data of specific particle feature within the searching criterion in a PIG folder:

    - **id**: ID of a PIG folder. It should be in [208, 230, 237, 216, 265, 244, 271, 258, 222, 251, 184, 197].
    - **ptype**: Name of pariticle type. It should be in ['gas', 'dm', 'star', 'bh'].
    - **feature**: Feature of the particle.
    - **criterion**: Searching criterion. It should be in ['bh_mass', 'gas_mass', 'dm_mass', 'star_mass', 'bh_mdot'].
    """
    data = utils.get_particle_data_criterion(pig_id=id, ptype=ptype,
                                             feature=feature, criterion=criterion,
                                             min_range=min_range, max_range=max_range)
    return data


###################################################################
#                        FoF Group Queries                        #
###################################################################
# Regular query for particle data in a Group={group_id} of type={ptype}
@app.get(
    "/pig/{id}/fofgroup/{feature}/{group_id}", 
    tags=["particle"],
    responses={
    404: constants.response_404["read_fofgroup_data"],
    # 200: constants.response_200["read_fofgroup_data"]
    },)
async def read_fofgroup_data(id: int = Path(..., description="ID of a PIG folder"), group_id: int = Path(..., description="ID of a halo group"), feature: str = Path(..., description="Feature of FoFGroup")):
    """
    Get the the FoFGroup feature data of the nth halo group in a PIG folder with all the information:

    - **id**: ID of a PIG folder. It should be in [208, 230, 237, 216, 265, 244, 271, 258, 222, 251, 184, 197].
    - **feature**: Feature of FoFGroup.
    - **group_id**: ID of a halo group. It should be between 1 to the max halo group size.
    """
    data = utils.get_fofgroup_data(pig_id=id, group_id=group_id, feature=feature)
    return {('fofgroup' + '_' + feature.lower()): data}


###################################################################
#                        Particle Queries                         #
###################################################################
# Regular query for particle data in a Group={group_id} of type={ptype}
@app.get(
    "/pig/{id}/{ptype}/{feature}/{group_id}", 
    tags=["particle"],
    responses={
    404: constants.response_404["read_particle_data_by_groupid"],
    # 200: constants.response_200["read_particle_data_by_groupid"]
    },)
async def read_particle_data_by_groupid(id: int = Path(..., description="ID of a PIG folder"), group_id: int = Path(..., description="ID of a halo group"), 
    ptype: str = Path(..., description="Name of particle type"), feature: str = Path(..., description="Feature of the particle")):
    """
    Get the the particle feature data of the nth halo group in a PIG folder with all the information:

    - **id**: ID of a PIG folder. It should be in [208, 230, 237, 216, 265, 244, 271, 258, 222, 251, 184, 197].
    - **feature**: Feature of the particle.
    - **group_id**: ID of a halo group. It should be between 1 to the max halo group size.
    """
    data = utils.get_particle_data(pig_id=id, group_id=group_id, ptype=ptype, feature=feature)
    return {(ptype + '_' + feature.lower()): data}


### bulk query post
@app.post(
    "/pig/{id}/{ptype}/{feature}/", 
    tags=["advanced"],
    responses={
    404: constants.response_404["read_particle_data_by_post_groupid_list"],
    # 200: constants.response_200["read_particle_data_by_post_groupid_list"]
    },)
async def read_particle_data_by_post_groupid_list(id: int = Path(..., description="ID of a PIG folder"), ptype: str = Path(..., description="Name of particle type"), 
    feature: str = Path(..., description="Feature of the particle"), groupid_list: List[int] = Body(..., description="A list of group IDs")):
    """
    Get all particle feature data of the a halo group list in a PIG folder with all the information:

    - **id**: ID of a PIG folder. It should be in [208, 230, 237, 216, 265, 244, 271, 258, 222, 251, 184, 197].
    - **feature**: Feature of the particle.
    - **groupid_list**: A list of group IDs. It should be a list and be passed as request body with post method
    """
    data = {}
    utils.check_query_list(groupid_list)
    for group_id in groupid_list:
        data[group_id] = utils.get_particle_data(pig_id=id, group_id=group_id, ptype=ptype, feature=feature)
    return {(ptype + '_' + feature.lower()): data}
