import random
from server import server_logic, c4server
from threading import Thread


class C4ServerClass(Thread):
    def __init__(self, client_socket_1, client_socket_2, first_p1):
        Thread.__init__(self)
        self.client_socket_1 = client_socket_1
        self.client_socket_2 = client_socket_2
        self.first_p1 = first_p1

    def run(self):

        count = 0
        rand = random.randint(0, 1)
        turn = rand
        #        turn = rand = 1
        if rand == 0:
            print("Sending Turn to player 1")
            server_logic.format_and_send(self.client_socket_1, "turn", "red")
            server_logic.format_and_send(self.client_socket_2, "turn", "yellow")
        else:
            print("Sending Turn to player 2")
            server_logic.format_and_send(self.client_socket_2, "turn", "red")
            server_logic.format_and_send(self.client_socket_1, "turn", "yellow")

        print("In handleServerC4")
        while True:
            if turn == 0:
                data = self.client_socket_1.recv(1024).decode('utf-8')
            else:
                data = self.client_socket_2.recv(1024).decode('utf-8')

            print("Turn = " + str(turn) + ". Data recieced: " + data)
            split = data.split("##")
            print(split[0])
            if split[0] == "move":
                c4server.set_player_move(split[2])
                server_logic.format_and_send(self.client_socket_1, "move", split[2])
                server_logic.format_and_send(self.client_socket_2, "move", split[2])
                winner = c4server.check_game_end(count)
                count = count + 1

                if winner == "red":
                    if self.first_p1 == "0":
                        self.client_socket_1.send(bytes("Win", 'utf-8'))
                        self.client_socket_2.send(bytes("Lose", 'utf-8'))
                        break
                    else:
                        self.client_socket_2.send(bytes("Win", 'utf-8'))
                        self.client_socket_1.send(bytes("Lose", 'utf-8'))
                        break
                elif winner == "yellow":
                    if self.first_p1 == "1":
                        self.client_socket_1.send(bytes("Win", 'utf-8'))
                        self.client_socket_2.send(bytes("Lose", 'utf-8'))
                        break
                    else:
                        self.client_socket_2.send(bytes("Win", 'utf-8'))
                        self.client_socket_1.send(bytes("Lose", 'utf-8'))
                        break
                elif winner == "draw":
                    self.client_socket_1.send(bytes("Draw", 'utf-8'))
                    self.client_socket_2.send(bytes("Draw", 'utf-8'))
                    break

                if turn == 1:
                    turn = 0
                else:
                    turn = 1
