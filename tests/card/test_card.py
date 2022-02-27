from loasim.card import lostark_default_card_repository


def test_get_stat_from_repository():
    stat = lostark_default_card_repository.get_stat(["남겨진 바람의 절벽 (12)"])
    assert stat.crit == 7
