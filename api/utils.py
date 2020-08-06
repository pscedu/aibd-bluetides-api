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
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


def check_pig_id(pig_id: int):
    subdirectories = get_pig_folders()
    pig_folder = "PIG_" + str(pig_id)
    if pig_folder not in subdirectories:
        raise HTTPException(status_code=404, detail="PIG folder does not exist, should in {}".format(subdirectories))


def check_type_id_range(type_id: int):
    if type_id < 0 or type_id >= 6:
        raise HTTPException(status_code=404, detail="type_id out of range, should be [0,6)")


def check_group_id_range(pig, group_id: int):
    total_group = pig.open('FOFGroups/LengthByType').size
    if group_id <= 0 or group_id > total_group:
        raise HTTPException(status_code=404, detail="group_id out of range, should be [1,{}]".format(total_group))


def check_halo_id_range(pig, halo_id: int):
    total_halo = pig.open('FOFGroups/LengthByType').size
    if halo_id < 0 or halo_id >= total_halo:
        raise HTTPException(status_code=404, detail="halo_id out of range, should be [0,{})".format(total_halo))


def check_type_name(ptype:str):
    type_list = ['gas','dm','star','bh']
    if ptype not in type_list:
        raise HTTPException(status_code=404, detail="Particle type {} does not exist, should be in {}".format(ptype,type_list))


def check_query_list(id_list):
    if id_list is None:
        raise HTTPException(status_code=404, detail="ID list is needed. Please input a valid one.")


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


def get_lbt_by_haloid(pig_id: int, halo_id: int):
    check_pig_id(pig_id=pig_id)
    pig = get_pig_data(pig_id)
    check_halo_id_range(pig=pig, halo_id=halo_id)
    nhalo = pig.open('FOFGroups/LengthByType')[halo_id]
    numpy_array_type_data = numpy.array(nhalo)
    encoded_numpy_type_data = json.dumps(numpy_array_type_data, cls=NumpyArrayEncoder)
    return encoded_numpy_type_data


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


def get_fof_subfield(pig_id:int):
    check_pig_id(pig_id = pig_id)
    subdirectories = []
    directory_contents = os.listdir(constants.PIG_BASE_DIR + 'PIG_' + str(pig_id) + '/FOFGroups')
    for item in directory_contents:
        subdirectories.append(item)
    return subdirectories


def check_feature(pig_id:int, ptype:str,feature:str):
    type_list = ['gas','dm','star','bh']
    if ptype in type_list:
        subdirectories = get_part_subfield(pig_id = pig_id, ptype = ptype)
    elif ptype=='fofgroup':
        subdirectories = get_fof_subfield(pig_id = pig_id)
    else:
        raise HTTPException(status_code=404, detail="Particle type {} does not exist, should be in {}".format(ptype,type_list))
    if feature not in subdirectories:
        raise HTTPException(status_code=404, detail="Feature {} does not exist, should be in {}".format(feature,subdirectories))
    
def check_criterion(criterion:str):
    # for now we only have limited criterions
    criterion_list = ['bh_mass','gas_mass','dm_mass','star_mass','bh_mdot']
    if criterion not in criterion_list:
        raise HTTPException(status_code=404, detail="Search criterion {} does not exist, should be in {}".format(criterion,criterion_list))
        
    
def get_particle_data(pig_id: int, group_id: int, ptype: str, feature: str):
    check_pig_id(pig_id=pig_id)
    pig = get_pig_data(pig_id)

    check_group_id_range(pig=pig, group_id=group_id)
    lbt = pig.open('FOFGroups/LengthByType')[:group_id]
    obt = numpy.cumsum(lbt, axis=0).astype(int)
    obt = get_obt(pig_id, group_id)

    check_feature(pig_id = pig_id, ptype = ptype, feature = feature)
    type_ind = {'gas':0,'dm':1,'star':4,'bh':5}
    ind = type_ind[ptype]

    path = str(ind)+'/' + feature
    if group_id == 1:
        data = pig.open(path)[:obt[0][ind]]
    else:
        data = pig.open(path)[obt[-2][ind]:obt[-1][ind]]
    numpy_array_data = numpy.array(data)
    encoded_numpy_data = json.dumps(numpy_array_data, cls=NumpyArrayEncoder)
    return encoded_numpy_data


def get_particle_data_criterion(pig_id: int, ptype: str, \
                                feature: str,criterion:str,\
                                min_range:float,max_range:float):
    check_pig_id(pig_id=pig_id)
    pig = get_pig_data(pig_id)
    check_criterion(criterion)
    check_feature(pig_id = pig_id, ptype = ptype, feature = feature)
    lbt = pig.open('FOFGroups/LengthByType')[:]
    obt = numpy.cumsum(lbt, axis=0).astype(int)
    obt = numpy.concatenate((numpy.zeros((1,6)),obt)).astype(int)
    
    type_ind = {'gas':0,'dm':1,'star':4,'bh':5}
    ind = type_ind[ptype]
    path = str(ind)+'/' + feature
    if criterion == 'gas_mass':
        id_list = ((pig.open('FOFGroups/MassByType')[:,0] >= min_range) \
                & (pig.open('FOFGroups/MassByType')[:,0] <= max_range)).nonzero()[0]
    elif criterion == 'dm_mass':
        id_list = ((pig.open('FOFGroups/MassByType')[:,1] >= min_range) \
                & (pig.open('FOFGroups/MassByType')[:,1] <= max_range)).nonzero()[0]
    elif criterion == 'star_mass':
        id_list = ((pig.open('FOFGroups/MassByType')[:,4] >= min_range) \
                & (pig.open('FOFGroups/MassByType')[:,4] <= max_range)).nonzero()[0]
    elif criterion == 'bh_mass':  # need to use individual BH mass instead of MBT
        index = (pig.open('5/BlackholeMass')[:] >= min_range) & (pig.open('5/BlackholeMass')[:] <= max_range)
        id_list = list(set(pig.open('5/GroupID')[:][index]-1))
    elif criterion == 'bh_mdot': 
        index = (pig.open('5/BlackholeAccretionRate')[:] >= min_range) & (pig.open('5/BlackholeAccretionRate')[:] <= max_range)
        id_list = list(set(pig.open('5/GroupID')[:][index]-1))
    data = {i: json.dumps(pig.open(path)[obt[i,ind]:obt[i+1,ind]], cls=NumpyArrayEncoder) for i in id_list}
    return data
        
    
    


def get_fofgroup_data(pig_id: int, group_id: int, feature: str):
    check_pig_id(pig_id=pig_id)
    pig = get_pig_data(pig_id)
    check_group_id_range(pig=pig, group_id=group_id)
    check_feature(pig_id = pig_id, ptype = 'fofgroup', feature = feature)
    data = pig.open('FOFGroups/'+ feature)[group_id-1]
    numpy_array_data = numpy.array(data)
    encoded_numpy_data = json.dumps(numpy_array_data, cls=NumpyArrayEncoder)
    return encoded_numpy_data
