from typing import Dict

from pydantic import BaseModel

from loasim.core.stat import InternalStat


class Avatar(BaseModel):
    grade: str
    internal_stat: InternalStat


class AvatarState(BaseModel):
    head: str
    top: str
    bottom: str
    weapon: str

class AvatarRepository:
    def __init__(self):
        self._avatars: Dict[str, Avatar] = {}

    def add(self, avatar: Avatar):
        self._avatars[avatar.grade] = avatar

    def get_internal_stat(self, avatar_state: AvatarState) -> InternalStat:
        internal_stat = InternalStat()
        for grade in avatar_state.dict().values():
            if grade is not None:
                avatar = self._avatars.get(grade)
                if avatar is None:
                    raise TypeError(f"Given avatar grade is not available. {grade}")
                internal_stat = internal_stat + avatar.internal_stat

        return internal_stat
