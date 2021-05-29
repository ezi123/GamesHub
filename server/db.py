import sqlite3
from sqlite3 import Error

db_file = r"gamehub.db"

def create_connection():
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_user(userData):

    conn = create_connection()

    # check if the userName is already taken
    cur = conn.cursor()
    userExists = cur.execute("SELECT COUNT(*) FROM users WHERE userName=?", (userData[2],))

    result = cur.fetchone()[0]
    if result != 0:
        print('userName Exists!')
        return -1 # Error creating the user

    """
    Create a new user into the users table
    :param conn:
    :param userData:
    :return: user id
    """
    sql = ''' INSERT INTO users(firstName, lastName, userName, password, email)
              VALUES(?,?,?,?,?) '''

    cur.execute(sql, userData)
    conn.commit()
    conn.close()
    return cur.lastrowid


def validate_user(loginUserData):

    conn = create_connection()

    """
    Query user by userName
    :param conn: the Connection object
    :param userName:
    :return:
    """
    cur = conn.cursor()
    userExists = cur.execute("SELECT COUNT(*) FROM users WHERE userName=? AND password=?", (loginUserData))

    result = cur.fetchone()[0]

    conn.close()

    if result == 0:
        print('User Not Found!')
        return -1
    else:
        print('User Exists!')
        return 1