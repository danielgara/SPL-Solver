from spla.xcsp import *


def test_build_root():
    condition = build_root("F1")

    assert condition == "eq(F1, 1)"


def test_build_optional():
    condition = build_optional("F1", "F2")

    assert condition == "ge(F1, F2)"


def test_build_mandatory():
    condition = build_mandatory("F1", "F2")

    assert condition == "eq(F1, F2)"


def test_build_requires():
    condition = build_requires("F1", "F2")

    assert condition == "gt(add(sub(1, F1), F2), 0)"


def test_build_excludes():
    condition = build_excludes("F1", "F2")

    assert condition == "gt(add(sub(1, F1), sub(1, F2)), 0)"


def test_build_bundle_or():
    condition = build_bundle_or("F1", ["F2", "F3", "F4"])

    assert condition == "and(F1, or(F2, F3, F4))"


def test_build_bundle_and():
    condition = build_bundle_and("F1", ["F2", "F3", "F4"])

    assert condition == "and(F1, F2, F3, F4)"


def test_build_bundle_xor():
    condition = build_bundle_xor("F1", ["F2", "F3", "F4"])

    assert condition == "and(F1, xor(F2, F3, F4))"


def test_build_bundle_range():
    condition = build_bundle_range("F1", ["F2", "F3", "F4"], 1, 4)

    assert condition == "and(gt(mult(1, F1), sum(F2, F3, F4)), lt(sum(F2, F3, F4), mult(4, F1)))"
