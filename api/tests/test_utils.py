from fastapi.testclient import TestClient

# Common basic positive tests
def common_positive_tests(response):
    # Validate the status code: 200
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"