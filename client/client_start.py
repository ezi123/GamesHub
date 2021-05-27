import client_comm
import client_logic
import login_ui

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # connect to the server
    client_comm.start_client_comm()

    # open the login UI
    login_ui.openLoginUI()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
