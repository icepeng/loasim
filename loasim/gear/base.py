from typing import Dict, List, Tuple

from pydantic import BaseModel

from loasim.core.stat import InternalStat


class Gear(BaseModel):
    grade: str
    slot: str
    internal_stat_list: List[InternalStat]


class GearState(BaseModel):
    head: Tuple[str, int]
    shoulder: Tuple[str, int]
    top: Tuple[str, int]
    bottom: Tuple[str, int]
    glove: Tuple[str, int]
    weapon: Tuple[str, int]


class GearRepository:
    def __init__(self):
        self._gears: Dict[Tuple[str, str], Gear] = {}

    def add(self, gear: Gear):
        self._gears[(gear.slot, gear.grade)] = gear

    def get_internal_stat(self, gear_state: GearState) -> InternalStat:
        internal_stat = InternalStat()
        for slot, (grade, level) in gear_state.dict().items():
            gear = self._gears.get((slot, grade))
            if gear is None:
                raise TypeError(f"Given gear grade is not available. {grade}")
            internal_stat = internal_stat + gear.internal_stat_list[level]

        return internal_stat
