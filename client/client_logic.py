from client import client_comm, login_ui, handleClientC4, c4client

clientId = "XX"

# outgoing messages
def formatServerMsg(operation, operationData):
    # format the needed extra information
    # Operation, Username, Game, Message
    global clientId
    outStr = operation + "##" + clientId + "##" + operationData
    client_comm.sendToServer(outStr)
    return outStr

def bl_login(outStr):
    sendStr = formatServerMsg("login", outStr)

def bl_signup(outStr):
    sendStr = formatServerMsg("signup", outStr)

#incoming messages
def processServerMessage(msg):
    split = msg.split("##")
    message_type = split[0].lower()

    if message_type == "login":
        returnCode = split[1]
        returnMsg = split[2]
        if returnCode == '1':
            login_ui.closeLoginUI()
            handleClientC4.run()
        else:
            login_ui.showLoginMsgInfo(returnMsg)

    elif message_type == "signup":
        returnCode = split[1]
        returnMsg = split[2]
        if returnCode == '1':
            login_ui.closeSignupUI()
        else:
            login_ui.showSignupMsgInfo(returnMsg)

    elif message_type == "inqueue":
        c4client.set_message("Waiting for second player to connect...")
        c4client.draw_status()
        return

    elif message_type == "move" or message_type == "winner" or message_type == "draw":
        handleClientC4.processC4ServerMessage(msg)

    elif message_type == "turn":
        c4client.set_turn(split[1])

