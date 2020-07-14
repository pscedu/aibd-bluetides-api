import json

from fastapi.testclient import TestClient
from main import app

# command: pytest

client = TestClient(app)


###################################################################
#                           FoFGroup Tests                        #
###################################################################  
### endpoint: /pig/{id}/lengthbytype/{halo_id}/{type_id}
# Basic positive tests
def test_get_length():
    response = client.get("/pig/251/lengthbytype/100/1")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- length should match the file data.
    assert response.json() == {
        "halo_id": 100,
        "type_id": 1,
        "length": "74788"
    }
    # Validate headers
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Missing required parameters
def test_get_length_missing_input():
    response = client.get("/pig/251/lengthbytype//")
    # Validate the status code: 404
    assert response.status_code == 404
#######################################################################
def test_get_length_wrong_field():
    response = client.get("/pig/251/length/10/1")
    # Validate the status code: 404
    assert response.status_code == 404
#######################################################################

# Invalid value for endpoint parameters. E.g. halo_id not in [0,286036300) 
def test_get_length_invalid_haloid():
    response = client.get("/pig/251/lengthbytype/-1/5")
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. type_id not in [0,6)
def test_get_length_invalid_typeid():
    response = client.get("/pig/251/lengthbytype/5/10")
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_length_invalid_pig_id():
    response = client.get("/pig/200/lengthbytype/5/10")
    # Validate the status code: 404
    assert response.status_code == 404


### endpoint: /pig/{id}/lengthbytype/n={num}
# Basic positive tests
def test_get_lbt():
    response = client.get("/pig/251/lengthbytype/n=4")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- length should match the file data.
    assert response.json() == {
        "length_by_type": "[[446499, 507723, 0, 0, 561897, 7], [700225, 0, 0, 0, 1, 0], [239021, 247773, 0, 0, 173607, 8], [125966, 152736, 0, 0, 206388, 2]]"
    }
    # Validate headers
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Missing required parameters
def test_get_lbt_missing_input():
    response = client.get("/pig/251/lengthbytype/")
    # Validate the status code: 404
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. halo_id not in [0,286036300) 
def test_get_lbt_invalid_num():
    response = client.get("/pig/251/lengthbytype/n=-1")
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_lbt_invalid_pig_id():
    response = client.get("/pig/200/lengthbytype/n=4")
    # Validate the status code: 404
    assert response.status_code == 404


### endpoint: /pig/{id}/lengthbytype/{halo_id}/
# Basic positive tests
def test_get_lbh():
    response = client.get("/pig/251/lengthbytype/100")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- length should match the file data.
    assert response.json() == {
        "halo_id": 100,
        "type_length": "[71937, 74788, 0, 0, 54739, 4]"
    }
    # Validate headers
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Missing required parameters
def test_get_lbh_missing_input():
    response = client.get("/pig/251/lengthbytype/")
    # Validate the status code: 404
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. halo_id not in [0,286036300) 
def test_get_lbh_invalid_haloid():
    response = client.get("/pig/251/lengthbytype/-1")
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_lbh_invalid_pig_id():
    response = client.get("/pig/200/lengthbytype/5/")
    # Validate the status code: 404
    assert response.status_code == 404


### endpoint: /pig/{id}/offsetbytype/{halo_id}/
# Basic positive tests
def test_get_index():
    response = client.get("/pig/251/offsetbytype/100/")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object
    # response data -- beginning and ending index should be 1 row 6 colums array and match the file data.
    assert len(json.loads(response.json()["beginning_index"])) == 6
    assert len(json.loads(response.json()["ending_index"])) == 6
    assert response.json() == {
        "halo_id": 100,
        "beginning_index": "[9806101, 9899951, 0, 0, 8568855, 414]",
        "ending_index": "[9878038, 9974739, 0, 0, 8623594, 418]"
    }
    # Validate headers
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Missing required parameters
def test_get_index_missing_input():
    response = client.get("/pig/251/offsetbytype/")
    # Validate the status code: 404
    assert response.status_code == 404


# Invalid value for endpoint parameters. E.g. halo_id not in [0,286036300) 
def test_get_index_invalid_haloid():
    response = client.get("/pig/251/offsetbytype/-1")
    # Validate the status code: 400
    assert response.status_code == 400
#####################################################################
def test_get_index_invalid_haloid_large():
    response = client.get("/pig/251/offsetbytype/286036400")
    # Validate the status code: 400
    assert response.status_code == 400
#####################################################################
# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
def test_get_index_invalid_pig_id():
    response = client.get("/pig/200/offsetbytype/5")
    # Validate the status code: 404
    assert response.status_code == 404


