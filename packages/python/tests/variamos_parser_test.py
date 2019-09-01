from lxml import etree
from spl.variamos_parser import *


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
    pass


def test_get_relations_2():
    pass


def test_get_bundled_relations_1():
    pass


def test_get_bundled_relations_2():
    pass
