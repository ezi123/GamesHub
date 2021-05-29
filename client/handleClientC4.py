import socket
from threading import Thread
import time
from client import client_logic, c4client, client_comm

def run():

    newBoard = launchC4(1)
    newBoard.start()

    msg = "startGame"
    client_logic.formatServerMsg(msg, "")



def processC4ServerMessage(servResp):

    split = servResp.split("##")
    split[0] = split[0].lower()




    if split[0] == "win":
        print("You win!!!")
    elif split[0] == "lose":
        print("You lose :(")
    elif split[0] == "draw":
        print("It's a draw!")

    elif split[0] == "move":
        c4client.set_player_move(split[1])


class launchC4(Thread):

    def __init__(self, firstTurn):
        Thread.__init__(self)

        self.myTurn = str(firstTurn)
        if self.myTurn == "0":
            self.myTurn = "red"
        if self.myTurn == "1":
            self.myTurn = "yellow"

    def run(self):
        c4client.start_pg()
        print(self.myTurn)
        c4client.game_initiating_window()



        while True:
            move = c4client.check_client_activity()
            move = str(move)
            print("sending move: " + move)
            client_logic.formatServerMsg("move", move)
