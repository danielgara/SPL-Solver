import json

from flask import Blueprint, jsonify, request
from solvers.main.service import cnf


blueprint = Blueprint(
    "CNF",
    __name__,
)


@blueprint.route("/solutions", methods=["POST"])
def get_solutions():
    args = request.get_json(force=True)

    solver = args.get("solver", "cadical")
    statements = args.get("statements")
    restrictions = args.get("restrictions", [])
    num_solutions = args.get("num_solutions", float('inf'))

    if not statements:
        return jsonify({
            "error": "Post request must contain statements"
        }), 400

    solver = cnf.solver_map[solver]
    formula = cnf.get_formula(statements, restrictions)

    solutions = cnf.get_solutions(formula, solver, num_solutions)

    return jsonify({
        "solutions": solutions
    }), 200
