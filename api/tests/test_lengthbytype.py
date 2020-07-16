from fastapi.testclient import TestClient

from ..main import app
from . import test_utils

client = TestClient(app)


# endpoint: /pig/{id}/lengthbytype/{halo_id}/{type_id}
# Basic positive tests
def test_get_length_251():
    response = client.get("/pig/251/lengthbytype/100/1")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- length should match the file data.
    assert response.json() == {
        "halo_id": 100,
        "type_id": 1,
        "length": "74788"
    }


def test_get_length_271():
    response = client.get("/pig/271/lengthbytype/100/1")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- length should match the file data.
    assert response.json() == {
        "halo_id": 100,
        "type_id": 1,
        "length": "87802"
    }


# Negative testing with invalid input
# Missing required parameters
def test_get_length_missing_input():
    # Validate the status code: 404 when missing input for pig 251 and pig 271
    response = client.get("/pig/251/lengthbytype//")
    assert response.status_code == 404
    response = client.get("/pig/271/lengthbytype//")
    assert response.status_code == 404


def test_get_length_wrong_field():
    # Validate the status code: 404 when input wrong field
    response = client.get("/pig/251/length/10/1")
    assert response.status_code == 404
    response = client.get("/pig/271/lbt/10/1")
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. pig 251 halo_id not in [0,286036300) and pig 271 halo_id not in [0,294288056)
def test_get_length_invalid_haloid():
    # Validate the status code: 400 when halo id is invalid
    response = client.get("/pig/251/lengthbytype/-1/5")
    assert response.status_code == 404
    response = client.get("/pig/251/lengthbytype/-100/5")
    assert response.status_code == 404
    response = client.get("/pig/251/lengthbytype/294288057/5")
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. type_id not in [0,6)
def test_get_length_invalid_typeid():
    # Validate the status code: 400 when type id is invalid
    response = client.get("/pig/251/lengthbytype/5/10")
    assert response.status_code == 404
    response = client.get("/pig/251/lengthbytype/5/-1")
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_length_invalid_pig_id():
    # Validate the status code: 404
    response = client.get("/pig/200/lengthbytype/5/10")
    assert response.status_code == 404


### endpoint: /pig/{id}/lengthbytype/n={num}
# Basic positive tests
def test_get_lbt_251():
    response = client.get("/pig/251/lengthbytype/n=4")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- length should match the file data.
    assert response.json() == {
        "length_by_type": "[[446499, 507723, 0, 0, 561897, 7], [700225, 0, 0, 0, 1, 0], "
                          "[239021, 247773, 0, 0, 173607, 8], [125966, 152736, 0, 0, 206388, 2]]"
    }


def test_get_lbt_271():
    response = client.get("/pig/271/lengthbytype/n=4")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- length should match the file data.
    assert response.json() == {
        "length_by_type": "[[513379, 579338, 0, 0, 622535, 9], [791952, 0, 0, 0, 7, 0], [226008, 237161, 0, 0, 182457, 7], [127491, 160510, 0, 0, 232226, 2]]"
    }


# Negative testing with invalid input
# Missing required parameters
def test_get_lbt_missing_input():
    # Validate the status code: 404
    response = client.get("/pig/251/lengthbytype/")
    assert response.status_code == 404
    response = client.get("/pig/271/lengthbytype/")
    assert response.status_code == 404

# Invalid value for endpoint parameters. E.g. pig 251 halo_id not in [0,286036300) and pig 271 halo_id not in [0,294288056)
def test_get_lbt_invalid_num():
    # Validate the status code: 400
    response = client.get("/pig/251/lengthbytype/n=-1")
    assert response.status_code == 404
    response = client.get("/pig/271/lengthbytype/n=-10")
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_lbt_invalid_pig_id():
    # Validate the status code: 404
    response = client.get("/pig/200/lengthbytype/n=4")
    assert response.status_code == 404
    response = client.get("/pig/100/lengthbytype/n=4")
    assert response.status_code == 404


### endpoint: /pig/{id}/lengthbytype/{halo_id}/
# Basic positive tests
def test_get_lbh_251():
    response = client.get("/pig/251/lengthbytype/100")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- length should match the file data.
    assert response.json() == {
        "halo_id": 100,
        "type_length": "[71937, 74788, 0, 0, 54739, 4]"
    }


def test_get_lbh_271():
    response = client.get("/pig/271/lengthbytype/100")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- length should match the file data.
    assert response.json() == {
        "halo_id": 100,
        "type_length": "[89069, 87802, 0, 0, 50623, 5]"
    }


# Negative testing with invalid input
# Missing required parameters
def test_get_lbh_missing_input():
    # Validate the status code: 404
    response = client.get("/pig/251/lengthbytype/")
    assert response.status_code == 404
    response = client.get("/pig/271/lengthbytype/")
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. pig 251 halo_id not in [0,286036300) and pig 271 halo_id not in [0,294288056)
def test_get_lbh_invalid_haloid():
    # Validate the status code: 400
    response = client.get("/pig/251/lengthbytype/-1")
    assert response.status_code == 404
    response = client.get("/pig/271/lengthbytype/294288056")
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_lbh_invalid_pig_id():
    # Validate the status code: 404
    response = client.get("/pig/200/lengthbytype/5/")
    assert response.status_code == 404
