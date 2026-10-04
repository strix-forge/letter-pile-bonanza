from letter_pile_bonanza.scoring import score_word


def test_longer_words_score_higher() -> None:
    assert score_word("at") < score_word("cat") < score_word("letter")


def test_empty_word_scores_zero() -> None:
    assert score_word("") == 0
