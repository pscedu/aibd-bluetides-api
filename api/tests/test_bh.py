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
    # Validate payload: Response is a well-formed JSON object and response data -- star Velocity data should be a 561897*3 array list
    data = json.loads(response.json()["bh_position"])
    assert type(data) is list
    assert data == []


def test_get_bh_position_271():
    response = client.get("/pig/271/bh/Position/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Velocity data should be a 561897*3 array list
    data = json.loads(response.json()["bh_position"])
    assert type(data) is list
    assert len(data) == 5
    assert data[0] == [72656.0567335518135224,194831.9271345908055082,229774.9501834622642491]




### endpoint: /pig/{id}/bh/Velocity/{group_id}
# Basic positive tests
def test_get_bh_velocity_251():
    response = client.get("/pig/251/bh/Velocity/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Velocity data should be a 561897*3 array list
    data = json.loads(response.json()["bh_velocity"])
    assert type(data) is list
    assert len(data) == 8
    assert data[0] == [54.4735107421875000,-16.7231864929199219,-10.2117156982421875]


def test_get_bh_velocity_271():
    response = client.get("/pig/271/bh/Velocity/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Velocity data should be a 561897*3 array list
    data = json.loads(response.json()["bh_velocity"])
    assert type(data) is list
    assert len(data) == 7
    assert data[0] == [24.9600467681884766,37.8858528137207031,-24.7577743530273438]



### endpoint: /pig/{id}/bh/Generation/{group_id}
# Basic positive tests
def test_get_bh_generation_251():
    response = client.get("/pig/251/bh/Generation/3")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Generation data should be a 1*1 array list
    data = json.loads(response.json()["bh_generation"])
    assert type(data) is list
    assert data == [1, 1, 1, 1, 2, 1, 2, 1]



def test_get_bh_generation_271():
    response = client.get("/pig/271/bh/Generation/3")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Generation data should be a 1*1 array list
    data = json.loads(response.json()["bh_generation"])
    assert type(data) is list
    assert data == [1, 1, 1, 1, 2, 1, 2]


### endpoint: /pig/{id}/bh/GroupID/{group_id}
# Basic positive tests
def test_get_bh_groupid_251():
    response = client.get("/pig/251/bh/GroupID/5")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star GroupID data should be a 173607*1 array list
    data = json.loads(response.json()["bh_groupid"])
    assert type(data) is list
    assert data[0] == 5
    assert len(data) == 11


def test_get_bh_groupid_271():
    response = client.get("/pig/271/bh/GroupID/5")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star GroupID data should be a 173607*1 array list
    data = json.loads(response.json()["bh_groupid"])
    assert type(data) is list
    assert data[6] == 5
    assert len(data) == 7


### endpoint: /pig/{id}/bh/Mass/{group_id}
# Basic positive tests
def test_get_bh_mass_251():
    response = client.get("/pig/251/bh/Mass/6")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Mass data should be a 83207*1 array list
    data = json.loads(response.json()["bh_mass"])
    assert type(data) is list
    assert abs(data[0] - 0.0003362224379089) < 1e-8
    assert len(data) == 7


def test_get_bh_mass_271():
    response = client.get("/pig/271/bh/Mass/6")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Mass data should be a 83207*1 array list
    data = json.loads(response.json()["bh_mass"])
    assert type(data) is list
    assert abs(data[0] - 0.0002862224355340) < 1e-8
    assert len(data) == 8


### endpoint: /pig/{id}/bh/BlackholeMass/{group_id}
# Basic positive tests
def test_get_bh_blackholemass_251():
    response = client.get("/pig/251/bh/BlackholeMass/6")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholemass"])
    assert type(data) is list
    assert abs(data[0] - 0.0001233712100657) < 1e-8
    assert len(data) == 7


def test_get_bh_blackholemass_271():
    response = client.get("/pig/271/bh/BlackholeMass/6")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholemass"])
    assert type(data) is list
    assert abs(data[0] - 0.0001511774753453) <1e-8
    
    assert len(data) == 8


### endpoint: /pig/{id}/bh/Potential/{group_id}
# Basic positive tests
def test_get_bh_potential_251():
    response = client.get("/pig/251/bh/Potential/8")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_potential"])
    assert type(data) is list
    assert data[0] == -277161.1250
    assert len(data) == 5


def test_get_bh_potential_271():
    response = client.get("/pig/271/bh/Potential/8")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_potential"])
    assert type(data) is list
    assert data[0] == 44106.32031250
    assert len(data) == 10



### endpoint: /pig/{id}/bh/ID/{group_id}
# Basic positive tests
def test_get_bh_id_251():
    response = client.get("/pig/251/bh/ID/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_id"])
    assert type(data) is list
    assert data[8] == 72057843939697633
    assert len(data) == 9


def test_get_bh_id_271():
    response = client.get("/pig/271/bh/ID/8")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_id"])
    assert type(data) is list
    assert data[9] == 72057727253357575
    assert len(data) == 10



### endpoint: /pig/{id}/bh/BlackholeProgenitors/{group_id}
# Basic positive tests
def test_get_bh_blackholeprogenitors_251():
    response = client.get("/pig/251/bh/BlackholeProgenitors/12")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeprogenitors"])
    assert type(data) is list
    assert data == [0,0]



def test_get_bh_blackholeprogenitors_271():
    response = client.get("/pig/271/bh/BlackholeProgenitors/8")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeprogenitors"])
    assert type(data) is list
    assert data[5] == 0
    assert len(data) == 10




### endpoint: /pig/{id}/bh/BlackholeMinPotVel/{group_id}
# Basic positive tests
def test_get_bh_blackholeminpotvel_251():
    response = client.get("/pig/251/bh/BlackholeMinPotVel/14")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeminpotvel"])
    assert type(data) is list
    assert data[0] == [30.8339633941650391,-8.3439722061157227,-1.4297494888305664]
    assert len(data) == 5

def test_get_bh_blackholeminpotvel_271():
    response = client.get("/pig/271/bh/BlackholeMinPotVel/14")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeminpotvel"])
    assert type(data) is list
    assert data[0] == [-68.5757751464843750,-48.4527740478515625,22.2900638580322266]
    assert len(data) == 6



### endpoint: /pig/{id}/bh/BlackholeMinPotPos/{group_id}
# Basic positive tests
def test_get_bh_blackholeminpotpos_251():
    response = client.get("/pig/251/bh/BlackholeMinPotPos/16")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeminpotpos"])
    assert type(data) is list
    assert data[0] == [385029.0029749941313639,386472.4315522146061994,188237.1807050006464124]
    assert len(data) == 7

def test_get_bh_blackholeminpotpos_271():
    response = client.get("/pig/271/bh/BlackholeMinPotPos/16")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeminpotpos"])
    assert type(data) is list
    assert data[0] == [321746.1416593762696721,45754.5331728641976952,119495.5197756342240609]
    assert len(data) == 6



### endpoint: /pig/{id}/bh/BlackholeLastMergerID/{group_id}
# Basic positive tests
def test_get_bh_blackholelastmergerid_251():
    response = client.get("/pig/251/bh/BlackholeLastMergerID/18")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholelastmergerid"])
    assert type(data) is list
    assert data == [0,0,0,0,0]


def test_get_bh_blackholelastmergerid_271():
    response = client.get("/pig/271/bh/BlackholeLastMergerID/18")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholelastmergerid"])
    assert type(data) is list
    assert data == [0,72057930757709835,0,0,0]




### endpoint: /pig/{id}/bh/BlackholeGasVel/{group_id}
# Basic positive tests
def test_get_bh_blackholegasvel_251():
    response = client.get("/pig/251/bh/BlackholeGasVel/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholegasvel"])
    assert type(data) is list
    assert data[0] == [59.5527992248535156,-23.2456321716308594,-10.0467796325683594]
    assert len(data) == 8

def test_get_bh_blackholegasvel_271():
    response = client.get("/pig/271/bh/BlackholeGasVel/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholegasvel"])
    assert type(data) is list
    assert data[0] == [17.7611846923828125,44.2505416870117188,-26.4937973022460938]
    assert len(data) == 7


