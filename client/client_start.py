from client import client_comm, client_ui

if __name__ == '__main__':
    # connect to the server
    client_comm.start_client_comm()

    # open the login UI
    client_ui.open_login_ui()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
