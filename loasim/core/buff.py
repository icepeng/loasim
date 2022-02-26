from typing import Any, Callable, Dict, List, Literal, Union
from pydantic import BaseModel
from loasim.core.skill import Skill

from loasim.core.stat import Stat


class OnoffBuff(BaseModel):
    name: str = None
    stat: Stat
    type: Literal["onoff"] = "onoff"

    def get_stat(self, onoff: bool):
        if onoff:
            return self.stat
        return Stat()


class StaticBuff(BaseModel):
    name: str = None
    stat: Stat
    type: Literal["static"] = "static"

    def get_stat(self):
        return self.stat


class StackBuff(BaseModel):
    name: str = None
    get_stat: Callable[[int], Stat]
    type: Literal["stack"] = "stack"


class SkillBuff(BaseModel):
    name: str = None
    get_stat: Callable[[Skill], Stat]
    type: Literal["skill"] = "skill"


Buff = Union[OnoffBuff, SkillBuff, StaticBuff, StackBuff]


class BuffManager:
    def __init__(self, buff_list: List[Buff]) -> None:
        self._buffs: Dict[str, Buff] = {buff.name: buff for buff in buff_list}

    def get_stat(self, state: Dict[str, Any], skill: Skill) -> Stat:
        stat = Stat()
        for buff in self._buffs.values():
            if buff.type == "onoff":
                stat = stat + buff.get_stat(state[buff.name])
            elif buff.type == "static":
                stat = stat + buff.get_stat()
            elif buff.type == "stack":
                stat = stat + buff.get_stat(state[buff.name])
            elif buff.type == "skill":
                stat = stat + buff.get_stat(skill)

        return stat
