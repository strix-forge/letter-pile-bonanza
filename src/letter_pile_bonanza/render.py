from __future__ import annotations

import pygame

from letter_pile_bonanza import GAME_TITLE
from letter_pile_bonanza.effects import FlyingLetter
from letter_pile_bonanza.pile import LetterPile
from letter_pile_bonanza.style import GRAY, typed_word_color

BACKGROUND = (24, 28, 36)
PANEL = (18, 22, 28)
LETTER_COLOR = (240, 232, 210)
HUD_COLOR = (180, 190, 200)
SCORE_FLASH = (255, 236, 170)
TOP_BAR_HEIGHT = 56
BOTTOM_BAR_HEIGHT = 80


def score_magnet(width: int) -> tuple[float, float]:
    return (width - 52.0, TOP_BAR_HEIGHT / 2 - 8)


def draw_frame(
    surface: pygame.Surface,
    pile: LetterPile,
    typed: str,
    score: int,
    hud_font: pygame.font.Font,
    entry_font: pygame.font.Font,
    shake_x: float = 0.0,
    flying: list[FlyingLetter] | None = None,
    score_pulse: float = 0.0,
) -> None:
    width, height = surface.get_size()
    surface.fill(BACKGROUND)

    pygame.draw.rect(surface, PANEL, (0, 0, width, TOP_BAR_HEIGHT))
    title = hud_font.render(GAME_TITLE, True, HUD_COLOR)
    remaining = hud_font.render(f"Letters {len(pile.letters())}", True, HUD_COLOR)
    score_color = _mix(HUD_COLOR, SCORE_FLASH, min(1.0, score_pulse))
    score_text = hud_font.render(f"Score {score}", True, score_color)
    surface.blit(title, (16, (TOP_BAR_HEIGHT - title.get_height()) // 2))
    surface.blit(
        remaining,
        (
            width - remaining.get_width() - score_text.get_width() - 40,
            (TOP_BAR_HEIGHT - remaining.get_height()) // 2,
        ),
    )
    surface.blit(score_text, (width - score_text.get_width() - 16, (TOP_BAR_HEIGHT - score_text.get_height()) // 2))

    for letter in pile.letters():
        glyph = hud_font.render(letter.char.upper(), True, LETTER_COLOR)
        surface.blit(glyph, (int(letter.x), int(letter.y)))

    pygame.draw.rect(surface, PANEL, (0, height - BOTTOM_BAR_HEIGHT, width, BOTTOM_BAR_HEIGHT))
    display = typed.upper()
    color = typed_word_color(len(display)) if display else GRAY
    entry = entry_font.render(display or "TYPE A WORD", True, color)
    entry_x = (width - entry.get_width()) // 2 + int(shake_x)
    entry_y = height - BOTTOM_BAR_HEIGHT + (BOTTOM_BAR_HEIGHT - entry.get_height()) // 2
    surface.blit(entry, (entry_x, entry_y))

    for letter in flying or ():
        _blit_flying(surface, hud_font, letter)


def _mix(
    a: tuple[int, int, int], b: tuple[int, int, int], t: float
) -> tuple[int, int, int]:
    return (
        int(a[0] + (b[0] - a[0]) * t),
        int(a[1] + (b[1] - a[1]) * t),
        int(a[2] + (b[2] - a[2]) * t),
    )


def _blit_flying(surface: pygame.Surface, font: pygame.font.Font, letter: FlyingLetter) -> None:
    glyph = font.render(letter.char.upper(), True, LETTER_COLOR)
    scale = max(0.2, letter.scale)
    width = max(1, int(glyph.get_width() * scale))
    height = max(1, int(glyph.get_height() * scale))
    glyph = pygame.transform.smoothscale(glyph, (width, height))
    glyph.set_alpha(int(255 * max(0.0, min(1.0, letter.alpha))))
    surface.blit(glyph, (int(letter.x), int(letter.y)))
