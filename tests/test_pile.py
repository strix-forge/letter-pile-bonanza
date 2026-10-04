import pytest

from letter_pile_bonanza.pile import LetterPile, PileLetter


def _pile(*chars: str) -> LetterPile:
    return LetterPile([PileLetter(id=i, char=ch) for i, ch in enumerate(chars)])


def test_can_spell_uses_letter_counts() -> None:
    pile = _pile("c", "a", "t")
    assert pile.can_spell("cat")
    assert not pile.can_spell("ccat")


def test_remove_word_subtracts_one_instance_each() -> None:
    pile = _pile("l", "e", "t", "t", "e", "r")
    removed = pile.remove_word("letter")
    assert len(removed) == 6
    assert pile.letters() == []


def test_remove_word_raises_when_missing_letters() -> None:
    pile = _pile("a", "t")
    with pytest.raises(ValueError):
        pile.remove_word("cat")
