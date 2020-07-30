import json

from fastapi.testclient import TestClient

from ..main import app
from . import utils

client = TestClient(app)

""" BlackholeAccretionRate  BlackholeJumpToMinPot  BlackholeMinPotVel    GroupID   Potential
BlackholeDensity        BlackholeLastMergerID  BlackholePressure     ID        StarFormationTime
BlackholeEntropy        BlackholeMass          BlackholeProgenitors  Mass      Velocity
BlackholeGasVel         BlackholeMinPotPos     Generation                      Position    """

def test_get_negative_bh():
    utils.test_get_negative("bh")


### endpoint: /pig/{id}/bh/Position/{group_id}
# Basic positive tests
def test_get_bh_position_251():
    response = client.get("/pig/251/bh/Position/2")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Velocity data should be a 561897*3 array list
    data = json.loads(response.json()["bh_position"])
    assert type(data) is list
    assert data == []


def test_get_bh_position_271():
    response = client.get("/pig/271/bh/Position/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Velocity data should be a 561897*3 array list
    data = json.loads(response.json()["bh_position"])
    assert type(data) is list
    assert len(data) == 5
    assert data[0] == [72656.0567335518135224,194831.9271345908055082,229774.9501834622642491]




### endpoint: /pig/{id}/bh/Velocity/{group_id}
# Basic positive tests
def test_get_bh_velocity_251():
    response = client.get("/pig/251/bh/Velocity/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Velocity data should be a 561897*3 array list
    data = json.loads(response.json()["bh_velocity"])
    assert type(data) is list
    assert len(data) == 8
    assert data[0] == [54.4735107421875000,-16.7231864929199219,-10.2117156982421875]


def test_get_bh_velocity_271():
    response = client.get("/pig/271/bh/Velocity/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Velocity data should be a 561897*3 array list
    data = json.loads(response.json()["bh_velocity"])
    assert type(data) is list
    assert len(data) == 7
    assert data[0] == [24.9600467681884766,37.8858528137207031,-24.7577743530273438]



### endpoint: /pig/{id}/bh/Generation/{group_id}
# Basic positive tests
def test_get_bh_generation_251():
    response = client.get("/pig/251/bh/Generation/3")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Generation data should be a 1*1 array list
    data = json.loads(response.json()["bh_generation"])
    assert type(data) is list
    assert data == [1, 1, 1, 1, 2, 1, 2, 1]



def test_get_bh_generation_271():
    response = client.get("/pig/271/bh/Generation/3")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Generation data should be a 1*1 array list
    data = json.loads(response.json()["bh_generation"])
    assert type(data) is list
    assert data == [1, 1, 1, 1, 2, 1, 2]


### endpoint: /pig/{id}/bh/GroupID/{group_id}
# Basic positive tests
def test_get_bh_groupid_251():
    response = client.get("/pig/251/bh/GroupID/5")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh GroupID data should be a 173607*1 array list
    data = json.loads(response.json()["bh_groupid"])
    assert type(data) is list
    assert data[0] == 5
    assert len(data) == 11


def test_get_bh_groupid_271():
    response = client.get("/pig/271/bh/GroupID/5")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh GroupID data should be a 173607*1 array list
    data = json.loads(response.json()["bh_groupid"])
    assert type(data) is list
    assert data[6] == 5
    assert len(data) == 7


### endpoint: /pig/{id}/bh/Mass/{group_id}
# Basic positive tests
def test_get_bh_mass_251():
    response = client.get("/pig/251/bh/Mass/6")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Mass data should be a 83207*1 array list
    data = json.loads(response.json()["bh_mass"])
    assert type(data) is list
    assert abs(data[0] - 0.0003362224379089) < 1e-8
    assert len(data) == 7


def test_get_bh_mass_271():
    response = client.get("/pig/271/bh/Mass/6")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Mass data should be a 83207*1 array list
    data = json.loads(response.json()["bh_mass"])
    assert type(data) is list
    assert abs(data[0] - 0.0002862224355340) < 1e-8
    assert len(data) == 8


### endpoint: /pig/{id}/bh/BlackholeMass/{group_id}
# Basic positive tests
def test_get_bh_blackholemass_251():
    response = client.get("/pig/251/bh/BlackholeMass/6")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholemass"])
    assert type(data) is list
    assert abs(data[0] - 0.0001233712100657) < 1e-8
    assert len(data) == 7


def test_get_bh_blackholemass_271():
    response = client.get("/pig/271/bh/BlackholeMass/6")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholemass"])
    assert type(data) is list
    assert abs(data[0] - 0.0001511774753453) <1e-8
    
    assert len(data) == 8


### endpoint: /pig/{id}/bh/Potential/{group_id}
# Basic positive tests
def test_get_bh_potential_251():
    response = client.get("/pig/251/bh/Potential/8")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_potential"])
    assert type(data) is list
    assert data[0] == -277161.1250
    assert len(data) == 5


def test_get_bh_potential_271():
    response = client.get("/pig/271/bh/Potential/8")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_potential"])
    assert type(data) is list
    assert data[0] == 44106.32031250
    assert len(data) == 10



### endpoint: /pig/{id}/bh/ID/{group_id}
# Basic positive tests
def test_get_bh_id_251():
    response = client.get("/pig/251/bh/ID/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_id"])
    assert type(data) is list
    assert data[8] == 72057843939697633
    assert len(data) == 9


def test_get_bh_id_271():
    response = client.get("/pig/271/bh/ID/8")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_id"])
    assert type(data) is list
    assert data[9] == 72057727253357575
    assert len(data) == 10



### endpoint: /pig/{id}/bh/BlackholeProgenitors/{group_id}
# Basic positive tests
def test_get_bh_blackholeprogenitors_251():
    response = client.get("/pig/251/bh/BlackholeProgenitors/12")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeprogenitors"])
    assert type(data) is list
    assert data == [0,0]



def test_get_bh_blackholeprogenitors_271():
    response = client.get("/pig/271/bh/BlackholeProgenitors/8")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeprogenitors"])
    assert type(data) is list
    assert data[5] == 0
    assert len(data) == 10




### endpoint: /pig/{id}/bh/BlackholeMinPotVel/{group_id}
# Basic positive tests
def test_get_bh_blackholeminpotvel_251():
    response = client.get("/pig/251/bh/BlackholeMinPotVel/14")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeminpotvel"])
    assert type(data) is list
    assert data[0] == [30.8339633941650391,-8.3439722061157227,-1.4297494888305664]
    assert len(data) == 5

def test_get_bh_blackholeminpotvel_271():
    response = client.get("/pig/271/bh/BlackholeMinPotVel/14")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeminpotvel"])
    assert type(data) is list
    assert data[0] == [-68.5757751464843750,-48.4527740478515625,22.2900638580322266]
    assert len(data) == 6



### endpoint: /pig/{id}/bh/BlackholeMinPotPos/{group_id}
# Basic positive tests
def test_get_bh_blackholeminpotpos_251():
    response = client.get("/pig/251/bh/BlackholeMinPotPos/16")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeminpotpos"])
    assert type(data) is list
    assert data[0] == [385029.0029749941313639,386472.4315522146061994,188237.1807050006464124]
    assert len(data) == 7

def test_get_bh_blackholeminpotpos_271():
    response = client.get("/pig/271/bh/BlackholeMinPotPos/16")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeminpotpos"])
    assert type(data) is list
    assert data[0] == [321746.1416593762696721,45754.5331728641976952,119495.5197756342240609]
    assert len(data) == 6



### endpoint: /pig/{id}/bh/BlackholeLastMergerID/{group_id}
# Basic positive tests
def test_get_bh_blackholelastmergerid_251():
    response = client.get("/pig/251/bh/BlackholeLastMergerID/18")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholelastmergerid"])
    assert type(data) is list
    assert data == [0,0,0,0,0]


def test_get_bh_blackholelastmergerid_271():
    response = client.get("/pig/271/bh/BlackholeLastMergerID/18")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholelastmergerid"])
    assert type(data) is list
    assert data == [0,72057930757709835,0,0,0]




### endpoint: /pig/{id}/bh/BlackholeGasVel/{group_id}
# Basic positive tests
def test_get_bh_blackholegasvel_251():
    response = client.get("/pig/251/bh/BlackholeGasVel/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholegasvel"])
    assert type(data) is list
    assert data[0] == [59.5527992248535156,-23.2456321716308594,-10.0467796325683594]
    assert len(data) == 8

def test_get_bh_blackholegasvel_271():
    response = client.get("/pig/271/bh/BlackholeGasVel/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholegasvel"])
    assert type(data) is list
    assert data[0] == [17.7611846923828125,44.2505416870117188,-26.4937973022460938]
    assert len(data) == 7


