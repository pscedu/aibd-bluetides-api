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
        "content": {
            "application/json": {
                "example": {
                    "detail": "PIG_{id} folder does not exist, and should be in ['PIG_208', 'PIG_230', 'PIG_237', 'PIG_216', 'PIG_265', 'PIG_244', 'PIG_271', 'PIG_258', 'PIG_222', 'PIG_251', 'PIG_184', 'PIG_197']"},
                "schema": {
                    "$ref": "#/components/schemas/HTTPValidationError"}
            }
        }
    }
response_404["ptype"] = \
    {
        "description": "Particle type does not exist",
        "content": {
            "application/json": {
                "example": {
                    "detail": "{ptype} does not exist, should be in ['gas', 'dm', 'star', 'bh']"},
                "schema": {
                    "$ref": "#/components/schemas/HTTPValidationError"}
            }
        }
    }
response_404["read_snapshot_type_info"] = \
    {
        "description": response_404["pig_id"]["description"] + " or " + response_404["ptype"]["description"],
        "content": {
            "application/json": {
                "example": {
                    "detail": response_404["pig_id"]["content"]["application/json"]["example"]["detail"] + " or " + response_404["ptype"]["content"]["application/json"]["example"]["detail"]},
                "schema": {
                    "$ref": "#/components/schemas/HTTPValidationError"}
            }
        }
    }
# 200 response description
response_200 = {}
response_200["read_pig"] = \
    {
        "description": "Successful Response - Snapshot info requested by pig ID",
    }
response_200["read_snapshot_info"] = \
    {
        "description": "Particle type does not exist",
        "content": {
                "application/json": {
                    "example": {
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
                        "num_bh": 235967},
                    "schema": {
                        "$ref": "#/components/schemas/Snapshot"}
                    }
                }
    }
response_200["read_snapshot_fof_info"] = \
    {
        "description": "Successful Response - FoFGroup info requested by pig ID",
        "content": {
            "application/json": {
                "example": {
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
                    ]},
                "schema": {
                    "$ref": "#/components/schemas/FoFGroup"}
                }
            }
        }
response_200["read_snapshot_type_info"] = \
    {
        "description": "Successful Response - Particle feature requested by pig ID and type",
        "content": {
            "application/json": {
                "example": {
                    "id": 251,
                    "type": "dm",
                    "subdirs": [
                        "GroupID",
                        "Velocity",
                        "ID",
                        "Potential",
                        "Generation",
                        "Position"
                    ]},
                "schema": {
                    "$ref": "#/components/schemas/Particle"}
                }
            }
    }