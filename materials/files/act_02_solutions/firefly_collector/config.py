"""Settings for the Firefly Collector game.

This module holds every number, color, and name that the game needs.  Keeping
these values in one place is a common Python habit: when you want the round to
last longer or the fireflies to glow brighter, you change one literal here
instead of hunting through the whole program.

Three kinds of value appear in this file:

* literals   -- fixed values you type directly, such as 900 or "owl"
* lists      -- ordered collections written with square brackets [ ]
* dictionaries -- name-to-value lookups written with curly braces { }

Bugs fixed in this file: numbers 1, 2, 3, 4, and 5.
"""

# ---------------------------------------------------------------------------
# Window size
# ---------------------------------------------------------------------------
# Pygame builds the game window out of two whole numbers: a width and a
# height, both measured in pixels.

# DONE 1: The width was written as the string literal "900".  Removing the
# quotation marks turns it back into the integer literal Pygame needs.
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

# How many times per second the game redraws itself.  Sixty is smooth.
FRAMES_PER_SECOND = 60

# ---------------------------------------------------------------------------
# Colors
# ---------------------------------------------------------------------------
# COLORS is a dictionary.  Each key is a short name written as a string, and
# each value is a tuple of three integers: (red, green, blue).  Every number
# runs from 0 (none of that light) to 255 (as much as possible).
#
# Look up a color by its key, like this:
#
#     screen.fill(COLORS["night_sky"])

COLORS = {
    "night_sky": (12, 16, 34),
    "player": (90, 200, 255),
    "lantern": (255, 240, 180),
    # DONE 2: The key was spelled "fire_fly", so every COLORS["firefly"] lookup
    # raised a KeyError.  Dictionary keys must match character for character.
    "firefly": (255, 255, 120),
    # DONE 3: The tuple literal held only two numbers.  A color needs all
    # three components -- red, green, and blue -- so the blue value was added.
    "tree": (18, 60, 38),
    "owl": (196, 168, 120),
    "shadow": (120, 70, 190),
    "text": (235, 235, 245),
    "warning": (255, 120, 120),
}

# ---------------------------------------------------------------------------
# Gameplay settings
# ---------------------------------------------------------------------------
# GAME_SETTINGS is a dictionary of tuning knobs.  Every value here is a
# number, because the game does arithmetic with all of them.

GAME_SETTINGS = {
    # DONE 4: The value was the string literal "60", which cannot be used in
    # arithmetic.  It is now the integer literal 60.
    "round_seconds": 60,
    # How many pixels the player moves each frame.
    "player_speed": 4,
    # How big the player circle is, measured from its center outward.
    "player_radius": 14,
    # How far the player's lantern light reaches.
    "lantern_radius": 95,
    # How big each firefly is.
    "firefly_radius": 4,
    # How many points a single firefly is worth.
    "firefly_points": 10,
    # How many fireflies glow on screen at the same time.
    "max_fireflies": 8,
    # How many times the player can be caught before the round ends.
    "starting_lives": 3,
    # Seconds remaining when the owl wakes up and starts hunting.
    "owl_appears_at": 30,
    # Seconds remaining when the slow shadow creature appears.
    "shadow_appears_at": 15,
    # How fast each creature drifts toward the player each frame.
    "owl_speed": 2,
    "shadow_speed": 1,
    # How long the player is safe after being caught, in seconds.
    "recovery_seconds": 2,
}

# ---------------------------------------------------------------------------
# The forest
# ---------------------------------------------------------------------------
# TREE_POSITIONS is a list of tuples.  Each tuple describes one tree as four
# integers: (left, top, width, height).  Pygame needs all four numbers to draw
# a rectangle, and the game also uses them to keep the player out of the
# trunks.
#
# DONE 5: One tuple in the list held only three numbers, so the game could
# not tell how tall that tree was.  Every tuple now has all four values.

TREE_POSITIONS = [
    (60, 70, 40, 130),
    (180, 300, 36, 110),
    (95, 470, 44, 100),
    (330, 120, 38, 120),
    (430, 430, 42, 125),
    (600, 90, 40, 115),
    (700, 330, 44, 120),
    (820, 480, 38, 105),
    (250, 200, 30, 80),
    (760, 160, 34, 95),
]

# ---------------------------------------------------------------------------
# Messages
# ---------------------------------------------------------------------------
# A small dictionary of the words the game shows on screen.  Storing text in
# one place makes it easy to reword the game later.

MESSAGES = {
    "title": "Firefly Collector",
    "instructions": "Move with WASD or the arrow keys.  Collect the fireflies!",
    "owl_warning": "An owl is awake in the forest...",
    "shadow_warning": "Something in the shadows is following you...",
    "caught": "Caught!",
    "time_up": "Time's up!",
    "game_over": "The forest goes quiet.",
    "replay": "Press R to play again, or Q to quit.",
}
