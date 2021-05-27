import socket
import threading
import client_logic

client_socket = None

from threading import Lock


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

    #    def broadcast(self):

    def run(self):
        while True:
            data = self.clientSocket.recv(2048)
            msg = data.decode('utf-8').lower()
            if msg == 'bye':
                self.clientSocket.close()
            #        sys.exit()
            #      if msg == 'startgame':
            #          handleClientC4.run(self.csocket)
            print("from server", msg)
            client_logic.processServerMessage(msg)

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


def sendToServer(out_data):
    global client_socket

    client_socket.sendall(bytes(out_data, 'UTF-8'))
    if out_data == 'bye':
        client_socket.close()

def start_client_comm():
    global client_socket

    SERVER = "127.0.0.1"
    PORT = 5050
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER, PORT))

    newthread1 = ClientThread('1.1.1.1', client_socket)
    newthread1.start()

#    newthread = SocketHandler(client_socket)
#    newthread.start()
#    print("123")
#    time.sleep(100)
#    msg = "123"
