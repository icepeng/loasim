import pytest

from loasim.setitem import SetItemState, lostark_setitem_repository


@pytest.mark.parametrize(
    "setitem_name, setitem_lv1, setitem_lv2",
    [
        ("환각", 2, 2),
        ("악몽", 3, 4),
        ("지배", 0, 6),
        ("구원", 6, 0),
    ],
)
def test_setitem_repository(setitem_name, setitem_lv1, setitem_lv2):
    lostark_setitem_repository.get_stat(
        [SetItemState(name=setitem_name, level_1=setitem_lv1, level_2=setitem_lv1)]
    )
