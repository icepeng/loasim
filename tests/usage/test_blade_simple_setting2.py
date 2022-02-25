from loguru import logger

from loasim.calculate import calculate
from loasim.card import lostark_default_card_repository
from loasim.core import Enemy, InternalStat, Stat
from loasim.Engraving import EngravingManager
from loasim.core.stat import sub_pdamage_indep
from loasim.job.blade import lostark_blade_skill_repository
from loasim.setitem import SetItemState, lostark_setitem_repository

base_internal_stat = InternalStat(
    weapon_att=41814, stat_main=137148, crit=568, special=1733, swift=28
)

base_stat = base_internal_stat.get_stat()
weapon_stat = Stat(pdamage=30)  # 무기 품질

logger.info(base_stat)
logger.info(weapon_stat)

setitem_state = [
    SetItemState(
        name="사멸",
        level_1=6,
        level_2=4,
    ),
]

engraving_manager = EngravingManager(
    ("원한", 3),
    ("슈퍼 차지", 3),
    ("기습의 대가", 3),
    ("예리한 둔기", 3),
    ("버스트", 3),
)

card = lostark_default_card_repository.get("남겨진 바람의 절벽 (12)")

spin_cutter_synergy = Stat(pdamage_indep=3, pdamage_indep_back=sub_pdamage_indep(12, 3))
blade_arts_3 = Stat(patt=30)
burst_stat = Stat(pdamage_indep=base_internal_stat.special * 0.11444)

basis_stat = (
    base_stat
    + weapon_stat
    + lostark_setitem_repository.get_stat(setitem_state)
    + engraving_manager.get_static_modifier()
    + card.stat
    + spin_cutter_synergy
)

logger.info(basis_stat)

SpinCutter = lostark_blade_skill_repository.build(
    name="스핀 커터",
    level=10,
    additional_stat=basis_stat.add_indep(blade_arts_3).add_indep(
        engraving_manager.get_dynamic_modifier(
            charge=False,
        )
    ),
)

SoulAbsorber = lostark_blade_skill_repository.build(
    name="소울 앱소버",
    level=11,
    gem=7,
    tripod={
        "암흑 공격": 5,
        "반 가르기": 4,
    },
    additional_stat=basis_stat.add_indep(blade_arts_3).add_indep(
        engraving_manager.get_dynamic_modifier(
            charge=True,
        )
    ),
)

VoidStrike = lostark_blade_skill_repository.build(
    name="보이드 스트라이크",
    level=11,
    gem=7,
    tripod={
        "암흑 공격": 4,
        "블랙 익스플로젼": 4,
    },
    additional_stat=basis_stat.add_indep(
        engraving_manager.get_dynamic_modifier(
            charge=True,
        )
    ),
)

BlitzRush = lostark_blade_skill_repository.build(
    name="블리츠 러시",
    level=11,
    gem=7,
    tripod={
        "급소 타격": 4,
        "차지 강화": 5,
        "쉐도우 러시": 5,
    },
    additional_stat=basis_stat.add_indep(blade_arts_3).add_indep(
        engraving_manager.get_dynamic_modifier(
            charge=True,
        )
    ),
)

WindCut = lostark_blade_skill_repository.build(
    name="윈드 컷",
    level=11,
    gem=5,
    tripod={
        "지속력 강화": 4,
    },
    additional_stat=basis_stat.add_indep(blade_arts_3).add_indep(
        engraving_manager.get_dynamic_modifier(
            charge=False,
        )
    ),
)

EarthSlash = lostark_blade_skill_repository.build(
    name="어스 슬래쉬",
    level=10,
    gem=5,
    tripod={
        "밀어내기": 4,
        "약점 포착": 4,
        "대지 폭발": 4,
    },
    additional_stat=basis_stat.add_indep(blade_arts_3).add_indep(
        engraving_manager.get_dynamic_modifier(
            charge=True,
        )
    ),
)

BladeBurst = lostark_blade_skill_repository.build(
    name="블레이드 버스트",
    level=11,
    gem=7,
    additional_stat=basis_stat.add_indep(blade_arts_3)
    .add_indep(
        engraving_manager.get_dynamic_modifier(
            charge=False,
            burst_stack=12,
        )
    )
    .add_indep(burst_stat),
)

dealcycle = [
    (SpinCutter, "back"),
    (SpinCutter, "back"),
    (SpinCutter, "back"),
    (WindCut, "back"),
    (SoulAbsorber, "back"),
    (EarthSlash, "back"),
    (BlitzRush, "back"),
    (WindCut, "back"),
    (BladeBurst, "back"),
    (VoidStrike, "back"),
]
cycle_time = 9.375

enemy = Enemy(armor=6000, reduction=23)

calculate(dealcycle, cycle_time, enemy)
