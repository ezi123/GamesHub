from client import client_comm, client_ui

if __name__ == '__main__':
    client_ui.create_login_window()

    # connect to the server
    client_comm.start_client_comm()

    # open the login UI
    client_ui.open_login_ui()
