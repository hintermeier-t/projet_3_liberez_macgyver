# -*coding: UTF-8-*
"""Main module of the game."""

import core as c
import graph as g


def main():
    """Main function of the game.

    Runs eveyrthind, initialize the sprites and the game.
    """
    game = c.game.Game()
    interface = g.interface.Interface(game)
    interface.run_game(game)


main()
