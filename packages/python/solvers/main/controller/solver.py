import json

from flask import Blueprint, jsonify, request

from solvers.main.service import feature_model
from solvers.main.service import cnf


solver_blueprint = Blueprint(
    "solver",
    __name__,
)


@solver_blueprint.route("/cnf/is_empty", methods=["POST"])
def is_empty_cnf():
    args = request.get_json(force=True)

    print(args)
    print(request.form)

    solver = args.get("solver", "cadical")
    solver = cnf.solver_map[solver]

    feature_model_json = args["feature_model"]
    fm = cnf.FeatureModelCNF(feature_model_json)

    if not feature_model.validate_feature_model(feature_model_json):
        return jsonify({
            "error": "invalid feature model"
        }), 500

    ans = cnf.is_empty_feture_model(fm, solver)

    return jsonify({
        "response": ans
    }), 200


@solver_blueprint.route("/cnf/is_real", methods=["POST"])
def is_real_cnf():
    args = request.get_json(force=True)

    solver = args.get("solver", "cadical")
    solver = cnf.solver_map[solver]

    feature_model_json = args["feature_model"]
    fm = cnf.FeatureModelCNF(feature_model_json)

    if not feature_model.validate_feature_model(feature_model_json):
        return jsonify({
            "error": "invalid feature model"
        }), 500

    ans = cnf.is_real_product_line(fm, solver)

    return jsonify({
        "response": ans
    }), 200


@solver_blueprint.route("/cnf/dead_features", methods=["POST"])
def dead_features_cnf():
    args = request.get_json(force=True)

    solver = args.get("solver", "cadical")
    solver = cnf.solver_map[solver]

    feature_model_json = args["feature_model"]
    fm = cnf.FeatureModelCNF(feature_model_json)

    if not feature_model.validate_feature_model(feature_model_json):
        return jsonify({
            "error": "invalid feature model"
        }), 500

    ans = cnf.get_dead_features(fm, solver)

    return jsonify({
        "response": ans
    }), 200


@solver_blueprint.route("/cnf/fake_optionals", methods=["POST"])
def dead_fake_optionals():
    args = request.get_json(force=True)

    solver = args.get("solver", "cadical")
    solver = cnf.solver_map[solver]

    feature_model_json = args["feature_model"]
    fm = cnf.FeatureModelCNF(feature_model_json)

    if not feature_model.validate_feature_model(feature_model_json):
        return jsonify({
            "error": "invalid feature model"
        }), 500

    ans = cnf.get_fake_optionals(fm, solver)

    return jsonify({
        "response": ans
    }), 200
