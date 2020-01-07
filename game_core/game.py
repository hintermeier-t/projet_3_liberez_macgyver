#-*coding: UTF-8-*
#!/usr/bin/python3.8

"""Module containing the Game class"""

import os
import random
from .board import GamingBoard
from .hero import McGyver
from .items import UseableItem
from .guard import EnnemyGuard

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
            choice=input("Choisissez votre niveau :\n")

        #Generating the maze with the chosen file, will be called with game.maze
        self.maze = GamingBoard(os.path.join("maps", maps_list[int(choice)-1]+".txt"))
        self.player = McGyver(self.maze.start)
        self.ennemy = EnnemyGuard(self.maze.exit)

        #generating the 3 items position
        tmp_list = random.sample(self.maze.path, 3)
        self.needle = UseableItem("needle",tmp_list[0])
        self.tube = UseableItem("tube",tmp_list[1])
        self.ether = UseableItem("ether",tmp_list[2])

    def win_or_lose(self):
        """Every move, Game verify if the player is on the guard, if so,
        does he have the items to knock him out ?"""

        if player.position == ennemy.position:
            if needle.is_collected and tube.is_collected and ether.is_collected:
                return "Bravo, Mac ! Vous vous êtes enfui, et sans un trombonne !"
            else :
                return "Oh non ! Le garde vous a attrapé ! Perdu !"

    def collect (item): #shouldn't it be in McGyver or UseableItem class ?
        """Every move, Game verify if the player can collect and item"""

        if player.position == item.position:
            item.switch()
