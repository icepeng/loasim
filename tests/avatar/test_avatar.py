import pytest

from loasim.avatar import AvatarStatus, lostark_avatar_repository


@pytest.mark.parametrize(
    "grade, expected_pstat_main",
    [("rare", 2), ("epic", 4), ("legendary", 8)],
)
def test_avatar(grade: str, expected_pstat_main: float):
    internal_stat = lostark_avatar_repository.get_internal_stat(
        AvatarStatus(head=grade, top=grade, bottom=grade, weapon=grade)
    )

    assert internal_stat.pstat_main == expected_pstat_main
