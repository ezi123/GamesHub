import sys
#Creates the board
board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
screen = ""
#Set turn yellow/red
turn = 'red'

#Store winner/draw
winner = None
draw = None

def check_win():

    print("IN Checkwin")
    for x in range(len(board)):
        for y in range(len(board[x])):

            # Check horiz
            if y < 4:
                if board[x][y] == board[x][y+1] == board[x][y+2] == board[x][y+3] != ' ':
                    return True

            # Check vert
            if x < 3:
                if board[x][y] == board[x + 1][y] == board[x + 2][y] == board[x + 3][y] != ' ':
                    return True

            # check Diag1
            if x < 3 and y < 4:
                if board[x][y] == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3] != ' ':
                    return True

            # check Diag2
            if x < 3 and y < 4:
                if board[x][y] == board[x-1][y-1] == board[x-2][y-2] == board[x-3][y-3] != ' ':
                    return True
    return False



def set_player_move(move):
    print("In setplayermove")
    global turn
    added = False
    move = int(move)
    for x in range(len(board)):
        if not added:
            board[x][move - 1] = turn
            added = True

def check_game_end():
    global turn
    count = 0
    if count >= 6:
        if check_win():
            print("Player " + turn + " won!")
            winner = turn
            return winner
    if count >= 41:
        print("It's a tie!")
        draw = True
        return "draw"

    if turn == "red":
        turn = "yellow"
    else:
        turn = "red"
    count += 1

    return None



