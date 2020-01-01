#-*coding: UTF-8-*
#!/usr/bin/python3.8

class UseableItem:
    """Class defining an item, wich will be used by the player, identified by:
    -its name
    -its location (on an empty space)
    -wherever it is collected or not"""

    def __init__(self, name_string,item_loc):
        """Initializing the item with its name (Needle, Tube, Ether), the loc will
        be defined randomly, and the collected state is False at the begining."""
        self.name = name_string
        self.loc = item_loc
        self.col_state = False

    def what_is(self):#Forget it
        print(self.name,self.loc,self.col_state)
