from lxml import etree


def get_root(variamoso_model):
    """Get the VariaMos mxGraph root
    """
    feature = variamoso_model.xpath("//root[@type]")[0]

    return dict(feature.items())


def get_features(variamos_model):
    """Get the VariaMos mxGrpah list of features
    """
    selector = variamos_model.xpath(
        """//concrete[not(contains(@id, 'clon'))] |
           //abstract[not(contains(@id, 'clon'))]"""
    )

    return [dict(feature.items()) for feature in selector]


def get_relations(variamos_model):
    """Get the VariaMos mxGraph list of relations
    """
    relations = []

    for relation in variamos_model.xpath(
        """//rel_concrete_root |
           //rel_abstract_root |
           //rel_concrete_abstract |
           //rel_abstract_abstract |
           //rel_concrete_concrete"""
    ):
        relation_dict = dict(relation.items())
        relation_source_dict = dict(relation.find(".//mxCell").items())

        relations.append(
            {
                "type": relation_dict.get("relType"),
                "source": relation_source_dict.get("source"),
                "target": relation_source_dict.get("target"),
            }
        )

    return relations


def get_bundled_relations(variamos_model):
    """Get the VariaMos list of bundled relations
    """
    bundles = []
    bundle_relations = []

    selector = variamos_model.xpath("//bundle")
    bundle_features = [dict(feature.items()) for feature in selector]

    for relation in variamos_model.xpath(
        """//rel_abstract_bundle |
           //rel_concrete_bundle |
           //rel_bundle_abstract |
           //rel_bundle_concrete"""
    ):
        relation_dict = dict(relation.items())
        relation_source_dict = dict(relation.find(".//mxCell").items())

        bundle_relations.append(
            {
                "source": relation_source_dict["source"],
                "target": relation_source_dict["target"],
            }
        )

    for feature in bundle_features:
        source_relation = filter(
            lambda x: feature.get("id") == x.get("source"), bundle_relations
        )

        target_relations = filter(
            lambda x: feature.get("id") == x.get("target"), bundle_relations
        )

        for source in source_relation:
            bundle = {
                "type": "bundle",
                "bundle_type": feature.get("bundleType"),
                "source": source.get("target"),
                "targets": [target.get("source") for target in target_relations],
            }

            if bundle.get("bundle_type") == "RANGE":
                bundle["low_range"] = feature.get("lowRange")
                bundle["high_range"] = feature.get("highRange")

            bundles.append(bundle)

    return bundles


def build_feature_model(variamos_xml):
    """Create a new feature model dict from VariaMos mxGraph
    """
    tree = etree.fromstring(variamos_xml)

    root = get_root(tree)
    features = get_features(tree) + [root]
    relations = get_relations(tree) + get_bundled_relations(tree)

    return {"root": root.get("id"), "features": features, "relations": relations}
