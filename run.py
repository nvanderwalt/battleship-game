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


#Main game loop that controls the flow of the game between the player and the computer. While loop allows each player to make guesses until the game is over.
def play_game(computer_board, player_board):
    while True:
        print(f"\n{player_board.name}'s Board:")
        player_board.print()
        print(f"\n{computer_board.name}'s Board:")
        computer_board.print()

        try:
            x, y = map(int, input("Enter your guess (row and column separated by space): ").split())
            result = Board.make_guess(computer_board, x, y)
            print(result)

            #Check if all ships on the computer's board have been sunk
            if all(computer_board.board[x][y] != "S" for x, y in computer_board.ships):
                print("You sank all the ships! You win!")
                scores["player"] += 1
                break

            #Computer makes a random guess
            x, y = Board.random_point(player_board.size)
            result = Board.make_guess(player_board, x, y)
            print(f"Computer guessed ({x}, {y}) and it was a {result}")

            #Check if all ships on the player's board have been sunk
            if all(player_board.board[x][y] != "S" for x, y in player_board.ships):
                print("Computer sank all your ships! You lose!")
                scores["computer"] += 1
                break
            
        except ValueError:
            print("Invalid input. Please enter row and column numbers separated by space.")

