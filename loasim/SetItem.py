from typing import List, Tuple
from loasim.CharacterModifier import CharacterModifier


class SetItem:
    def __init__(
        self, name: str, mdf_list: List[Tuple[CharacterModifier, CharacterModifier]]
    ) -> None:
        self.name = name
        self.mdf_list = mdf_list

    def get_modifier(self, level1_set, level2_set):
        mdf = CharacterModifier()
        for i in range(level2_set // 2):
            mdf = mdf + self.mdf_list[i][1]
        for i in range(level2_set // 2, level1_set // 2):
            mdf = mdf + self.mdf_list[i][0]
        return mdf


set_item_list = [
    SetItem(
        "환각",
        [
            (CharacterModifier(), CharacterModifier()),  #  2환각 미지원
            (CharacterModifier(crit=15), CharacterModifier(crit=18)),
            (CharacterModifier(pdamage_indep=25, crit=5), CharacterModifier(pdamage_indep=29, crit=7)),
        ],
    ),
    SetItem(
        "악몽",
        [
            (CharacterModifier(pdamage_indep=12), CharacterModifier(pdamage_indep=15)),
            (CharacterModifier(pdamage=15), CharacterModifier(pdamage=18)),
            (CharacterModifier(pdamage_indep=15), CharacterModifier(pdamage_indep=18)),
        ],
    ),
    SetItem(
        "지배",
        [
            (CharacterModifier(pdamage_indep=10), CharacterModifier(pdamage_indep=10)),
            (
                CharacterModifier(pdamage_indep=25)
                - CharacterModifier(pdamage_indep=10),
                CharacterModifier(pdamage_indep=28)
                - CharacterModifier(pdamage_indep=10),
            ),
            (CharacterModifier(pdamage_indep=15), CharacterModifier(pdamage_indep=18)),
        ],
    ),
    SetItem(
        "구원",
        [
            (CharacterModifier(pdamage=14), CharacterModifier(pdamage=18)),
            (CharacterModifier(pdamage=14), CharacterModifier(pdamage=18)),
            (
                CharacterModifier(pdamage=14, pdamage_indep=5),
                CharacterModifier(pdamage=18, pdamage_indep=5),
            ),
        ],
    ),
]

set_item_dict = {set_item.name: set_item for set_item in set_item_list}


class SetItemManager:
    def __init__(self, *equipped_list: List[Tuple[str, int, int]]) -> None:
        self.equipped_list = equipped_list

    def get_static_modifier(self):
        mdf = CharacterModifier()
        for name, level1_set, level2_set in self.equipped_list:
            set_item = set_item_dict.get(name)
            if set_item is None:
                raise Exception(f"{name} is not an set_item")
            mdf = mdf + set_item.get_modifier(level1_set, level2_set)
        return mdf
