from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo
from client import client_logic

loginWin = None
registerWin = None

# ---------------------------------------------------------------Login Function --------------------------------------
def close():
    global loginWin
    loginWin.destroy()


# ---------------------------------------------------------------End Login Function ---------------------------------
# ----------------------------------------------------------- Signup Window --------------------------------------------------

def signup():
    # signup database connect
    def register():
        if first_name.get() == "" or last_name.get() == "" or user_name.get() == "" or password.get() == "" or very_pass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=winsignup)
        elif password.get() != very_pass.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=winsignup)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="docterapp")
                cur = con.cursor()
                cur.execute("select * from user_information where username=%s", user_name.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User Name Already Exits", parent=winsignup)
                else:
                    cur.execute(
                        "insert into user_information(first_name,last_name,age,gender,city,address,username,password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            first_name.get(),
                            last_name.get(),
                            user_name.get(),
                            password.get()
                        ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Ragistration Successfull", parent=winsignup)

            except Exception as es:
                messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=winsignup)


# start register Window
def openRegisterUI():
    global registerWin
    registerWin = Tk()
    registerWin.title("GameHub - Register")
    registerWin.maxsize(width=430, height=340)
    registerWin.minsize(width=430, height=340)

    # bg color
    bg_color = "DeepSkyBlue2"
    fg_color = "#383a39"
    registerWin.configure(background=bg_color)

    # heading label
    heading = Label(registerWin, text="Register", font='Verdana 20 bold', bg=bg_color)
    heading.place(x=40, y=25)

    # form data label
    first_name = Label(registerWin, text="First Name :", font='Verdana 10 bold', bg=bg_color)
    first_name.place(x=40, y=70)

    last_name = Label(registerWin, text="Last Name :", font='Verdana 10 bold', bg=bg_color)
    last_name.place(x=40, y=110)

    user_name = Label(registerWin, text="User Name :", font='Verdana 10 bold', bg=bg_color)
    user_name.place(x=40, y=150)

    password = Label(registerWin, text="Password :", font='Verdana 10 bold', bg=bg_color)
    password.place(x=40, y=190)

    very_pass = Label(registerWin, text="Verify Password:", font='Verdana 10 bold', bg=bg_color)
    very_pass.place(x=40, y=230)

    # Entry Box ------------------------------------------------------------------
    first_name = StringVar()
    last_name = StringVar()
    user_name = StringVar()
    password = StringVar()
    very_pass = StringVar()

    first_name = Entry(registerWin, width=25, textvariable=first_name)
    first_name.place(x=150, y=65)

    last_name = Entry(registerWin, width=25, textvariable=last_name)
    last_name.place(x=150, y=105)

    user_name = Entry(registerWin, width=25, textvariable=user_name)
    user_name.place(x=150, y=145)

    password = Entry(registerWin, width=25, show="*", textvariable=password)
    password.place(x=150, y=185)

    very_pass = Entry(registerWin, width=25, show="*", textvariable=very_pass)
    very_pass.place(x=150, y=225)

    # button register and login
    btn_signup = Button(registerWin, text="Register", font='Verdana 10 bold', command=register)
    btn_signup.place(x=290, y=270)

    btn_login = Button(registerWin, text="Login", font='Verdana 10 bold', command=switchLogin)
    btn_login.place(x=350, y=270)

    registerWin.mainloop()

def closeRegisterUI():
    global registerWin
    if registerWin != None:
        registerWin.destroy()

def showRegisterMsgInfo(msg):
    showinfo("Register", msg)

# ---------------------------------------------------------------------------End Register Window-----------------------------------


# ------------------------------------------------------------ Login Window -----------------------------------------
userentry = None
passentry = None
username = ""
password = ""

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
    sign_up_btn = Button(loginWin, text="Signup", font='Verdana 10 bold', command=signup)
    sign_up_btn.place(x=320, y=340)

    loginWin.mainloop()

def closeLoginUI():
    global loginWin
    # if loginWin != None:
        # loginWin.destroy()
        # loginWin = None

def showLoginMsgInfo(msg):
    showinfo("Login", msg)

# -------------------------------------------------------------------------- End Login Window ---------------------------------------------------
