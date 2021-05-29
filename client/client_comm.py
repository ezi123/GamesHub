import socket
import threading
from threading import Lock
from client import client_logic

import client.client_ui

client_socket = None


class ClientThread(threading.Thread):
    clientAddress = None
    clientSocket = None
    clients = []
    lock = Lock()
    user = ""

    def __init__(self, clientAddress, clientSocket):
        self.clientAddress = clientAddress
        self.clientSocket = clientSocket

        threading.Thread.__init__(self)

    #    def broadcast(self):

    def run(self):
        while True:
            try:
                data = self.clientSocket.recv(2048)
                msg = data.decode('utf-8').lower()
                if msg == 'bye':
                    self.clientSocket.close()
            except socket.error as err:
                print("Caught exception socket.error: " + err.strerror)
                self.clientSocket.close()
                client.client_ui.show_message_box("Error",
                                                 "Oops... We lost connection to server. Would you kindly restart?")
                self.clientSocket.close()

            print("from server: ", msg)
            client_logic.process_server_message(msg)


def send_to_server(out_data):
    global client_socket

    client_socket.sendall(bytes(out_data, 'UTF-8'))
    if out_data == 'bye':
        client_socket.close()


def start_client_comm():
    global client_socket

    SERVER = "127.0.0.1"
    PORT = 5050
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER, PORT))
    except socket.error as err:
        client.client_ui.show_message_box("Error",
                                         "Oops... Unable to connect to server... \n\nError: " + err.strerror)
        exit(-1)

    new_thread = ClientThread('1.1.1.1', client_socket)
    new_thread.start()
