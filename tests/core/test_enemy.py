import pytest

from loasim.core.enemy import Enemy


@pytest.mark.parametrize(
    "armor, reduction, armor_ignore, reduction_rate", [(12000, 25, 50, 0.39)]
)
def test_get_reduction_rate(armor: float, reduction: float, armor_ignore: float, reduction_rate: float):
    enemy = Enemy(
        armor=armor,
        reduction=reduction,
    )

    assert enemy.get_reduction_rate(armor_ignore) == reduction_rate
