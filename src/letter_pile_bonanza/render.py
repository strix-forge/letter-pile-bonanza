from __future__ import annotations

import pygame

from letter_pile_bonanza import GAME_TITLE
from letter_pile_bonanza.pile import LetterPile

BACKGROUND = (24, 28, 36)
LETTER_COLOR = (240, 232, 210)
HUD_COLOR = (180, 190, 200)


def draw_frame(
    surface: pygame.Surface,
    pile: LetterPile,
    typed: str,
    score: int,
    font: pygame.font.Font,
) -> None:
    surface.fill(BACKGROUND)
    for letter in pile.letters():
        glyph = font.render(letter.char.upper(), True, LETTER_COLOR)
        surface.blit(glyph, (int(letter.x), int(letter.y)))

    hud = font.render(f"{GAME_TITLE}  |  type a word  |  {typed}  |  score {score}", True, HUD_COLOR)
    surface.blit(hud, (16, 16))
