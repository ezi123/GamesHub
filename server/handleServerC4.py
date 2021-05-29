import random
import socket
import random
from server import server_comm, server_logic, c4server
from threading import Thread


class c4ServerClass(Thread):
    def __init__(self, clientSocket1, clientSocket2, firstP1):
        Thread.__init__(self)
        self.clientSocket1 = clientSocket1
        self.clientSocket2 = clientSocket2
        self.firstP1 = firstP1

    def run(self):

#        rand = random.randint(0,1)
#        turn = rand
# for testing, first user runs first
        turn = rand = 1
        if rand == 0:
            print("Sending Turn to player 1")
            server_logic.formatAndSend(self.clientSocket1, "turn", "red")
            server_logic.formatAndSend(self.clientSocket2, "turn", "yellow")
        else:
            print("Sending Turn to player 2")
            server_logic.formatAndSend(self.clientSocket2, "turn", "red")
            server_logic.formatAndSend(self.clientSocket1, "turn", "yellow")

        print("In handleServerC4")
        while True:
            if turn == 0:
                data = self.clientSocket1.recv(1024).decode('utf-8')
            else:
                data = self.clientSocket2.recv(1024).decode('utf-8')


            print("Turn = " + str(turn) + ". Data recieced: " + data)
            split = data.split("##")
            print(split[0])
            if split[0] == "move":
                c4server.set_player_move(split[2])
                server_logic.formatAndSend(self.clientSocket1, "move", split[2])
                server_logic.formatAndSend(self.clientSocket2, "move", split[2])
                winner = c4server.check_game_end()

                if winner == "red":
                    if self.firstP1 == "0":
                        self.clientSocket1.send(bytes("Win", 'utf-8'))
                        self.clientSocket2.send(bytes("Lose", 'utf-8'))
                        break
                    else:
                        self.clientSocket2.send(bytes("Win", 'utf-8'))
                        self.clientSocket1.send(bytes("Lose", 'utf-8'))
                        break
                elif winner == "yellow":
                    if self.firstP1 == "1":
                        self.clientSocket1.send(bytes("Win", 'utf-8'))
                        self.clientSocket2.send(bytes("Lose", 'utf-8'))
                        break
                    else:
                        self.clientSocket2.send(bytes("Win", 'utf-8'))
                        self.clientSocket1.send(bytes("Lose", 'utf-8'))
                        break
                elif winner == "draw":
                    self.clientSocket1.send(bytes("Draw", 'utf-8'))
                    self.clientSocket2.send(bytes("Draw", 'utf-8'))
                    break