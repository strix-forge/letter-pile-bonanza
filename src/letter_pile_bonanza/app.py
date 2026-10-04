from __future__ import annotations

import pygame

from letter_pile_bonanza import GAME_TITLE
from letter_pile_bonanza.effects import FlyingLetter, InputShake, prune_flying, spawn_poof, update_flying
from letter_pile_bonanza.pile import LetterPile, PileLetter
from letter_pile_bonanza.render import draw_frame, score_magnet
from letter_pile_bonanza.submit import try_submit


def _starter_pile() -> LetterPile:
    samples = "letterpilebonanza"
    pile = LetterPile()
    for index, char in enumerate(samples):
        col = index % 8
        row = index // 8
        pile.add(PileLetter(id=index, char=char, x=80 + col * 48, y=120 + row * 56))
    return pile


def main() -> None:
    pygame.init()
    pygame.display.set_caption(GAME_TITLE)
    screen = pygame.display.set_mode((720, 480))
    hud_font = pygame.font.Font(None, 32)
    entry_font = pygame.font.Font(None, 56)
    clock = pygame.time.Clock()
    pile = _starter_pile()
    typed = ""
    score = 0
    shake = InputShake()
    flying: list[FlyingLetter] = []
    score_pulse = 0.0
    running = True

    while running:
        dt = min(clock.tick(60) / 1000.0, 0.05)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    typed = typed[:-1]
                elif event.key == pygame.K_RETURN:
                    result = try_submit(typed, pile)
                    if result.accepted:
                        magnet = score_magnet(screen.get_width())
                        flying.extend(spawn_poof(result.removed, magnet[0], magnet[1], result.points))
                        typed = ""
                    elif typed:
                        shake.start()
                elif event.unicode.isalpha():
                    typed += event.unicode.upper()

        shake.update(dt)
        gained = update_flying(flying, dt)
        if gained:
            score += gained
            score_pulse = 1.0
        flying = prune_flying(flying)
        score_pulse = max(0.0, score_pulse - dt * 2.8)

        draw_frame(
            screen,
            pile,
            typed,
            score,
            hud_font,
            entry_font,
            shake_x=shake.offset_x(),
            flying=flying,
            score_pulse=score_pulse,
        )
        pygame.display.flip()

    pygame.quit()
