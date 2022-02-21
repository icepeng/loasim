from typing import List
from loasim.CharacterModifier import CharacterModifier
from loasim.Enemy import Enemy

gem_dict = {
    1: 3,
    2: 6,
    3: 9,
    4: 12,
    5: 15,
    6: 18,
    7: 21,
    8: 24,
    9: 30,
    10: 40,
}


class Tripod:
    def __init__(self, name: str, mdf_list: List[CharacterModifier]) -> None:
        self.name = name
        self.mdf_list = mdf_list

    def get_modifier(self, level):
        return self.mdf_list[level - 1]


class Skill:
    def __init__(
        self,
        name: str,
        base: float,
        coefficient: float,
        multiplier: float = 1,
        head: bool = False,
        back: bool = False,
        tripods: List[Tripod] = [],
    ) -> None:
        self.name = name
        self.base = base
        self.coefficient = coefficient
        self.multiplier = multiplier
        self.head = head
        self.back = back
        self.tripods = {tripod.name: tripod for tripod in tripods}
        self.mdf = CharacterModifier()

    def set_gem(self, level: int):
        self.mdf = self.mdf + CharacterModifier(pdamage_indep=gem_dict.get(level))
        return self

    def set_tripod(self, name: str, level: int):
        self.mdf = self.mdf + self.tripods.get(name).get_modifier(level)
        return self


class SkillWrapper:
    def __init__(
        self, skill: Skill, mdf: CharacterModifier = CharacterModifier()
    ) -> None:
        self.name = skill.name
        self.mdf = skill.mdf + mdf
        self.skill = skill

    def get_damage(
        self,
        enemy: Enemy,
        backhead: str = None,
        mdf: CharacterModifier = CharacterModifier(),
    ) -> float:
        mdf = self.mdf + mdf
        if self.skill.head and backhead == "head":
            mdf += CharacterModifier(pdamage_indep=20)
        if self.skill.back and backhead == "back":
            mdf += CharacterModifier(pdamage_indep=5, crit=10)

        base_dmg = (
            self.skill.base + (mdf.att * (1 + mdf.patt / 100)) * self.skill.coefficient
        )
        mdf_multiplier = (1 + mdf.pdamage_indep / 100) * (1 + mdf.pdamage / 100)
        enemy_reduction_rate = enemy.get_reduction_rate(mdf.armor_ignore)
        nocrit_dmg = base_dmg * mdf_multiplier * enemy_reduction_rate
        crit_dmg = nocrit_dmg * mdf.crit_damage / 100

        crit = min(mdf.crit, 100) / 100
        damage = (1 - crit) * nocrit_dmg + crit * crit_dmg
        # print(self.name, nocrit_dmg, crit_dmg)
        # print(mdf.log())

        return damage * self.skill.multiplier
