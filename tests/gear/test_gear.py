from loasim.gear import GearState, GearStatus, lostark_gear_repository


def test_gear_repository():
    lostark_gear_repository.get_internal_stat(
        GearStatus(
            head=GearState(base_item_level=1340, grade="relic", upgrade=19),
            shoulder=GearState(base_item_level=1340, grade="relic", upgrade=19),
            top=GearState(base_item_level=1340, grade="relic", upgrade=18),
            bottom=GearState(base_item_level=1340, grade="relic", upgrade=18),
            glove=GearState(base_item_level=1340, grade="relic", upgrade=19),
            weapon=GearState(base_item_level=1340, grade="relic", upgrade=19),
        ),
    )
