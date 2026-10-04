from letter_pile_bonanza.style import GRAY, GREEN, ORANGE, RED, typed_word_color


def test_typed_word_color_by_length() -> None:
    assert typed_word_color(0) == GRAY
    assert typed_word_color(3) == GRAY
    assert typed_word_color(4) == GREEN
    assert typed_word_color(5) == GREEN
    assert typed_word_color(6) == ORANGE
    assert typed_word_color(7) == ORANGE
    assert typed_word_color(8) == RED
    assert typed_word_color(12) == RED
