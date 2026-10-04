from __future__ import annotations

from collections import Counter
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PileLetter:
    """One letter in the pile. Position is for the renderer, not for rules."""

    id: int
    char: str
    x: float = 0.0
    y: float = 0.0


class LetterPile:
    """Multiset of letters. Words consume one matching instance per character."""

    def __init__(self, letters: list[PileLetter] | None = None) -> None:
        self._letters: dict[int, PileLetter] = {}
        if letters:
            for letter in letters:
                self.add(letter)

    def add(self, letter: PileLetter) -> None:
        char = letter.char.lower()
        if len(char) != 1 or not char.isalpha():
            raise ValueError(f"Pile letters must be a single alphabetic character, got {letter.char!r}")
        self._letters[letter.id] = PileLetter(letter.id, char, letter.x, letter.y)

    def letters(self) -> list[PileLetter]:
        return list(self._letters.values())

    def counts(self) -> Counter[str]:
        return Counter(letter.char for letter in self._letters.values())

    def can_spell(self, word: str) -> bool:
        needed = Counter(ch.lower() for ch in word if ch.isalpha())
        if not needed:
            return False
        return all(self.counts()[ch] >= n for ch, n in needed.items())

    def remove_word(self, word: str) -> list[PileLetter]:
        if not self.can_spell(word):
            raise ValueError(f"Pile cannot spell {word!r}")
        remaining = Counter(ch.lower() for ch in word if ch.isalpha())
        removed: list[PileLetter] = []
        for letter in list(self._letters.values()):
            if remaining[letter.char] > 0:
                del self._letters[letter.id]
                removed.append(letter)
                remaining[letter.char] -= 1
        return removed
