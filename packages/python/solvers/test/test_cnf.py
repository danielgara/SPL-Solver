import unittest

from solvers.main.service import cnf


class TestCNF(unittest.TestCase):
    def test_timple_cnf_formula(self):
        formula = cnf.CNF()

        formula.add_comment("Francisco J. Piedrahíta-Vélez")
        formula.add_comment("Simple CNF formula")
        formula.add_comment("Example on how to use CNF formula class")

        formula.append([1, 2])
        formula.append([-3, 4])

        formula_str = str(formula)

        expected_str = "\n".join(
            [
                "c Francisco J. Piedrahíta-Vélez",
                "c Simple CNF formula",
                "c Example on how to use CNF formula class",
                "c",
                "p cnf 4 2",
                "1 1 2 0",
                "2 -3 4 0",
            ]
        )

        self.assertEqual(formula_str, expected_str)

    def test_feature_model_to_cnf(self):
        feature_model = {
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

        feature_model = cnf.FeatureModelCNF(feature_model)

        feature_model_str = str(feature_model.CNF)

        expected_str = "\n".join(
            [
                "c Mobile Phone Feature Model",
                "c Paolo Vavassori",
                "c Example of a Feature Model",
                "c",
                "p cnf 9 10",
                "1 1 0",
                "2 -1 2 0",
                "3 1 -2 0",
                "4 -1 3 0",
                "5 -1 4 0",
                "6 1 -4 0",
                "7 -1 5 0",
                "8 -3 -6 0",
                "9 -6 -3 0",
                "10 -9 8 0",
            ]
        )

        self.assertEqual(feature_model_str, expected_str)
