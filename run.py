from random import randint

#Score tracking 
scores = {"computer": 0, "player": 0} 


#The __init__ method sets up a new game board with the specified size, number of ships and initializes it with empty guesses and ship placements. 
class Board:
    def __init__(self, size, num_ships, name, type): 
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []