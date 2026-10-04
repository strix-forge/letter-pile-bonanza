# Agent notes — Letter Pile Bonanza

Desktop word game: a scattered pile of letters is cleared by typing words that use those letters. Longer words score better. Window title is **Letter Pile Bonanza**.

## Layout

- `src/letter_pile_bonanza/pile.py` — pile state and letter removal (no pygame).
- `src/letter_pile_bonanza/scoring.py` — word scores (no pygame).
- `src/letter_pile_bonanza/words.py` — dictionary / validation (no pygame).
- `src/letter_pile_bonanza/render.py` — pygame drawing only.
- `src/letter_pile_bonanza/app.py` — window, event loop, wiring.
- `tests/` — unit tests for pile, scoring, and words. Tests must not open a window.

Keep rules and rendering separate. Do not import pygame from `pile.py`, `scoring.py`, or `words.py`.

## Commands (Windows)

From the repo root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m letter_pile_bonanza
python -m pytest
```

Use `python -m pip` (bare `pip` may be missing from PATH).

## Product constraints

- First visual: scattered 2D letters, still readable; overlapping layers can come later.
- Typing a valid word removes those letters from the pile (multiset: one letter instance per use).
- Prefer small, testable changes. Do not mix scoring changes with renderer refactors in the same edit unless asked.
