from typing import Dict, List, Tuple

from pydantic import BaseModel

from loasim.core import Stat


class SetItem(BaseModel):
    name: str
    stat_list: List[Tuple[Stat, Stat]]

    def get_stat(self, level1_set: int, level2_set: int):
        stat = Stat()
        for i in range(level2_set // 2):
            stat = stat + self.stat_list[i][1]
        for i in range(level2_set // 2, level1_set // 2):
            stat = stat + self.stat_list[i][0]
        return stat


class SetItemRepository:
    def __init__(self):
        self._set_items: Dict[str, SetItem] = {}

    def add(self, setitem: SetItem):
        self._set_items[setitem.name] = setitem

    def get_stat(self, setitem_state: List[Tuple[str, int, int]]) -> Stat:
        stat = Stat()
        for name, level1, level2 in setitem_state:
            stat = stat + self._set_items[name].get_stat(level1, level2)

        return stat
