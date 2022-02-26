from loguru import logger

from collections import defaultdict
from typing import Any, Callable, List, Dict, Literal, Tuple

from pydantic import BaseModel

from loasim.core import Skill, Enemy, BuffManager, InternalStat
from loasim.core.buff import Buff
from loasim.core.stat import Stat
from loasim.setitem import lostark_setitem_repository
from loasim.card import lostark_default_card_repository
from loasim.engraving import lostark_engraving_repository


class DealCycle(BaseModel):
    buff_list: List[Buff]
    skill_list: List[Tuple[Skill, Dict[str, Any], Literal["back", "head"] | None]]
    cycle_time: float


def calculate(
    internal_stat: InternalStat,
    weapon_pdamage: float,
    setitem_state: List[Tuple[str, int, int]],
    engraving_state: List[Tuple[str, int]],
    card_state: List[str],
    generator: Callable[[InternalStat], DealCycle],
    enemy: Enemy,
):
    deal_cycle = generator(internal_stat)
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

    engraving_buffs = lostark_engraving_repository.get_buffs(engraving_state)
    buff_manager = BuffManager(engraving_buffs + deal_cycle.buff_list)

    total_damage = 0.0
    damage_dict: defaultdict[str, float] = defaultdict(float)
    for skill, buff_state, backhead in deal_cycle.skill_list:
        buff_stat = buff_manager.get_stat(buff_state, skill)
        damage = skill.get_damage(enemy, backhead, basis_stat + buff_stat)
        total_damage += damage
        damage_dict[skill.name] += damage

    for sk, dmg in damage_dict.items():
        print(sk, f"{dmg / total_damage *100:,.3f}%")
    print(f"total damage: {total_damage:,.0f}")
    print(deal_cycle.cycle_time)
    print(f"dps: {total_damage / deal_cycle.cycle_time:,.0f}")
