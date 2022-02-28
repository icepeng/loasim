from collections import defaultdict
from typing import Dict, List, Tuple

from loguru import logger

from loasim.card import lostark_default_card_repository
from loasim.core import AttackType, BuffManager, BuffState, Enemy, InternalStat, Stat
from loasim.engraving import lostark_engraving_repository
from loasim.job import SkillState, get_job
from loasim.setitem import lostark_setitem_repository

DealCycle = List[Tuple[str, Dict[str, BuffState], AttackType]]


def calculate(
    job_name: str,
    internal_stat: InternalStat,
    weapon_pdamage: float,
    setitem_state: List[Tuple[str, int, int]],
    engraving_state: List[Tuple[str, int]],
    card_state: List[str],
    skill_state: Dict[str, SkillState],
    enemy: Enemy,
    deal_cycle: DealCycle,
    cycle_time: float,
):
    base_stat = internal_stat.get_stat()
    weapon_stat = Stat(pdamage=weapon_pdamage)  # 무기 품질
    basis_stat = (
        base_stat
        + weapon_stat
        + lostark_setitem_repository.get_stat(setitem_state)
        + lostark_default_card_repository.get_stat(card_state)
    )

    logger.info(base_stat)
    logger.info(basis_stat)

    job = get_job(job_name)
    skills, buffs = job.build(skill_state, internal_stat)
    engraving_buffs = lostark_engraving_repository.get_buffs(engraving_state)
    buff_manager = BuffManager(engraving_buffs + buffs)

    total_damage = 0.0
    damage_dict: defaultdict[str, float] = defaultdict(float)
    for skill_name, buff_state, attack_type in deal_cycle:
        skill = skills[skill_name]
        buff_stat = buff_manager.get_stat(buff_state, skill, basis_stat, internal_stat)
        damage = skill.get_damage(enemy, attack_type, basis_stat + buff_stat)
        total_damage += damage
        damage_dict[skill.name] += damage

    for sk, dmg in damage_dict.items():
        print(sk, f"{dmg / total_damage *100:,.3f}%")
    print(f"total damage: {total_damage:,.0f}")
    print(f"dps: {total_damage / cycle_time:,.0f}")
