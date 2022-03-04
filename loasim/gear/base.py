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
    head: Tuple[int, GearGrade, int]
    shoulder: Tuple[int, GearGrade, int]
    top: Tuple[int, GearGrade, int]
    bottom: Tuple[int, GearGrade, int]
    glove: Tuple[int, GearGrade, int]
    weapon: Tuple[int, GearGrade, int]


class GearRepository:
    def __init__(self):
        self._gears: Dict[Tuple[int, GearGrade, str, int], Gear] = {}

    def add(self, gear: Gear):
        self._gears[
            (gear.base_item_level, gear.grade, gear.category, gear.upgrade)
        ] = gear

    def get_internal_stat(self, gear_state: GearState) -> InternalStat:
        internal_stat = InternalStat()
        for category, (base_item_level, grade, upgrade) in gear_state.dict().items():
            gear = self._gears.get((base_item_level, grade, category, upgrade))
            if gear is None:
                raise TypeError(f"Given gear grade is not available. {grade}")
            internal_stat = internal_stat + gear.internal_stat

        return internal_stat
