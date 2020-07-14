import json

from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


###################################################################
#                           DM Tests                              #
################################################################### 

#DM POSITION

### endpoint: /pig/{id}/gas/position/{group_id}
# Basic positive tests
def test_get_dm_position():
    response = client.get("/pig/244/dm/Position/331526")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 446499*3 array list
    dm_position = json.loads(response.json()["dm_position"])
    assert type(dm_position) is list
    assert dm_position[456] == [394903.89612031489, 43208.98194487528,257613.16877157817]
    assert len(dm_position[0]) == 3
    assert len(dm_position) == 2585
    assert response.headers["content-type"] == "application/json"

# Negative testing with invalid input
# Missing required parameters
def test_get_dm_position_missing_input():
    response = client.get("/pig/244/dm/Position/")
    # Validate the status code: 404
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. group_id not in [1,286036300) 
def test_get_dm_position_invalid_groupid():
    response = client.get("/pig/244/dm/Position/0")
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_dm_position_invalid_pig_id():
    response = client.get("/pig/200/dm/Position/80")
    # Validate the status code: 404
    assert response.status_code == 404




#DM VELOCITY
def test_get_dm_velocity():
    response = client.get("/pig/244/dm/Velocity/1862")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 12857*3 array list
    data = json.loads(response.json()["dm_velocity"])
    assert type(data) is list
    assert data[2000] == [14.788228034973145, 49.952144622802734,23.566410064697266]
    assert len(data[0]) == 3
    assert len(data) == 26324
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Missing required parameters
def test_get_dm_velocity_missing_input():
    response = client.get("/pig/244/dm/Velocity/")
    # Validate the status code: 404
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. group_id not in [1,286036300) 
def test_get_dm_velocity_invalid_groupid():
    response = client.get("/pig/244/dm/Velocity/0")
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_dm_velocity_invalid_pig_id():
    response = client.get("/pig/20/dm/Velocity/203940")
    # Validate the status code: 404
    assert response.status_code == 404
