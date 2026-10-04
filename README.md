# Letter Pile Bonanza

A small Python desktop game: a huge pile of letters, cleared only by typing words that use letters from the pile. Longer words are worth more.

## Requirements

- Python 3.10+ (developed on 3.14)
- [pygame-ce](https://pyga.me/) for the window and drawing

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

## Run

```powershell
python -m letter_pile_bonanza
```

## Tests

```powershell
python -m pytest
```

Game rules live in Python modules without pygame so they can be tested without opening a window. Drawing stays in `render.py`.
