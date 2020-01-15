#-*coding: UTF-8-*
#!/usr/bin/python3.6

import os, sys

import graph as g
import core as c


partie = c.game.Game()
print(partie.player.position)
partie.player.move_down(partie.maze.path)
print(partie.player.position)
g.gdisplay.display_screen()

