from pydantic import BaseModel

from loasim.accessory import AccessoryState, lostark_accessory_repository
from loasim.avatar import AvatarState, lostark_avatar_repository
from loasim.core import InternalStat
from loasim.gear import GearState, lostark_gear_repository

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


class Character(BaseModel):
    combat_level: int
    expedition_stat: int
    crit: int
    special: int
    swift: int
    gear_state: GearState
    accessory_state: AccessoryState
    avatar_state: AvatarState

    def get_internal_stat(
        self,
    ) -> InternalStat:
        return (
            InternalStat(
                stat_main=combat_level_map[self.combat_level] + self.expedition_stat,
                crit=self.crit,
                special=self.special,
                swift=self.swift,
            )
            + lostark_gear_repository.get_internal_stat(self.gear_state)
            + lostark_accessory_repository.get_internal_stat(self.accessory_state)
            + lostark_avatar_repository.get_internal_stat(self.avatar_state)
        )