### endpoint: /pig/{id}/bh/BlackholeEntropy/{group_id}
# Basic positive tests
def test_get_bh_blackholeentropy_251():
    response = client.get("/pig/251/bh/BlackholeEntropy/22")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeentropy"])
    assert type(data) is list
    assert data[0] == 267099.3125
    assert len(data) == 7

def test_get_bh_blackholeentropy_271():
    response = client.get("/pig/271/bh/BlackholeEntropy/22")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeentropy"])
    assert type(data) is list
    assert data[0] == 439651.875
    assert len(data) == 6



### endpoint: /pig/{id}/bh/BlackholeDensity/{group_id}
# Basic positive tests
def test_get_bh_blackholedensity_251():
    response = client.get("/pig/251/bh/BlackholeDensity/24")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholedensity"])
    assert type(data) is list
    assert abs(data[0] - 0.0003469409130048) < 1e-8
    assert len(data) == 4

def test_get_bh_blackholedensity_271():
    response = client.get("/pig/271/bh/BlackholeDensity/24")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholedensity"])
    assert type(data) is list
    assert abs(data[0] - 0.0008554264204577) < 1e-8
    assert len(data) == 8


### endpoint: /pig/{id}/bh/BlackholeAccretionRate/{group_id}
# Basic positive tests
def test_get_bh_blackholeaccretionrate_251():
    response = client.get("/pig/251/bh/BlackholeAccretionRate/26")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeaccretionrate"])
    assert type(data) is list
    assert abs(data[0] - 0.0025596539489925) < 1e-8
    assert len(data) == 3

