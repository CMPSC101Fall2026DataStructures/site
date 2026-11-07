"""Application entry point for the Space Invaders game."""

from .game import Game


def main() -> None:
    """Create the game and start its event loop."""
    Game().run()


if __name__ == "__main__":
    main()
