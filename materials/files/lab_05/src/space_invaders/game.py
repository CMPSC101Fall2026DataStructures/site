"""Main game loop and coordination between the game modules."""

import random

import pygame

from . import config
from .background import Starfield
from .enemy import Invader
from .player import Player
from .projectile import Projectile


class Game:
    """Own the window, game state, sprites, and main event loop."""

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(config.TITLE)
        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 30)
        self.large_font = pygame.font.Font(None, 76)
        self.small_font = pygame.font.Font(None, 22)
        self.background = Starfield()
        self.running = True
        self.started = False
        self.game_over = False
        self.reset_round()

    def reset_round(self) -> None:
        """Start a fresh game with a new player and invader formation."""
        self.player = Player()
        self.player_shots = pygame.sprite.Group()
        self.enemy_shots = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.score = 0
        self.lives = 3
        self.wave = 1
        self.enemy_direction = 1
        self.enemy_shot_timer = 0.0
        self._create_formation()

    def _create_formation(self) -> None:
        """Create a centered grid of invaders."""
        formation_width = config.ENEMY_COLUMNS * 64
        left = (config.WIDTH - formation_width) // 2
        for row in range(config.ENEMY_ROWS):
            for column in range(config.ENEMY_COLUMNS):
                self.enemies.add(
                    Invader(left + column * 64, 115 + row * 52, row)
                )

    def run(self) -> None:
        """Run until the player quits."""
        while self.running:
            delta_seconds = min(self.clock.tick(config.FPS) / 1000, 0.05)
            self._handle_events()
            self.background.update(delta_seconds)
            if self.started and not self.game_over:
                self._update_game(delta_seconds)
            self._draw()
        pygame.quit()

    def _handle_events(self) -> None:
        """Handle window events and the game's keyboard controls."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif not self.started and event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    self.started = True
                elif self.game_over and event.key == pygame.K_r:
                    self.reset_round()
                    self.started = True
                elif self.started and not self.game_over and event.key == pygame.K_SPACE:
                    shot = self.player.shoot(pygame.time.get_ticks())
                    if shot is not None:
                        self.player_shots.add(shot)

    def _update_game(self, delta_seconds: float) -> None:
        """Advance sprites, formation movement, and collision-driven state."""
        keys = pygame.key.get_pressed()
        self.player.update(keys, delta_seconds)
        self.player_shots.update(delta_seconds)
        self.enemy_shots.update(delta_seconds)
        self._move_formation(delta_seconds)
        self._update_enemy_fire(delta_seconds)
        self._handle_collisions()
        if not self.enemies and not self.game_over:
            self.wave += 1
            self.enemy_direction = 1
            self._create_formation()

    def _move_formation(self, delta_seconds: float) -> None:
        """Move the formation sideways and step down at the screen edges."""
        speed = 42 + (self.wave - 1) * 9
        for enemy in self.enemies:
            enemy.rect.x += round(self.enemy_direction * speed * delta_seconds)
        if self.enemies:
            left_edge = min(enemy.rect.left for enemy in self.enemies)
            right_edge = max(enemy.rect.right for enemy in self.enemies)
            if left_edge <= 18 or right_edge >= config.WIDTH - 18:
                self.enemy_direction *= -1
                for enemy in self.enemies:
                    enemy.rect.y += config.ENEMY_DROP
                    if enemy.rect.bottom >= self.player.rect.top:
                        self.game_over = True

    def _update_enemy_fire(self, delta_seconds: float) -> None:
        """Occasionally let a randomly selected invader fire at the player."""
        self.enemy_shot_timer += delta_seconds
        interval = max(0.35, config.ENEMY_SHOT_INTERVAL - (self.wave - 1) * 0.08)
        if self.enemies and self.enemy_shot_timer >= interval:
            self.enemy_shot_timer = 0.0
            shooter = random.choice(self.enemies.sprites())
            self.enemy_shots.add(
                Projectile(
                    shooter.rect.centerx,
                    shooter.rect.bottom,
                    config.ENEMY_BULLET_SPEED,
                    config.PINK,
                )
            )

    def _handle_collisions(self) -> None:
        """Update score and lives when projectiles hit their targets."""
        hits = pygame.sprite.groupcollide(
            self.enemies, self.player_shots, True, True
        )
        self.score += len(hits) * 10
        if pygame.sprite.spritecollide(self.player, self.enemy_shots, True):
            self.lives -= 1
            if self.lives <= 0:
                self.game_over = True

    def _draw(self) -> None:
        """Render the starfield, sprites, HUD, and any screen overlays."""
        self.screen.fill(config.BACKGROUND)
        self.background.draw(self.screen)
        pygame.draw.line(
            self.screen, (30, 58, 84), (0, config.HEIGHT - 15), (config.WIDTH, config.HEIGHT - 15), 2
        )
        if self.started:
            self.enemies.draw(self.screen)
            self.player_shots.draw(self.screen)
            self.enemy_shots.draw(self.screen)
            if not self.game_over:
                self.screen.blit(self.player.image, self.player.rect)
            self._draw_hud()
        else:
            self._draw_centered("SPACE INVADERS", self.large_font, config.CYAN, 250)
            self._draw_centered("A MODULES IN MOTION ARCADE GAME", self.font, config.WHITE, 310)
            self._draw_centered("Press ENTER or SPACE to begin", self.font, config.YELLOW, 390)
            self._draw_centered("Move: LEFT / RIGHT or A / D     Fire: SPACE", self.small_font, config.MUTED, 435)
        if self.game_over:
            pygame.draw.rect(
                self.screen,
                (8, 12, 34),
                pygame.Rect(190, 250, 520, 190),
                border_radius=18,
            )
            pygame.draw.rect(
                self.screen,
                config.PINK,
                pygame.Rect(190, 250, 520, 190),
                width=2,
                border_radius=18,
            )
            self._draw_centered("GAME OVER", self.large_font, config.PINK, 300)
            self._draw_centered("Press R to play again", self.font, config.WHITE, 370)
        pygame.display.flip()

    def _draw_hud(self) -> None:
        """Draw score, lives, and wave number."""
        self.screen.blit(
            self.font.render(f"SCORE  {self.score:05d}", True, config.WHITE), (24, 20)
        )
        self.screen.blit(
            self.font.render(f"WAVE  {self.wave}", True, config.CYAN), (config.WIDTH // 2 - 45, 20)
        )
        self.screen.blit(
            self.font.render(f"LIVES  {self.lives}", True, config.GREEN),
            (config.WIDTH - 145, 20),
        )

    def _draw_centered(
        self,
        text: str,
        font: pygame.font.Font,
        color: tuple[int, int, int],
        y: int,
    ) -> None:
        """Draw text centered horizontally at a chosen vertical position."""
        image = font.render(text, True, color)
        self.screen.blit(image, image.get_rect(center=(config.WIDTH // 2, y)))
