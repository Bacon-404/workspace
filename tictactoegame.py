
turn = 0

# Build a map data structure to create a game of tic tac toe in terminal
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def handle_turn():
    global turn

    if turn % 2 == 0:
        player = "X"
    else:
        player = "O"

    position = input(f"Player {player}, please choose a position from 1-9: ")
    position = int(position) - 1

    print(f"Player {player}'s turn")
    print(f"### Turn {turn} ###")
    print("####################")

    board[position] = player
    display_board()
    print("####################")
    turn += 1

def check_win():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != "-":
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != "-":
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] != "-":
        return True
    if board[2] == board[4] == board[6] != "-":
        return True

    return False

    

def main():
    # Create a game loop
    print("Welcome to Tic Tac Toe!")
    print("The game will begin shortly...")
    display_board()
    print("Postions are as follows: ")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")
    print("####################")
    print("Player 1 will be X and Player 2 will be O")

    #main gameloop
    while turn < 8:
        handle_turn()
        if check_win():
            print("Game Over!")
            print(f"Player {board[turn-1]} wins!")
            



if __name__ == "__main__":
    main()    
