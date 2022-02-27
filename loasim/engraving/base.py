from typing import Callable, Dict, List, Tuple

from pydantic import BaseModel

from loasim.core.buff import AbstractBuff, OnoffBuff, SkillBuff, StackBuff, StaticBuff
from loasim.core.skill import Skill
from loasim.core.stat import Stat


class AbstractEngraving(BaseModel):
    name: str

    def get_buff(self, level: int) -> AbstractBuff:
        raise NotImplementedError()


class OnoffEngraving(AbstractEngraving):
    stat_list: List[Stat]

    def get_buff(self, level: int) -> OnoffBuff:
        return OnoffBuff(
            name=self.name,
            stat=self.stat_list[level - 1],
        )


class StaticEngraving(AbstractEngraving):
    stat_list: List[Stat]

    def get_buff(self, level: int) -> StaticBuff:
        return StaticBuff(
            name=self.name,
            stat=self.stat_list[level - 1],
        )


class StackEngraving(AbstractEngraving):
    stat_fn_list: List[Callable[[int], Stat]]

    def get_buff(self, level: int) -> StackBuff:
        return StackBuff(
            name=self.name,
            stat_fn=self.stat_fn_list[level - 1],
        )


class SkillEngraving(AbstractEngraving):
    stat_fn_list: List[Callable[[Skill], Stat]]

    def get_buff(self, level: int) -> SkillBuff:
        return SkillBuff(
            name=self.name,
            stat_fn=self.stat_fn_list[level - 1],
        )


class EngravingRepository:
    def __init__(self):
        self._engravings: Dict[str, AbstractEngraving] = {}

    def add(self, engraving: AbstractEngraving):
        self._engravings[engraving.name] = engraving

    def get_buffs(self, engraving_state: List[Tuple[str, int]]) -> List[AbstractBuff]:
        buffs: List[AbstractBuff] = []
        for name, level in engraving_state:
            engraving = self._engravings.get(name)
            if engraving is None:
                raise Exception(f"{name} is not an engraving")
            buffs.append(engraving.get_buff(level))

        return buffs
