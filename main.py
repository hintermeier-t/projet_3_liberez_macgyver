#-*coding: UTF-8-*
"""Module de test de class "graphiques" pour le terminal"""

import core as c
import graph as g
import pygame as pg

def main():
    game = c.game.Game()
    maze = g.maze.MazeSprite()
    player = g.player.McSprite(game.player.x, game.player.y)
    needle = g.item.ItemSprite("aiguille.png", game.needle.x, game.needle.y)
    tube = g.item.ItemSprite("tube_plastique.png", game.tube.x, game.tube.y)
    ether = g.item.ItemSprite("ether.png", game.ether.x, game.ether.y)
    ennemy = g.guard.GuardSprite(game.ennemy.x, game.ennemy.y)
    g.gdisplay.display_screen(game, maze, player, needle, tube, ether, ennemy)

main()