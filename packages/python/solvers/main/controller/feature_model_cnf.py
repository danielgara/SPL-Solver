import json

from flask import Blueprint, jsonify, request

from solvers.main.service import cnf


blueprint = Blueprint(
    "cnf_feature_model",
    __name__,
)


@blueprint.route("/feature-model/cnf/solutions", methods=["POST"])
def get_solutions():
    args = request.get_json(force=True)

    solver = args.get("solver", "cadical")
    solver = cnf.solver_map[solver]

    feature_model_json = args["feature_model"]
    fm = cnf.feature_model.FeatureModelCNF(feature_model_json)

    # TODO: Add Validation
    #if not feature_model.validate_feature_model(feature_model_json):
    #    return jsonify({
    #        "error": "invalid feature model"
    #    }), 500

    ans = cnf.get_solutions(fm.CNF, solver, float("inf"))

    return jsonify({
        "response": ans
    }), 200


@blueprint.route("/feature-model/cnf/is-empty", methods=["POST"])
def is_empty_cnf():
    args = request.get_json(force=True)

    solver = args.get("solver", "cadical")
    solver = cnf.solver_map[solver]

    feature_model_json = args["feature_model"]
    fm = cnf.feature_model.FeatureModelCNF(feature_model_json)

    # TODO: Add Validation
    #if not feature_model.validate_feature_model(feature_model_json):
    #    return jsonify({
    #        "error": "invalid feature model"
    #    }), 500

    ans = cnf.feature_model.is_empty_feture_model(fm, solver)

    return jsonify({
        "response": ans
    }), 200


@blueprint.route("/feature-model/cnf/is-real", methods=["POST"])
def is_real_cnf():
    args = request.get_json(force=True)

    solver = args.get("solver", "cadical")
    solver = cnf.solver_map[solver]

    feature_model_json = args["feature_model"]
    fm = cnf.feature_model.FeatureModelCNF(feature_model_json)

    # TODO: Add Validation
    #if not feature_model.validate_feature_model(feature_model_json):
    #    return jsonify({
    #        "error": "invalid feature model"
    #    }), 500

    ans = cnf.feature_model.is_real_product_line(fm, solver)

    return jsonify({
        "response": ans
    }), 200


@blueprint.route("/feature-model/cnf/dead-features", methods=["POST"])
def dead_features_cnf():
    args = request.get_json(force=True)

    solver = args.get("solver", "cadical")
    solver = cnf.solver_map[solver]

    feature_model_json = args["feature_model"]
    fm = cnf.feature_model.FeatureModelCNF(feature_model_json)

    # TODO: Add Validation
    #if not feature_model.validate_feature_model(feature_model_json):
    #    return jsonify({
    #        "error": "invalid feature model"
    #    }), 500

    ans = cnf.feature_model.get_dead_features(fm, solver)

    return jsonify({
        "response": ans
    }), 200


@blueprint.route("/feature-model/cnf/fake-optionals", methods=["POST"])
def dead_fake_optionals():
    args = request.get_json(force=True)

    solver = args.get("solver", "cadical")
    solver = cnf.solver_map[solver]

    feature_model_json = args["feature_model"]
    fm = cnf.feature_model.FeatureModelCNF(feature_model_json)

    # TODO: Add Validation
    #if not feature_model.validate_feature_model(feature_model_json):
    #    return jsonify({
    #        "error": "invalid feature model"
    #    }), 500

    ans = cnf.feature_model.get_fake_optionals(fm, solver)

    return jsonify({
        "response": ans
    }), 200
