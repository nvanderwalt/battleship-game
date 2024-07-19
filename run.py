from random import randint

# Dictionary to keep track of scores
scores = {"computer": 0}

#Initializes the board with given size, number of ships, name, and type (computer or player).
class Board:
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)]
                      for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    #Prints the board. For the computer's board, ships are hidden.
    def print(self):
        if self.type == "computer":
            for row in self.board:
                print(" ".join(["." if cell == "S" else cell
                                for cell in row]))
        else:
            for row in self.board:
                print(" ".join(row))

    #Generates a random point within the board.
    def random_point(size):
        return randint(0, size-1), randint(0, size-1)

    def valid_coordinates(x, y, board):
        return 0 <= x < board.size and 0 <= y < board.size

    def populate_board(board):
        for _ in range(board.num_ships):
            while True:
                x, y = Board.random_point(board.size)
                if board.board[x][y] == ".":
                    board.board[x][y] = "S"
                    board.ships.append((x, y))
                    break
        
    #Processes a guess on the board at coordinates (x, y).
    #Returns a message indicating if it was a hit, miss, or an invalid guess.
    def make_guess(board, x, y):
        if not Board.valid_coordinates(x, y, board):
            return "Invalid coordinates."
        if (x, y) in board.guesses:
            return "You already guessed that captain."
        board.guesses.append((x, y))
        if board.board[x][y] == "S":
            board.board[x][y] = "X"
            return "HIT!!"
        else:
            board.board[x][y] = "O"
            return "Miss!"

#Main game loop where the player and computer take turns to guess the location of ships.
def play_game(computer_board, player_board):
    global scores

    computer_guesses = []
    last_player_guess = None

    while True:
        print(f"\n{player_name}'s Board:")
        player_board.print()
        print(f"\n{computer_board.name}'s Board:")
        computer_board.print()

        while True:
            try:
                x, y = map(int, input("Enter your guess (row and column "
                                      "separated by space): ").split())
                # Check if coordinates are valid                      
                if not Board.valid_coordinates(x, y, computer_board):
                    print("Invalid coordinates. Try again.")
                    continue

                if last_player_guess == (x, y):
                    print("You already guessed that.")
                    continue

                result = Board.make_guess(computer_board, x, y)
                if "already guessed" not in result:
                    last_player_guess = (x, y)
                    break
                print(result)
            except ValueError:
                print("Invalid input. Please enter row and column numbers.")

        print(f"\nYou guessed ({x}, {y}) and it was a {result}")

        # Check if all ships on the computer's board have been sunk
        if all(computer_board.board[x][y] != "S"
               for x, y in computer_board.ships):
            print("\nHoooray! You sank all the ships! You win!\n")
            scores["player"] += 1
            break
        
        # Computer's turn
        while True:
            x, y = Board.random_point(player_board.size)
            if (x, y) not in computer_guesses:
                computer_guesses.append((x, y))
                break

        result = Board.make_guess(player_board, x, y)
        print(f"Computer guessed ({x}, {y}) and it was a {result}")

        # Check if all ships on the player's board have been sunk
        if all(player_board.board[x][y] != "S"
               for x, y in player_board.ships):
            print("\nCaptain you have no more ships! You lose!\n")
            scores["computer"] += 1
            break

# Sets up a new game by initializing the boards for the player and the computer.
def new_game():
    global player_name
    
    while True:
        try:
            size = int(input("Please enter the size of the board (e.g., 5 "
                             "for a 5x5 board): "))
            if size < 2:
                print("Board size must be at least 2.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            num_ships = int(input("Enter the number of ships: "))
            max_ships = size * size // 4
            if num_ships < 1 or num_ships > max_ships:
                print(f"Number of ships must be between 1 and {max_ships}.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Initialize boards for player and computer  
    computer_board = Board(size, num_ships, "Computer", "computer")
    player_board = Board(size, num_ships, player_name, "player")

    # Populate boards with ships
    Board.populate_board(computer_board)
    Board.populate_board(player_board)

    play_game(computer_board, player_board)

# Main loop to start and manage the game, including handling multiple game sessions and resetting scores.
def main():
    global player_name  # To declare that player_name is global
    global scores

    # Ask for player's name once at the beginning
    if "player_name" not in globals():
        player_name = input("Please enter your name: ")
        scores[player_name] = 0  # Initialize the player's score

    while True:
        new_game()
        print(f"Scores:\n{player_name}: {scores[player_name]}\nComputer: {scores['computer']}")

        while True:
            another_game = input("Do you want to play another game? (yes/no): "
                                 "").lower()
            if another_game in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if another_game == "yes":
            while True:
                reset_scores = input("Reset scores? (yes/no): ").lower()

                if reset_scores in ["yes", "no"]:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            if reset_scores == "yes":
                scores["computer"] = 0
                scores[player_name] = 0
                print(f"Scores have been reset, {player_name}.")
                player_name = input("Please enter your new name: ")  # Ask for a new name only if scores are reset
                if player_name not in scores:
                    scores[player_name] = 0  # Initialize the player's score if new name
        else:
            print("Thank you for playing captain! Have a nice day!")
            break

print("Welcome to Battleships Captain! Load the canons and set the sails! \n"
      "Please note that rows and columns start from 0\n")
main()