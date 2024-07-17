from random import randint

#Score tracking 
scores = {"computer": 0, "player": 0} 


#The __init__ method sets up a new game board with the specified size, number of ships and initializes it with empty guesses and ship placements.
# IMPORTANT - Code was taken from the video of Code Institute-Project 3
class Board:
    def __init__(self, size, num_ships, name, type): 
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

#This defines a method named print that belongs to the Board class.
    def print(self):
        for row in self.board: #This is a for loop that iterates over each row in the board.
            print(" ".join(row)) #To print this string to the console, effectively printing the row with spaces between the cells for better readability.