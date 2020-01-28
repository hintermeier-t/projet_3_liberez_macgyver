#-*coding: UTF-8-*
#!/usr/bin/python3.6

"""Module containing the Game class"""

import os
import random
from . import board
from . import hero
from . import items
from . import guard

class Game:
    """Game is the main class, used to generate the objects (the 3 items,
    the player, the maze, and the guard), and manage the game options
    (Load or save a game, start a new one etc...)"""

    def __init__(self):
        """Class constructor, no parameter needed. Initialise the game, the
        maze, the player, the ennemy and the needed items in order to win."""

        maps_list = []
        choice = 0
        self.win = False
        self.lose = False

        for file_name in os.listdir("maps"):
            if file_name.endswith(".txt"):
                maps_list.append(file_name[:-4].lower())

        for i, map in enumerate(maps_list):
            #Displaying the files in maps directory
            print("{} : {}".format(i + 1, map))

        while int(choice) <= 0 or int(choice) > len(maps_list):
            choice=input("Chose your level :\n")

        #Generating the maze with the chosen file, will be called with game.maze
        self.maze = board.GamingBoard(os.path.join("maps", maps_list[int(choice)-1]+".txt"))
        self.player = hero.McGyver(self.maze.start)
        self.ennemy = guard.EnnemyGuard(self.maze.exit)

        #generating the 3 items position
        tmp_list = random.sample(self.maze.path-{self.player.position,self.ennemy.position}, 3)
        self.needle = items.UseableItem("needle",tmp_list[0])
        self.tube = items.UseableItem("tube",tmp_list[1])
        self.ether = items.UseableItem("ether",tmp_list[2])

    def win_or_lose(self):
        """Every move, Game verify if the player is on the guard, if so,
        does he have the items to knock him out ?"""

        if self.player.position == self.ennemy.position:
            if self.needle.is_collected and self.tube.is_collected and self.ether.is_collected:
                return True
            else :
                return False
        return None

    def collect (self,item:items.UseableItem):
        """Every move, Game verify if the player can collect and item"""

        if self.player.position == item.position:
            item.switch()
        return item.is_collected