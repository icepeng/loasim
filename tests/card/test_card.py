from loasim.card import lostark_default_card_repository


def test_get_card_from_repository():
    card = lostark_default_card_repository.get("남겨진 바람의 절벽 (12)")
    assert card.stat.crit == 7
