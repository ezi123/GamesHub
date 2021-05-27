import socket, threading, os
from threading import Thread, Lock
import server_logic


class ClientThread(threading.Thread):
    global users
    clientAddress = None
    clientSocket = None
    clients = []
    lock = Lock()
    user = ""

    def __init__(self, clientAddress, clientSocket):
        self.clientAddress = clientAddress
        self.clientSocket = clientSocket

        threading.Thread.__init__(self)
        print("New connection added: ", self.clientAddress)
        ClientThread.clients.append(self.clientSocket)

    #    def broadcast(self):

    def run(self):
        self.loggedIn = False
        print("Connection from : ", self.clientAddress)

        while True:
            data = self.clientSocket.recv(2048)
            msg = data.decode('utf-8')
            if msg == 'bye':
                break
            print("from client", msg)
            retVal = server_logic.parse_client_msg(self.clientSocket, msg)
#            self.clientSocket.send(bytes(retVal, "utf-8"))

"""            if self.loggedIn is False:
                self.user = server_logic.parse_client_msg(msg)
                self.loggedIn = True
                users[self.user] = self.clientSocket

            else:
                self.clientSocket.send(bytes('startGame', 'utf-8'))
                otherUser = server_logic.parse_client_msg(msg)
                otherSocket = users[otherUser]
                otherSocket.send(bytes("startGame", 'utf-8'))
                threading.Thread.__init__(self)

            self.csocket.send(bytes(msg, 'UTF-8'))
        print("Client at ", self.clientAddress, " disconnected...")
"""

def startServer():
    LOCALHOST = "127.0.0.1"
    PORT = 5050
    users = {}
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((LOCALHOST, PORT))
        print("Server started")
        print("Waiting for client request..")
    except socket.error as err:
        print('Unable to start server: ' + err.strerror)
        os._exit(1)

    while True:
        server.listen(1)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()
