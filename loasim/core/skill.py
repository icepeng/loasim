from __future__ import annotations

from typing import Dict, List, Literal, Optional, Tuple

from pydantic import BaseModel

from loasim.core.enemy import Enemy
from loasim.core.stat import Stat

gem_dict = {
    0: 0,
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

SkillType = Literal["Normal", "Chain", "Combo", "Charge", "Holding", "Casting", "Area"]


class Tripod(BaseModel):
    name: str
    stat_list: Optional[List[Stat]] = []
    type_override: Optional[SkillType] = None
    skill_after: Optional[str] = None

    def get_stat(self, level: int) -> Stat:
        if not self.stat_list:
            raise ValueError(f"stat_list is not defined {self.name}")
        return self.stat_list[level - 1]



class Skill(BaseModel):
    name: str
    base: float
    coefficient: float
    multiplier: float
    type: SkillType
    head: bool
    back: bool
    stat: Stat
    skill_afters: List[Skill]

    def modify_stat(self, stat: Stat) -> Skill:
        self.stat = self.stat + stat
        return self

    def get_damage(
        self,
        enemy: Enemy,
        backhead: str | None = None,
        additional_stat: Stat = Stat(),
    ) -> float:
        skill_afters_damage = sum(
            [
                sk.get_damage(enemy, backhead, additional_stat)
                for sk in self.skill_afters
            ]
        )

        stat = self.stat + additional_stat
        if self.head and backhead == "head":
            stat += Stat(pdamage_indep=20) + Stat(
                pdamage_indep=stat.pdamage_indep_head, crit_damage=stat.crit_damage_head
            )
        if self.back and backhead == "back":
            stat += Stat(pdamage_indep=5, crit=10) + Stat(
                pdamage_indep=stat.pdamage_indep_back, crit_damage=stat.crit_damage_back
            )

        base_dmg = self.base + stat.get_total_att() * self.coefficient
        enemy_reduction_rate = enemy.get_reduction_rate(stat.armor_ignore)
        nocrit_dmg = base_dmg * stat.get_multiplier() * enemy_reduction_rate * self.multiplier
        crit_dmg = nocrit_dmg * stat.crit_damage / 100

        crit = min(stat.crit, 100) / 100
        damage = (1 - crit) * nocrit_dmg + crit * crit_dmg
        # print(self.name, nocrit_dmg, crit_dmg)
        # print(stat)

        return damage + skill_afters_damage


class SkillSpecification(BaseModel):
    name: str
    damage_table: Dict[int, Tuple[float, float]]  # base, coefficient
    multiplier: float = 1
    type: SkillType
    head: bool = False
    back: bool = False
    tripods: List[Tripod] = []
    skill_afters: List[str] = []

    def get_tripod(self, name: str) -> Optional[Tripod]:
        for tripod in self.tripods:
            if tripod.name == name:
                return tripod

        return None


class SkillRepository:
    def __init__(self):
        self._skills: Dict[str, SkillSpecification] = {}

    def add(self, skill: SkillSpecification):
        self._skills[skill.name] = skill

    def build(
        self,
        name: str,
        level: int,
        gem: int = 0,
        tripod: Dict[str, int] = {},
        additional_stat: Optional[Stat] = None,
    ) -> Skill:
        skill = self._skills[name]
        skill_type = skill.type
        skill_afters = [
            self.build(
                name=skill_name,
                level=level,
                gem=gem,
                tripod=tripod,
                additional_stat=additional_stat,
            )
            for skill_name in skill.skill_afters
        ]

        stat = Stat()
        stat = stat + Stat(pdamage_indep=gem_dict.get(gem, 0))
        for name, tripod_level in tripod.items():
            given_tripod = skill.get_tripod(name)
            if given_tripod is None:
                raise TypeError(f"Given tripod not available in this spec. {name}")
            if given_tripod.type_override:
                skill_type = given_tripod.type_override
            if given_tripod.skill_after:
                skill_afters = skill_afters + [
                    self.build(
                        name=given_tripod.skill_after,
                        level=level,
                        gem=gem,
                        tripod=tripod,
                        additional_stat=additional_stat,
                    )
                ]
            if given_tripod.stat_list:
                stat = stat + given_tripod.get_stat(tripod_level)

        if additional_stat is not None:
            stat = stat + additional_stat

        return Skill(
            name=skill.name,
            base=skill.damage_table[level][0],
            coefficient=skill.damage_table[level][1],
            multiplier=skill.multiplier,
            type=skill_type,
            head=skill.head,
            back=skill.back,
            stat=stat,
            skill_afters=skill_afters,
        )
