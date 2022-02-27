import pytest

from loasim.core.stat import Stat

eps = 1e-8


@pytest.mark.parametrize(
    "arg_name, a, b, c",
    [
        ("crit", 3, 4, 7),
        ("crit_damage", 3, 4, 7),
        ("pdamage", 3, 4, 7),
        ("pdamage_indep", 10, 20, 32),
        ("armor_ignore", 20, 20, 36),
        ("patt_common", 3, 4, 7),
        ("patt_indep", 10, 20, 32),
        ("att", 3, 4, 7),
    ],
)
def test_partial_stat_addition(arg_name: str, a: float, b: float, c: float):
    stat_a = Stat(**{arg_name: a})
    stat_b = Stat(**{arg_name: b})

    stat_result = stat_a + stat_b

    assert abs(getattr(stat_result, arg_name) - c) < eps


@pytest.mark.parametrize(
    "arg_name, a, b, c",
    [
        ("crit", 3, 4, 7),
        ("crit_damage", 3, 4, 7),
        ("pdamage", 3, 4, 7),
        ("pdamage_indep", 10, 20, 32),
        ("armor_ignore", 20, 20, 36),
        ("patt_common", 3, 4, 7),
        ("patt_indep", 10, 20, 32),
        ("att", 3, 4, 7),
    ],
)
def test_partial_stat_substract(arg_name: str, a: float, b: float, c: float):
    stat_c = Stat(**{arg_name: c})
    stat_b = Stat(**{arg_name: b})

    stat_result = stat_c - stat_b

    assert abs(getattr(stat_result, arg_name) - a) < eps


def test_stat_operation():
    ...
