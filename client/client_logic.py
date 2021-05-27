import client_comm
import login_ui

clientId = "XX"

# outgoing messages
def formatServerMsg(operation, operationData):
    # format the needed extra information
    # Operation, Username, Game, Message
    global clientId
    outStr = operation + "##" + clientId + "##" + operationData
    return outStr

def bl_login(outStr):
    sendStr = formatServerMsg("login", outStr)
    client_comm.sendToServer(sendStr)

#incoming messages
def processServerMessage(msg):
    split = msg.split("##")
    message_type = split[0].lower()

    if message_type == "login":
        returnCode = split[1]
        returnMsg = split[2]
        if returnCode == '1':
            login_ui.closeLoginUI()
        else:
            login_ui.popup_window(returnMsg)
