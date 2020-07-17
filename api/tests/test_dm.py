import json

from fastapi.testclient import TestClient

from ..main import app
from . import utils

client = TestClient(app)


###################################################################
#                           DM Tests                              #
################################################################### 


#DM POSITION
### endpoint: /pig/{id}/dm/position/{group_id}
# Basic positive tests
def test_get_dm_position_244():
    response = client.get("/pig/244/dm/Position/331526")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 2585*3 array list
    dm_position = json.loads(response.json()["dm_position"])
    assert type(dm_position) is list
    assert dm_position[456] == [394903.89612031489, 43208.98194487528,257613.16877157817]
    assert len(dm_position[0]) == 3
    assert len(dm_position) == 2585


def test_get_dm_position_271():
    response = client.get("/pig/271/dm/Position/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 158970*3 array list
    dm_position = json.loads(response.json()["dm_position"])
    assert type(dm_position) is list
    assert dm_position[1] == [72973.67144294265, 195179.85487456998, 229742.43473667066]
    assert len(dm_position[0]) == 3
    assert len(dm_position) == 158970


def test_get_dm_position_negative():
    # missing required parameters
    utils.test_get_missing_input(244, "dm", "Position", 10)
    utils.test_get_missing_input(271, "dm", "Position", 10)
    # pig 271 group_id not in [1,294288056]
    utils.test_get_invalid_input(244, "dm", "Position", 0)
    utils.test_get_invalid_input(244, "dm", "Position", 282939567)
    utils.test_get_invalid_input(271, "dm", "Position", 0)
    utils.test_get_invalid_input(271, "dm", "Position", 294288057)
    # pig id not in folder
    utils.test_get_invalid_input(10, "dm", "Position", 10000)
    # invalid feature
    utils.test_get_invalid_input(10, "dm", "H2Fraction", 10000)


#DM VELOCITY
def test_get_dm_velocity_244():
    response = client.get("/pig/244/dm/Velocity/1862")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 26324*3 array list
    data = json.loads(response.json()["dm_velocity"])
    assert type(data) is list
    assert data[2000] == [14.788228034973145, 49.952144622802734,23.566410064697266]
    assert len(data[0]) == 3
    assert len(data) == 26324


def test_get_dm_velocity_271():
    response = client.get("/pig/271/dm/Velocity/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 158970*3 array list
    data = json.loads(response.json()["dm_velocity"])
    assert type(data) is list
    assert data[0] == [-2.3727707862854004, 65.58319854736328, 70.11107635498047]
    assert len(data[0]) == 3
    assert len(data) == 158970


def test_get_dm_velocity_negative():
    # missing required parameters
    utils.test_get_missing_input(244, "dm", "Velocity", 10)
    utils.test_get_missing_input(271, "dm", "Velocity", 10)
    # pig 271 group_id not in [1,294288056]
    utils.test_get_invalid_input(244, "dm", "Velocity", 0)
    utils.test_get_invalid_input(244, "dm", "Velocity", 282939567)
    utils.test_get_invalid_input(271, "dm", "Velocity", 0)
    utils.test_get_invalid_input(271, "dm", "Velocity", 294288057)
    # pig id not in folder
    utils.test_get_invalid_input(10, "dm", "Velocity", 10000)


#DM MASS
def test_get_dm_mass_271():
    response = client.get("/pig/271/dm/Mass/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 158970*1 array list
    data = json.loads(response.json()["dm_mass"])
    assert type(data) is list
    assert data[0] == 0.0011963852448388934
    assert data[:4] == [0.0011963852448388934, 0.0011963852448388934, 0.0011963852448388934, 0.0011963852448388934]
    assert len(data) == 158970

def test_get_dm_mass_negative():
    # missing required parameters
    utils.test_get_missing_input(271, "dm", "Mass", 10)
    # pig 271 group_id not in [1,294288056]
    utils.test_get_invalid_input(271, "dm", "Mass", 0)
    utils.test_get_invalid_input(271, "dm", "Mass", 294288057)
    # pig id not in folder
    utils.test_get_invalid_input(20, "dm", "Mass", 203940)


#DM POTENTIAL
def test_get_dm_potential_271():
    response = client.get("/pig/271/dm/Potential/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 158970*1 array list
    data = json.loads(response.json()["dm_potential"])
    assert type(data) is list
    assert data[0] == -330457.6875
    assert data[:4] == [-330457.6875, -329781.90625, -330611.59375, -330459.625]
    assert len(data) == 158970

def test_get_dm_potential_negative():
    # missing required parameters
    utils.test_get_missing_input(271, "dm", "Potential", 10)
    # pig 271 group_id not in [1,294288056]
    utils.test_get_invalid_input(271, "dm", "Potential", 0)
    utils.test_get_invalid_input(271, "dm", "Potential", 294288057)
    # pig id not in folder
    utils.test_get_invalid_input(200, "dm", "Potential", 1)


#DM GENERATION
def test_get_dm_generation_271():
    response = client.get("/pig/271/dm/Generation/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 158970*1 array list
    data = json.loads(response.json()["dm_generation"])
    assert type(data) is list
    assert data[0] == 0
    assert data[:4] == [0, 0, 0, 0]
    assert len(data) == 158970

def test_get_dm_generation_negative():
    # missing required parameters
    utils.test_get_missing_input(271, "dm", "Generation", 5)
    # pig 271 group_id not in [1,294288056]
    utils.test_get_invalid_input(271, "dm", "Generation", 0)
    utils.test_get_invalid_input(271, "dm", "Generation", 294288057)
    # pig id not in folder
    utils.test_get_invalid_input(200, "dm", "Generation", -5)


#DM GROUPID
def test_get_dm_groupid_271():
    response = client.get("/pig/271/dm/GroupID/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 158970*1 array list
    data = json.loads(response.json()["dm_groupid"])
    assert type(data) is list
    assert data[0] == 10
    assert data[:4] == [10, 10, 10, 10]
    assert len(data) == 158970

def test_get_dm_groupid_negative():
    # missing required parameters
    utils.test_get_missing_input(271, "dm", "GroupID", 500)
    # pig 271 group_id not in [1,294288056]
    utils.test_get_invalid_input(271, "dm", "GroupID", 0)
    utils.test_get_invalid_input(271, "dm", "GroupID", 294288057)
    # pig id not in folder
    utils.test_get_invalid_input(200, "dm", "GroupID", 000)