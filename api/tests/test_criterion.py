import json

from fastapi.testclient import TestClient

from ..main import app
from . import utils

client = TestClient(app)

# def test_criterion_positive_271():
#     response = client.get("/pig/271/search/bh/BlackholeMass/bh_mass",params={"min_range":5e-3,"max_range":1e-2})
#     utils.common_positive_tests(response)
#     idlist = sorted(response.json().keys())
#     assert idlist[:10] == [str(i) for i in [0,2,7,8,11,14,18,19,29,34]]
#     bhmass = json.loads(response.json()[idlist[10]])
#     assert type(bhmass) is list
#     assert len(bhmass) == 5
#     assert bhmass == [8.8822002e-05, 1.0435666e-04, 4.1642028e-04, 5.1176852e-05, 7.6095015e-03]