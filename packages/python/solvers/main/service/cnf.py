from pysat.solvers import Cadical
from pysat.solvers import Glucose3
from pysat.solvers import Glucose4
from pysat.solvers import Lingeling
from pysat.solvers import MapleChrono
from pysat.solvers import MapleCM
from pysat.solvers import Maplesat
from pysat.solvers import Minicard
from pysat.solvers import Minisat22
from pysat.solvers import MinisatGH


solver_map = {
    "cadical": Cadical,
    "glucose_3": Glucose3,
    "glucose_4": Glucose4,
    "lingeling": Lingeling,
    "maple_chrono": MapleChrono,
    "maple_cm": MapleCM,
    "maple_sat": Maplesat,
    "minicard": Minicard,
    "minisat_22": Minisat22,
    "minista_gh": MinisatGH,
}


class CNF:
    def __init__(self):
        self.num_variables = 0
        self.num_clauses = 0

        self.comments = []
        self.clauses = []

    def _get_max_var(self, clause):
        return max([abs(var) for var in clause] + [self.num_variables])

    def add_comment(self, comment):
        self.comments.append(comment)

    def append(self, clause):
        self.num_variables = self._get_max_var(clause)
        self.clauses.append(clause)

        self.num_clauses += 1

    def extend(self, clauses):
        for clause in clauses:
            self.append(clause)

    def __repr__(self):
        cnf_lines = []

        comments_str = [f"c {comment}" for comment in self.comments]
        cnf_lines.extend(comments_str)
        cnf_lines.append("c")

        cnf_lines.append(f"p cnf {self.num_variables} {self.num_clauses}")

        for index, clause in enumerate(self.clauses):
            clause_str = " ".join([str(val) for val in clause])
            cnf_lines.append(f"{index + 1} {clause_str} 0")

        return "\n".join(cnf_lines)


class FeatureModelCNF:
    def __init__(self, feature_model_json):
        self.name = feature_model_json.get("name")
        self.author = feature_model_json.get("author")
        self.description = feature_model_json.get("description")

        self.JSON = feature_model_json
        self.CNF = CNF()

        comments = [self.name, self.author, self.description]
        [self.CNF.add_comment(comment) for comment in comments if comment]

        self.CNF.extend(self._generate_feature_model_clauses(feature_model_json))

    def _generate_feature_model_clauses(self, feature_model_json):
        clauses = []

        constraints_mapping = {
            "mandatory": self._generate_mandatory_clause,
            "optional": self._generate_optional_clause,
            "excludes": self._generate_excludes_clause,
            "requires": self._generate_requires_clause,
            "and": self._generate_and_clause,
            "xor": self._generate_xor_clause,
            "or": self._generate_or_clause,
            "group_cardinality": self._generate_group_cardinality_clause,
        }

        for feature in feature_model_json.get("features", []):
            source = feature.get("id")

            for constraint in feature.get("constraints", []):
                destination = constraint.get("destination")

                if constraint.get("constraint_type") == "root":
                    clauses.extend(self._generate_root_clause(source))
                else:
                    clauses.extend(
                        constraints_mapping[constraint.get("constraint_type")](
                            source, destination
                        )
                    )

        return clauses

    def _generate_root_clause(self, source):
        return [[source]]

    def _generate_mandatory_clause(self, source, destination):
        return [[-1 * source, destination], [source, -1 * destination]]

    def _generate_optional_clause(self, source, destination):
        return [[-1 * source, destination]]

    def _generate_excludes_clause(self, source, destination):
        return [[-1 * source, -1 * destination]]

    def _generate_requires_clause(self, source, destination):
        return [[-1 * source, destination]]

    def _generate_and_clause(self, source, destination):
        # Not Implemented
        return []

    def _generate_or_clause(self, source, destination):
        # Not Implemented
        return []

    def _generate_xor_clause(self, source, destination):
        # Not Implemented
        return []

    def _generate_group_cardinality_clause(self, source, destination):
        # Not Implemented
        return []


def is_empty_feture_model(feature_model, solver_class):
    with solver_class(bootstrap_with=feature_model.CNF.clauses) as solver:
        return solver.solve()


def is_real_product_line(feature_model, solver_class):
    with solver_class(bootstrap_with=feature_model.CNF.clauses) as solver:
        for index, solution in enumerate(solver.enum_models()):
            if index >= 1:
                return True

    return False


def get_dead_features(feature_model, solver_class):
    dead_features = []

    with solver_class(bootstrap_with=feature_model.CNF.clauses) as solver:
        features = feature_model.JSON.get("features")

        for feature_id in range(1, feature_model.CNF.num_variables):
            if not solver.solve(assumptions=[feature_id]):
                dead_features.append(feature_id)

    return dead_features


def get_fake_optionals(feature_model, solver_class):
    fake_optionals = []

    with solver_class(bootstrap_with=feature_model.CNF.clauses) as solver:

        for feature in feature_model.JSON.get("features", []):
            feature_id = feature.get("id")

            for constraint in feature.get("constraints", []):
                constraint_id = constraint.get("destination")

                if constraint.get("constraint_type") == "optional":
                    if not solver.solve(assumptions=[-1 * feature_id]):
                        fake_optionals.append(constraint_id)

    return fake_optionals
