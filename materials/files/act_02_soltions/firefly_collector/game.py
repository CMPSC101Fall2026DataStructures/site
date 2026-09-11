"""The Pygame window, the main loop, and all of the drawing for the game.

Run the game from the top of the project with:

    uv run firefly-collector

Everything you see on screen is drawn from simple shapes -- circles for the
player, the fireflies, and the creatures, and rectangles for the trees.  The
atmosphere comes from stacking several translucent circles on top of one
another to make a soft glow.

Bug fixed in this file: number 10.
"""

import math
import sys

import pygame

from firefly_collector import config
from firefly_collector import entities


# ---------------------------------------------------------------------------
# Drawing helpers
# ---------------------------------------------------------------------------


def draw_forest(screen):
    """Fill the screen with night sky and draw the trees on top of it."""
    screen.fill(config.COLORS["night_sky"])

    for left, top, width, height in config.TREE_POSITIONS:
        # The trunk: a narrow, slightly browner rectangle.
        trunk_width = max(4, width // 4)
        trunk_left = left + (width - trunk_width) // 2
        pygame.draw.rect(
            screen,
            (34, 26, 22),
            pygame.Rect(trunk_left, top + height // 2, trunk_width, height // 2),
        )

        # The canopy: a triangle of dark forest green sitting on the trunk.
        tree_color = config.COLORS["tree"]
        canopy = [
            (left + width // 2, top),
            (left, top + height // 2 + 10),
            (left + width, top + height // 2 + 10),
        ]
        pygame.draw.polygon(screen, tree_color, canopy)


def draw_darkness(screen, player):
    """Darken the whole forest, then punch a soft lantern hole around player.

    The trick here is to build a second, see-through surface, fill it with
    black, and then draw shrinking circles of less and less black into it.
    Blitting that surface over the forest leaves a pool of light around the
    player and gloom everywhere else.
    """
    darkness = pygame.Surface(
        (config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SRCALPHA
    )
    darkness.fill((0, 0, 0, 170))

    lantern_radius = config.GAME_SETTINGS["lantern_radius"]
    center = (int(player["x"]), int(player["y"]))
    rings = 24

    # Draw the biggest circle first and the smallest one last, so that each
    # circle overwrites the middle of the one before it.
    for step in range(rings):
        radius = int(lantern_radius * (rings - step) / rings)
        alpha = int(170 * (rings - step - 1) / rings)
        pygame.draw.circle(darkness, (0, 0, 0, alpha), center, radius)

    screen.blit(darkness, (0, 0))


def draw_glowing_circle(screen, color, center, radius, brightness):
    """Draw one circle wrapped in a soft halo of the same color.

    The halo is four circles: a wide, very faint one, then smaller and
    brighter ones, and finally the solid dot in the middle.
    """
    # Each pair is (how many times wider than the dot, how solid).
    halo_layers = [(6.0, 22), (4.0, 38), (2.4, 70), (1.0, 255)]

    widest = int(radius * halo_layers[0][0]) + 2
    size = widest * 2
    halo = pygame.Surface((size, size), pygame.SRCALPHA)

    for scale, alpha in halo_layers:
        layer_color = (
            color[0],
            color[1],
            color[2],
            int(alpha * brightness),
        )
        pygame.draw.circle(
            halo, layer_color, (widest, widest), max(1, int(radius * scale))
        )

    screen.blit(halo, (int(center[0]) - widest, int(center[1]) - widest))


def draw_firefly(screen, firefly, milliseconds):
    """Draw one gently flickering firefly."""
    # sin() slides smoothly between -1 and 1, so this expression slides
    # smoothly between 0.45 and 1.0: a gentle pulse rather than a blink.
    pulse = 0.72 + 0.28 * math.sin(milliseconds / 260.0 + firefly["flicker"])

    draw_glowing_circle(
        screen,
        config.COLORS["firefly"],
        (firefly["x"], firefly["y"]),
        firefly["radius"],
        pulse,
    )


def draw_player(screen, player, milliseconds):
    """Draw the player and the warm pool of lantern light around them."""
    # Flash the player while they are recovering from being caught.
    if player["recovery"] > 0 and int(milliseconds / 120) % 2 == 0:
        return

    # A small warm halo right at the lantern.  The wide pool of light around
    # the player is made by draw_darkness(), not here.
    draw_glowing_circle(
        screen,
        config.COLORS["lantern"],
        (player["x"], player["y"]),
        player["radius"] // 2,
        0.6,
    )
    pygame.draw.circle(
        screen,
        config.COLORS["player"],
        (int(player["x"]), int(player["y"])),
        player["radius"],
    )
    # A small pale dot for the lantern the player is carrying.
    pygame.draw.circle(
        screen,
        config.COLORS["lantern"],
        (int(player["x"]) + player["radius"] // 2, int(player["y"])),
        3,
    )


def draw_creature(screen, creature, milliseconds):
    """Draw one nocturnal creature."""
    color = config.COLORS[creature["kind"]]
    center = (int(creature["x"]), int(creature["y"]))

    if creature["kind"] == "shadow":
        # The shadow creature breathes in and out as it drifts along.
        wobble = 1.0 + 0.12 * math.sin(milliseconds / 300.0)
        draw_glowing_circle(screen, color, center, creature["radius"], 0.5)
        pygame.draw.circle(screen, color, center, int(creature["radius"] * wobble))
    else:
        # The owl: a round body with two staring eyes.
        pygame.draw.circle(screen, color, center, creature["radius"])
        for side in (-6, 6):
            pygame.draw.circle(screen, (250, 250, 220), (center[0] + side, center[1] - 4), 4)
            pygame.draw.circle(screen, (20, 20, 20), (center[0] + side, center[1] - 4), 2)


def draw_hud(screen, font, state, seconds_left):
    """Draw the score, the timer, the lives, and any warning message."""
    score_text = font.render(
        "Score: " + str(state["score"]), True, config.COLORS["text"]
    )
    screen.blit(score_text, (16, 14))

    timer_text = font.render(
        "Time: " + str(int(seconds_left)), True, config.COLORS["text"]
    )
    screen.blit(timer_text, (16, 40))

    lives_text = font.render(
        "Lives: " + "*" * state["lives"], True, config.COLORS["warning"]
    )
    screen.blit(lives_text, (16, 66))

    # Warn the player as each creature wakes up.
    warning = ""
    if seconds_left <= config.GAME_SETTINGS["shadow_appears_at"]:
        warning = config.MESSAGES["shadow_warning"]
    elif seconds_left <= config.GAME_SETTINGS["owl_appears_at"]:
        warning = config.MESSAGES["owl_warning"]

    if warning != "":
        warning_text = font.render(warning, True, config.COLORS["warning"])
        screen.blit(warning_text, (config.SCREEN_WIDTH - warning_text.get_width() - 16, 14))


def draw_centered_lines(screen, lines, big_font, font):
    """Draw a stack of centered lines of text, used for the ending screen."""
    total_height = big_font.get_height() + font.get_height() * len(lines)
    top = config.SCREEN_HEIGHT // 2 - total_height // 2

    for index, line in enumerate(lines):
        chosen_font = big_font if index == 0 else font
        surface = chosen_font.render(line, True, config.COLORS["text"])
        screen.blit(
            surface,
            (config.SCREEN_WIDTH // 2 - surface.get_width() // 2, top),
        )
        top += chosen_font.get_height() + 8


# ---------------------------------------------------------------------------
# Reading the keyboard
# ---------------------------------------------------------------------------


def read_direction(pressed_keys):
    """Turn the currently held keys into a horizontal and vertical step.

    Each returned value is -1, 0, or 1.  Both WASD and the arrow keys work.
    """
    horizontal = 0
    vertical = 0

    if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
        horizontal -= 1
    if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
        horizontal += 1
    if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
        vertical -= 1
    if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
        vertical += 1

    return horizontal, vertical


# ---------------------------------------------------------------------------
# Keeping score
# ---------------------------------------------------------------------------


def add_points(state, points_earned):
    """Record newly collected fireflies in the state dictionary.

    The state dictionary is changed in place and also returned.
    """
    # DONE 10: The assignment used to replace the value stored under the
    # "score" key instead of adding to it, so the score never rose above 10.
    # It now reads the old value out of the dictionary first.
    state["score"] = state["score"] + points_earned

    fireflies_this_frame = points_earned // config.GAME_SETTINGS["firefly_points"]
    state["fireflies_collected"] = state["fireflies_collected"] + fireflies_this_frame

    return state


# ---------------------------------------------------------------------------
# One round of the game
# ---------------------------------------------------------------------------


def play_round(screen, clock, font, big_font, frame_limit=None):
    """Play a single round and return the final state dictionary.

    The frame_limit argument is only used by the automatic self test, which
    plays a few frames without a human at the keyboard.
    """
    player = entities.make_player()
    fireflies = entities.spawn_fireflies([])
    creatures = []

    # The state dictionary keeps track of everything the scoreboard shows.
    state = {
        "score": 0,
        "fireflies_collected": 0,
        "lives": player["lives"],
        "outcome": "",
    }

    elapsed_seconds = 0.0
    round_seconds = config.GAME_SETTINGS["round_seconds"]
    frames_played = 0
    running = True

    while running:
        # How much real time passed since the last frame, in seconds.
        seconds_this_frame = clock.tick(config.FRAMES_PER_SECOND) / 1000.0
        elapsed_seconds += seconds_this_frame
        seconds_left = round_seconds - elapsed_seconds
        milliseconds = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state["outcome"] = "quit"
                return state
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                state["outcome"] = "quit"
                return state

        # --- Move the player -------------------------------------------
        if frame_limit is None:
            horizontal, vertical = read_direction(pygame.key.get_pressed())
        else:
            # The self test steers toward a firefly instead of reading the
            # keyboard, so that the automatic checker exercises collecting
            # and scoring as well as drawing.
            target = fireflies[0]
            horizontal = 0
            vertical = 0
            if target["x"] > player["x"]:
                horizontal = 1
            elif target["x"] < player["x"]:
                horizontal = -1
            if target["y"] > player["y"]:
                vertical = 1
            elif target["y"] < player["y"]:
                vertical = -1
        entities.move_player(player, horizontal, vertical)

        # --- Collect any fireflies the player is standing on ------------
        fireflies, points_earned = entities.collect_fireflies(player, fireflies)

        add_points(state, points_earned)

        # Refill the forest so a firefly is always waiting somewhere.
        fireflies = entities.spawn_fireflies(fireflies)

        # --- Wake up and move the creatures -----------------------------
        creatures = entities.spawn_due_creatures(creatures, seconds_left)
        entities.move_creatures(creatures, player)

        # --- Did anything catch the player? -----------------------------
        if player["recovery"] > 0:
            player["recovery"] = max(0.0, player["recovery"] - seconds_this_frame)

        if entities.player_is_caught(player, creatures):
            player["lives"] -= 1
            state["lives"] = player["lives"]
            player["recovery"] = config.GAME_SETTINGS["recovery_seconds"]
            # Send the player back to the middle of the clearing.
            player["x"] = config.SCREEN_WIDTH // 2
            player["y"] = config.SCREEN_HEIGHT // 2

        # --- Is the round over? -----------------------------------------
        if state["lives"] <= 0:
            state["outcome"] = "caught"
            running = False
        elif seconds_left <= 0:
            state["outcome"] = "time_up"
            running = False

        # --- Draw everything, back to front -----------------------------
        draw_forest(screen)
        draw_darkness(screen, player)
        for firefly in fireflies:
            draw_firefly(screen, firefly, milliseconds)
        for creature in creatures:
            draw_creature(screen, creature, milliseconds)
        draw_player(screen, player, milliseconds)
        draw_hud(screen, font, state, max(0.0, seconds_left))
        pygame.display.flip()

        frames_played += 1
        if frame_limit is not None and frames_played >= frame_limit:
            state["outcome"] = "self_test"
            running = False

    return state


def show_ending(screen, clock, font, big_font, state):
    """Show the results and wait for the player to replay or quit.

    Returns True when the player wants another round.
    """
    if state["outcome"] == "caught":
        headline = config.MESSAGES["game_over"]
    else:
        headline = config.MESSAGES["time_up"]

    lines = [
        headline,
        "",
        "Fireflies collected: " + str(state["fireflies_collected"]),
        "Final score: " + str(state["score"]),
        "",
        config.MESSAGES["replay"],
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    return False

        screen.fill(config.COLORS["night_sky"])
        draw_centered_lines(screen, lines, big_font, font)
        pygame.display.flip()
        clock.tick(config.FRAMES_PER_SECOND)


# ---------------------------------------------------------------------------
# Starting the game
# ---------------------------------------------------------------------------


def main():
    """Set up Pygame, then play rounds until the player quits."""
    # The self test plays a few frames with nobody at the keyboard.  The
    # automatic checker uses it to prove that the game really runs.
    self_test = "--self-test" in sys.argv

    pygame.init()
    pygame.display.set_caption(config.MESSAGES["title"])
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("menlo,dejavusansmono,monospace", 18)
    big_font = pygame.font.SysFont("menlo,dejavusansmono,monospace", 34, bold=True)

    # font = pygame.font.SysFont(None, 18)
    # big_font = pygame.font.SysFont(None, 34, bold=True)

    print(config.MESSAGES["title"])
    print(config.MESSAGES["instructions"])

    playing = True
    while playing:
        state = play_round(
            screen, clock, font, big_font, frame_limit=90 if self_test else None
        )

        if state["outcome"] == "quit":
            playing = False
        elif self_test:
            print("Self test finished.  Score:", state["score"])
            playing = False
        else:
            playing = show_ending(screen, clock, font, big_font, state)

    pygame.quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
