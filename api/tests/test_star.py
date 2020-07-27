import json

from fastapi.testclient import TestClient

from ..main import app
from . import utils

client = TestClient(app)

def test_get_negative_star():
    utils.test_get_negative("star")


### endpoint: /pig/{id}/star/Velocity/{group_id}
# Basic positive tests
def test_get_star_velocity_251():
    response = client.get("/pig/251/star/Velocity/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Velocity data should be a 561897*3 array list
    star_velocity = json.loads(response.json()["star_velocity"])
    assert type(star_velocity) is list
    assert star_velocity[0] == [37.31153869628906, 0.5733818411827087, 84.45280456542969]
    assert len(star_velocity) == 561897


def test_get_star_velocity_271():
    response = client.get("/pig/271/star/Velocity/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Velocity data should be a 622535*3 array list
    star_velocity = json.loads(response.json()["star_velocity"])
    assert type(star_velocity) is list
    assert star_velocity[0] == [-36.19582748413086, -32.4619255065918, 53.46745681762695]
    assert len(star_velocity) == 622535


### endpoint: /pig/{id}/star/Generation/{group_id}
# Basic positive tests
def test_get_star_generation_251():
    response = client.get("/pig/251/star/Generation/2")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Generation data should be a 1*1 array list
    star_generation = json.loads(response.json()["star_generation"])
    assert type(star_generation) is list
    assert star_generation == [1]
    assert len(star_generation) == 1


def test_get_star_generation_271():
    response = client.get("/pig/271/star/Generation/2")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Generation data should be a 7*1 array list
    star_generation = json.loads(response.json()["star_generation"])
    assert type(star_generation) is list
    assert star_generation == [1, 3, 1, 1, 1, 1, 1]
    assert len(star_generation) == 7


### endpoint: /pig/{id}/star/GroupID/{group_id}
# Basic positive tests
def test_get_star_groupid_251():
    response = client.get("/pig/251/star/GroupID/3")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star GroupID data should be a 173607*1 array list
    star_groupid = json.loads(response.json()["star_groupid"])
    assert type(star_groupid) is list
    assert star_groupid[0] == 3
    assert star_groupid[1000] == 3
    assert len(star_groupid) == 173607


def test_get_star_groupid_271():
    response = client.get("/pig/271/star/GroupID/4")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star GroupID data should be a 232226*1 array list
    star_groupid = json.loads(response.json()["star_groupid"])
    assert type(star_groupid) is list
    assert star_groupid[0] == 4
    assert star_groupid[4000] == 4
    assert len(star_groupid) == 232226


### endpoint: /pig/{id}/star/Mass/{group_id}
# Basic positive tests
def test_get_star_mass_251():
    response = client.get("/pig/251/star/Mass/5")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Mass data should be a 83207*1 array list
    star_mass = json.loads(response.json()["star_mass"])
    assert type(star_mass) is list
    assert star_mass[0] == 5.9055611927760765e-05
    assert star_mass[:4] == [5.9055611927760765e-05, 5.9055611927760765e-05, 5.9055611927760765e-05, 5.9055611927760765e-05]
    assert len(star_mass) == 83207


def test_get_star_mass_271():
    response = client.get("/pig/271/star/Mass/5")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Mass data should be a 129814*1 array list
    star_mass = json.loads(response.json()["star_mass"])
    assert type(star_mass) is list
    assert star_mass[0] == 5.9055611927760765e-05
    assert star_mass[:4] == [5.9055611927760765e-05, 5.9055611927760765e-05, 5.9055611927760765e-05, 5.9055611927760765e-05]
    assert len(star_mass) == 129814


### endpoint: /pig/{id}/star/Metallicity/{group_id}
# Basic positive tests
def test_get_star_metallicity_251():
    response = client.get("/pig/251/star/Metallicity/6")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 112913*1 array list
    star_metallicity = json.loads(response.json()["star_metallicity"])
    assert type(star_metallicity) is list
    assert star_metallicity[0] == 0.00014949783508200198
    assert star_metallicity[:4] == [0.00014949783508200198, 2.5153325623250566e-05, 9.778260573511943e-05, 6.009096250636503e-05]
    assert len(star_metallicity) == 112913


def test_get_star_metallicity_271():
    response = client.get("/pig/271/star/Metallicity/6")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Metallicity data should be a 166805*1 array list
    star_metallicity = json.loads(response.json()["star_metallicity"])
    assert type(star_metallicity) is list
    assert star_metallicity[0] == 0.0005383077659644186
    assert star_metallicity[:4] == [0.0005383077659644186, 0.00023857371706981212, 9.642468648962677e-05, 0.00032759408350102603]
    assert len(star_metallicity) == 166805


### endpoint: /pig/{id}/star/Position/{group_id}
# Basic positive tests
def test_get_star_position_251():
    response = client.get("/pig/251/star/Position/7")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Position data should be a 72130*1 array list
    star_position = json.loads(response.json()["star_position"])
    assert type(star_position) is list
    assert star_position[0] == [15306.750499744992, 146851.4949004134, 290343.8793858092]
    assert star_position[1] == [15299.60735418374, 146849.01632511956, 290340.75453723327]
    assert len(star_position) == 72130


def test_get_star_position_271():
    response = client.get("/pig/271/star/Position/7")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Position data should be a 87826*1 array list
    star_position = json.loads(response.json()["star_position"])
    assert type(star_position) is list
    assert star_position[0] == [15291.412338536844, 146606.6175727497, 290255.58836157114]
    assert star_position[1] == [15291.47553922203, 146606.87190717706, 290255.52017585444]
    assert len(star_position) == 87826


### endpoint: /pig/{id}/star/Potential/{group_id}
# Basic positive tests
def test_get_star_potential_251():
    response = client.get("/pig/251/star/Potential/8")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Potential data should be a 112659*1 array list
    star_potential = json.loads(response.json()["star_potential"])
    assert type(star_potential) is list
    assert star_potential[0] == -325438.15625
    assert star_potential[4] == -323459.0
    assert len(star_potential) == 112659


def test_get_star_potential_271():
    response = client.get("/pig/271/star/Potential/8")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star Potential data should be a 88416*1 array list
    star_potential = json.loads(response.json()["star_potential"])
    assert type(star_potential) is list
    assert star_potential[0] == 67014.3359375
    assert star_potential[4] == 66768.3671875
    assert len(star_potential) == 88416


### endpoint: /pig/{id}/star/StarFormationTime/{group_id}
# Basic positive tests
def test_get_star_starformationtime_251():
    response = client.get("/pig/251/star/StarFormationTime/9")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star StarFormationTime data should be a 112659*1 array list
    star_starformationtime = json.loads(response.json()["star_starformationtime"])
    assert type(star_starformationtime) is list
    assert star_starformationtime[0] == 0.11749737709760666
    assert star_starformationtime[:4] == [0.11749737709760666, 0.11677927523851395, 0.12459807097911835, 0.12012547254562378]
    assert len(star_starformationtime) == 103097


def test_get_star_starformationtime_271():
    response = client.get("/pig/271/star/StarFormationTime/9")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- star StarFormationTime data should be a 88416*1 array list
    star_starformationtime = json.loads(response.json()["star_starformationtime"])
    assert type(star_starformationtime) is list
    assert star_starformationtime[0] == 0.12901991605758667
    assert star_starformationtime[:4] == [0.12901991605758667, 0.12974964082241058, 0.12079867720603943, 0.10510993748903275]
    assert len(star_starformationtime) == 102714
