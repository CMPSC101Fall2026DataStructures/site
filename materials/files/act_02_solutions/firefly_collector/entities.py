"""The things that live in the forest: the player, fireflies, and creatures.

Every single thing in this game is stored as a **dictionary**, and every group
of things is stored as a **list**.  A firefly, for example, is just this:

    {"x": 412, "y": 88, "radius": 4, "flicker": 1.9}

and all of the fireflies together are just a list of those dictionaries:

    [{"x": 412, ...}, {"x": 120, ...}, {"x": 733, ...}]

There is no Pygame code in this file at all -- only lists, dictionaries, and
arithmetic.  That is what makes it easy to test.

Bugs fixed in this file: numbers 6, 7, 8, and 9.
"""

import math
import random

from firefly_collector import config


# ---------------------------------------------------------------------------
# The player
# ---------------------------------------------------------------------------


def make_player():
    """Build and return the player dictionary, centered on the screen."""
    return {
        "x": config.SCREEN_WIDTH // 2,
        "y": config.SCREEN_HEIGHT // 2,
        "radius": config.GAME_SETTINGS["player_radius"],
        "lives": config.GAME_SETTINGS["starting_lives"],
        # Seconds of safety left after being caught.  Zero means "not safe".
        "recovery": 0.0,
    }


def clamp(value, lowest, highest):
    """Keep a number inside a range, so the player cannot walk off screen."""
    if value < lowest:
        return lowest
    if value > highest:
        return highest
    return value


def move_player(player, horizontal, vertical):
    """Move the player by one step and keep it inside the forest.

    The horizontal and vertical arguments are -1, 0, or 1, and they come from
    whichever keys are being held down.
    """
    speed = config.GAME_SETTINGS["player_speed"]
    radius = player["radius"]

    # Update the two position values that are stored in the dictionary.
    player["x"] = clamp(
        player["x"] + horizontal * speed, radius, config.SCREEN_WIDTH - radius
    )
    player["y"] = clamp(
        player["y"] + vertical * speed, radius, config.SCREEN_HEIGHT - radius
    )
    return player


# ---------------------------------------------------------------------------
# Fireflies
# ---------------------------------------------------------------------------


def make_firefly():
    """Build and return one firefly dictionary at a random spot on screen."""
    edge = 30  # keep fireflies away from the very edge of the window
    # DONE 6: The keys were named "pos_x" and "pos_y", but every other part of
    # the game looks up "x" and "y".  The names now match the player's keys.
    return {
        "x": random.randint(edge, config.SCREEN_WIDTH - edge),
        "y": random.randint(edge, config.SCREEN_HEIGHT - edge),
        "radius": config.GAME_SETTINGS["firefly_radius"],
        # A random starting point in the flicker cycle, so that the fireflies
        # do not all pulse in unison.
        "flicker": random.uniform(0.0, 2.0 * math.pi),
    }


def spawn_fireflies(fireflies):
    """Add new fireflies to the list until the forest is full again.

    The list is changed in place and also returned, which is a common and
    convenient Python pattern.
    """
    wanted = config.GAME_SETTINGS["max_fireflies"]

    # DONE 9: The loop used <=, which let it add one firefly too many.  With <
    # it stops as soon as the list holds exactly "wanted" fireflies.
    while len(fireflies) < wanted:
        new_firefly = make_firefly()
        # DONE 7: The square brackets wrapped each firefly in a one-item list
        # before appending it.  .append() already adds a single item, so the
        # dictionary is now appended on its own.
        fireflies.append(new_firefly)

    return fireflies


def distance(first, second):
    """Return the straight-line distance between two entity dictionaries."""
    side_a = first["x"] - second["x"]
    side_b = first["y"] - second["y"]
    return math.sqrt(side_a * side_a + side_b * side_b)


def is_touching(first, second):
    """Return True when two circles overlap each other."""
    return distance(first, second) < first["radius"] + second["radius"]


def collect_fireflies(player, fireflies):
    """Collect every firefly the player is touching.

    Returns a tuple of two things: the list of fireflies that are still
    glowing, and the number of points the player just earned.
    """
    points_earned = 0

    # DONE 8: The loop used to call fireflies.remove() on the same list it was
    # looping over, which made Python skip the item that slid into the freed
    # slot.  Building a separate "remaining" list leaves the original list
    # untouched while the loop runs.
    remaining = []

    for firefly in fireflies:
        if is_touching(player, firefly):
            points_earned += config.GAME_SETTINGS["firefly_points"]
        else:
            remaining.append(firefly)

    return remaining, points_earned


# ---------------------------------------------------------------------------
# Nocturnal creatures
# ---------------------------------------------------------------------------


def make_creature(kind):
    """Build and return one creature dictionary of the given kind.

    The kind is a string, either "owl" or "shadow".  Notice how the kind is
    used to look up that creature's speed in the settings dictionary.
    """
    # Creatures walk in from a random edge, never on top of the player.
    corners = [
        (20, 20),
        (config.SCREEN_WIDTH - 20, 20),
        (20, config.SCREEN_HEIGHT - 20),
        (config.SCREEN_WIDTH - 20, config.SCREEN_HEIGHT - 20),
    ]
    # The owl swoops in from above and the shadow seeps in from below, so
    # that the two creatures never appear on top of one another.
    if kind == "owl":
        start_x, start_y = random.choice(corners[:2])
    else:
        start_x, start_y = random.choice(corners[2:])

    return {
        "kind": kind,
        "x": start_x,
        "y": start_y,
        "radius": 16,
        # Build the settings key by joining the kind onto "_speed", so that
        # "owl" becomes "owl_speed" and "shadow" becomes "shadow_speed".
        "speed": config.GAME_SETTINGS[kind + "_speed"],
    }


def spawn_due_creatures(creatures, seconds_left):
    """Wake up any creature whose time has come.

    The creatures list is changed in place and returned.
    """
    # Build a list of the kinds already prowling around, so that no creature
    # is added twice.
    kinds_on_screen = [creature["kind"] for creature in creatures]

    if seconds_left <= config.GAME_SETTINGS["owl_appears_at"]:
        if "owl" not in kinds_on_screen:
            creatures.append(make_creature("owl"))

    if seconds_left <= config.GAME_SETTINGS["shadow_appears_at"]:
        if "shadow" not in kinds_on_screen:
            creatures.append(make_creature("shadow"))

    return creatures


def move_creatures(creatures, player):
    """Step every creature a little closer to the player."""
    for creature in creatures:
        gap = distance(creature, player)
        if gap == 0:
            continue

        # Move along the line that points from the creature to the player.
        step_x = (player["x"] - creature["x"]) / gap
        step_y = (player["y"] - creature["y"]) / gap

        creature["x"] += step_x * creature["speed"]
        creature["y"] += step_y * creature["speed"]

    return creatures


def player_is_caught(player, creatures):
    """Return True when any creature is touching the player."""
    if player["recovery"] > 0:
        return False

    for creature in creatures:
        if is_touching(player, creature):
            return True

    return False
