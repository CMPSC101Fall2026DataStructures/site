"""Invader sprite definitions."""

import pygame

from . import config


class Invader(pygame.sprite.Sprite):
    """A colorful alien in the marching formation."""

    def __init__(self, x: int, y: int, row: int) -> None:
        super().__init__()
        self.image = pygame.Surface((42, 34), pygame.SRCALPHA)
        color = (config.PINK, config.GREEN, config.YELLOW, config.CYAN)[row % 4]
        pygame.draw.rect(self.image, color, (8, 5, 26, 21), border_radius=6)
        pygame.draw.rect(self.image, color, (2, 13, 8, 11), border_radius=3)
        pygame.draw.rect(self.image, color, (32, 13, 8, 11), border_radius=3)
        pygame.draw.rect(self.image, config.BACKGROUND, (13, 12, 5, 6))
        pygame.draw.rect(self.image, config.BACKGROUND, (24, 12, 5, 6))
        pygame.draw.line(self.image, color, (12, 25), (7, 32), 4)
        pygame.draw.line(self.image, color, (30, 25), (35, 32), 4)
        self.rect = self.image.get_rect(topleft=(x, y))

