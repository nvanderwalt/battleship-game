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

    def print(self):
        for row in self.board: #This is a for loop that iterates over each row in the board.
            print(" ".join(row)) #To print this string to the console, effectively printing the row with spaces between the cells for better readability.

    #Function to generate random points on the board with the parameters
    def random_point(size):
        return randint(0, size-1), randint(0, size-1) 

    def valid_coordinates(x, y, board):
        return 0 <= x < board.size and 0 <= y < board.size


    #Populate_board function is responsible for placing a specified number of ships (board.num_ships) randomly on the game board (board.board) without overlapping.
    def populate_board(board):
        for _ in range(board.num_ships):
        while True:
            x, y = Board.random_point(board.size)
            if board.board[x][y] == ".":
                board.board[x][y] = "S"
                board.ships.append((x, y))
                break

    #Processes a guess on the board at coordinates (x, y).
    def make_guess(board, x, y):
    if not Board.valid_coordinates(x, y, board):
        return "Invalid coordinates. Try again."
    if (x, y) in board.guesses:
        return "You already guessed that. Try again."
    board.guesses.append((x, y))
    if board.board[x][y] == "S":
        board.board[x][y] = "X"
        return "Hit!"
    else:
        board.board[x][y] = "O"
        return "Miss!"