def score_word(word: str) -> int:
    """Longer words score better. Non-letters are ignored."""
    letters = [ch for ch in word if ch.isalpha()]
    n = len(letters)
    if n == 0:
        return 0
    return n * n
