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