from typing import Any, Callable, List, Tuple
from loasim.CharacterModifier import CharacterModifier
from pydantic import BaseModel

class Engraving(BaseModel):
    name: str
    mdf_list: List[Callable[[Any], CharacterModifier]]
    is_static: bool

    def __init__(
        self,
        name: str,
        mdf_list: List[Callable[[Any], CharacterModifier]],
        is_static: bool,
    ) -> None:
        self.name = name
        self.mdf_list = mdf_list
        self.is_static = is_static

    def get_modifier(self, level, **kwargs) -> CharacterModifier:
        return self.mdf_list[level - 1](**kwargs)


engraving_list = [
    Engraving(
        "원한",
        [
            lambda: CharacterModifier(pdamage_indep=4),
            lambda: CharacterModifier(pdamage_indep=10),
            lambda: CharacterModifier(pdamage_indep=20),
        ],
        True,
    ),
    Engraving(
        "예리한 둔기",
        [
            lambda: CharacterModifier(pdamage_indep=-2, crit_damage=10),
            lambda: CharacterModifier(pdamage_indep=-2, crit_damage=25),
            lambda: CharacterModifier(pdamage_indep=-2, crit_damage=50),
        ],
        True,
    ),
    Engraving(
        "저주받은 인형",
        [
            lambda: CharacterModifier(patt=3),
            lambda: CharacterModifier(patt=8),
            lambda: CharacterModifier(patt=16),
        ],
        True,
    ),
    Engraving(
        "정밀 단도",
        [
            lambda: CharacterModifier(crit=4, crit_damage=-12),
            lambda: CharacterModifier(crit=10, crit_damage=-12),
            lambda: CharacterModifier(crit=20, crit_damage=-12),
        ],
        True,
    ),
    Engraving(
        "바리케이드",
        [
            lambda: CharacterModifier(pdamage_indep=3),
            lambda: CharacterModifier(pdamage_indep=8),
            lambda: CharacterModifier(pdamage_indep=16),
        ],
        True,
    ),
    Engraving(
        "안정된 상태",
        [
            lambda: CharacterModifier(pdamage_indep=3),
            lambda: CharacterModifier(pdamage_indep=8),
            lambda: CharacterModifier(pdamage_indep=16),
        ],
        True,
    ),
    Engraving(
        "아드레날린",
        [
            lambda: CharacterModifier(patt=1.8, crit=5),
            lambda: CharacterModifier(patt=3.6, crit=10),
            lambda: CharacterModifier(patt=6, crit=15),
        ],
        True,
    ),
    Engraving(
        "돌격대장",
        [
            lambda **kwargs: CharacterModifier(pdamage_indep=min(kwargs.get("spd"), 40) * 0.1),
            lambda **kwargs: CharacterModifier(pdamage_indep=min(kwargs.get("spd"), 40) * 0.22),
            lambda **kwargs: CharacterModifier(pdamage_indep=min(kwargs.get("spd"), 40) * 0.45),
        ],
        False,
    ),
    Engraving(
        "진화의 유산",
        [
            lambda **kwargs: CharacterModifier(
                pdamage_indep=kwargs.get("legacy_stack") * 2
            ),
            lambda **kwargs: CharacterModifier(
                pdamage_indep=kwargs.get("legacy_stack") * 4
            ),
            lambda **kwargs: CharacterModifier(
                pdamage_indep=kwargs.get("legacy_stack") * 6
            ),
        ],
        False,
    ),
]

engraving_dict = {engraving.name: engraving for engraving in engraving_list}


class EngravingManager:
    def __init__(self, *equipped_list: List[Tuple[str, int]]) -> None:
        self.equipped_list = equipped_list

    def get_static_modifier(self):
        mdf = CharacterModifier()
        for name, level in self.equipped_list:
            engraving = engraving_dict.get(name)
            if engraving is None:
                raise Exception(f"{name} is not an engraving")
            if engraving.is_static:
                mdf = mdf + engraving.get_modifier(level)
        return mdf

    def get_dynamic_modifier(self, **kwargs):
        mdf = CharacterModifier()
        for name, level in self.equipped_list:
            engraving = engraving_dict.get(name)
            if engraving is None:
                raise Exception(f"{name} is not an engraving")
            if not engraving.is_static:
                mdf = mdf + engraving.get_modifier(level, **kwargs)
        return mdf
