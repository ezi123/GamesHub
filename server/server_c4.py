def check_win(board):
    print("IN Checkwin")
    for x in range(len(board)):
        for y in range(len(board[x])):

            # Check horizontal
            if y < 4:
                if board[x][y] == board[x][y + 1] == board[x][y + 2] == board[x][y + 3] != ' ':
                    return True

            # Check vertical
            if x < 3:
                if board[x][y] == board[x + 1][y] == board[x + 2][y] == board[x + 3][y] != ' ':
                    return True

            # check Diagonal 1
            if x < 3 and y < 4:
                if board[x][y] == board[x + 1][y + 1] == board[x + 2][y + 2] == board[x + 3][y + 3] != ' ':
                    return True

            # check Diagonal 2
            if x < 3 and y < 4:
                if board[x][y] == board[x - 1][y - 1] == board[x - 2][y - 2] == board[x - 3][y - 3] != ' ':
                    return True
    return False


def set_player_move(in_move, turn, board):
    print("In setplayermove")

    move = int(in_move)
    for x in range(len(board)):
        if board[x][move - 1] == ' ':
            board[x][move - 1] = turn
            break


def check_game_end(count, turn, board):
    if count >= 6:
        if check_win(board):
            print("Player " + turn + " won!")
            winner = turn
            return winner
        
    if count >= 41:
        print("It's a tie!")
        reset_game()
        return "draw"

    return None

def reset_game():
    global board, screen, turn, winner, draw
    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    screen = ""
    # Set turn yellow/red
    turn = 'red'

    # Store winner/draw
    winner = None
    draw = None
