import pytest

from loasim.accessory import AccessoryStatus, lostark_accessory_repository


@pytest.mark.parametrize(
    "grade",
    ["epic", "legendary", "relic", "ancient"],
)
def test_accessory(grade: str):
    lostark_accessory_repository.get_internal_stat(
        AccessoryStatus(
            necklace=grade, ear1=grade, ear2=grade, ring1=grade, ring2=grade
        )
    )
