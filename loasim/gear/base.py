from typing import Dict, Literal, Tuple

from pydantic import BaseModel

from loasim.core.stat import InternalStat

GearGrade = Literal["epic", "legendary", "relic", "ancient"]


class Gear(BaseModel):
    base_item_level: int
    grade: GearGrade
    category: str
    upgrade: int
    internal_stat: InternalStat


class GearState(BaseModel):
    base_item_level: int
    grade: GearGrade
    upgrade: int


class GearStatus(BaseModel):
    head: GearState
    shoulder: GearState
    top: GearState
    bottom: GearState
    glove: GearState
    weapon: GearState


class GearRepository:
    def __init__(self):
        self._gears: Dict[Tuple[int, GearGrade, str, int], Gear] = {}

    def add(self, gear: Gear):
        self._gears[
            (gear.base_item_level, gear.grade, gear.category, gear.upgrade)
        ] = gear

    def get_internal_stat(self, gear_status: GearStatus) -> InternalStat:
        internal_stat = InternalStat()
        for category, state in gear_status:
            gear = self._gears.get(
                (state.base_item_level, state.grade, category, state.upgrade)
            )
            if gear is None:
                raise TypeError(f"Given gear grade is not available. {state.grade}")
            internal_stat = internal_stat + gear.internal_stat

        return internal_stat
