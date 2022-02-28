import pytest

from loasim.core import (
    BuffManager,
    BuffState,
    InternalStat,
    InternalStatOnoffBuff,
    OnoffBuff,
    Skill,
    StackBuff,
    Stat,
    StatBuff,
)


@pytest.mark.parametrize("onoff, expected_pdamage_indep", [(False, 0), (True, 6)])
def test_onoff_buff(onoff: bool, expected_pdamage_indep: float, test_skill: Skill):
    buff_manager = BuffManager(
        buff_list=[
            OnoffBuff(
                name="약점 노출",
                stat=Stat(pdamage_indep=6),
            )
        ]
    )
    result_stat = buff_manager.get_stat(
        {"약점 노출": BuffState(onoff=onoff)}, test_skill, Stat(), InternalStat()
    )

    assert result_stat.pdamage_indep == expected_pdamage_indep


@pytest.mark.parametrize(
    "stack, expected_pdamage_indep", [(0, 0), (1, 2), (2, 4), (3, 6)]
)
def test_stack_buff(stack: int, expected_pdamage_indep: float, test_skill: Skill):
    buff_manager = BuffManager(
        buff_list=[
            StackBuff(
                name="진화의 유산",
                stat_fn=lambda stack: Stat(pdamage_indep=stack * 2),
            )
        ]
    )
    result_stat = buff_manager.get_stat(
        {"진화의 유산": BuffState(onoff=True, stack=stack)},
        test_skill,
        Stat(),
        InternalStat(),
    )

    assert result_stat.pdamage_indep == expected_pdamage_indep


@pytest.mark.parametrize("moving_speed, expected_pdamage_indep", [(0, 0), (40, 18)])
def test_stat_buff(
    moving_speed: float, expected_pdamage_indep: float, test_skill: Skill
):
    buff_manager = BuffManager(
        buff_list=[
            StatBuff(
                name="돌격대장",
                stat_fn=lambda stat: Stat(
                    pdamage_indep=min(stat.moving_speed, 40) * 0.45
                ),
            )
        ]
    )

    result_stat = buff_manager.get_stat(
        {}, test_skill, Stat(moving_speed=moving_speed), InternalStat()
    )

    assert result_stat.pdamage_indep == expected_pdamage_indep


@pytest.mark.parametrize("special, expected_pdamage_indep", [(0, 10), (1800, 19.785)])
def test_internal_stat_buff(
    special: float, expected_pdamage_indep: float, test_skill: Skill
):
    buff_manager = BuffManager(
        buff_list=[
            InternalStatOnoffBuff(
                name="저무는 달",
                stat_fn=lambda internal_stat: Stat(
                    pdamage_indep=10 * (1 + internal_stat.special * 0.000543611)
                ),
            )
        ]
    )

    result_stat = buff_manager.get_stat(
        {"저무는 달": BuffState(onoff=True)},
        test_skill,
        Stat(),
        InternalStat(special=special),
    )

    assert abs(result_stat.pdamage_indep - expected_pdamage_indep) < 0.0005
