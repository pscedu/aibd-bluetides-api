PIG_BASE_DIR = '/pylon5/as5pi3p/bluetides3/'

WEB_URL = "http://vm041.bridges.psc.edu/cosmo_api/"

#  metadata for tags
tags_metadata = [
    {
        "name": "pig",
        "description": "Get the snapshot info of PIG folders.",
    },
    {
        "name": "lengthbytype",
        "description": "Get the lengthbytype of particles.",
    },
    {
        "name": "particle",
        "description": "Get particle data.",
    },
    {
        "name": "advanced",
        "description": "Searching criterion by field and bulk queries for halo data.",
    },
]


        
# 404 response description
response_404 = {}
response_404["pig_id"] = \
    {
        "description": "PIG folder does not exist",
        "detail": "PIG_{id} folder does not exist, and should be in ['PIG_208', 'PIG_230', 'PIG_237', 'PIG_216', 'PIG_265', 'PIG_244', 'PIG_271', 'PIG_258', 'PIG_222', 'PIG_251', 'PIG_184', 'PIG_197']."
    }

response_404["ptype"] = \
    {
        "description": "Particle type does not exist",
        "detail": "{ptype} does not exist, should be in ['gas', 'dm', 'star', 'bh']."
    }

response_404["group_id"] = \
    {
        "description": "group_id out of range",
        "detail": "group_id out of range, should be in [1,max_group_size]."
    }

response_404["halo_id"] = \
    {
        "description": "halo_id out of range",
        "detail": "halo_id out of range, should be in [1,max_halo_size]."
    }

response_404["haloid_list"] = \
    {
        "description": "haloid_list is empty",
        "detail": "ID list is empty. Please input a valid one."
    }

response_404["type_id"] = \
    {
        "description": "type_id out of range",
        "detail": "type_id out of range, should be in [0,6)."
    }

response_404["ptype"] = \
    {
        "description": "ptype does not exist",
        "detail": "ptype does not exist, should be in ['gas', 'dm', 'star', 'bh']."
    }

response_404["feature"] = \
    {
        "description": "feature does not exist",
        "detail": "feature does not exist."
    }

response_404["criterion"] = \
    {
        "description": "Search criterion does not exist",
        "detail": "Search criterion does not exist, should be in ['bh_mass', 'gas_mass', 'dm_mass', 'star_mass', 'bh_mdot']."
    }

def construct_response_404(error_list):
    response = {
        "description": "",
        "content": {
            "application/json": {
                "example": {
                    "detail": ""},
                "schema": {
                    "$ref": "#/components/schemas/HTTPValidationError"}
            }
        }
    }
    for error in error_list:
        if response["description"] == "":
            response["description"] += response_404[error]["description"]
        else:
            response["description"] += " | " + response_404[error]["description"]
        if response["content"]["application/json"]["example"]["detail"] == "":
            response["content"]["application/json"]["example"]["detail"] += response_404[error]["detail"]
        else:
            response["content"]["application/json"]["example"]["detail"] += " Or " + response_404[error]["detail"]
    return response

response_404["read_snapshot_info"] = construct_response_404(["pig_id"])
response_404["read_snapshot_type_info"] = construct_response_404(["pig_id", "ptype"])
response_404["read_lbt_file"] = construct_response_404(["pig_id", "group_id"])
response_404["read_lbt_by_haloid"] = construct_response_404(["pig_id", "halo_id"])
response_404["read_lbt_by_haloid_list"] = construct_response_404(["pig_id", "haloid_list", "halo_id"])
response_404["read_lbht"] = construct_response_404(["pig_id", "halo_id", "type_id"])
response_404["read_obh"] = construct_response_404(["pig_id", "halo_id"])
response_404["read_haloid_by_criterion"] = construct_response_404(["pig_id", "ptype", "feature"])
response_404["read_particle_data_by_criterion"] = construct_response_404(["pig_id", "ptype", "feature", "criterion", ])
response_404["read_fofgroup_data"] = construct_response_404(["pig_id", "feature", "group_id"])
response_404["read_particle_data_by_groupid"] = construct_response_404(["pig_id", "ptype", "feature", "group_id"])
response_404["read_particle_data_by_post_groupid_list"] = construct_response_404(["pig_id", "ptype", "feature", "haloid_list"])

# 200 response description
response_200 = {}
def construct_response_200(description, example, model):
    response = {
        "description": description,
        "content": {
                "application/json": {
                    "example": example,
                    "schema": {
                        "$ref": "#/components/schemas/" + model
                    }
                }
            }
    }
    return response

response_200["read_pig"] = \
    {
        "description": "Successful Response - Snapshot info requested by pig ID",
    }

response_200["read_snapshot_info"] = \
    construct_response_200(
        "Successful Response - Particle info requested by pig ID",
        {
            "id": 251,
            "subdirs": [
                    "fofgroup",
                    "gas",
                    "dm",
                    "star",
                    "bh"
                ],
            "num_gas": 19358022252,
            "num_dm": 21165203462,
            "num_star": 587619843,
            "num_bh": 235967
        },
        "Snapshot")

response_200["read_snapshot_fof_info"] = \
    construct_response_200(
        "Successful Response - FoFGroup info requested by pig ID",
        {
            "id": 251,
            "fof_subdirs": [
            "Imom",
            "GroupID",
            "Mass",
            "Jmom",
            "OffsetByType",
            "BlackholeMass",
            "LengthByType",
            "FirstPos",
            "MassCenterPosition",
            "BlackholeAccretionRate",
            "MinID",
            "MassByType",
            "MassCenterVelocity",
            "StarFormationRate"
            ]
        },
        "SnapshotFoFGroup")

response_200["read_snapshot_type_info"] = \
    construct_response_200(
        "Successful Response - Particle feature requested by pig ID and type",
        {
            "id": 251,
            "type": "dm",
            "subdirs": [
                "GroupID",
                "Velocity",
                "ID",
                "Potential",
                "Generation",
                "Position"
            ]
        },
        "SnapshotParticle")

response_200["read_lbt_file"] = \
    construct_response_200(
        "Successful Response - Lengthbytype data requested by pig ID and halo number",
        {
            "id": 251,
            "num": 1,
            "length_by_type": [
                [
                446499,
                507723,
                0,
                0,
                561897,
                7
                ]
            ]
        },
        "LengthbytypeN")

response_200["read_lbt_by_haloid"] = \
    construct_response_200(
        "Successful Response - Lengthbytype data requested by pig ID and halo ID",
        {
            "id": 251,
            "halo_id": 10,
            "type_length": [
                102244,
                121770,
                0,
                0,
                140880,
                6
            ]
        },
        "LengthbytypeHaloID")