### endpoint: /pig/{id}/bh/BlackholeEntropy/{group_id}
# Basic positive tests
def test_get_bh_blackholeentropy_251():
    response = client.get("/pig/251/bh/BlackholeEntropy/22")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeentropy"])
    assert type(data) is list
    assert data[0] == 267099.3125
    assert len(data) == 7

def test_get_bh_blackholeentropy_271():
    response = client.get("/pig/271/bh/BlackholeEntropy/22")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeentropy"])
    assert type(data) is list
    assert data[0] == 439651.875
    assert len(data) == 6



### endpoint: /pig/{id}/bh/BlackholeDensity/{group_id}
# Basic positive tests
def test_get_bh_blackholedensity_251():
    response = client.get("/pig/251/bh/BlackholeDensity/24")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholedensity"])
    assert type(data) is list
    assert abs(data[0] - 0.0003469409130048) < 1e-8
    assert len(data) == 4

def test_get_bh_blackholedensity_271():
    response = client.get("/pig/271/bh/BlackholeDensity/24")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholedensity"])
    assert type(data) is list
    assert abs(data[0] - 0.0008554264204577) < 1e-8
    assert len(data) == 8


### endpoint: /pig/{id}/bh/BlackholeAccretionRate/{group_id}
# Basic positive tests
def test_get_bh_blackholeaccretionrate_251():
    response = client.get("/pig/251/bh/BlackholeAccretionRate/26")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeaccretionrate"])
    assert type(data) is list
    assert abs(data[0] - 0.0025596539489925) < 1e-8
    assert len(data) == 3

def test_get_bh_blackholeaccretionrate_271():
    response = client.get("/pig/271/bh/BlackholeAccretionRate/26")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    data = json.loads(response.json()["bh_blackholeaccretionrate"])
    assert type(data) is list
    assert abs(data[0] - 0.0007860922487453) < 1e-8
    assert len(data) == 8








