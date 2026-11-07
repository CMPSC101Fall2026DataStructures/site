"""Animated starfield for the game background."""

import random

import pygame

from . import config


class Starfield:
    """A lightweight, randomly generated scrolling star background."""

    def __init__(self) -> None:
        self.stars = [
            [
                random.randrange(config.WIDTH),
                random.randrange(config.HEIGHT),
                random.choice((1, 1, 1, 2, 2, 3)),
                random.uniform(18, 90),
            ]
            for _ in range(config.STAR_COUNT)
        ]

    def update(self, delta_seconds: float) -> None:
        """Scroll stars down and wrap them to the top of the screen."""
        for star in self.stars:
            star[1] += star[3] * delta_seconds
            if star[1] > config.HEIGHT:
                star[0] = random.randrange(config.WIDTH)
                star[1] = 0

    def draw(self, surface: pygame.Surface) -> None:
        """Draw all stars with brightness based on their size."""
        for x, y, radius, _speed in self.stars:
            brightness = 95 + radius * 48
            pygame.draw.circle(
                surface,
                (brightness, brightness, min(255, brightness + 30)),
                (round(x), round(y)),
                radius,
            )
