from collections import defaultdict
from typing import Dict, List

from loguru import logger
from pydantic import BaseModel

from loasim.accessory import lostark_accessory_repository
from loasim.avatar import lostark_avatar_repository
from loasim.card import lostark_default_card_repository
from loasim.character.base import Character
from loasim.core import (
    AttackPosition,
    BuffManager,
    BuffState,
    Enemy,
    InternalStat,
    Stat,
)
from loasim.engraving import lostark_engraving_repository
from loasim.gear import lostark_gear_repository
from loasim.job import get_job
from loasim.setitem import lostark_setitem_repository


class SkillAction(BaseModel):
    name: str
    status: Dict[str, BuffState]
    position: AttackPosition


class DealCycle(BaseModel):
    skill_actions: List[SkillAction]
    cycle_time: float


combat_level_map = {
    50: 409,
    51: 410,
    52: 411,
    53: 412,
    54: 414,
    55: 416,
    56: 418,
    57: 420,
    58: 423,
    59: 426,
    60: 429,
}


def get_internal_stat(character: Character) -> InternalStat:
    return (
        InternalStat(
            stat_main=combat_level_map[character.combat_level]
            + character.expedition_stat,
            crit=character.crit,
            special=character.special,
            swift=character.swift,
        )
        + character.bracelet_internal_stat
        + lostark_gear_repository.get_internal_stat(character.gear_status)
        + lostark_accessory_repository.get_internal_stat(character.accessory_status)
        + lostark_avatar_repository.get_internal_stat(character.avatar_status)
    )


def get_basis_stat(
    character: Character, internal_stat: InternalStat, additional_stat: Stat
) -> Stat:
    return (
        internal_stat.get_stat()
        + character.bracelet_stat
        + Stat(pdamage=character.weapon_pdamage)
        + additional_stat
        + lostark_setitem_repository.get_stat(character.setitem_status)
        + lostark_default_card_repository.get_stat(character.card_status)
    )


def calculate(
    character: Character,
    enemy: Enemy,
    deal_cycle: DealCycle,
    additional_stat: Stat = Stat(),
):
    internal_stat = get_internal_stat(character)
    basis_stat = get_basis_stat(character, internal_stat, additional_stat)

    logger.info(internal_stat)
    logger.info(basis_stat)

    job = get_job(character.job_name)
    skills, buffs = job.build(character.skill_status, internal_stat)
    engraving_buffs = lostark_engraving_repository.get_buffs(character.engraving_status)
    setitem_buffs = lostark_setitem_repository.get_buffs(character.setitem_status)
    buff_manager = BuffManager(engraving_buffs + setitem_buffs + buffs)

    total_damage = 0.0
    damage_dict: defaultdict[str, float] = defaultdict(float)
    for skill_action in deal_cycle.skill_actions:
        skill = skills[skill_action.name]
        buff_stat = buff_manager.get_stat(
            skill_action.status, skill, basis_stat, internal_stat
        )
        damage = skill.get_damage(enemy, skill_action.position, basis_stat + buff_stat)
        total_damage += damage
        damage_dict[skill.name] += damage

    for sk, dmg in damage_dict.items():
        print(sk, f"{dmg / total_damage *100:,.3f}%")
    print(f"total damage: {total_damage:,.0f}")
    print(f"dps: {total_damage / deal_cycle.cycle_time:,.0f}")

    return total_damage / deal_cycle.cycle_time
