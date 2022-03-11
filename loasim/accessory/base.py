from typing import Dict, Tuple

from pydantic import BaseModel

from loasim.core.stat import InternalStat

slot_category_map = {
    "necklace": "necklace",
    "ear1": "ear",
    "ear2": "ear",
    "ring1": "ring",
    "ring2": "ring",
}


class Accessory(BaseModel):
    grade: str
    category: str
    internal_stat: InternalStat


class AccessoryStatus(BaseModel):
    necklace: str
    ear1: str
    ear2: str
    ring1: str
    ring2: str


class AccessoryRepository:
    def __init__(self):
        self._accessories: Dict[Tuple[str, str], Accessory] = {}

    def add(self, accessory: Accessory):
        self._accessories[(accessory.category, accessory.grade)] = accessory

    def get_internal_stat(self, accessory_status: AccessoryStatus) -> InternalStat:
        internal_stat = InternalStat()
        for slot, grade in accessory_status:
            if grade is not None:
                accessory = self._accessories.get((slot_category_map[slot], grade))
                if accessory is None:
                    raise TypeError(f"Given accessory grade is not available. {grade}")
                internal_stat = internal_stat + accessory.internal_stat

        return internal_stat
