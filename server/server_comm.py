import socket, threading, os
from threading import Thread, Lock
from server import server_logic

wait_list = []


class ClientThread(threading.Thread):
    client_address = None
    client_socket = None
    clients = []
    lock = Lock()
    user = ""

    def __init__(self, client_address, client_socket):
        self.client_address = client_address
        self.client_socket = client_socket

        threading.Thread.__init__(self)
        print("New connection added: ", self.client_address)
        ClientThread.clients.append(self.client_socket)

    #    def broadcast(self):

    def run(self):
        print("Connection from : ", self.client_address)

        while True:
            data = self.client_socket.recv(2048)
            msg = data.decode('utf-8')
            print("from client: ", msg)

            server_logic.parse_client_msg(self.client_socket, msg)

            # once the game starts. the communication is through the game class, so stop listening here
            if 'startGame' in msg:
                break


def start_server():
    localhost = "127.0.0.1"
    port = 5050

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((localhost, port))
        print("Server started")
        print("Waiting for client request..")
    except socket.error as err:
        print('Unable to start server: ' + err.strerror)
        os._exit()

    while True:
        server.listen(1)
        clientsock, client_address = server.accept()
        newthread = ClientThread(client_address, clientsock)
        newthread.start()


def send_to_client(client_socket, message):
    client_socket.send(bytes(message, 'utf-8'))


def get_wait_list():
    global wait_list
    return wait_list


def set_wait_list(waiting_list):
    global wait_list
    wait_list = waiting_list
