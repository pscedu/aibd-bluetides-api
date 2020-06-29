import json

from fastapi.testclient import TestClient
from main import app

# command: pytest

client = TestClient(app)


### endpoint: /lengthbytype/{halo_id}/{type_id}
# Basic positive tests
def test_get_length():
    response = client.get("/lengthbytype/100/1")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- length should match the file data.
    assert response.json() == {
        "halo_id": 100,
        "type_id": 1,
        "length": "74788"
    }
    # Validate headers
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Missing required parameters
def test_get_length_missing_input():
    response = client.get("/lengthbytype//")
    # Validate the status code: 404
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. halo_id not in [0,286036300) 
def test_get_length_invalid_haloid():
    response = client.get("/lengthbytype/-1/5")
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. type_id not in [0,6)
def test_get_length_invalid_typeid():
    response = client.get("/lengthbytype/5/10")
    # Validate the status code: 400
    assert response.status_code == 400


### endpoint: /offsetbytype/{halo_id}/
# Basic positive tests
def test_get_index():
    response = client.get("/offsetbytype/100")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object
    # response data -- beginning and ending index should be 1 row 6 colums array and match the file data.
    assert len(json.loads(response.json()["beginning_index"])) == 6
    assert len(json.loads(response.json()["ending_index"])) == 6
    assert response.json() == {
        "halo_id": 100,
        "beginning_index": "[9806101, 9899951, 0, 0, 8568855, 414]",
        "ending_index": "[9878038, 9974739, 0, 0, 8623594, 418]"
    }
    # Validate headers
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Missing required parameters
def test_get_index_missing_input():
    response = client.get("/offsetbytype/")
    # Validate the status code: 404
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. halo_id not in [0,286036300) 
def test_get_index_invalid_haloid():
    response = client.get("/offsetbytype/-1")
    # Validate the status code: 400
    assert response.status_code == 400
