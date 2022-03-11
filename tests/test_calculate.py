from loasim.accessory import AccessoryStatus
from loasim.avatar import AvatarStatus
from loasim.calculate import DealCycle, SkillAction, calculate
from loasim.character import Character
from loasim.core import BuffState, Enemy
from loasim.gear import GearState, GearStatus
from loasim.job import SkillState
from loasim.setitem import SetItemState


def test_calculate():
    test_character = Character(
        job_name="scouter",
        combat_level=60,
        expedition_stat=0,
        crit=600,
        special=1800,
        swift=0,
        weapon_pdamage=30,
        gear_status=GearStatus(
            head=GearState(base_item_level=1390, grade="ancient", upgrade=25),
            top=GearState(base_item_level=1390, grade="ancient", upgrade=25),
            bottom=GearState(base_item_level=1390, grade="ancient", upgrade=25),
            glove=GearState(base_item_level=1390, grade="ancient", upgrade=25),
            shoulder=GearState(base_item_level=1390, grade="ancient", upgrade=25),
            weapon=GearState(base_item_level=1390, grade="ancient", upgrade=25),
        ),
        accessory_status=AccessoryStatus(
            necklace="ancient",
            ear1="ancient",
            ear2="ancient",
            ring1="ancient",
            ring2="ancient",
        ),
        avatar_status=AvatarStatus(
            head="legendary",
            top="legendary",
            bottom="legendary",
            weapon="legendary",
        ),
        setitem_status={"환각": SetItemState(level1=6, level2=6)},
        card_status=["세상을 구하는 빛 (30)"],
        engraving_status={
            "원한": 3,
            "바리케이드": 3,
            "돌격대장": 3,
            "예리한 둔기": 3,
            "아드레날린": 3,
            "진화의 유산": 1,
        },
        skill_status={"엑셀리온 빔": SkillState(level=12, gem=10)},
    )

    calculate(
        character=test_character,
        enemy=Enemy(armor=6000, reduction=23),
        deal_cycle=DealCycle(
            skill_actions=[
                SkillAction(
                    name="엑셀리온 빔",
                    status={
                        "진화의 유산": BuffState(onoff=True, stack=3),
                        "하이퍼 싱크": BuffState(onoff=True),
                        "환각": BuffState(onoff=False),
                        "실체": BuffState(onoff=True),
                    },
                    position=None,
                )
            ],
            cycle_time=1,
        ),
    )
