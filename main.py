#-*coding: UTF-8-*
"""Module de test de class "graphiques" pour le terminal"""

import core as c
import graph as g

def main():
    play = c.game.Game()
    print (play.player.position)
    player_position = c.position.Position(play.player.position)
    print (player_position.x)

main()