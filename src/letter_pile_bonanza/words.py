from __future__ import annotations

# Tiny starter lexicon so rules can be tested without a full dictionary file.
STARTER_WORDS = frozenset(
    {
        "a",
        "at",
        "cat",
        "act",
        "tac",
        "letter",
        "pile",
        "bonanza",
        "word",
        "game",
    }
)


def normalize_word(text: str) -> str:
    return "".join(ch.lower() for ch in text if ch.isalpha())


def is_valid_word(word: str, lexicon: frozenset[str] = STARTER_WORDS) -> bool:
    normalized = normalize_word(word)
    return bool(normalized) and normalized in lexicon