def test_get_bh_blackholeaccretionrate_271():
    response = client.get("/pig/271/bh/BlackholeAccretionRate/26")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- bh Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeaccretionrate"])
    assert type(data) is list
    assert abs(data[0] - 0.0007860922487453) < 1e-8
    assert len(data) == 8


### advanced bh query tests: /pig/{id}/{ptype}/{feature}/
def test_get_advanced_bh_generation_251():
    response = client.get("/pig/251/bh/Generation/", params = {'groupid_list': [1,2,3]})
    utils.common_positive_tests(response)
    bh_generation_1 = json.loads(response.json()["bh_generation"]["1"])
    assert type(bh_generation_1) is list
    assert bh_generation_1 == [1, 1, 1, 1, 1, 2, 1]
    assert len(bh_generation_1) == 7
    bh_generation_2 = json.loads(response.json()["bh_generation"]["2"])
    assert type(bh_generation_2) is list
    assert bh_generation_2 == []
    assert len(bh_generation_2) == 0
    bh_generation_3 = json.loads(response.json()["bh_generation"]["3"])
    assert type(bh_generation_3) is list
    assert bh_generation_3 == [1, 1, 1, 1, 2, 1, 2, 1]
    assert len(bh_generation_3) == 8


def test_get_advanced_bh_groupid_251():
    response = client.get("/pig/251/bh/GroupID/", params = {'groupid_list': [4,5,6]})
    utils.common_positive_tests(response)
    bh_groupid_4 = json.loads(response.json()["bh_groupid"]["4"])
    assert type(bh_groupid_4) is list
    assert bh_groupid_4[:4] == [4, 4]
    assert len(bh_groupid_4) == 2
    bh_groupid_5 = json.loads(response.json()["bh_groupid"]["5"])
    assert type(bh_groupid_5) is list
    assert bh_groupid_5[:4] == [5, 5, 5, 5]
    assert len(bh_groupid_5) == 11
    bh_groupid_6 = json.loads(response.json()["bh_groupid"]["6"])
    assert type(bh_groupid_6) is list
    assert bh_groupid_6[:4] == [6, 6, 6, 6]
    assert len(bh_groupid_6) == 7


def test_get_advanced_bh_position_251():
    response = client.get("/pig/251/bh/Position/", params = {'groupid_list': [7,8,9]})
    utils.common_positive_tests(response)
    bh_position_7 = json.loads(response.json()["bh_position"]["7"])
    assert type(bh_position_7) is list
    assert bh_position_7[0] == [15382.678998266496, 145925.19427169597, 290399.2446326842]
    assert len(bh_position_7) == 12
    bh_position_8 = json.loads(response.json()["bh_position"]["8"])
    assert type(bh_position_8) is list
    assert bh_position_8[0] == [72208.11967420416, 194269.7290507568, 229826.71613942046]
    assert len(bh_position_8) == 5
    bh_position_9 = json.loads(response.json()["bh_position"]["9"])
    assert type(bh_position_9) is list
    assert bh_position_9[0] == [40455.22049012193, 38824.604163998105, 388659.6113405379]
    assert len(bh_position_9) == 8


