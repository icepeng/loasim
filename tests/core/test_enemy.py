from loasim.character import AccessoryState, AvatarState, Character, GearState


def test_get_internal_stat():
    character = Character(
        combat_level=59,
        expedition_stat=637,
        crit=537,
        special=56,
        swift=1691,
        gear_state=GearState(
            head=(1340, "relic", 19),
            shoulder=(1340, "relic", 19),
            top=(1340, "relic", 18),
            bottom=(1340, "relic", 18),
            glove=(1340, "relic", 19),
            weapon=(1340, "relic", 19),
        ),
        accessory_state=AccessoryState(
            necklace="relic",
            ear1="relic",
            ear2="relic",
            ring1="relic",
            ring2="relic",
        ),
        avatar_state=AvatarState(
            head="epic",
            top="epic",
            bottom="epic",
            weapon="epic",
        ),
    )

    assert character.get_internal_stat().stat_main == 115010
    assert character.get_internal_stat().weapon_att == 28800
    assert character.get_internal_stat().pstat_main == 4
