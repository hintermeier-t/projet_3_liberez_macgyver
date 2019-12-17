#-*coding: UTF-8-*
class McGyver :
    """Class representing the player, with a position on the map, and the items
    he posess, and the action he can do like moving, catching and item or
    knocking the guard"""
    def __init__(self, position_initiale):
        """Initializing the Hero at the start_place of the map.
        We get the tuple containing the starting coordinates and change
        them into a list of coordinates we can work on"""
        self.position=[]
        for coordinate in position_initiale:
            self.position.append(coordinate)

    def where_is (self):
        print(self.position)
