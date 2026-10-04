from __future__ import annotations

import pygame

from letter_pile_bonanza import GAME_TITLE
from letter_pile_bonanza.pile import LetterPile, PileLetter
from letter_pile_bonanza.render import draw_frame
from letter_pile_bonanza.scoring import score_word
from letter_pile_bonanza.words import is_valid_word, normalize_word


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
    font = pygame.font.Font(None, 42)
    clock = pygame.time.Clock()
    pile = _starter_pile()
    typed = ""
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    typed = typed[:-1]
                elif event.key == pygame.K_RETURN:
                    word = normalize_word(typed)
                    if is_valid_word(word) and pile.can_spell(word):
                        pile.remove_word(word)
                        score += score_word(word)
                    typed = ""
                elif event.unicode.isalpha():
                    typed += event.unicode

        draw_frame(screen, pile, typed, score, font)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
