from letter_pile_bonanza.pile import LetterPile, PileLetter
from letter_pile_bonanza.submit import try_submit


def _pile(*chars: str) -> LetterPile:
    return LetterPile([PileLetter(id=i, char=ch) for i, ch in enumerate(chars)])


def test_valid_word_removes_letters_and_scores() -> None:
    pile = _pile("c", "a", "t", "s")
    result = try_submit("cat", pile)
    assert result.accepted
    assert result.points == 9
    assert len(result.removed) == 3
    assert pile.can_spell("s")
    assert not pile.can_spell("cat")


def test_invalid_word_keeps_pile() -> None:
    pile = _pile("c", "a", "t")
    result = try_submit("xyzzy", pile)
    assert not result.accepted
    assert result.removed == ()
    assert pile.can_spell("cat")


def test_empty_submit_is_rejected() -> None:
    pile = _pile("a")
    result = try_submit("", pile)
    assert not result.accepted
