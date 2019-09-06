from lxml import etree
from lxml.builder import E


def build_root(source):
    condition = f"eq({source}, 1)"

    return condition


def build_optional(source, destination):
    condition = f"ge({source}, {destination})"

    return condition


def build_mandatory(source, destination):
    condition = f"eq({source}, {destination})"

    return condition


def build_requires(source, destination):
    condition = f"gt(add(sub(1, {source}), {destination}), 0)"

    return condition


def build_excludes(source, destination):
    condition = f"gt(add(sub(1, {source}), sub(1, {destination})), 0)"

    return condition


def build_bundle_or(source, destination_list):
    or_condition = ", ".join(destination_list)
    or_condition = f"or({or_condition})"

    condition = f"and({source}, {or_condition})"

    return condition


def build_bundle_and(source, destination_list):
    condition = ", ".join(destination_list)
    condition = f"and({source}, {condition})"

    return condition


def build_bundle_xor(source, destination_list):
    xor_condition = ", ".join(destination_list)
    xor_condition = f"xor({xor_condition})"

    condition = f"and({source}, {xor_condition})"

    return condition


def build_bundle_range(source, destination_list, range_min, range_max):
    sum_destinations = ", ".join(destination_list)
    sum_destinations = f"sum({sum_destinations})"

    condition_min = f"gt(mult({range_min}, {source}), {sum_destinations})"
    condition_max = f"lt({sum_destinations}, mult({range_max}, {source}))"

    condition = f"and({condition_min}, {condition_max})"

    return condition


xcsp_restriction_map = {
    "root": build_root,
    "optional": build_optional,
    "requires": build_requires,
    "excludes": build_excludes,
    "mandatory": build_mandatory,
    "bundle": {
        "or": build_bundle_or,
        "and": build_bundle_and,
        "xor": build_bundle_xor,
        "range": build_bundle_range,
    },
}


def build_xcsp_file(feature_model):
    features = feature_model["features"]
    features_xcsp = [
        E.var(" 0 1 ", id=f"F{feature['id']}", note=f"{feature['label']}")
        for feature in features
    ]

    root = feature_model["root"]
    root_xcsp = [E.intension(E.function(xcsp_restriction_map["root"](f"F{root}")))]

    relations = filter(lambda x: not x["type"] == "bundle", feature_model["relations"])
    relations_xcsp = [
        E.intension(
            E.function(
                xcsp_restriction_map[relation["type"]](
                    f"F{relation['source']}", f"F{relation['target']}"
                )
            )
        )
        for relation in relations
    ]

    bundles = filter(lambda x: x["type"] == "bundle", feature_model["relations"])
    bundles_xcsp = []

    for bundle in bundles:
        args = [f"F{bundle['source']}", [f"F{target}" for target in bundle["targets"]]]

        if bundle["bundle_type"].lower() == "range":
            args.append(bundle["low_range"])
            args.append(bundle["high_range"])

        bundles_xcsp.append(
            E.intension(
                E.function(
                    xcsp_restriction_map["bundle"][bundle["bundle_type"].lower()](*args)
                )
            )
        )

    constraints_xcsp = root_xcsp + relations_xcsp + bundles_xcsp

    xcsp = E.instance(
        E.variables(*features_xcsp),
        E.constraints(*constraints_xcsp),
        format="XCSP3",
        type="CSP",
    )

    return str(etree.tostring(xcsp, pretty_print=True), "UTF-8")