def test_get_advanced_bh_potential_251():
    response = client.get("/pig/251/bh/Potential/", params = {'groupid_list': [10,11,12]})
    utils.common_positive_tests(response)
    bh_potential_10 = json.loads(response.json()["bh_potential"]["10"])
    assert type(bh_potential_10) is list
    assert bh_potential_10[:4] == [-292802.53125, -311502.59375, -299892.75, -319366.15625]
    assert len(bh_potential_10) == 9
    bh_potential_11 = json.loads(response.json()["bh_potential"]["11"])
    assert type(bh_potential_11) is list
    assert bh_potential_11[:4] == [48769.54296875, 73449.7421875, 87866.609375, 104375.203125]
    assert len(bh_potential_11) == 6
    bh_potential_12 = json.loads(response.json()["bh_potential"]["12"])
    assert type(bh_potential_12) is list
    assert bh_potential_12 == [-401701.46875, -592302.5]
    assert len(bh_potential_12) == 2


def test_get_advanced_bh_velocity_251():
    response = client.get("/pig/251/bh/Velocity/", params = {'groupid_list': [13,14,15]})
    utils.common_positive_tests(response)
    bh_velocity_13 = json.loads(response.json()["bh_velocity"]["13"])
    assert type(bh_velocity_13) is list
    assert bh_velocity_13[0] == [51.82337188720703, 57.168174743652344, 16.91756248474121]
    assert len(bh_velocity_13) == 3
    bh_velocity_14 = json.loads(response.json()["bh_velocity"]["14"])
    assert type(bh_velocity_14) is list
    assert bh_velocity_14[0] == [20.97827911376953, -3.9093408584594727, -18.333993911743164]
    assert len(bh_velocity_14) == 5
    bh_velocity_15 = json.loads(response.json()["bh_velocity"]["15"])
    assert type(bh_velocity_15) is list
    assert bh_velocity_15[0] == [9.807731628417969, -31.17384147644043, 39.47724533081055]
    assert len(bh_velocity_15) == 4


def test_get_advanced_bh_mass_251():
    response = client.get("/pig/251/bh/Mass/", params = {'groupid_list': [16,17,18]})
    utils.common_positive_tests(response)
    bh_mass_16 = json.loads(response.json()["bh_mass"]["16"])
    assert type(bh_mass_16) is list
    assert bh_mass_16[:4] == [0.00023622244771104306, 0.013051284477114677, 0.00023622244771104306, 0.00023622244771104306]
    assert len(bh_mass_16) == 7
    bh_mass_17 = json.loads(response.json()["bh_mass"]["17"])
    assert type(bh_mass_17) is list
    assert bh_mass_17[:4] == [0.0002862224355340004, 0.0002862224355340004, 0.007765813730657101, 0.0005224448977969587]
    assert len(bh_mass_17) == 8
    bh_mass_18 = json.loads(response.json()["bh_mass"]["18"])
    assert type(bh_mass_18) is list
    assert bh_mass_18[:4] == [0.0002862224355340004, 0.0012401678832247853, 0.004192948807030916, 0.001003945479169488]
    assert len(bh_mass_18) == 5


def test_get_advanced_bh_starformationtime_251():
    response = client.get("/pig/251/bh/StarFormationTime/", params = {'groupid_list': [22,23,24]})
    utils.common_positive_tests(response)
    bh_sft_22 = json.loads(response.json()["bh_starformationtime"]["22"])
    assert type(bh_sft_22) is list
    assert bh_sft_22 == [0.0, 0.1111111119389534, 0.0, 0.0, 0.0, 0.0, 0.0]
    assert len(bh_sft_22) == 7
    bh_sft_23 = json.loads(response.json()["bh_starformationtime"]["23"])
    assert type(bh_sft_23) is list
    assert bh_sft_23 == [0.0, 0.11428570747375488, 0.12747056782245636, 0.1149425283074379]
    assert len(bh_sft_23) == 4
    bh_sft_24 = json.loads(response.json()["bh_starformationtime"]["24"])
    assert type(bh_sft_24) is list
    assert bh_sft_24[:4] == [0.0, 0.11956783384084702, 0.0, 0.0]
    assert len(bh_sft_24) == 4