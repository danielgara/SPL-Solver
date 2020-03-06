import jsonschema


feature_model_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string",},
        "author": {"type": "string",},
        "description": {"type": "string",},
        "features": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer",},
                    "name": {"type": "string",},
                    "constraints": {
                        "type": "array",
                        "items": {
                            "allOf": [
                                {
                                    "if": {
                                        "properties": {
                                            "constraint_type": {"const": "root",},
                                        },
                                    },
                                    "then": {
                                        "properties": {
                                            "constraint_type": {"type": "string",}
                                        },
                                        "additionalProperties": False,
                                    },
                                },
                                {
                                    "if": {
                                        "properties": {
                                            "constraint_type": {
                                                "enum": [
                                                    "mandatory",
                                                    "optional",
                                                    "excludes",
                                                    "requires",
                                                ],
                                            },
                                        },
                                    },
                                    "then": {
                                        "properties": {
                                            "constraint_type": {"type": "string",},
                                            "destination": {"type": "integer",},
                                        },
                                        "additionalProperties": False,
                                    },
                                },
                                {
                                    "if": {
                                        "properties": {
                                            "constraint_type": {
                                                "enum": ["and", "or", "xor"],
                                            },
                                        },
                                    },
                                    "then": {
                                        "properties": {
                                            "constraint_type": {"type": "string",},
                                            "destination": {
                                                "type": "array",
                                                "items": {"type": "integer"},
                                            },
                                        },
                                        "additionalProperties": False,
                                    },
                                },
                                {
                                    "if": {
                                        "properties": {
                                            "constraint_type": {
                                                "const": "group_cardinality",
                                            },
                                        },
                                    },
                                    "then": {
                                        "properties": {
                                            "constraint_type": {"type": "string",},
                                            "low_threshold": {"type": "integer",},
                                            "high_threshold": {"type": "integer",},
                                            "destination": {
                                                "type": "array",
                                                "items": {"type": "integer"},
                                            },
                                        },
                                    },
                                },
                            ]
                        },
                    },
                },
            },
        },
    },
}


def validate_feature_model(feature_model):
    try:
        jsonschema.validate(instance=feature_model, schema=feature_model_schema)
    except jsonschema.ValidationError:
        return False

    return True
