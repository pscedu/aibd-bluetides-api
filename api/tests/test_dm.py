import json

from fastapi.testclient import TestClient

from ..main import app
from . import test_utils

client = TestClient(app)


###################################################################
#                           DM Tests                              #
################################################################### 

# Invalid feature for dm particle
def test_get_dm_invalid_feature():
    response = client.get("/pig/251/dm/H2Fraction/80")
    # Validate the status code: 404
    assert response.status_code == 404



#DM POSITION
### endpoint: /pig/{id}/dm/position/{group_id}
# Basic positive tests
def test_get_dm_position_244():
    response = client.get("/pig/244/dm/Position/331526")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 446499*3 array list
    dm_position = json.loads(response.json()["dm_position"])
    assert type(dm_position) is list
    assert dm_position[456] == [394903.89612031489, 43208.98194487528,257613.16877157817]
    assert len(dm_position[0]) == 3
    assert len(dm_position) == 2585


def test_get_dm_position_271():
    response = client.get("/pig/271/dm/Position/10")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 446499*3 array list
    dm_position = json.loads(response.json()["dm_position"])
    assert type(dm_position) is list
    assert dm_position[1] == [72973.67144294265, 195179.85487456998, 229742.43473667066]
    assert len(dm_position[0]) == 3
    assert len(dm_position) == 158970


# Negative testing with invalid input
# Missing required parameters
def test_get_dm_position_missing_input():
    # Validate the status code: 404 when missing group id or pig id or feature
    response = client.get("/pig/244/dm/Position/")
    assert response.status_code == 404
    response = client.get("/pig/271/dm/Position/")
    assert response.status_code == 404
    response = client.get("/pig//dm/Position/")
    assert response.status_code == 404
    response = client.get("/pig/271//Position/")
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. pig 244 group_id not in [1,282939566] or pig 271 group_id not in [1,294288056]
def test_get_dm_position_invalid_groupid():
    # Validate the status code: 400
    response = client.get("/pig/244/dm/Position/0")
    assert response.status_code == 400
    response = client.get("/pig/271/dm/Position/294288057")
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_dm_position_invalid_pig_id():
    # Validate the status code: 404
    response = client.get("/pig/200/dm/Position/80")
    assert response.status_code == 404
    

#DM VELOCITY
def test_get_dm_velocity_244():
    response = client.get("/pig/244/dm/Velocity/1862")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 12857*3 array list
    data = json.loads(response.json()["dm_velocity"])
    assert type(data) is list
    assert data[2000] == [14.788228034973145, 49.952144622802734,23.566410064697266]
    assert len(data[0]) == 3
    assert len(data) == 26324


def test_get_dm_velocity_271():
    response = client.get("/pig/271/dm/Velocity/10")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 12857*3 array list
    data = json.loads(response.json()["dm_velocity"])
    assert type(data) is list
    assert data[0] == [-2.3727707862854004, 65.58319854736328, 70.11107635498047]
    assert len(data[0]) == 3
    assert len(data) == 158970


# Negative testing with invalid input
# Missing required parameters
def test_get_dm_velocity_missing_input():
    # Validate the status code: 404
    response = client.get("/pig/244/dm/Velocity/")
    assert response.status_code == 404
    response = client.get("/pig/271/dm/Velocity/")
    assert response.status_code == 404
    response = client.get("/pig//dm/Velocity/10")
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. pig 244 group_id not in [1,282939566] or pig 271 group_id not in [1,294288056]
def test_get_dm_velocity_invalid_groupid():
    # Validate the status code: 400
    response = client.get("/pig/244/dm/Velocity/0")
    assert response.status_code == 400
    response = client.get("/pig/271/dm/Velocity/294288057")
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_dm_velocity_invalid_pig_id():
    # Validate the status code: 404
    response = client.get("/pig/20/dm/Velocity/203940")
    assert response.status_code == 404


#DM MASS
def test_get_dm_mass_271():
    response = client.get("/pig/271/dm/Mass/10")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 12857*1 array list
    data = json.loads(response.json()["dm_mass"])
    assert type(data) is list
    assert data[0] == 0.0011963852448388934
    assert data[:4] == [0.0011963852448388934, 0.0011963852448388934, 0.0011963852448388934, 0.0011963852448388934]
    assert len(data) == 158970


# Negative testing with invalid input
# Missing required parameters
def test_get_dm_mass_missing_input():
    # Validate the status code: 404
    response = client.get("/pig/271/dm/Mass/")
    assert response.status_code == 404
    response = client.get("/pig//dm/Mass/10")
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. pig 271 group_id not in [1,294288056]
def test_get_dm_mass_invalid_groupid():
    # Validate the status code: 400
    response = client.get("/pig/271/dm/Mass/0")
    assert response.status_code == 400
    response = client.get("/pig/271/dm/Mass/294288057")
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_dm_mass_invalid_pig_id():
    # Validate the status code: 404
    response = client.get("/pig/20/dm/Mass/203940")
    assert response.status_code == 404

