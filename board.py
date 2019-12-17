class GamingBoard:
    """Class defining the board wich will be used to play.
    It is defined by 2D list with x and y coordinates, each one related to a
    letter that will be used to design the structure as follow :
    -'S' is the Start
    -'W' is a Wall
    -'X' is the Exit
    -'C' is a free space"""

    def __init__(self):
        self.board=[]

        with open ('lab.txt','r') as lab_file:
            temp=" "
            while temp != "":
                temp=lab_file.readline().rstrip("\n") #We catch the first line in a string, and remove the \n char.
                self.board.append(temp.split(" "))

    def affiche (self):
        for elt in self.board:
            print (elt)
