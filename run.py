import random

# Score tracking for player and computer
scores = {"computer": 0, "player": 0} 


# The __init__ method sets up a new game board with the specified size, number of ships and initializes it with empty guesses and ship placements.
# IMPORTANT - Code was taken from the video of Code Institute-Project 3
class Board:
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for _ in range(self.size)] for _ in range(self.size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        if self.type == "computer":
            for row in self.board: # This is a for loop that iterates over each row in the board.
                print(" ".join(["." if cell == "S" else cell for cell in row])) # This is to hide the computer's boat from the player.
        else:
            for row in self.board:
                print(" ".join(row)) # To print this string to the console, effectively printing the row with spaces between the cells for better readability.

    # Function to generate random points on the board with the parameters
    def random_point(self):
        return randint(0, size-1), randint(0, self.size-1) 

    def valid_coordinates(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    # Populate_board function is responsible for placing a specified number of ships (board.num_ships) randomly on the game board (board.board) without overlapping.
    def populate_board(self):
        for _ in range(self.num_ships):
            while True:
                x, y = self.random_point()
                if self.board[x][y] == ".":
                    self.board[x][y] = "S"
                    self.ships.append((x, y))
                    break

    # Processes a guess on the board at coordinates (x, y).
    def make_guess(self, x, y):
        if not self.valid_coordinates(x, y):
            return "Arrrrggg. Invalid coordinates. Please try again."
        if (x, y) in self.guesses:
            return "You already guessed that captain.\nPlease try again."
        self.guesses.append((x, y))
        if self.board[x][y] == "S":
            self.board[x][y] = "X" # To indicate hit on the board
            return "HIT!!"
        else:
            self.board[x][y] = "O" # To indicate a miss on the board
            return "Miss!"


# Main game loop that controls the flow of the game between the player and the computer. While loop allows each player to make guesses until the game is over.
def play_game(computer_board, player_board):
    computer_guesses = [] # to track the computer's guesses
    last_player_guess = None

    while True:
        print(f"\n{player_board.name}'s Board:")
        player_board.print()
        print(f"\n{computer_board.name}'s Board:")
        computer_board.print()

        while True:
            try:
                x, y = map(int, input("Enter your guess (row and column separated by space): ").split())
                if last_player_guess == (x, y):
                    print("You already guessed that. Please try again.")
                    continue

                result = player_board.make_guess(x, y)
                if "already guessed" not in result:
                    last_player_guess = (x, y)
                    break
                print(result)
            except ValueError:
                print("Invalid input. Please enter row and column numbers separated by space.")

        print(f"\nYou guessed ({x}, {y}) and it was a {result}")

        if all(computer_board.board[x][y] != "S" for x, y in computer_board.ships):
            print("\nHoooray! You sank all the ships! You win!\n")
            scores["player"] += 1
            break

            # Computer makes a unique random guess
        while True:
            x, y = computer_board.random_point()
            if (x, y) not in computer_guesses:
                computer_guesses.append((x, y))
                break
            
        result = computer_board.make_guess(x, y)
        print(f"Computer guessed ({x}, {y}) and it was a {result}")

        if all(player_board.board[x][y] != "S" for x, y in player_board.ships):
            print("\nCaptain you have no more ships! You lose!\n")
            scores["computer"] += 1
            break

def new_game():

    # Prompt the player to choose the size of the board
    while True:
        try:
            size = int(input("Please enter the size of the board (e.g., 5 for a 5x5 board): "))
            if size < 2:
                print("Board size must be at least 2. Please enter a valid size.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

     # Prompt the player to choose the number of ships
    while True:
        try:
            num_ships = int(input("Enter the number of ships: "))
            if num_ships < 1 or num_ships > size * size // 4:
                print(f"Number of ships must be between 1 and {size * size // 4}. Please enter a valid number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Create boards with user-chosen size and number of ships
    computer_board = Board(size, num_ships, "Computer", "computer")
    player_board = Board(size, num_ships, "Player", "player")

    # Populate boards with ships
    computer_board.populate_board()
    player_board.populate_board()

    # Start the game with the created boards
    play_game(computer_board, player_board)

def main():
    while True:
        new_game()
        print(f"Scores:\nPlayer: {scores['player']}\nComputer: {scores['computer']}")

        while True:
            another_game = input("Do you want to play another game? (yes/no): ").lower()
            if another_game in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if another_game == "yes":
            while True:
                reset_scores = input("Do you want to reset the scores? (yes/no): ").lower()
                if reset_scores in ["yes", "no"]:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            if reset_scores == "yes":
                scores["computer"] = 0
                scores["player"] = 0
                print("Scores have been reset.")
        else:
            print("Thank you for playing captain! Have a nice day!")
            break

print("Welcome to Battleships Captain! Load the canons and set the sails! \nPlease note that rows and columns start from 0\n")
main()
