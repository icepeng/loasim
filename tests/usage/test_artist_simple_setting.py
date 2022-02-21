from loguru import logger

from loasim.calculate import calculate
from loasim.card import lostark_default_card_repository
from loasim.core import Enemy, InternalStat, Stat
from loasim.Engraving import EngravingManager
from loasim.job import artist
from loasim.setitem import SetItemState, lostark_setitem_repository

base_internal_stat = InternalStat(
    weapon_att=28800, stat_main=119610, crit=537, special=56, swift=1691
)
spd = base_internal_stat.get_spd() + 10  # 갈망 +10

base_stat = base_internal_stat.get_stat()
weapon_stat = Stat(pdamage=21.86)  # 무기 품질

logger.info(base_stat)
logger.info(weapon_stat)

setitem_state = [
    SetItemState(
        name="악몽",
        level_1=2,
        level_2=0,
    ),
    SetItemState(
        name="지배",
        level_1=4,
        level_2=0,
    ),
]

engraving_manager = EngravingManager(
    ("원한", 3), ("예리한 둔기", 3), ("안정된 상태", 3), ("돌격대장", 3), ("회귀", 3)
)
card = lostark_default_card_repository.get("남겨진 바람의 절벽 (12)")
if card is None:
    raise

SunDrawBuff = Stat(crit=49.7)  # 나만의 권능 5
SunWellBuff = Stat(patt=30)  # 나만의 우물

basis_stat = (
    base_stat
    + weapon_stat
    + lostark_setitem_repository.get_stat(setitem_state)
    + engraving_manager.get_static_modifier()
    + card.stat
    + SunDrawBuff
    + SunWellBuff
    + engraving_manager.get_dynamic_modifier(spd=spd)
)

logger.info(basis_stat)

OneStroke = artist.OneStroke.build_skill(
    gem=7,
    tripod={
        "거대한 붓": 5,
        "강화된 일격": 5,
    },
    additional_stat=basis_stat,
)

Cranes = artist.Cranes.build_skill(
    gem=5,
    tripod={
        "치명적인 일격": 5,
        "학익진": 5,
    },
    additional_stat=basis_stat,
)

Tiger = artist.Tiger.build_skill(
    gem=6,
    tripod={
        "궤뚫는 일격": 5,
        "강화된 일격": 5,
    },
    additional_stat=basis_stat,
)

Moon = artist.Moon.build_skill(
    gem=7,
    tripod={
        "별 그리기": 4,
        "붉은 달": 4,
    },
    additional_stat=basis_stat,
)

InkRise = artist.InkRise.build_skill(
    gem=5,
    tripod={
        "치명적인 일격": 1,
        "먹물점정": 1,
    },
    additional_stat=basis_stat,
)

dealcycle = [
    OneStroke,
    Cranes,
    Tiger,
    Moon,
    InkRise,
]
cycle_time = 12.127

enemy = Enemy(armor=6000, reduction=23)

calculate(dealcycle, cycle_time, enemy)
