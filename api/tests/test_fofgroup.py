import json

from fastapi.testclient import TestClient

from ..main import app
from . import utils

client = TestClient(app)



#     ### endpoint: /pig/{id}/MassCenterPosition/{halo_id}/{type_id}
# # Basic positive tests
# def test_get_mcp():
#     response = client.get("/pig/251/MassCenterPosition/100/1")
#     # Validate the status code: 200
#     assert response.status_code == 200
#     # Validate payload: Response is a well-formed JSON object and response data -- length should match the file data.
#     assert response.json() == {
#         "halo_id": 100,
#         "type_id": 1,
#         "length": "74788"
#     }
#     # Validate headers
#     assert response.headers["content-type"] == "application/json"



# ### endpoint: /pig/{id}/gas/JUV/{group_id}
# # Basic positive tests
# def test_get_fofgroup_mcv_251():
#     response = client.get("/pig/251/fofgroup/MassCenterVelocity/10")
#     utils.common_positive_tests(response)
#     # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 446499*1 array list
#     fof_mcv = json.loads(response.json()["fofgroup_masscentervelocity"])
#     assert type(gas_juv) is list
#     assert gas_juv[0] == 9.999999682655225e-22
#     assert len(gas_juv) == 134377


# def test_get_fofgroup_mcv_271():
#     response = client.get("/pig/271/fofgroup/MassCenterVelocity/10")
#     utils.common_positive_tests(response)
#     # Validate payload: Response is a well-formed JSON object and response data -- gas internal_energy data should be a 513379*1 array list
#     fof_mcv = json.loads(response.json()["fofgroup_masscentervelocity"])
#     assert type(gas_juv) is list
#     assert gas_juv[0] == 9.999999682655225e-22
#     assert len(gas_juv) == 145402


    
    
def test_get_fofgroup_negative():
    # missing required parameters
    for field in ['MassCenterVelocity','MassCenterPosition',]:
        utils.test_get_missing_input(251, "FoFGroup", field, 400)
        utils.test_get_missing_input(271, "FoFGroup", field, 400)
        # pig 251 group_id not in [1,286036300] or pig 271 group_id not [1,294288056]
        utils.test_get_invalid_input(251, "FoFGroup", field, -30)
        utils.test_get_invalid_input(251, "FoFGroup", field, 286036400)
        utils.test_get_invalid_input(271, "FoFGroup", field, 0)
        utils.test_get_invalid_input(271, "FoFGroup", field, 294288100)
        # pig id not in folder
        utils.test_get_invalid_input(333, "FoFGroup", field, 400)
        # invalid feature
        utils.test_get_invalid_input(10, "FoFGroup", "xyz", 400)