import json

from fastapi.testclient import TestClient

from ..main import app
from . import test_utils

client = TestClient(app)


### endpoint: /pig/{id}/gas/position/{group_id}
# Basic positive tests
def test_get_gas_position_251():
    response = client.get("/pig/251/gas/Position/1")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 446499*3 array list
    gas_position = json.loads(response.json()["gas_position"])
    assert type(gas_position) is list
    assert gas_position[0] == [278202.3184792972, 28013.68036349728, 248672.55276327548]
    assert len(gas_position[0]) == 3
    assert len(gas_position) == 446499

def test_get_gas_position_271():
    response = client.get("/pig/271/gas/Position/1")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 513379*3 array list
    gas_position = json.loads(response.json()["gas_position"])
    assert type(gas_position) is list
    assert gas_position[0] == [278198.07020316395, 27948.384391798045, 248697.5992484129]
    assert len(gas_position[0]) == 3
    assert len(gas_position) == 513379


def test_get_gas_position_largeID():
    response = client.get("/pig/251/gas/Position/2117968")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 804*3 array list
    gas_position = json.loads(response.json()["gas_position"])
    assert type(gas_position) is list
    assert gas_position[3] == [198335.0403950171, 40257.09799530143, 189707.9848941324]
    assert len(gas_position[0]) == 3
    assert len(gas_position) == 804


# Negative testing with invalid input
# Missing required parameters
def test_get_gas_position_missing_input():
    # Validate the status code: 404 when missing group id or pig id
    response = client.get("/pig/251/gas/Position/")
    assert response.status_code == 404
    response = client.get("/pig/271/gas/Position/")
    assert response.status_code == 404
    response = client.get("/pig//gas/Position/")
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. pig 251 group_id not in [1,286036300] or pig 271 group_id not [1,294288056]
def test_get_gas_position_invalid_group_id():
    # Validate the status code: 400 when group id is 0 or 286036301
    response = client.get("/pig/251/gas/Position/0")
    assert response.status_code == 400
    response = client.get("/pig/271/gas/Position/0")
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_gas_position_invalid_pig_id():
    response = client.get("/pig/1/gas/Position/0")
    # Validate the status code: 404
    assert response.status_code == 404


### endpoint: /pig/{id}/gas/electron/{group_id}
# Basic positive tests
def test_get_gas_electron_251():
    response = client.get("/pig/251/gas/ElectronAbundance/1")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas electron data should be a 446499*1 array list
    gas_electron = json.loads(response.json()["gas_electronabundance"])
    assert type(gas_electron) is list
    assert gas_electron[0] == 1.157894253730774
    assert len(gas_electron) == 446499


def test_get_gas_electron_271():
    response = client.get("/pig/271/gas/ElectronAbundance/1")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas electron data should be a 513379*1 array list
    gas_electron = json.loads(response.json()["gas_electronabundance"])
    assert type(gas_electron) is list
    assert gas_electron[0] == 1.157894492149353
    assert len(gas_electron) == 513379


# Negative testing with invalid input
# Missing required parameters
def test_get_gas_electron_missing_input():
    # Validate the status code: 404 when missing group id or pig id
    response = client.get("/pig/251/gas/ElectronAbundance/")
    assert response.status_code == 404
    response = client.get("/pig/271/gas/ElectronAbundance/")
    assert response.status_code == 404
    response = client.get("/pig//gas/ElectronAbundance/")
    assert response.status_code == 404

# Invalid value for endpoint parameters. E.g. pig 251 group_id not in [1,286036300] or pig 271 group_id not [1,294288056]
def test_get_gas_electron_invalid_group_id():
    # Validate the status code: 400 when group id is 286036301 in pig 271 and 0 in pig 251
    response = client.get("/pig/251/gas/ElectronAbundance/286036301")
    assert response.status_code == 400
    response1 = client.get("/pig/271/gas/ElectronAbundance/294288057")
    assert response1.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_gas_electron_invalid_pig_id():
    response = client.get("/pig/1/gas/ElectronAbundance/1000")
    # Validate the status code: 404
    assert response.status_code == 404


### endpoint: /pig/{id}/gas/h2fraction/{group_id}
# Basic positive tests
def test_get_gas_h2fraction_251():
    response = client.get("/pig/251/gas/H2Fraction/1")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas h2fraction data should be a 446499*1 array list
    gas_h2fraction = json.loads(response.json()["gas_h2fraction"])
    assert type(gas_h2fraction) is list
    assert gas_h2fraction[0] == 0.0
    assert gas_h2fraction[100000] == 0.9962370991706848
    assert len(gas_h2fraction) == 446499

def test_get_gas_h2fraction_271():
    response = client.get("/pig/271/gas/H2Fraction/1")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas h2fraction data should be a 513379*1 array list
    gas_h2fraction = json.loads(response.json()["gas_h2fraction"])
    assert type(gas_h2fraction) is list
    assert gas_h2fraction[0] == 0.0
    assert gas_h2fraction[100000] == 0.13368326425552368
    assert len(gas_h2fraction) == 513379


# Negative testing with invalid input
# Missing required parameters
def test_get_gas_h2fraction_missing_input():
    # Validate the status code: 404
    response = client.get("/pig/251/gas/H2Fraction/")
    assert response.status_code == 404
    response = client.get("/pig/271/gas/H2Fraction/")
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. pig 251 group_id not in [1,286036300] or pig 271 group_id not [1,294288056]
def test_get_gas_h2fraction_invalid_group_id():
    # Validate the status code: 400
    response = client.get("/pig/251/gas/H2Fraction/-1")
    assert response.status_code == 400
    response = client.get("/pig/271/gas/H2Fraction/-100")
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_gas_h2fraction_invalid_pig_id():
    response = client.get("/pig/1/gas/H2Fraction/1000")
    # Validate the status code: 404
    assert response.status_code == 404


### endpoint: /pig/{id}/gas/internalenergy/{group_id}
# Basic positive tests
def test_get_gas_internal_energy_251():
    response = client.get("/pig/251/gas/InternalEnergy/1")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 446499*1 array list
    gas_h2fraction = json.loads(response.json()["gas_internalenergy"])
    assert type(gas_h2fraction) is list
    assert gas_h2fraction[0] == 112487.609375
    assert len(gas_h2fraction) == 446499


def test_get_gas_internal_energy_271():
    response = client.get("/pig/271/gas/InternalEnergy/1")
    test_utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 513379*1 array list
    gas_h2fraction = json.loads(response.json()["gas_internalenergy"])
    assert type(gas_h2fraction) is list
    assert gas_h2fraction[0] == 163354.578125
    assert len(gas_h2fraction) == 513379

# Negative testing with invalid input
# Missing required parameters
def test_get_gas_internal_energy_missing_input():
    # Validate the status code: 404
    response = client.get("/pig/251/gas/InternalEnergy/")
    assert response.status_code == 404
    response = client.get("/pig/271/gas/InternalEnergy/")
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. pig 251 group_id not in [1,286036300] or pig 271 group_id not [1,294288056]
def test_get_gas_internal_energy_invalid_group_id():
    # Validate the status code: 400
    response = client.get("/pig/251/gas/InternalEnergy/286036302")
    assert response.status_code == 400
    response = client.get("/pig/251/gas/InternalEnergy/294288057")
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_gas_internal_energy_invalid_pig_id():
    # Validate the status code: 404
    response = client.get("/pig/1/gas/InternalEnergy/1000")
    assert response.status_code == 404
