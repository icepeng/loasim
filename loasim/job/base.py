from __future__ import annotations

from typing import Callable, Dict, List, Optional, Tuple

from pydantic import BaseModel

from loasim.core import AbstractBuff, OnoffBuff, Skill, SkillType, Stat
from loasim.core.stat import InternalStat

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


class Tripod(BaseModel):
    name: str
    stat_list: Optional[List[Stat]] = []
    buff_stat_list: Optional[List[Stat]] = []
    type_override: Optional[SkillType] = None
    skill_after: Optional[str] = None

    def get_stat(self, level: int) -> Stat:
        if not self.stat_list:
            raise ValueError(f"stat_list is not defined {self.name}")
        return self.stat_list[level - 1]

    def get_buff(self, level: int) -> OnoffBuff:
        if not self.buff_stat_list:
            raise ValueError(f"buff_stat_list is not defined {self.name}")
        return OnoffBuff(name=self.name, stat=self.buff_stat_list[level - 1])


class SkillSpecification(BaseModel):
    name: str
    damage_table: Dict[int, Tuple[float, float]]  # base, coefficient
    multiplier: float = 1
    type: SkillType
    head: bool = False
    back: bool = False
    tripods: List[Tripod] = []
    skill_afters: List[str] = []
    stat_from_special: Optional[Callable[[float], Stat]] = None

    def get_tripod(self, name: str) -> Optional[Tripod]:
        for tripod in self.tripods:
            if tripod.name == name:
                return tripod

        return None


class SkillState(BaseModel):
    level: int
    gem: int = 0
    tripod: Optional[Dict[str, int]] = None
    additional_stat: Optional[Stat] = None


class Job:
    def __init__(self):
        self._skills: Dict[str, SkillSpecification] = {}
        self._buffs: List[AbstractBuff] = []

    def add_skill(self, skill: SkillSpecification):
        self._skills[skill.name] = skill

    def add_buff(self, buff: AbstractBuff):
        self._buffs.append(buff)

    def build_skill(
        self, name: str, skill_state: SkillState, internal_stat: InternalStat
    ) -> Skill:
        skill = self._skills[name]
        skill_type = skill.type
        skill_afters = [
            self.build_skill(skill_name, skill_state, internal_stat)
            for skill_name in skill.skill_afters
        ]

        stat = Stat()
        stat = stat + Stat(pdamage_indep=gem_dict.get(skill_state.gem, 0))
        if skill_state.tripod is not None:
            for tripod_name, tripod_level in skill_state.tripod.items():
                given_tripod = skill.get_tripod(tripod_name)
                if given_tripod is None:
                    raise TypeError(
                        f"Given tripod not available in this spec. {tripod_name}"
                    )
                if given_tripod.type_override:
                    skill_type = given_tripod.type_override
                if given_tripod.skill_after:
                    skill_afters = skill_afters + [
                        self.build_skill(
                            given_tripod.skill_after, skill_state, internal_stat
                        )
                    ]
                if given_tripod.stat_list:
                    stat = stat + given_tripod.get_stat(tripod_level)

        if skill_state.additional_stat is not None:
            stat = stat + skill_state.additional_stat

        if skill.stat_from_special is not None:
            stat = stat + skill.stat_from_special(internal_stat.special)

        return Skill(
            name=skill.name,
            base=skill.damage_table[skill_state.level][0],
            coefficient=skill.damage_table[skill_state.level][1],
            multiplier=skill.multiplier,
            type=skill_type,
            head=skill.head,
            back=skill.back,
            stat=stat,
            skill_afters=skill_afters,
        )

    def build_skill_buffs(
        self, name: str, skill_state: SkillState
    ) -> List[AbstractBuff]:
        skill = self._skills[name]
        buff_list: List[AbstractBuff] = []
        if skill_state.tripod is not None:
            for tripod_name, tripod_level in skill_state.tripod.items():
                given_tripod = skill.get_tripod(tripod_name)
                if given_tripod is None:
                    raise TypeError(
                        f"Given tripod not available in this spec. {tripod_name}"
                    )
                if given_tripod.buff_stat_list:
                    buff_list.append(given_tripod.get_buff(tripod_level))

        return buff_list

    def build(
        self, skill_states: Dict[str, SkillState], internal_stat: InternalStat
    ) -> Tuple[Dict[str, Skill], List[AbstractBuff]]:
        skills: Dict[str, Skill] = {}
        buffs: List[AbstractBuff] = self._buffs.copy()
        for skill_name, skill_state in skill_states.items():
            skills[skill_name] = self.build_skill(
                skill_name, skill_state, internal_stat
            )
            buffs += self.build_skill_buffs(skill_name, skill_state)

        return skills, buffs
