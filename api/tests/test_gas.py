import json

from fastapi.testclient import TestClient

from ..main import app
from . import utils

client = TestClient(app)


### endpoint: /pig/{id}/gas/position/{group_id}
# Basic positive tests
def test_get_gas_position_251():
    response = client.get("/pig/251/gas/Position/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 446499*3 array list
    gas_position = json.loads(response.json()["gas_position"])
    assert type(gas_position) is list
    assert gas_position[0] == [278202.3184792972, 28013.68036349728, 248672.55276327548]
    assert len(gas_position[0]) == 3
    assert len(gas_position) == 446499

def test_get_gas_position_271():
    response = client.get("/pig/271/gas/Position/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 513379*3 array list
    gas_position = json.loads(response.json()["gas_position"])
    assert type(gas_position) is list
    assert gas_position[0] == [278198.07020316395, 27948.384391798045, 248697.5992484129]
    assert len(gas_position[0]) == 3
    assert len(gas_position) == 513379


def test_get_gas_position_largeID():
    response = client.get("/pig/251/gas/Position/2117968")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 804*3 array list
    gas_position = json.loads(response.json()["gas_position"])
    assert type(gas_position) is list
    assert gas_position[3] == [198335.0403950171, 40257.09799530143, 189707.9848941324]
    assert len(gas_position[0]) == 3
    assert len(gas_position) == 804


def test_get_gas_position_negative():
    # missing required parameters
    utils.test_get_missing_input(251, "gas", "Position", 10)
    utils.test_get_missing_input(271, "gas", "Position", 10)
    # pig 251 group_id not in [1,286036300] or pig 271 group_id not [1,294288056]
    utils.test_get_invalid_input(251, "gas", "Position", 0)
    utils.test_get_invalid_input(251, "gas", "Position", 286036301)
    utils.test_get_invalid_input(271, "gas", "Position", 0)
    utils.test_get_invalid_input(271, "gas", "Position", 294288057)
    # pig id not in folder
    utils.test_get_invalid_input(1, "gas", "Position", 10000)
    # invalid feature
    utils.test_get_invalid_input(10, "gas", "XXX", 100)


### endpoint: /pig/{id}/gas/electron/{group_id}
# Basic positive tests
def test_get_gas_electron_251():
    response = client.get("/pig/251/gas/ElectronAbundance/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas electron data should be a 446499*1 array list
    gas_electron = json.loads(response.json()["gas_electronabundance"])
    assert type(gas_electron) is list
    assert gas_electron[0] == 1.157894253730774
    assert len(gas_electron) == 446499


def test_get_gas_electron_271():
    response = client.get("/pig/271/gas/ElectronAbundance/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas electron data should be a 513379*1 array list
    gas_electron = json.loads(response.json()["gas_electronabundance"])
    assert type(gas_electron) is list
    assert gas_electron[0] == 1.157894492149353
    assert len(gas_electron) == 513379


def test_get_gas_electron_negative():
    # missing required parameters
    utils.test_get_missing_input(251, "gas", "ElectronAbundance", 100)
    utils.test_get_missing_input(271, "gas", "ElectronAbundance", 100)
    # pig 251 group_id not in [1,286036300] or pig 271 group_id not [1,294288056]
    utils.test_get_invalid_input(251, "gas", "ElectronAbundance", 0)
    utils.test_get_invalid_input(251, "gas", "ElectronAbundance", 286036301)
    utils.test_get_invalid_input(271, "gas", "ElectronAbundance", 0)
    utils.test_get_invalid_input(271, "gas", "ElectronAbundance", 294288060)
    # pig id not in folder
    utils.test_get_invalid_input(1000, "gas", "ElectronAbundance", 10000)
    # invalid feature
    utils.test_get_invalid_input(10, "gas", "Imom", 100)


### endpoint: /pig/{id}/gas/H2fraction/{group_id}
# Basic positive tests
def test_get_gas_h2fraction_251():
    response = client.get("/pig/251/gas/H2Fraction/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas h2fraction data should be a 446499*1 array list
    gas_h2fraction = json.loads(response.json()["gas_h2fraction"])
    assert type(gas_h2fraction) is list
    assert gas_h2fraction[0] == 0.0
    assert gas_h2fraction[100000] == 0.9962370991706848
    assert len(gas_h2fraction) == 446499

def test_get_gas_h2fraction_271():
    response = client.get("/pig/271/gas/H2Fraction/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas h2fraction data should be a 513379*1 array list
    gas_h2fraction = json.loads(response.json()["gas_h2fraction"])
    assert type(gas_h2fraction) is list
    assert gas_h2fraction[0] == 0.0
    assert gas_h2fraction[100000] == 0.13368326425552368
    assert len(gas_h2fraction) == 513379


def test_get_gas_h2fraction_negative():
    # missing required parameters
    utils.test_get_missing_input(251, "gas", "H2Fraction", 200)
    utils.test_get_missing_input(271, "gas", "H2Fraction", 200)
    # pig 251 group_id not in [1,286036300] or pig 271 group_id not [1,294288056]
    utils.test_get_invalid_input(251, "gas", "H2Fraction", -1)
    utils.test_get_invalid_input(251, "gas", "H2Fraction", 286036301)
    utils.test_get_invalid_input(271, "gas", "H2Fraction", -100)
    utils.test_get_invalid_input(271, "gas", "H2Fraction", 294288060)
    # pig id not in folder
    utils.test_get_invalid_input(2000, "gas", "H2Fraction", 10000)
    # invalid feature
    utils.test_get_invalid_input(10, "gas", "Imom", 100)


### endpoint: /pig/{id}/gas/InternalEnergy/{group_id}
# Basic positive tests
def test_get_gas_internal_energy_251():
    response = client.get("/pig/251/gas/InternalEnergy/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 446499*1 array list
    gas_internal_energy = json.loads(response.json()["gas_internalenergy"])
    assert type(gas_internal_energy) is list
    assert gas_internal_energy[0] == 112487.609375
    assert len(gas_internal_energy) == 446499


def test_get_gas_internal_energy_271():
    response = client.get("/pig/271/gas/InternalEnergy/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 513379*1 array list
    gas_internal_energy = json.loads(response.json()["gas_internalenergy"])
    assert type(gas_internal_energy) is list
    assert gas_internal_energy[0] == 163354.578125
    assert len(gas_internal_energy) == 513379


def test_get_gas_internal_energy_negative():
    # missing required parameters
    utils.test_get_missing_input(251, "gas", "InternalEnergy", 300)
    utils.test_get_missing_input(271, "gas", "InternalEnergy", 300)
    # pig 251 group_id not in [1,286036300] or pig 271 group_id not [1,294288056]
    utils.test_get_invalid_input(251, "gas", "InternalEnergy", -2)
    utils.test_get_invalid_input(251, "gas", "InternalEnergy", 286036302)
    utils.test_get_invalid_input(271, "gas", "InternalEnergy", -200)
    utils.test_get_invalid_input(271, "gas", "InternalEnergy", 294288060)
    # pig id not in folder
    utils.test_get_invalid_input(-1, "gas", "InternalEnergy", 10000)
    # invalid feature
    utils.test_get_invalid_input(10, "gas", "Jmom", 100)


### endpoint: /pig/{id}/gas/Density/{group_id}
# Basic positive tests
def test_get_gas_density_251():
    response = client.get("/pig/251/gas/Density/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 446499*1 array list
    gas_density = json.loads(response.json()["gas_density"])
    assert type(gas_density) is list
    assert gas_density[0] == 2.9312253957414214e-08
    assert gas_density[:4] == [2.9312253957414214e-08, 3.0495591829549085e-08, 3.838168538550235e-08, 4.375229067932196e-08]
    assert len(gas_density) == 446499


def test_get_gas_density_271():
    response = client.get("/pig/271/gas/Density/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 513379*1 array list
    gas_density = json.loads(response.json()["gas_density"])
    assert type(gas_density) is list
    assert gas_density[0] == 2.121526954113051e-08
    assert gas_density[:4] == [2.121526954113051e-08, 2.48780214207045e-08, 3.295386008517198e-08, 3.252150193588932e-08]
    assert len(gas_density) == 513379


def test_get_gas_density_negative():
    # missing required parameters
    utils.test_get_missing_input(251, "gas", "Density", 120)
    utils.test_get_missing_input(271, "gas", "Density", 120)
    # pig 251 group_id not in [1,286036300] or pig 271 group_id not [1,294288056]
    utils.test_get_invalid_input(251, "gas", "Density", 0)
    utils.test_get_invalid_input(251, "gas", "Density", 286036303)
    utils.test_get_invalid_input(271, "gas", "Density", -200)
    utils.test_get_invalid_input(271, "gas", "Density", 294288061)
    # pig id not in folder
    utils.test_get_invalid_input(-1, "gas", "Density", 120)
    # invalid feature
    utils.test_get_invalid_input(10, "gas", "Jmom", 120)


### endpoint: /pig/{id}/gas/Entropy/{group_id}
# Basic positive tests
def test_get_gas_entropy_251():
    response = client.get("/pig/251/gas/Entropy/100")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 446499*1 array list
    gas_entropy = json.loads(response.json()["gas_entropy"])
    assert type(gas_entropy) is list
    assert gas_entropy[0] == 2959285.5
    assert gas_entropy[:4] == [2959285.5, 77811.4609375, 100789.5625, 111917.515625]
    assert len(gas_entropy) == 68419


def test_get_gas_entropy_271():
    response = client.get("/pig/271/gas/Entropy/100")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 513379*1 array list
    gas_entropy = json.loads(response.json()["gas_entropy"])
    assert type(gas_entropy) is list
    assert gas_entropy[0] == 40433988.0
    assert gas_entropy[:4] == [40433988.0, 11036351.0, 22856564.0, 211525.53125]
    assert len(gas_entropy) == 77457


def test_get_gas_entropy_negative():
    # missing required parameters
    utils.test_get_missing_input(251, "gas", "Entropy", 330)
    utils.test_get_missing_input(271, "gas", "Entropy", 330)
    # pig 251 group_id not in [1,286036300] or pig 271 group_id not [1,294288056]
    utils.test_get_invalid_input(251, "gas", "Entropy", 0)
    utils.test_get_invalid_input(251, "gas", "Entropy", 286036400)
    utils.test_get_invalid_input(271, "gas", "Entropy", -10)
    utils.test_get_invalid_input(271, "gas", "Entropy", 294288100)
    # pig id not in folder
    utils.test_get_invalid_input(333, "gas", "Entropy", 330)
    # invalid feature
    utils.test_get_invalid_input(10, "gas", "abcd", 330)


### endpoint: /pig/{id}/gas/JUV/{group_id}
# Basic positive tests
def test_get_gas_juv_251():
    response = client.get("/pig/251/gas/JUV/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 446499*1 array list
    gas_juv = json.loads(response.json()["gas_juv"])
    assert type(gas_juv) is list
    assert gas_juv[0] == 9.999999682655225e-22
    assert len(gas_juv) == 134377


def test_get_gas_juv_271():
    response = client.get("/pig/271/gas/JUV/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 513379*1 array list
    gas_juv = json.loads(response.json()["gas_juv"])
    assert type(gas_juv) is list
    assert gas_juv[0] == 9.999999682655225e-22
    assert len(gas_juv) == 145402


def test_get_gas_juv_negative():
    # missing required parameters
    utils.test_get_missing_input(251, "gas", "JUV", 400)
    utils.test_get_missing_input(271, "gas", "JUV", 400)
    # pig 251 group_id not in [1,286036300] or pig 271 group_id not [1,294288056]
    utils.test_get_invalid_input(251, "gas", "JUV", -30)
    utils.test_get_invalid_input(251, "gas", "JUV", 286036400)
    utils.test_get_invalid_input(271, "gas", "JUV", 0)
    utils.test_get_invalid_input(271, "gas", "JUV", 294288100)
    # pig id not in folder
    utils.test_get_invalid_input(333, "gas", "JUV", 400)
    # invalid feature
    utils.test_get_invalid_input(10, "gas", "xyz", 400)
