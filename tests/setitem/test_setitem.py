import pytest

from loasim.setitem import SetItemState, lostark_setitem_repository


@pytest.mark.parametrize(
    "setitem_name",
    ["환각", "악몽", "지배", "구원", "사멸"],
)
@pytest.mark.parametrize(
    "setitem_lv1, setitem_lv2",
    [
        (2, 0),
        (4, 0),
        (6, 0),
        (6, 2),
        (6, 4),
        (6, 6),
    ],
)
def test_setitem_repository(setitem_name: str, setitem_lv1: int, setitem_lv2: int):
    lostark_setitem_repository.get_stat(
        {setitem_name: SetItemState(level1=setitem_lv1, level2=setitem_lv2)}
    )
    lostark_setitem_repository.get_buffs(
        {setitem_name: SetItemState(level1=setitem_lv1, level2=setitem_lv2)}
    )
