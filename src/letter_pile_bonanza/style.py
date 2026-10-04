"""Display colors for typed words. Longer entries change color by length."""

GRAY = (160, 160, 168)
GREEN = (72, 196, 96)
ORANGE = (232, 148, 48)
RED = (220, 64, 64)


def typed_word_color(letter_count: int) -> tuple[int, int, int]:
    """Gray through 3 letters, green at 4, orange at 6, red at 8."""
    if letter_count >= 8:
        return RED
    if letter_count >= 6:
        return ORANGE
    if letter_count >= 4:
        return GREEN
    return GRAY
