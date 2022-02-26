from typing import Dict, List, Tuple

from pydantic import BaseModel

from loasim.core import Stat


class SetItem(BaseModel):
    name: str
    stat_list: List[Tuple[Stat, Stat]]

    def get_stat(self, level1_set, level2_set):
        stat = Stat()
        for i in range(level2_set // 2):
            stat = stat + self.stat_list[i][1]
        for i in range(level2_set // 2, level1_set // 2):
            stat = stat + self.stat_list[i][0]
        return stat


class SetItemState(BaseModel):
    name: str
    level_1: int
    level_2: int


class SetItemRepository:
    def __init__(self):
        self._set_items: Dict[str, SetItem] = {}

    def add(self, setitem: SetItem):
        self._set_items[setitem.name] = setitem

    def get_stat(self, states: List[SetItemState]) -> Stat:
        stat = Stat()
        for set_item_state in states:
            stat = stat + self._set_items[set_item_state.name].get_stat(
                set_item_state.level_1, set_item_state.level_2
            )

        return stat
