"""Player ship controls and firing behavior."""

import pygame

from . import config
from .projectile import Projectile


class Player(pygame.sprite.Sprite):
    """The ship controlled by the player."""

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((54, 42), pygame.SRCALPHA)
        pygame.draw.polygon(
            self.image,
            config.CYAN,
            [(27, 0), (52, 36), (40, 34), (34, 24), (20, 24), (14, 34), (2, 36)],
        )
        pygame.draw.rect(self.image, config.WHITE, (21, 28, 12, 5), border_radius=2)
        self.rect = self.image.get_rect(midbottom=(config.WIDTH // 2, config.HEIGHT - 28))
        self.position_x = float(self.rect.x)
        self.last_shot = 0

    def update(self, keys: pygame.key.ScancodeWrapper, delta_seconds: float) -> None:
        """Move horizontally and keep the ship inside the playfield."""
        direction = int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(
            keys[pygame.K_LEFT] or keys[pygame.K_a]
        )
        self.position_x += direction * config.PLAYER_SPEED * delta_seconds
        self.rect.x = round(self.position_x)
        self.rect.left = max(12, self.rect.left)
        self.rect.right = min(config.WIDTH - 12, self.rect.right)
        self.position_x = float(self.rect.x)

    def shoot(self, now_ms: int) -> Projectile | None:
        """Return a player shot when the firing cooldown has elapsed."""
        if now_ms - self.last_shot < config.PLAYER_COOLDOWN_MS:
            return None
        self.last_shot = now_ms
        return Projectile(
            self.rect.centerx,
            self.rect.top,
            -config.PLAYER_BULLET_SPEED,
            config.CYAN,
        )
