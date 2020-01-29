# -*coding: UTF-8-*

"""Module containing the Game class."""

import os
import random
from . import board
from . import hero
from . import items
from . import guard


class Game:
    """Game is the main core class which manage everything.

    It is used to generate every objects the game (the 3 items, the player,
    the ennemy and the maze), and manage the game state.

    Attributes:
        maze (board.GamingBoard): maze of the game, chosen in a list
        player (hero.McGyver): McGyver will move in the maze
        ennemy (guard.EnnemyGuard): The ennemy to knock out
        needle (items.UseableItems): One of the three items to collect
        tube (items.UseableItems): One of the three items to collect
        ether (items.UseableItems): One of the three items to collect
    """

    def __init__(self):
        """Initialise the game.

        Initialize every object needed in order to make the program
        work. First, the player chose the maze from a list created by
        reading the "maps" folder.
        """

        maps_list = []
        choice = 0
        for file_name in os.listdir("maps"):
            if file_name.endswith(".txt"):
                maps_list.append(file_name[:-4].lower())

        for i, map in enumerate(maps_list):
            #  Displaying the files in "maps" directory in order to chose
            print("{} : {}".format(i + 1, map))

        while int(choice) <= 0 or int(choice) > len(maps_list):
            choice = input("Chose your level :\n")

        #  Generate the maze with the chosen file"
        self.maze = board.GamingBoard(os.path.join(
            "maps", maps_list[int(choice)-1]+".txt"))
        self.player = hero.McGyver(self.maze.start)
        self.ennemy = guard.EnnemyGuard(self.maze.exit)

        #  Generate the 3 items position
        tmp_list = random.sample(
            self.maze.path-{self.player.position, self.ennemy.position}, 3)
        self.needle = items.UseableItem(tmp_list[0])
        self.tube = items.UseableItem(tmp_list[1])
        self.ether = items.UseableItem(tmp_list[2])

    def win_or_lose(self):
        """Verify if the player win or lose the game.

        When the player is on the guard, verify if the 3 items are collected
        to knock out the guard.

        Returns:
            True if the player has collected the needle, the tube and the
            ether AND he's on the guard.
            False if at least one item is missing.
            None if the player isn't on the guard.
        """

        if self.player.position == self.ennemy.position:
            if self.needle.is_collected \
                    and self.tube.is_collected \
                    and self.ether.is_collected:
                return True
            else:
                return False
        return None

    def collect(self, item: items.UseableItem):
        """Game verify if the player can collect and item.

        When the player arrives on an item, switch the "is_collected" to True.

        Args:
            item (item.UseableItems): the item to collect.

        Returns :
            is_collected attribute from the item instance.
        """

        if self.player.position == item.position:
            item.switch()
        return item.is_collected