### endpoint: /pig/
# Basic positive tests
def test_get_pig():
    response = client.get("/pig/")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object
    # response data -- LIST should be a list and match the file data.
    assert type(response.json()["LIST"]) is list
    assert type(response.json()["LIST"][0]["num_halos"]) is int
    assert type(response.json()["LIST"][0]["time"]) is float
    assert response.json() == {
        "LIST": [
            {
            "id": "208", "name": "PIG_208", "num_halos": 267649410, "time": 7.000000015821968
            },
            {
            "id": "230", "name": "PIG_230", "num_halos": 276771522, "time": 6.8500000034945225
            },
            {
            "id": "237", "name": "PIG_237", "num_halos": 279858719, "time": 6.800000003768498
            },
            {
            "id": "216", "name": "PIG_216", "num_halos": 271256543, "time": 6.94000002648998
            },
            {
            "id": "265", "name": "PIG_265", "num_halos": 292040891, "time": 6.600000041506778
            },
            {
            "id": "244", "name": "PIG_244", "num_halos": 282939566, "time": 6.750000008196768
            },
            {
            "id": "271", "name": "PIG_271", "num_halos": 294288056, "time": 6.560000154967445
            },
            {
            "id": "258", "name": "PIG_258", "num_halos": 289106271, "time": 6.650000043417158
            },
            {
            "id": "222", "name": "PIG_222", "num_halos": 273696821, "time": 6.900000011215548
            },
            {
            "id": "251", "name": "PIG_251", "num_halos": 286036300, "time": 6.700000064799543
            },
            {
            "id": "184", "name": "PIG_184", "num_halos": 255434058, "time": 7.200000019001509
            },
            {
            "id": "197", "name": "PIG_197", "num_halos": 261596356, "time": 7.100000019919435
            }
        ]
    }
    # Validate headers
    assert response.headers["content-type"] == "application/json"


# Negative testing with invalid input
# Invalid URL path.
def test_get_pig_invalid_url():
    response = client.get("/pig/2")
    # Validate the status code: 404
    assert response.status_code == 404
    
    
    
 ### endpoint: /pig/{id}/MassCenterPosition/{halo_id}/{type_id}
# Basic positive tests
def test_get_mcp():
    response = client.get("/pig/251/MassCenterPosition/100/1")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- length should match the file data.
    assert response.json() == {
        "halo_id": 100,
        "type_id": 1,
        "length": "74788"
    }
    # Validate headers
    assert response.headers["content-type"] == "application/json"


    
### endpoint: /pig/{id}/MassCenterVelocity/{halo_id}/{type_id}
# Basic positive tests
def test_get_mcp():
    response = client.get("/pig/251/MassCenterVelocity/100/1")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- length should match the file data.
    assert response.json() == {
        "halo_id": 100,
        "type_id": 1,
        "length": "74788"
    }
    # Validate headers
    assert response.headers["content-type"] == "application/json"

    
###################################################################
#                           Gas Tests                             #
###################################################################    

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
    
<<<<<<< HEAD

=======
    
>>>>>>> master
def test_get_gas_position_largeID():
    response = client.get("/pig/251/gas/position/2117968")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 12857*3 array list
    gas_position = json.loads(response.json()["gas_position"])
    assert type(gas_position) is list
    assert gas_position[3] == [198335.0403950171, 40257.09799530143,189707.9848941324]
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
<<<<<<< HEAD
    
    
    
###################################################################
#                           DM Tests                              #
################################################################### 
    
#DM POSITION

### endpoint: /pig/{id}/gas/position/{group_id}
# Basic positive tests
def test_get_dm_position():
    response = client.get("/pig/244/dm/position/331526")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 446499*3 array list
    dm_position = json.loads(response.json()["dm_position"])
    assert type(dm_position) is list
    assert dm_position[456] == [394903.89612031489, 43208.98194487528,257613.16877157817]
    assert len(dm_position[0]) == 3
    assert len(dm_position) == 2585
    assert response.headers["content-type"] == "application/json"
    
# Negative testing with invalid input
# Missing required parameters
def test_get_dm_position_missing_input():
    response = client.get("/pig/244/dm/position/")
=======


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
>>>>>>> master
    # Validate the status code: 404
    assert response.status_code == 404


<<<<<<< HEAD
# Invalid value for endpoint parameters. E.g. group_id not in [1,286036300) 
def test_get_dm_position_invalid_groupid():
    response = client.get("/pig/244/dm/position/0")
=======
# Invalid value for endpoint parameters. E.g. group_id not in [1,286036300]
def test_get_gas_electron_invalid_group_id():
    response = client.get("/pig/251/gas/electron/286036301")
>>>>>>> master
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
<<<<<<< HEAD
def test_get_dm_position_invalid_pig_id():
    response = client.get("/pig/200/dm/position/80")
    # Validate the status code: 404
    assert response.status_code == 404
    
    
    
        
#DM VELOCITY
def test_get_dm_velocity():
    response = client.get("/pig/244/dm/velocity/1862")
    # Validate the status code: 200
    assert response.status_code == 200
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 12857*3 array list
    data = json.loads(response.json()["dm_velocity"])
    assert type(data) is list
    assert data[2000] == [14.788228034973145, 49.952144622802734,23.566410064697266]
    assert len(data[0]) == 3
    assert len(data) == 26324
    assert response.headers["content-type"] == "application/json"

    
# Negative testing with invalid input
# Missing required parameters
def test_get_dm_velocity_missing_input():
    response = client.get("/pig/244/dm/velocity/")
=======
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
>>>>>>> master
    # Validate the status code: 404
    assert response.status_code == 404


<<<<<<< HEAD
# Invalid value for endpoint parameters. E.g. group_id not in [1,286036300) 
def test_get_dm_velocity_invalid_groupid():
    response = client.get("/pig/244/dm/velocity/0")
=======
# Invalid value for endpoint parameters. E.g. group_id not in [1,286036300]
def test_get_gas_h2fraction_invalid_group_id():
    response = client.get("/pig/251/gas/h2fraction/-1")
>>>>>>> master
    # Validate the status code: 400
    assert response.status_code == 400


# Invalid value for endpoint parameters. E.g. pig id not in PIG folder
<<<<<<< HEAD
def test_get_dm_velocity_invalid_pig_id():
    response = client.get("/pig/20/dm/velocity/203940")
    # Validate the status code: 404
    assert response.status_code == 404
    

=======
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
>>>>>>> master
