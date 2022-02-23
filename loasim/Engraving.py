from typing import Any, Callable, List, Tuple

from pydantic import BaseModel

from loasim.core import Stat


class Engraving(BaseModel):
    name: str
    mdf_list: List[Callable[[Any], Stat]]
    is_static: bool

    def get_modifier(self, level, **kwargs) -> Stat:
        return self.mdf_list[level - 1](**kwargs)


def get_blade_buff(engraving_grade, burst_grade):
    buff_table = {
        1: {
            0: 0,
            1: 8,
            2: 10,
            3: 12,
        },
        2: {
            0: 0,
            1: 16,
            2: 20,
            3: 24,
        },
        3: {
            0: 0,
            1: 25,
            2: 30,
            3: 36,
        }
    }
    return buff_table.get(engraving_grade).get(burst_grade)

engraving_list = [
    Engraving(
        name="원한",
        mdf_list=[
            lambda: Stat(pdamage_indep=4),
            lambda: Stat(pdamage_indep=10),
            lambda: Stat(pdamage_indep=20),
        ],
        is_static=True,
    ),
    Engraving(
        name="예리한 둔기",
        mdf_list=[
            lambda: Stat(pdamage_indep=-2, crit_damage=10),
            lambda: Stat(pdamage_indep=-2, crit_damage=25),
            lambda: Stat(pdamage_indep=-2, crit_damage=50),
        ],
        is_static=True,
    ),
    Engraving(
        name="저주받은 인형",
        mdf_list=[
            lambda: Stat(patt=3),
            lambda: Stat(patt=8),
            lambda: Stat(patt=16),
        ],
        is_static=True,
    ),
    Engraving(
        name="정밀 단도",
        mdf_list=[
            lambda: Stat(crit=4, crit_damage=-12),
            lambda: Stat(crit=10, crit_damage=-12),
            lambda: Stat(crit=20, crit_damage=-12),
        ],
        is_static=True,
    ),
    Engraving(
        name="바리케이드",
        mdf_list=[
            lambda: Stat(pdamage_indep=3),
            lambda: Stat(pdamage_indep=8),
            lambda: Stat(pdamage_indep=16),
        ],
        is_static=True,
    ),
    Engraving(
        name="안정된 상태",
        mdf_list=[
            lambda: Stat(pdamage_indep=3),
            lambda: Stat(pdamage_indep=8),
            lambda: Stat(pdamage_indep=16),
        ],
        is_static=True,
    ),
    Engraving(
        name="아드레날린",
        mdf_list=[
            lambda: Stat(patt=1.8, crit=5),
            lambda: Stat(patt=3.6, crit=10),
            lambda: Stat(patt=6, crit=15),
        ],
        is_static=True,
    ),
    Engraving(
        name="타격의 대가",
        mdf_list=[
            lambda: Stat(pdamage_indep=3),
            lambda: Stat(pdamage_indep=8),
            lambda: Stat(pdamage_indep=16),
        ],
        is_static=True,
    ),
    Engraving(
        name="기습의 대가",
        mdf_list=[
            lambda: Stat(pdamage_indep_back=5),
            lambda: Stat(pdamage_indep_back=12),
            lambda: Stat(pdamage_indep_back=25),
        ],
        is_static=True,
    ),
    Engraving(
        name="돌격대장",
        mdf_list=[
            lambda **kwargs: Stat(pdamage_indep=min(kwargs.get("spd"), 40) * 0.1),
            lambda **kwargs: Stat(pdamage_indep=min(kwargs.get("spd"), 40) * 0.22),
            lambda **kwargs: Stat(pdamage_indep=min(kwargs.get("spd"), 40) * 0.45),
        ],
        is_static=False,
    ),
    Engraving(
        name="슈퍼 차지",
        mdf_list=[
            lambda **kwargs: Stat(pdamage_indep=kwargs.get("charge") * 4),
            lambda **kwargs: Stat(pdamage_indep=kwargs.get("charge") * 10),
            lambda **kwargs: Stat(pdamage_indep=kwargs.get("charge") * 20),
        ],
        is_static=False,
    ),
    Engraving(
        name="진화의 유산",
        mdf_list=[
            lambda **kwargs: Stat(pdamage_indep=kwargs.get("legacy_stack") * 2),
            lambda **kwargs: Stat(pdamage_indep=kwargs.get("legacy_stack") * 4),
            lambda **kwargs: Stat(pdamage_indep=kwargs.get("legacy_stack") * 6),
        ],
        is_static=False,
    ),
    Engraving(
        name="회귀",
        mdf_list=[
            lambda: Stat(crit=6, crit_damage=20),
            lambda: Stat(crit=9, crit_damage=30),
            lambda: Stat(crit=12, crit_damage=40),
        ],
        is_static=True,
    ),
    Engraving(
        name="잔재된 기운",
        mdf_list=[
            lambda **kwargs: Stat(patt=get_blade_buff(1, kwargs.get("burst_grade"))),
            lambda **kwargs: Stat(patt=get_blade_buff(2, kwargs.get("burst_grade"))),
            lambda **kwargs: Stat(patt=get_blade_buff(3, kwargs.get("burst_grade"))),
        ],
        is_static=False,
    ),
]

engraving_dict = {engraving.name: engraving for engraving in engraving_list}


class EngravingManager:
    def __init__(self, *equipped_list: List[Tuple[str, int]]) -> None:
        self.equipped_list = equipped_list

    def get_static_modifier(self):
        mdf = Stat()
        for name, level in self.equipped_list:
            engraving = engraving_dict.get(name)
            if engraving is None:
                raise Exception(f"{name} is not an engraving")
            if engraving.is_static:
                mdf = mdf + engraving.get_modifier(level)
        return mdf

    def get_dynamic_modifier(self, **kwargs):
        mdf = Stat()
        for name, level in self.equipped_list:
            engraving = engraving_dict.get(name)
            if engraving is None:
                raise Exception(f"{name} is not an engraving")
            if not engraving.is_static:
                mdf = mdf + engraving.get_modifier(level, **kwargs)
        return mdf
