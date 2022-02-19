from loasim.CharacterModifier import CharacterModifier
from loasim.Enemy import Enemy


class Skill:
    def __init__(
        self,
        name: str,
        base: float,
        coefficient: float,
        multiplier: float = 1,
        mdf: CharacterModifier = CharacterModifier(),
    ) -> None:
        self.name = name
        self.base = base
        self.coefficient = coefficient
        self.multiplier = multiplier
        self.mdf = mdf

    def get_damage(
        self, enemy: Enemy, mdf: CharacterModifier = CharacterModifier()
    ) -> float:
        mdf = self.mdf + mdf
        base_dmg = self.base + (mdf.att * (1 + mdf.patt / 100)) * self.coefficient
        mdf_multiplier = (1 + mdf.pdamage_indep / 100) * (1 + mdf.pdamage / 100)
        enemy_reduction_rate = enemy.get_reduction_rate()
        nocrit_dmg = base_dmg * mdf_multiplier * enemy_reduction_rate
        crit_dmg = nocrit_dmg * mdf.crit_damage / 100

        crit = min(mdf.crit, 100) / 100
        damage = (1 - crit) * nocrit_dmg + crit * crit_dmg
        # print(self.name, nocrit_dmg, crit_dmg)
        # print(mdf.log())

        return damage * self.multiplier