from lxml.builder import E


def build_root(source):
    condition = f"{source} 0"

    return condition


def build_optional(source, destination):
    condition = f"-{source} {destinations} 0"

    return condition


def build_mandatory(source, destination):
    condition = f"-{source} {destination} 0\n-{source} {destination} 0"

    return condition


def build_requires(source, destination):
    condition = f"-{source} {destination} 0"

    return condition


def build_excludes(source, destination):
    condition = f"-{source} -{destination} 0"

    return condition


def build_bundle_or(source, destination_list):
    condition = " ".join(destination_list)
    condition = f"{condition} 0"

    return condition


def build_bundle_and(source, destination_list):
    condition = " 0\n".join(source, destination_list)

    return condition


def build_bundle_xor(source, destination_list):
    raise NotImplementedError


def build_bundle_range(source, destination_list, range_min, range_max):
    raise NotImplementedError


cnf_restriction_map = {
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


def build_cnf_file(feature_model):
    pass
