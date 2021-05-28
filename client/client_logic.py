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

    elif message_type == "inqueue":
        return


    elif message_type == "move" or message_type == "winner" or message_type == "draw":
        handleClientC4.processC4ServerMessage(msg)


