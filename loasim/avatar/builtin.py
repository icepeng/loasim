from loasim.avatar.base import Avatar, AvatarRepository
from loasim.core.stat import InternalStat

lostark_avatar_repository = AvatarRepository()

lostark_avatar_repository.add(
    Avatar(grade="rare", internal_stat=InternalStat(pstat_main=0.5))
)
lostark_avatar_repository.add(
    Avatar(grade="epic", internal_stat=InternalStat(pstat_main=1))
)
lostark_avatar_repository.add(
    Avatar(grade="legendary", internal_stat=InternalStat(pstat_main=2))
)
