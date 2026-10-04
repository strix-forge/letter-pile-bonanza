"""Input shake and letter-poof motion. No pygame — positions only."""

from __future__ import annotations

import math
from dataclasses import dataclass

from letter_pile_bonanza.pile import PileLetter

SHAKE_DURATION = 0.42
SHAKE_AMPLITUDE = 26.0
SHAKE_HZ = 18.0
POOF_SECONDS = 0.14
HOMING_RATE = 6.2
ARRIVE_DISTANCE = 18.0


@dataclass
class InputShake:
    elapsed: float = 0.0
    duration: float = SHAKE_DURATION
    playing: bool = False

    def start(self) -> None:
        self.elapsed = 0.0
        self.playing = True

    def update(self, dt: float) -> None:
        if not self.playing:
            return
        self.elapsed += dt
        if self.elapsed >= self.duration:
            self.playing = False

    def offset_x(self) -> float:
        if not self.playing:
            return 0.0
        decay = 1.0 - (self.elapsed / self.duration)
        return math.sin(self.elapsed * SHAKE_HZ * math.tau) * SHAKE_AMPLITUDE * decay


@dataclass
class FlyingLetter:
    char: str
    x: float
    y: float
    vx: float
    vy: float
    target_x: float
    target_y: float
    delay: float
    points: int
    age: float = 0.0
    scale: float = 1.0
    alpha: float = 1.0
    awarded: bool = False

    @property
    def gone(self) -> bool:
        return self.awarded and self.alpha <= 0.0


def split_points(total: int, count: int) -> list[int]:
    if count <= 0:
        return []
    base, extra = divmod(total, count)
    parts = [base] * count
    parts[-1] += extra
    return parts


def spawn_poof(
    removed: list[PileLetter] | tuple[PileLetter, ...],
    target_x: float,
    target_y: float,
    total_points: int,
) -> list[FlyingLetter]:
    n = len(removed)
    parts = split_points(total_points, n)
    flying: list[FlyingLetter] = []
    for index, letter in enumerate(removed):
        angle = (index / max(n, 1)) * math.tau + 0.55
        speed = 220.0 + index * 18.0
        flying.append(
            FlyingLetter(
                char=letter.char,
                x=letter.x,
                y=letter.y,
                vx=math.cos(angle) * speed,
                vy=math.sin(angle) * speed - 90.0,
                target_x=target_x,
                target_y=target_y,
                delay=index * 0.045,
                points=parts[index],
            )
        )
    return flying


def update_flying(letters: list[FlyingLetter], dt: float) -> int:
    awarded = 0
    for letter in letters:
        if letter.delay > 0:
            letter.delay -= dt
            continue
        letter.age += dt
        if letter.age <= POOF_SECONDS:
            letter.x += letter.vx * dt
            letter.y += letter.vy * dt
            letter.scale = 1.0 + 0.55 * (letter.age / POOF_SECONDS)
            continue
        step = 1.0 - math.exp(-HOMING_RATE * dt)
        letter.x += (letter.target_x - letter.x) * step
        letter.y += (letter.target_y - letter.y) * step
        dist = math.hypot(letter.target_x - letter.x, letter.target_y - letter.y)
        if dist < ARRIVE_DISTANCE:
            if not letter.awarded:
                letter.awarded = True
                awarded += letter.points
            letter.alpha = max(0.0, letter.alpha - dt * 7.0)
            letter.scale = max(0.2, letter.scale - dt * 3.5)
        else:
            letter.scale = max(0.85, 1.55 - (letter.age - POOF_SECONDS) * 0.9)
    return awarded


def prune_flying(letters: list[FlyingLetter]) -> list[FlyingLetter]:
    return [letter for letter in letters if not letter.gone]
