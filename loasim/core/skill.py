from typing import List, Dict
from loasim.core.stat import Stat
from loasim.core.enemy import Enemy

from pydantic import BaseModel

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


class Tripod(BaseModel):
    name: str
    stat_list: List[Stat]

    def get_modifier(self, level: int) -> Stat:
        return self.stat_list[level - 1]


class Skill(BaseModel):
    name: str
    base: float
    coefficient: float
    multiplier: float
    head: bool 
    back: bool
    stat: Stat
    
    def modify_stat(self, stat):
        self.stat = self.stat + stat
        return self

    def get_damage(
        self,
        enemy: Enemy,
        backhead: str = None,
        stat: Stat = Stat(),
    ) -> float:
        stat = self.stat + stat
        if self.head and backhead == "head":
            stat += Stat(pdamage_indep=20)
        if self.back and backhead == "back":
            stat += Stat(pdamage_indep=5, crit=10)

        base_dmg = (
            self.base + (stat.att * (1 + stat.patt / 100)) * self.coefficient
        )
        stat_multiplier = (1 + stat.pdamage_indep / 100) * (1 + stat.pdamage / 100)
        enemy_reduction_rate = enemy.get_reduction_rate(stat.armor_ignore)
        nocrit_dmg = base_dmg * stat_multiplier * enemy_reduction_rate
        crit_dmg = nocrit_dmg * stat.crit_damage / 100

        crit = min(stat.crit, 100) / 100
        damage = (1 - crit) * nocrit_dmg + crit * crit_dmg
        # print(self.name, nocrit_dmg, crit_dmg)
        # print(stat.log())

        return damage * self.multiplier


class SkillBuildConfiguration(BaseModel):
    tripod: Dict[str, int]
    gem: int


class SkillSpecification(BaseModel):
    name: str
    base: float
    coefficient: float
    multiplier: float = 1
    head: bool = False
    back: bool = False
    tripods: List[Tripod] = []

    def get_tripod(self, name):
        for tripod in self.tripods:
            if tripod.name == name:
                return tripod

    def build_skill(self, config: SkillBuildConfiguration) -> Skill:
        stat = Stat()
        stat = stat + Stat(pdamage_indep=gem_dict.get(config.gem))
        for name, level in config.tripod.items():
            stat = stat + self.get_tripod(name).get_modifier(level)

        return Skill(
            name=self.name,
            base=self.base,
            coefficient=self.coefficient,
            multiplier=self.multiplier,
            head=self.head,
            back=self.back,
            stat=stat
        )
