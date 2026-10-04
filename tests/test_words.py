from letter_pile_bonanza.words import is_valid_word, normalize_word


def test_normalize_strips_non_letters() -> None:
    assert normalize_word(" Cat! ") == "cat"


def test_starter_lexicon_accepts_known_words() -> None:
    assert is_valid_word("pile")
    assert not is_valid_word("xyzzy")
