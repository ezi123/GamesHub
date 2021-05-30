from threading import Thread
from client import client_logic, c4client


class LaunchC4(Thread):

    def __init__(self, first_turn):
        Thread.__init__(self)

        self.myTurn = str(first_turn)
        if self.myTurn == "0":
            self.myTurn = "red"
        if self.myTurn == "1":
            self.myTurn = "yellow"

    def run(self):
        c4client.start_pg()
        print(self.myTurn)
        c4client.game_initiating_window()

        msg = "startGame"
        client_logic.formats_server_msg(msg, "")

        while True:
            move = c4client.check_client_activity()
            move = str(move)
            print("sending move: " + move)
            client_logic.formats_server_msg("move", move)


def start_client_comm_thread():
    new_board = LaunchC4(1)
    new_board.start()


def process_c4_server_message(serv_resp):
    split = serv_resp.split("##")
    split[0] = split[0].lower()

    if split[0] == "win":
        print("You win!!!")
        c4client.end_game(split[0])
    elif split[0] == "lose":
        print("You lose :(")
        c4client.end_game(split[0])
    elif split[0] == "draw":
        print("It's a draw!")
        c4client.end_game(split[0])

    elif split[0] == "move":
        c4client.draw_board(split[1])


