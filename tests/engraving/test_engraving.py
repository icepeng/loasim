import pytest

from loasim.core import Stat
from loasim.core.buff import BuffState, StackBuff, StaticBuff
from loasim.core.skill import Skill
from loasim.core.stat import InternalStat
from loasim.engraving import lostark_engraving_repository


@pytest.mark.parametrize(
    "engraving_name, level, expected_stat",
    [
        ("원한", 1, Stat(pdamage_indep=4)),
        ("원한", 2, Stat(pdamage_indep=10)),
        ("원한", 3, Stat(pdamage_indep=20)),
    ],
)
def test_engraving_repository_static(
    engraving_name: str, level: int, expected_stat: Stat
):
    buff = lostark_engraving_repository.get_buffs([(engraving_name, level)])[0]
    assert isinstance(buff, StaticBuff)
    assert buff.stat == expected_stat


@pytest.mark.parametrize(
    "engraving_name, level, expected_stat",
    [
        ("진화의 유산", 1, Stat(pdamage_indep=6)),
        ("진화의 유산", 2, Stat(pdamage_indep=12)),
        ("진화의 유산", 3, Stat(pdamage_indep=18)),
    ],
)
def test_engraving_repository_stack(
    engraving_name: str, level: int, expected_stat: Stat, test_skill: Skill
):
    buff = lostark_engraving_repository.get_buffs([(engraving_name, level)])[0]
    assert isinstance(buff, StackBuff)
    assert (
        buff.get_stat(
            {"진화의 유산": BuffState(onoff=True, stack=3)},
            test_skill,
            Stat(),
            InternalStat(),
        )
        == expected_stat
    )
