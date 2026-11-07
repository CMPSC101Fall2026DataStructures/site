"""Projectile sprite used by both the player and the invaders."""

import pygame

from . import config


class Projectile(pygame.sprite.Sprite):
    """A small vertical shot that travels up or down the screen."""

    def __init__(
        self,
        x: int,
        y: int,
        velocity_y: float,
        color: tuple[int, int, int],
    ) -> None:
        super().__init__()
        self.image = pygame.Surface((5, 18), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (1, 0, 3, 18), border_radius=2)
        pygame.draw.circle(self.image, config.WHITE, (2, 4), 2)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity_y = velocity_y
        self.color = color
        self.position_y = float(self.rect.y)

    def update(self, delta_seconds: float) -> None:
        """Move the shot and remove it after it leaves the window."""
        self.position_y += self.velocity_y * delta_seconds
        self.rect.y = round(self.position_y)
        if self.rect.bottom < 0 or self.rect.top > config.HEIGHT:
            self.kill()
