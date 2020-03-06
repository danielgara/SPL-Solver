import unittest

from solvers.main.service import feature_model


class TestFeatureModel(unittest.TestCase):
    def test_valid_feature_models(self):
        feature_model_dict = {
            "name": "Mobile Phone Feature Model",
            "author": "Paolo Vavassori",
            "description": "Example of a Feature Model",
            "features": [
                {
                    "id": 1,
                    "name": "Mobile Phone",
                    "constraints": [
                        {"constraint_type": "root",},
                        {"constraint_type": "mandatory", "destination": 2,},
                        {"constraint_type": "optional", "destination": 3,},
                        {"constraint_type": "mandatory", "destination": 4,},
                        {"constraint_type": "optional", "destination": 5,},
                    ],
                },
                {"id": 2, "name": "Calls",},
                {
                    "id": 3,
                    "name": "GPS",
                    "constraints": [
                        {"constraint_type": "excludes", "destination": 6,},
                    ],
                },
                {
                    "id": 4,
                    "name": "Screen",
                    "constraints": [
                        {
                            "constraint_type": "group_cardinality",
                            "low_threshold": 1,
                            "high_threshold": 3,
                            "destination": [6, 7, 8],
                        },
                    ],
                },
                {
                    "id": 5,
                    "name": "Media",
                    "constraints": [{"constraint_type": "or", "destination": [9, 10]},],
                },
                {
                    "id": 6,
                    "name": "Basic",
                    "constraints": [{"constraint_type": "excludes", "destination": 3},],
                },
                {"id": 7, "name": "Colour",},
                {"id": 8, "name": "High Resolution",},
                {
                    "id": 9,
                    "name": "Camera",
                    "constraints": [
                        {"constraint_type": "requires", "destination": 8,},
                    ],
                },
                {"id": 10, "name": "MP3",},
            ],
        }

        self.assertTrue(feature_model.validate_feature_model(feature_model_dict))

    def test_invalid_feature_model(self):
        feature_model_dict = {
            "features": "Invalid item value"
        }

        self.assertFalse(feature_model.validate_feature_model(feature_model_dict))
