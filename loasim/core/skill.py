from __future__ import annotations

from typing import List, Literal, Union

from pydantic import BaseModel

from loasim.core.enemy import Enemy
from loasim.core.stat import Stat

SkillType = Literal["Normal", "Chain", "Combo", "Charge", "Holding", "Casting", "Area"]
AttackPosition = Union[Literal["head", "back"], None]


class Skill(BaseModel):
    name: str
    base: float
    coefficient: float
    multiplier: float
    type: SkillType
    head: bool
    back: bool
    consume_mana: bool
    stat: Stat
    skill_afters: List[Skill]

    def get_damage(
        self,
        enemy: Enemy,
        position: AttackPosition = None,
        stat: Stat = Stat(),
    ) -> float:
        skill_afters_damage = sum(
            [sk.get_damage(enemy, position, stat) for sk in self.skill_afters]
        )

        stat = self.stat + stat
        if self.head and position == "head":
            stat += Stat(pdamage_indep=20) + Stat(
                pdamage_indep=stat.pdamage_indep_head, crit_damage=stat.crit_damage_head
            )
        if self.back and position == "back":
            stat += Stat(pdamage_indep=5, crit=10) + Stat(
                pdamage_indep=stat.pdamage_indep_back, crit_damage=stat.crit_damage_back
            )

        base_dmg = self.base + stat.get_total_att() * self.coefficient
        enemy_reduction_rate = enemy.get_reduction_rate(stat.armor_ignore)
        nocrit_dmg = (
            base_dmg * stat.get_multiplier() * enemy_reduction_rate * self.multiplier
        )
        crit_dmg = nocrit_dmg * stat.crit_damage / 100

        crit = min(stat.crit, 100) / 100
        damage = (1 - crit) * nocrit_dmg + crit * crit_dmg
        # print(self.name, nocrit_dmg, crit_dmg)
        # print(stat)

        return damage + skill_afters_damage
