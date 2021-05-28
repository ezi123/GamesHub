import pygame as pg
import sys
from pygame.locals import *
from client import client_logic
from threading import Thread

# Creates the board
board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
screen = ""
# Set turn yellow/red
turn = ''
msg = ''
assigned = False

# Store winner/draw
winner = None
draw = None

# Size of board in pixels
width = 600
height = 600

# Background color, divider lines
white = (255, 255, 255)
line_color = (0, 0, 0)

# Set images that will be used
initiating_window = pg.image.load("../res/c4_cover.png")
red_img = pg.image.load("../res/c4_red_piece.png")
yellow_img = pg.image.load("../res/c4_yellow_piece.png")

# Scales the image to the size of the board
initiating_window = pg.transform.scale(initiating_window, (width, height + 100))
red_img = pg.transform.scale(red_img, (50, 50))
yellow_img = pg.transform.scale(yellow_img, (50, 50))


def start_pg():
    global screen
    # Starting up pygame
    pg.init()

    # Cap frames at 30
    fps = 30

    # Track time
    CLOCK = pg.time.Clock()

    # Set display
    screen = pg.display.set_mode((width, height + 100), 0, 32)
    pg.display.set_caption("Connect Four")


def game_initiating_window():
    
    # Puts the cover image over the screen
    # screen.blit(initiating_window, (0,0))
    # pg.display.update()
    # time.sleep(2)
    screen.fill(white)

    # draws the board
    # drawing vertical lines:
    for i in range(1, 7):
        pg.draw.line(screen, line_color, (width / 7 * i, 0), (width / 7 * i, height), 7)

    # drawing horizontal lines
    for i in range(1, 6):
        pg.draw.line(screen, line_color, (0, height / 6 * i), (width, height / 6 * i), 7)
    draw_status()


def draw_status():
    global draw, turn, msg, assigned


    print("Hi")

    if assigned:
        if winner is None:
            message = turn + "'s turn!"
            assigned = True
        else:
            message = turn + " won!"
            assigned = True
        if draw is True:
            message = "The game ended in a draw!"
            assigned = True

    if not assigned:
        message = msg
        assigned = True


    # setting a font object
    font = pg.font.Font(None, 30)

    # setting the font properties
    text = font.render(message, 1, (255, 255, 255))

    # copy the rendered message onto the board, creating a small block at the bottom of the main display
    screen.fill((0, 0, 0), (0, 600, 600, 100))
    text_rect = text.get_rect(center=(width / 2, 650))
    screen.blit(text, text_rect)
    pg.display.update()


def draw(row, col):
    global board, turn

    row = row - 1
    if row == 0:
        posx = 15
    elif row == 1:
        posx = 110
    elif row == 2:
        posx = 200
    elif row == 3:
        posx = 280
    elif row == 4:
        posx = 360
    elif row == 5:
        posx = 440
    else:
        posx = 530

    if col == 0:
        posy = 530
    elif col == 1:
        posy = 440
    elif col == 2:
        posy = 330
    elif col == 3:
        posy = 210
    elif col == 4:
        posy = 110
    else:
        posy = 30
    if turn == "red":
        screen.blit(red_img, (posx, posy))

    else:
        screen.blit(yellow_img, (posx, posy))

    pg.display.update()
    return


def get_player_move():
    x, y = pg.mouse.get_pos()

    for i in range(1, 8):
        if x < width / 7 * i:
            x = i
            break
    return x


def check_empty_tile(move):
    move = int(move)

    for x in range(len(board)):
        print(x)
        print(move)
        if board[x][move - 1] == ' ':
            return True, x
    return False


def set_player_move(move):
    global turn
    added = False
    move = int(move)
    for x in range(len(board)):
        if board[x][move] == ' ' and not added:
            board[x][move] = turn
            added = True

    if turn == "red":
        turn = "yellow"
    else:
        turn = "red"


def check_client_activity():
    global turn, winner, draw
    move = None


    while True:

        count = 0
        done = False

        while True:

            if not done:
                    for event in pg.event.get():
                            if event.type == QUIT:
                                pg.quit()
                                sys.exit()
                            elif event.type == MOUSEBUTTONDOWN:
                                print("got Turn mouse event. Turn is: " + str(turn))
                                if turn != "red":
                                    continue
                                move = get_player_move()
                                return move


            elif done:
                if pg.event.get(eventtype=QUIT):
                    pg.quit()
                    sys.exit()

            elif move != None:
                return move

def get_turn():
    global turn
    return turn


def set_turn(setTurn):
    global turn
    print(setTurn)
    turn = setTurn


def set_message(setMessage):
    global msg
    msg = setMessage