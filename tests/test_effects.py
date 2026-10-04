from letter_pile_bonanza.effects import InputShake, spawn_poof, split_points, update_flying
from letter_pile_bonanza.pile import PileLetter


def test_shake_moves_then_settles() -> None:
    shake = InputShake()
    assert shake.offset_x() == 0
    shake.start()
    shake.update(0.05)
    assert shake.offset_x() != 0
    shake.update(1.0)
    assert not shake.playing
    assert shake.offset_x() == 0


def test_poof_awards_all_points_on_arrival() -> None:
    removed = [PileLetter(id=i, char=ch, x=80.0, y=200.0) for i, ch in enumerate("cat")]
    flying = spawn_poof(removed, target_x=670.0, target_y=20.0, total_points=9)
    assert split_points(9, 3) == [3, 3, 3]
    total = 0
    for _ in range(240):
        total += update_flying(flying, 1 / 60)
        if all(letter.awarded for letter in flying):
            break
    assert total == 9
    assert all(letter.awarded for letter in flying)
