import json
from functools import partial
from typing import Dict, List

from pydantic import BaseModel

from loasim.accessory import AccessoryStatus
from loasim.avatar import AvatarStatus
from loasim.core import InternalStat, Stat
from loasim.gear import GearStatus
from loasim.job import SkillState
from loasim.setitem import SetItemState


class Character(BaseModel):
    job_name: str
    combat_level: int
    expedition_stat: int
    crit: int
    special: int
    swift: int
    weapon_pdamage: float
    gear_status: GearStatus
    accessory_status: AccessoryStatus
    avatar_status: AvatarStatus
    setitem_status: Dict[str, SetItemState]
    engraving_status: Dict[str, int]
    card_status: List[str]
    skill_status: Dict[str, SkillState]
    bracelet_stat: Stat = Stat()
    bracelet_internal_stat: InternalStat = InternalStat()

    class Config:
        json_dumps = partial(json.dumps, ensure_ascii=False)
