import pytest

from loasim.core import Enemy, Skill, Stat


@pytest.mark.parametrize("att, expected_damage", [(1000, 11000), (0, 1000)])
def test_skill_damage(
    att: float,
    expected_damage: float,
):
    test_skill = Skill(
        name="테스트 스킬",
        type="Normal",
        base=1000,
        coefficient=10,
        multiplier=1,
        head=False,
        back=False,
        consume_mana=True,
        stat=Stat(),
        skill_afters=[],
    )

    assert (
        test_skill.get_damage(Enemy(armor=0, reduction=0), None, Stat(att=att))
        == expected_damage
    )


@pytest.mark.parametrize(
    "att, expected_damage", [(1000, 11000 + 5500), (0, 1000 + 500)]
)
def test_chained_skill_damage(
    att: float,
    expected_damage: float,
):
    trailing_skill = Skill(
        name="후속 스킬",
        type="Normal",
        base=500,
        coefficient=5,
        multiplier=1,
        head=False,
        back=False,
        consume_mana=True,
        stat=Stat(),
        skill_afters=[],
    )

    test_chained_skill = Skill(
        name="테스트 스킬",
        type="Normal",
        base=1000,
        coefficient=10,
        multiplier=1,
        head=False,
        back=False,
        consume_mana=True,
        stat=Stat(),
        skill_afters=[trailing_skill],
    )

    assert (
        test_chained_skill.get_damage(Enemy(armor=0, reduction=0), None, Stat(att=att))
        == expected_damage
    )


@pytest.mark.parametrize("att, expected_damage", [(1000, 11000 * 1.2), (0, 1000 * 1.2)])
def test_skill_damage_head(
    att: float,
    expected_damage: float,
):
    test_skill = Skill(
        name="테스트 스킬",
        type="Normal",
        base=1000,
        coefficient=10,
        multiplier=1,
        head=True,
        back=False,
        consume_mana=True,
        stat=Stat(),
        skill_afters=[],
    )

    assert (
        test_skill.get_damage(Enemy(armor=0, reduction=0), "head", Stat(att=att))
        == expected_damage
    )


@pytest.mark.parametrize(
    "att, expected_damage",
    [
        (1000, (0.9 * 11000 + 0.1 * 11000 * 2) * 1.05),
        (0, (0.9 * 1000 + 0.1 * 1000 * 2) * 1.05),
    ],
)
def test_skill_damage_back(
    att: float,
    expected_damage: float,
):
    test_skill = Skill(
        name="테스트 스킬",
        type="Normal",
        base=1000,
        coefficient=10,
        multiplier=1,
        head=False,
        back=True,
        consume_mana=True,
        stat=Stat(),
        skill_afters=[],
    )

    assert (
        test_skill.get_damage(
            Enemy(armor=0, reduction=0), "back", Stat(att=att, crit_damage=200)
        )
        == expected_damage
    )
