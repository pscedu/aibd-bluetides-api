import json
import os
from json.encoder import JSONEncoder

import bigfile
import numpy
from fastapi import HTTPException

import constants


# JSON serializer
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


def check_pig_id(pig_id: int):
    subdirectories = get_pig_folders()
    pig_folder = "PIG_" + str(pig_id)
    if pig_folder not in subdirectories:
        raise HTTPException(status_code=404, detail="PIG folder does not exist, should in {}".format(subdirectories))


def check_type_id_range(type_id: int):
    if type_id < 0 or type_id >= 6:
        raise HTTPException(status_code=400, detail="type_id out of range, should be [0,6)")


def check_group_id_range(pig, group_id: int):
    total_group = pig.open('FOFGroups/LengthByType').size
    if group_id <= 0 or group_id > total_group:
        raise HTTPException(status_code=400, detail="group_id out of range, should be [1,{}]".format(total_group))


def check_halo_id_range(pig, halo_id: int):
    total_halo = pig.open('FOFGroups/LengthByType').size
    if halo_id < 0 or halo_id >= total_halo:
        raise HTTPException(status_code=400, detail="halo_id out of range, should be [0,{})".format(total_halo))


def check_type_name(ptype:str):
    type_list = ['gas','dm','star','gas']
    if ptype not in type_list:
        raise HTTPException(status_code=404, detail="Particle type {} does not exist, should be in {}".format(ptype,type_list))
        
        
        
def get_gas_data(pig_id: int, group_id: int, feature: str):
    check_pig_id(pig_id=pig_id)
    pig = get_pig_data(pig_id)
    check_group_id_range(pig=pig, group_id=group_id)
    lbt = pig.open('FOFGroups/LengthByType')[:group_id]
    obt = numpy.cumsum(lbt, axis=0).astype(int)
    obt = get_obt(pig_id, group_id)
    path = '0/' + feature
    if group_id == 1:
        gas_data = pig.open(path)[:obt[0][0]]
    else:
        gas_data = pig.open(path)[obt[-2][0]:obt[-1][0]]
    numpy_array_gas_data = numpy.array(gas_data)
    encoded_numpy_gas_data = json.dumps(numpy_array_gas_data, cls=NumpyArrayEncoder)
    return encoded_numpy_gas_data



def get_dm_data(pig_id: int, group_id: int, feature: str):
    check_pig_id(pig_id)
    pig = get_pig_data(pig_id)
    check_group_id_range(pig, group_id)
    lbt = pig.open('FOFGroups/LengthByType')[:group_id]
    obt = numpy.cumsum(lbt,axis=0).astype(int)
    obt = get_obt(pig_id, group_id)
    path = '1/' + feature
    if group_id==1:
        dm_data = pig.open(path)[:obt[0][1]]
    else:
        dm_data = pig.open(path)[obt[-2][1]:obt[-1][1]]
    numpyArrayDMData = numpy.array(dm_data)
    encodedNumpyDMData = json.dumps(numpyArrayDMData, cls=NumpyArrayEncoder)
    return encodedNumpyDMData



# Get the list of PIG folders
def get_pig_folders():
    subdirectories = []
    directory_contents = os.listdir(constants.PIG_BASE_DIR)
    for item in directory_contents:
        if item.startswith("PIG_"):
            subdirectories.append(item)
    return subdirectories


def get_pig_numhalo(sub_dir: str):
    pig_dir = constants.PIG_BASE_DIR + sub_dir + '/'
    pig = bigfile.File(pig_dir)
    Nhalo = pig['Header'].attrs['NumFOFGroupsTotal'][0]
    return Nhalo


def get_pig_redshift(sub_dir: str):
    pig_dir = constants.PIG_BASE_DIR + sub_dir + '/'
    pig = bigfile.File(pig_dir)
    scalefactor = pig['Header'].attrs['Time'][0]
    redshift = 1. / scalefactor - 1.
    return redshift


# Get a particular pig folder data in bigfile format
def get_pig_data(pig_id: int):
    # data directory
    pig_dir = constants.PIG_BASE_DIR + "PIG_" + str(pig_id) + "/"
    pig = bigfile.File(pig_dir)
    return pig


def get_obt(pig_id: int, group_id: int):
    check_pig_id(pig_id=pig_id)
    pig = get_pig_data(pig_id)
    check_group_id_range(pig=pig, group_id=group_id)
    lbt = pig.open('FOFGroups/LengthByType')[:group_id]
    obt = numpy.cumsum(lbt, axis=0).astype(int)
    return obt

def get_part_subfield(pig_id:int, ptype:str):
    check_pig_id(pig_id = pig_id)
    check_type_name(ptype)
    type_ind = {}
    type_ind['gas']  = 0
    type_ind['dm']   = 1
    type_ind['star'] = 4
    type_ind['bh']   = 5
    subdirectories = []
    directory_contents = os.listdir(constants.PIG_BASE_DIR + 'PIG_' + str(pig_id) + '/' + str(type_ind[ptype]))
    for item in directory_contents:
        subdirectories.append(item)
    return subdirectories
    
