import json

from fastapi.testclient import TestClient
from main import app

# command: pytest

client = TestClient(app)


### endpoint: /pig/{id}/lengthbytype/{halo_id}/{type_id}
# Basic positive tests
def test_get_length():
    response = client.get("/pig/251/lengthbytype/100/1")
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
    response = client.get("/pig/251/lengthbytype//")
    # Validate the status code: 404
    assert response.status_code == 404
#######################################################################
def test_get_length_wrong_field():
    response = client.get("/pig/251/length/10/1")
    # Validate the status code: 404
    assert response.status_code == 404
#######################################################################

# Invalid value for endpoint parameters. E.g. halo_id not in [0,286036300) 
def test_get_length_invalid_haloid():
    response = client.get("/pig/251/lengthbytype/-1/5")
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. type_id not in [0,6)
def test_get_length_invalid_typeid():
    response = client.get("/pig/251/lengthbytype/5/10")
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_length_invalid_pig_id():
    response = client.get("/pig/200/lengthbytype/5/10")
    # Validate the status code: 404
    assert response.status_code == 404


### endpoint: /pig/{id}/offsetbytype/{halo_id}/
# Basic positive tests
def test_get_index():
    response = client.get("/pig/251/offsetbytype/100/")
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
    response = client.get("/pig/251/offsetbytype/")
    # Validate the status code: 404
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. halo_id not in [0,286036300) 
def test_get_index_invalid_haloid():
    response = client.get("/pig/251/offsetbytype/-1")
    # Validate the status code: 400
    assert response.status_code == 400
#####################################################################
def test_get_index_invalid_haloid_large():
    response = client.get("/pig/251/offsetbytype/286036400")
    # Validate the status code: 400
    assert response.status_code == 400
#####################################################################
# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_index_invalid_pig_id():
    response = client.get("/pig/200/offsetbytype/5")
    # Validate the status code: 404
    assert response.status_code == 404


### endpoint: /pig/
# Basic positive tests
def test_get_pig():
    response = client.get("/pig/")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object
    # response data -- LIST should be a list and match the file data.
    assert type(response.json()["LIST"]) is list
    assert response.json() == {
        "LIST": [
            "PIG_208",
            "PIG_230",
            "PIG_237",
            "PIG_216",
            "PIG_265",
            "PIG_244",
            "PIG_271",
            "PIG_258",
            "PIG_222",
            "PIG_251",
            "PIG_184",
            "PIG_197"
        ]
    }
    # Validate headers
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Invalid URL path.
def test_get_pig_invalid_url():
    response = client.get("/pig/2")
    # Validate the status code: 404
    assert response.status_code == 404
