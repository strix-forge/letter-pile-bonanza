from __future__ import annotations

from dataclasses import dataclass

from letter_pile_bonanza.pile import LetterPile, PileLetter
from letter_pile_bonanza.scoring import score_word
from letter_pile_bonanza.words import is_valid_word, normalize_word


@dataclass(frozen=True, slots=True)
class SubmitResult:
    accepted: bool
    word: str
    removed: tuple[PileLetter, ...]
    points: int


def try_submit(typed: str, pile: LetterPile) -> SubmitResult:
    word = normalize_word(typed)
    if not word:
        return SubmitResult(False, word, (), 0)
    if is_valid_word(word) and pile.can_spell(word):
        removed = tuple(pile.remove_word(word))
        return SubmitResult(True, word, removed, score_word(word))
    return SubmitResult(False, word, (), 0)
