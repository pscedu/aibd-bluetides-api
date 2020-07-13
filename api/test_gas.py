import json

from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


### endpoint: /pig/{id}/gas/position/{group_id}
# Basic positive tests
def test_get_gas_position():
    response = client.get("/pig/251/gas/position/1")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 446499*3 array list
    gas_position = json.loads(response.json()["gas_position"])
    assert type(gas_position) is list
    assert gas_position[0] == [278202.3184792972, 28013.68036349728, 248672.55276327548]
    assert len(gas_position[0]) == 3
    assert len(gas_position) == 446499
    assert response.headers["content-type"] == "application/json"


def test_get_gas_position_largeID():
    response = client.get("/pig/251/gas/position/2117968")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 12857*3 array list
    gas_position = json.loads(response.json()["gas_position"])
    assert type(gas_position) is list
    assert gas_position[3] == [198335.0403950171, 40257.09799530143, 189707.9848941324]
    assert len(gas_position[0]) == 3
    assert len(gas_position) == 804
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Missing required parameters
def test_get_gas_position_missing_input():
    response = client.get("/pig/251/gas/position/")
    # Validate the status code: 404
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. group_id not in [1,286036300]
def test_get_gas_position_invalid_group_id():
    response = client.get("/pig/251/gas/position/0")
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_gas_position_invalid_pig_id():
    response = client.get("/pig/1/gas/position/0")
    # Validate the status code: 404
    assert response.status_code == 404


### endpoint: /pig/{id}/gas/electron/{group_id}
# Basic positive tests
def test_get_gas_electron():
    response = client.get("/pig/251/gas/electron/1")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- gas electron data should be a 446499*1 array list
    gas_electron = json.loads(response.json()["gas_electron_abundance"])
    assert type(gas_electron) is list
    assert gas_electron[0] == 1.157894253730774
    assert len(gas_electron) == 446499
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Missing required parameters
def test_get_gas_electron_missing_input():
    response = client.get("/pig/251/gas/electron/")
    # Validate the status code: 404
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. group_id not in [1,286036300]
def test_get_gas_electron_invalid_group_id():
    response = client.get("/pig/251/gas/electron/286036301")
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_gas_electron_invalid_pig_id():
    response = client.get("/pig/1/gas/electron/1000")
    # Validate the status code: 404
    assert response.status_code == 404


### endpoint: /pig/{id}/gas/h2fraction/{group_id}
# Basic positive tests
def test_get_gas_h2fraction():
    response = client.get("/pig/251/gas/h2fraction/1")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- gas h2fraction data should be a 446499*1 array list
    gas_h2fraction = json.loads(response.json()["gas_h2fraction"])
    assert type(gas_h2fraction) is list
    assert gas_h2fraction[0] == 0.0
    assert gas_h2fraction[100000] == 0.9962370991706848
    assert len(gas_h2fraction) == 446499
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Missing required parameters
def test_get_gas_h2fraction_missing_input():
    response = client.get("/pig/251/gas/h2fraction/")
    # Validate the status code: 404
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. group_id not in [1,286036300]
def test_get_gas_h2fraction_invalid_group_id():
    response = client.get("/pig/251/gas/h2fraction/-1")
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_gas_h2fraction_invalid_pig_id():
    response = client.get("/pig/1/gas/h2fraction/1000")
    # Validate the status code: 404
    assert response.status_code == 404


### endpoint: /pig/{id}/gas/internalenergy/{group_id}
# Basic positive tests
def test_get_gas_internal_energy():
    response = client.get("/pig/251/gas/internalenergy/1")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 446499*1 array list
    gas_h2fraction = json.loads(response.json()["gas_internal_energy"])
    assert type(gas_h2fraction) is list
    assert gas_h2fraction[0] == 112487.609375
    assert len(gas_h2fraction) == 446499
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Missing required parameters
def test_get_gas_internal_energy_missing_input():
    response = client.get("/pig/251/gas/internalenergy/")
    # Validate the status code: 404
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. group_id not in [1,286036300]
def test_get_gas_internal_energy_invalid_group_id():
    response = client.get("/pig/251/gas/internalenergy/286036302")
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_gas_internal_energy_invalid_pig_id():
    response = client.get("/pig/1/gas/h2fraction/1000")
    # Validate the status code: 404
    assert response.status_code == 404
