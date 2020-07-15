from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

# Common basic positive tests
def common_positive_tests(response):
    # Validate the status code: 200
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Missing required parameters
def test_get_missing_input(id: int, type: str, attribute: str, group_id: int):
    # Validate the status code: 404
    response_without_group_id = client.get("/pig/{id}/{type}/{attribute}/".format(id = id, type = type, attribute = attribute))
    assert response_without_group_id.status_code == 404
    response_without_pig_id = client.get("/pig//{type}/{attribute}/{group_id}".format(type = type, attribute = attribute, group_id = group_id))
    assert response_without_pig_id.status_code == 404
    response_without_type = client.get("/pig/{id}//{attribute}/{group_id}".format(id = id, attribute = attribute, group_id = group_id))
    assert response_without_type.status_code == 404
    response_without_attribure = client.get("/pig/{id}/{type}//{group_id}".format(id = id, type = type, group_id = group_id))
    assert response_without_attribure.status_code == 404


# Invalid value for endpoint parameters.
def test_get_invalid_input(id: int, type: str, attribute: str, group_id: int):
    # Validate the status code: 404
    response = client.get("/pig/{id}/{type}/{attribute}/{group_id}".format(id = id, type = type, attribute = attribute, group_id = group_id))
    assert response.status_code == 404

