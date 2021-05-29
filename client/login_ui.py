from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo
from client import client_logic
import re

loginWin = None
signupWin = None

# ---------------------------------------------------------------Login Function --------------------------------------
def close():
    global loginWin
    loginWin.destroy()


# ---------------------------------------------------------------End Login Function ---------------------------------
# ----------------------------------------------------------- Signup Window --------------------------------------------------

    # signup database connect
def signup():
    # Make a regular expression
    # for validating an Email
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    global signupWin
    first_name = signupWin.first_name.get()
    last_name = signupWin.last_name.get()
    user_name = signupWin.user_name.get()
    email = signupWin.email.get()
    password = signupWin.password.get()
    very_pass = signupWin.very_pass.get()

    if first_name == "" or last_name == "" or user_name == "" or email == "" or password == "" or very_pass == "":
        messagebox.showerror("Error", "All Fields Are Required", parent=signupWin)
    elif password != very_pass:
        messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=signupWin)
    elif re.search(regex, email) == None:
        messagebox.showerror("Error", "Please type a valid email address", parent=signupWin)
    else:
        try:
            userData = first_name + "##" + last_name + "##" + user_name + "##" + email + "##" + password
            client_logic.bl_signup(userData)

        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=signupWin)


# start register Window
def openRegisterUI():
    global signupWin
    signupWin = Tk()
    signupWin.title("GameHub - Register")
    signupWin.maxsize(width=430, height=360)
    signupWin.minsize(width=430, height=360)

    # bg color
    bg_color = "DeepSkyBlue2"
    fg_color = "#383a39"
    signupWin.configure(background=bg_color)

    # heading label
    heading = Label(signupWin, text="Register", font='Verdana 20 bold', bg=bg_color)
    heading.place(x=40, y=25)

    # form data label
    first_name = Label(signupWin, text="First Name :", font='Verdana 10 bold', bg=bg_color)
    first_name.place(x=40, y=70)

    last_name = Label(signupWin, text="Last Name :", font='Verdana 10 bold', bg=bg_color)
    last_name.place(x=40, y=110)

    user_name = Label(signupWin, text="User Name :", font='Verdana 10 bold', bg=bg_color)
    user_name.place(x=40, y=150)

    user_name = Label(signupWin, text="Email :", font='Verdana 10 bold', bg=bg_color)
    user_name.place(x=40, y=190)

    password = Label(signupWin, text="Password :", font='Verdana 10 bold', bg=bg_color)
    password.place(x=40, y=230)

    very_pass = Label(signupWin, text="Verify Password:", font='Verdana 10 bold', bg=bg_color)
    very_pass.place(x=40, y=270)

    # Entry Box ------------------------------------------------------------------
    first_name = StringVar()
    last_name = StringVar()
    user_name = StringVar()
    email = StringVar()
    password = StringVar()
    very_pass = StringVar()

    signupWin.first_name = Entry(signupWin, width=30, textvariable=first_name)
    signupWin.first_name.focus()
    signupWin.first_name.place(x=190, y=70)

    signupWin.last_name = Entry(signupWin, width=30, textvariable=last_name)
    signupWin.last_name.place(x=190, y=110)

    signupWin.user_name = Entry(signupWin, width=30, textvariable=user_name)
    signupWin.user_name.place(x=190, y=150)

    signupWin.email = Entry(signupWin, width=30, textvariable=email)
    signupWin.email.place(x=190, y=190)

    signupWin.password = Entry(signupWin, width=30, show="*", textvariable=password)
    signupWin.password.place(x=190, y=230)

    signupWin.very_pass = Entry(signupWin, width=30, show="*", textvariable=very_pass)
    signupWin.very_pass.place(x=190, y=270)

    # button register and login
    btn_signup = Button(signupWin, text="Register", font='Verdana 10 bold', command=signup)
    btn_signup.place(x=240, y=310)

    btn_login = Button(signupWin, text="Close", font='Verdana 10 bold', command=signupWin.destroy)
    btn_login.place(x=320, y=310)

#    signupWin.bind('<Return>', signup)

    signupWin.mainloop()

def closeSignupUI():
    global signupWin
    messagebox.showinfo("Success", "Signup successfully!", parent=signupWin)
    if signupWin != None:
        signupWin.destroy()

def showSignupMsgInfo(msg):
    global signupWin
    messagebox.showinfo("Error", msg, parent=signupWin)

# ---------------------------------------------------------------------------End Register Window-----------------------------------


# ------------------------------------------------------------ Login Window -----------------------------------------


def login():
    global loginWin

    username = loginWin.userentry.get()
    password = loginWin.passentry.get()
    if username == "" or password == "":
        messagebox.showerror("Error", "Enter User Name And Password")
    else:
        userData = username + "##" + password
        client_logic.bl_login(userData)
        return ("login", username, password)


def openLoginUI():
    global loginWin
    
    loginWin = Tk()

    # app title
    loginWin.title("GameHub - Login")

    # bg color
    bg_color = "DeepSkyBlue2"
    fg_color = "#383a39"
    loginWin.configure(background=bg_color)

    # window size
    loginWin.maxsize(width=430, height=380)
    loginWin.minsize(width=430, height=380)

    photo = ImageTk.PhotoImage(Image.open("../res/c4_cover_small.jpeg"))
    Label(loginWin, image=photo).grid(rowspan=3, columnspan=5, row=0, column=0)

    username = Label(loginWin, text="User Name :", font='Verdana 10 bold', bg=bg_color)
    username.place(x=60, y=260)

    userpass = Label(loginWin, text="Password :", font='Verdana 10 bold', bg=bg_color)
    userpass.place(x=60, y=300)

    # Entry Box
    user_name = StringVar()
    password = StringVar()

    loginWin.userentry = Entry(loginWin, width=35, textvariable=user_name)
    loginWin.userentry.focus()
    loginWin.userentry.place(x=170, y=260)

    loginWin.passentry = Entry(loginWin, width=35, show="*", textvariable=password)
    loginWin.passentry.place(x=170, y=300)

    # button login
    btn_login = Button(loginWin, text="Login", font='Verdana 10 bold', command=login)
    btn_login.place(x=260, y=340)

    # signup button
    sign_up_btn = Button(loginWin, text="Signup", font='Verdana 10 bold', command=openRegisterUI)
    sign_up_btn.place(x=320, y=340)

#    loginWin.bind('<Return>', login)

    loginWin.mainloop()

def closeLoginUI():
    global loginWin
    if loginWin != None:
         loginWin.withdraw()

def showLoginMsgInfo(msg):
    global loginWin
    messagebox.showinfo("Error", msg, parent=loginWin)
