import json

from fastapi.testclient import TestClient

from ..main import app
from . import utils

client = TestClient(app)

def test_get_negative_star():
    utils.test_get_negative("star")