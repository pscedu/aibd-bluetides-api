import json

from fastapi.testclient import TestClient

from ..main import app
from . import test_utils

client = TestClient(app)


### endpoint: /pig/{id}/offsetbytype/{halo_id}/
# Basic positive tests
def test_get_index_251():
    response = client.get("/pig/251/offsetbytype/100/")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object
    # response data -- beginning and ending index should be 1 row 6 colums array and match the file data.
    assert len(json.loads(response.json()["beginning_index"])) == 6
    assert len(json.loads(response.json()["ending_index"])) == 6
    assert response.json() == {
        "halo_id": 100,
        "beginning_index": "[9806101, 9899951, 0, 0, 8568855, 414]",
        "ending_index": "[9878038, 9974739, 0, 0, 8623594, 418]"
    }


def test_get_index_271():
    response = client.get("/pig/271/offsetbytype/1/")
    test_utils.common_positive_tests(response)
    assert len(json.loads(response.json()["beginning_index"])) == 6
    assert len(json.loads(response.json()["ending_index"])) == 6
    assert response.json() == {
        "halo_id": 1,
        "beginning_index": "[513379, 579338, 0, 0, 622535, 9]",
        "ending_index": "[1305331, 579338, 0, 0, 622542, 9]"
    }


# Negative testing with invalid input
# Missing required parameters
def test_get_index_missing_input():
    # Validate the status code: 404
    response = client.get("/pig/251/offsetbytype/")
    assert response.status_code == 404
    response = client.get("/pig/271/offsetbytype/")
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. pig 251 halo_id not in [0,286036300) and pig 271 halo_id not in [0,294288056)
def test_get_index_invalid_haloid():
    # Validate the status code: 400
    response = client.get("/pig/251/offsetbytype/-1")
    assert response.status_code == 400
    response = client.get("/pig/271/offsetbytype/294288056")
    assert response.status_code == 400


def test_get_index_invalid_haloid_large():
    response = client.get("/pig/251/offsetbytype/286036400")
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_index_invalid_pig_id():
    # Validate the status code: 404
    response = client.get("/pig/200/offsetbytype/5")
    assert response.status_code == 404
    response = client.get("/pig/0/offsetbytype/5")
    assert response.status_code == 404
