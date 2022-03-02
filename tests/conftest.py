import pytest

from loasim.core import Stat
from loasim.core.skill import Skill


@pytest.fixture
def test_skill():
    return Skill(
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
