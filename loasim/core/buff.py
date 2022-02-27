from typing import Callable, Dict, List, Union

from pydantic import BaseModel

from loasim.core.skill import Skill
from loasim.core.stat import Stat


class BuffState(BaseModel):
    onoff: bool
    stack: float = 0


class AbstractBuff(BaseModel):
    name: str

    def get_stat(self, state: Dict[str, BuffState], skill: Skill) -> Stat:
        raise NotImplementedError()


class OnoffBuff(AbstractBuff):
    name: str
    stat: Stat

    def get_stat(self, state: Dict[str, BuffState], skill: Skill):
        buff_state = state.get(self.name)
        if buff_state is None:
            raise ValueError(f"{self.name} is not found in state")
        if buff_state.onoff:
            return self.stat
        return Stat()


class StaticBuff(AbstractBuff):
    name: str
    stat: Stat

    def get_stat(self, state: Dict[str, BuffState], skill: Skill):
        return self.stat


class StackBuff(AbstractBuff):
    name: str
    stat_fn: Union[
        Callable[[float], Stat], Callable[[float], Stat]
    ]  # mypy #5485 workaround

    def get_stat(self, state: Dict[str, BuffState], skill: Skill):
        buff_state = state.get(self.name)
        if buff_state is None:
            raise ValueError(f"{self.name} is not found in state")
        if buff_state.onoff:
            return self.stat_fn(buff_state.stack)
        return Stat()


class SkillBuff(AbstractBuff):
    name: str
    stat_fn: Union[
        Callable[[Skill], Stat], Callable[[Skill], Stat]
    ]  # mypy #5485 workaround

    def get_stat(self, state: Dict[str, BuffState], skill: Skill):
        return self.stat_fn(skill)


class BuffManager:
    def __init__(self, buff_list: List[AbstractBuff]) -> None:
        self._buffs: Dict[str, AbstractBuff] = {buff.name: buff for buff in buff_list}

    def get_stat(self, state: Dict[str, BuffState], skill: Skill) -> Stat:
        stat = Stat()
        for buff in self._buffs.values():
            stat = stat + buff.get_stat(state, skill)

        return stat
