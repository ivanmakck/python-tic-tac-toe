def display_board(board):
    print(f"""
     {board[6]} | {board[7]} | {board[8]} 
    -----------
     {board[3]} | {board[4]} | {board[5]} 
    -----------
     {board[0]} | {board[1]} | {board[2]} 
    """)


def player_turn(player_marker, board, selected):
    while True:
        selection = int(input("Select a number between 1-9: "))
        if selection in range(1,10) and selection not in selected:
            selected.append(selection)
            board[selection-1] = player_marker
            display_board(board)
            break


def check_win(board):
    return board[0] == board[1] == board[2] != ' ' or \
        board[3] == board[4] == board[5] != ' ' or \
        board[6] == board[7] == board[8] != ' ' or \
        board[0] == board[3] == board[6] != ' ' or \
        board[1] == board[4] == board[7] != ' ' or \
        board[2] == board[5] == board[8] != ' ' or \
        board[0] == board[4] == board[8] != ' ' or \
        board[2] == board[4] == board[6] != ' '


def play_game():
    while True:
        p1_marker = input("Player 1, please choose your marker (O or X): ").upper()
        if p1_marker in ("O", "X"):
            p2_marker = "X" if p1_marker == "O" else "O"
            break

    board = [' '] * 9
    display_board(board)

    selected = []
    is_game_over = False
    while not is_game_over:
        print(f"Player 1's ({p1_marker}) turn. ")
        player_turn(p1_marker, board, selected)
        is_game_over = check_win(board)

        if is_game_over:
            print("Player 1 wins!")
        elif ' ' not in board:
            print("No one wins!")
            is_game_over = True
        else:
            print(f"Player 2's ({p2_marker}) turn.")
            player_turn(p2_marker, board, selected)
            is_game_over = check_win(board)

            if is_game_over:
                print("Player 2 wins!")
        
    replay()


def replay():
    while True:
        replay = input("Do you want to play again? (Y/N): ").upper()
        if replay == 'Y':
            play_game()
            break
        elif replay == 'N':
            break


if __name__=="__main__":

    print("""
      _______ _        _______           _______         
     |__   __(_)      |__   __|         |__   __|        
        | |   _  ___     | | __ _  ___     | | ___   ___ 
        | |  | |/ __|    | |/ _` |/ __|    | |/ _ \ / _ \\
        | |  | | (__     | | (_| | (__     | | (_) |  __/
        |_|  |_|\___|    |_|\__,_|\___|    |_|\___/ \___|

    Welcome! This is a python implementation of Tic Tac Toe played in the terminal.

    The board is represented below, with the numbers corresponding to the location
    of the board.

    7 | 8 | 9 
    -----------
    4 | 5 | 6 
    -----------
    1 | 2 | 3 

    The game will proceed to ask for your number input, and will place your marker
    (X or O) in the corresponding location in the board.

    Enjoy!
    """)

    play_game()