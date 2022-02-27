from typing import Dict, Tuple

from pydantic import BaseModel

from loasim.core.stat import InternalStat

slot_type_map = {
    "necklace": "necklace",
    "ear1": "ear",
    "ear2": "ear",
    "ring1": "ring",
    "ring2": "ring",
}


class Accessory(BaseModel):
    grade: str
    type: str
    internal_stat: InternalStat


class AccessoryState(BaseModel):
    necklace: str
    ear1: str
    ear2: str
    ring1: str
    ring2: str


class AccessoryRepository:
    def __init__(self):
        self._accessories: Dict[Tuple[str, str], Accessory] = {}

    def add(self, accessory: Accessory):
        self._accessories[(accessory.type, accessory.grade)] = accessory

    def get_internal_stat(self, accessory_state: AccessoryState) -> InternalStat:
        internal_stat = InternalStat()
        for slot, grade in accessory_state.dict().items():
            if grade is not None:
                accessory = self._accessories.get((slot_type_map[slot], grade))
                if accessory is None:
                    raise TypeError(f"Given accessory grade is not available. {grade}")
                internal_stat = internal_stat + accessory.internal_stat

        return internal_stat
