import db

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

    if message_type == "game":
        other = split[1]
        return other

def sendLoginStatus(socket, loginStatus):
    msg = ""
    if loginStatus == -1:
        msg = "Wrong username or password. Please try again."
    elif loginStatus == 1:
        msg = "Login successful!"
    sendMsg = "login##" + str(loginStatus) + "##" + msg
    socket.send(bytes(sendMsg, 'utf-8'))