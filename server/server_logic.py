from server import db, server_comm, handleServerC4
import random


def parse_client_msg(client_socket, client_message):
    split = client_message.split("##")
    message_type = split[0].lower()

    if message_type == "register":
        username = split[1]
        password = split[2]
        email = split[3]
        userData = (username, password, email)

        db.create_user(userData)
        return username

    if message_type == "login":
        username = split[2]
        password = split[3]

        loginUserData = (username, password)
        validUser = db.validate_user(loginUserData)
        if validUser == 1: # user exists
            loginStatus = 1
        else:
            loginStatus = -1

        sendLoginStatus(client_socket, loginStatus)
        return

    if message_type == "startgame":
        waitForGame(client_socket)


def sendLoginStatus(socket, loginStatus):
    msg = ""
    if loginStatus == -1:
        msg = "Wrong username or password. Please try again."
    elif loginStatus == 1:
        msg = "Login successful!"
    sendMsg = "login##" + str(loginStatus) + "##" + msg
    server_comm.sendToClient(socket, sendMsg)


def formatAndSend(socket, command, message):

    msg = command + "##" + message
    server_comm.sendToClient(socket, msg)


def waitForGame(client_socket):
    waitlist = server_comm.getWaitList()
    if len(waitlist) > 0:

        firstUser = waitlist[0]

        # Randomizes first player
        firstP1 = str(random.randint(0,1))

        newThread = handleServerC4.c4ServerClass(firstUser, client_socket, firstP1)
        newThread.start()

        if firstP1 == "1":
            formatAndSend(firstUser, "startgame", "0")
            formatAndSend(client_socket, "startgame", "1")
        else:
            formatAndSend(firstUser, "startgame", "1")
            formatAndSend(client_socket, "startgame", "0")

        # Resets the list of currently waiting users
        server_comm.setWaitList([])

    else:
        waitlist.append(client_socket)
        formatAndSend(client_socket, "inQueue", "You have been added to the queue")

