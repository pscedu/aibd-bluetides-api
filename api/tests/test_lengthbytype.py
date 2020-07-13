from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


# endpoint: /pig/{id}/lengthbytype/{halo_id}/{type_id}
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


### endpoint: /pig/{id}/lengthbytype/n={num}
# Basic positive tests
def test_get_lbt():
    response = client.get("/pig/251/lengthbytype/n=4")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- length should match the file data.
    assert response.json() == {
        "length_by_type": "[[446499, 507723, 0, 0, 561897, 7], [700225, 0, 0, 0, 1, 0], "
                          "[239021, 247773, 0, 0, 173607, 8], [125966, 152736, 0, 0, 206388, 2]]"
    }
    # Validate headers
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Missing required parameters
def test_get_lbt_missing_input():
    response = client.get("/pig/251/lengthbytype/")
    # Validate the status code: 404
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. halo_id not in [0,286036300) 
def test_get_lbt_invalid_num():
    response = client.get("/pig/251/lengthbytype/n=-1")
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_lbt_invalid_pig_id():
    response = client.get("/pig/200/lengthbytype/n=4")
    # Validate the status code: 404
    assert response.status_code == 404


### endpoint: /pig/{id}/lengthbytype/{halo_id}/
# Basic positive tests
def test_get_lbh():
    response = client.get("/pig/251/lengthbytype/100")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- length should match the file data.
    assert response.json() == {
        "halo_id": 100,
        "type_length": "[71937, 74788, 0, 0, 54739, 4]"
    }
    # Validate headers
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Missing required parameters
def test_get_lbh_missing_input():
    response = client.get("/pig/251/lengthbytype/")
    # Validate the status code: 404
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. halo_id not in [0,286036300) 
def test_get_lbh_invalid_haloid():
    response = client.get("/pig/251/lengthbytype/-1")
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_lbh_invalid_pig_id():
    response = client.get("/pig/200/lengthbytype/5/")
    # Validate the status code: 404
    assert response.status_code == 404
