from lxml import etree
from spla.variamos_parser import *


tree_test_1 = etree.parse("./tests/resources/test_1.xml")
tree_test_2 = etree.parse("./tests/resources/test_2.xml")


def test_get_root_1():
    root = get_root(tree_test_1)

    root_dict = {"id": "1", "label": "root", "type": "root"}

    assert root == root_dict


def test_get_root_2():
    root = get_root(tree_test_2)

    root_dict = {"id": "1", "label": "ClothingStores", "type": "root"}

    assert root == root_dict


def test_get_features_1():
    features = get_features(tree_test_1)

    feature_list = [
        {"label": "abstract_1", "type": "abstract", "id": "2"},
        {"label": "concrete_2", "type": "concrete", "selected": "false", "id": "6"},
        {"label": "concrete_4", "type": "concrete", "selected": "false", "id": "14"},
        {"label": "abstract_4", "type": "abstract", "id": "16"},
        {"label": "abstract_2", "type": "abstract", "id": "17"},
        {"label": "abstract", "type": "abstract", "id": "23"},
    ]

    assert features == feature_list


def test_get_features_2():
    features = get_features(tree_test_2)

    feature_list = [
        {"label": "Shipping", "type": "concrete", "selected": "true", "id": "2"},
        {"label": "Contact us", "type": "concrete", "selected": "true", "id": "3"},
        {"label": "Basic views", "type": "concrete", "selected": "true", "id": "6"},
        {
            "label": "Database management",
            "type": "concrete",
            "selected": "true",
            "id": "49",
        },
        {"label": "Demo data", "type": "concrete", "selected": "true", "id": "60"},
        {"label": "User model", "type": "concrete", "selected": "true", "id": "72"},
        {"label": "Account", "type": "concrete", "selected": "true", "id": "75"},
        {"label": "Login", "type": "concrete", "selected": "true", "id": "77"},
        {"label": "Cart", "type": "concrete", "selected": "true", "id": "113"},
        {
            "label": "Offline payment",
            "type": "concrete",
            "selected": "true",
            "id": "114",
        },
        {
            "label": "Online payment",
            "type": "concrete",
            "selected": "true",
            "id": "115",
        },
        {"label": "Rating", "type": "concrete", "selected": "true", "id": "141"},
        {"label": "Product model", "type": "concrete", "selected": "true", "id": "142"},
        {"label": "Comments", "type": "concrete", "selected": "true", "id": "143"},
        {
            "label": "List of products",
            "type": "concrete",
            "selected": "true",
            "id": "144",
        },
        {
            "label": "Sharing system",
            "type": "concrete",
            "selected": "true",
            "id": "145",
        },
        {"label": "Basic views", "type": "concrete", "selected": "true", "id": "205"},
        {
            "label": "Comment management",
            "type": "concrete",
            "selected": "true",
            "id": "206",
        },
        {
            "label": "Product management",
            "type": "concrete",
            "selected": "true",
            "id": "207",
        },
        {
            "label": "User management",
            "type": "concrete",
            "selected": "true",
            "id": "208",
        },
        {"label": "Shop", "type": "abstract", "id": "251"},
        {"label": "Product", "type": "abstract", "id": "256"},
        {"label": "Web management", "type": "abstract", "id": "263"},
        {"label": "User", "type": "abstract", "id": "270"},
    ]

    assert features == feature_list


def test_get_relations_1():
    relations = get_relations(tree_test_1)

    relation_list = [
        {"type": "mandatory", "source": "2", "target": "1"},
        {"type": "mandatory", "source": "23", "target": "1"},
    ]

    assert relations == relation_list


def test_get_relations_2():
    relations = get_relations(tree_test_2)

    relation_list = [
        {"type": "optional", "source": "2", "target": "1"},
        {"type": "optional", "source": "3", "target": "1"},
        {"type": "mandatory", "source": "6", "target": "1"},
        {"type": "mandatory", "source": "49", "target": "1"},
        {"type": "optional", "source": "60", "target": "1"},
        {"type": "requires", "source": "75", "target": "77"},
        {"type": "requires", "source": "208", "target": "72"},
        {"type": "requires", "source": "206", "target": "143"},
        {"type": "optional", "source": "251", "target": "1"},
        {"type": "mandatory", "source": "113", "target": "251"},
        {"type": "optional", "source": "115", "target": "251"},
        {"type": "optional", "source": "114", "target": "251"},
        {"type": "optional", "source": "141", "target": "256"},
        {"type": "mandatory", "source": "144", "target": "256"},
        {"type": "optional", "source": "145", "target": "256"},
        {"type": "mandatory", "source": "142", "target": "256"},
        {"type": "optional", "source": "143", "target": "256"},
        {"type": "mandatory", "source": "256", "target": "1"},
        {"type": "mandatory", "source": "205", "target": "263"},
        {"type": "optional", "source": "206", "target": "263"},
        {"type": "optional", "source": "207", "target": "263"},
        {"type": "optional", "source": "208", "target": "263"},
        {"type": "optional", "source": "263", "target": "1"},
        {"type": "optional", "source": "77", "target": "270"},
        {"type": "mandatory", "source": "72", "target": "270"},
        {"type": "optional", "source": "75", "target": "270"},
        {"type": "optional", "source": "270", "target": "1"},
    ]

    assert relations == relation_list


def test_get_bundled_relations_1():
    bundle_relations = get_bundled_relations(tree_test_1)

    bundle_relation_list = [
        {"type": "bundle", "bundle_type": "AND", "source": "2", "targets": ["6", "17"]},
        {
            "type": "bundle",
            "bundle_type": "RANGE",
            "source": "23",
            "targets": ["14", "16"],
            "low_range": "1",
            "high_range": "4",
        },
    ]

    assert bundle_relations == bundle_relation_list


def test_get_bundled_relations_2():
    bundle_relation = get_bundled_relations(tree_test_2)

    assert bundle_relation == []
