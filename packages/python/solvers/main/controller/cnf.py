import json

from flask import Blueprint, jsonify, request
from solvers.main.service import cnf


blueprint = Blueprint(
    "CNF",
    __name__,
)


@blueprint.route("/satisfiable", methods=["POST"])
def is_satisfiable():
    args = request.get_json(force=True)

    solver = cnf.solver_map[
        args.get("solver", "cadical")
    ]

    statement = "\n".join(args.get("statement"))
    formula = cnf.get_formula(statement)

    return jsonify({
        "is_staistiable": cnf.is_satisfiable(formula, solver)
    }), 200


@blueprint.route("/solutions", methods=["POST"])
def get_solutions():
    args = request.get_json(force=True)

    solver = cnf.solver_map[
        args.get("solver", "cadical")
    ]

    statement = "\n".join(args.get("statement"))
    formula = cnf.get_formula(statement)

    return jsonify({
        "solutions": cnf.get_solutions(formula, solver)
    }), 200
