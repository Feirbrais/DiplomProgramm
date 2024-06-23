import sqlite3
import hashlib

def LoginPasswordCheck(login, password):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute("SELECT id FROM users where login='" + login + "' AND pass='" + hashlib.sha1(password.encode()).hexdigest() + "';")
    data = cur.fetchall()
    
    if data:
        conn.close()
        return True
    else:
        conn.close()
        return False
    
def getUserInformation(login, password):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute("SELECT id, status FROM users where login='" + login + "' AND pass='" + hashlib.sha1(password.encode()).hexdigest() + "';")
    data = cur.fetchall()

    conn.close()
    return str(data[0][0]), login, password, str(data[0][1])

def UserCheck(login):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute("SELECT id FROM users where login='" + login + "';")
    data = cur.fetchall()

    conn.close()
    if data:
        return False
    else:
        return True

def NewUserRegistration(login, password):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO users(login, pass, status) VALUES('" + login + "', '" + hashlib.sha1(password.encode()).hexdigest() + "', 1);")
    conn.commit()
    conn.close()

def SaveNewLogin(login, id):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute("""update users set login='""" + login + """' where id=""" + id + """;""")
    conn.commit()
    conn.close()

def SaveNewPassword(password, id):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute("""update users set pass=""" + hashlib.sha1(password.encode()).hexdigest() + """ where id=""" + id + """;""")
    conn.commit()
    conn.close()

def SaveNewLogin(login, id):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute("""update users set login=""" + login + """ where id=""" + id + """;""")
    conn.commit()
    conn.close()

def SaveNewStatus(id):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute("""update users set status=0 where id=""" + id + """;""")
    conn.commit()
    conn.close()

def delUser(id):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute("""delete from users where id=""" + id + """;""")
    conn.commit()
    conn.close()

def getUsersDataFoTable():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")
    data = cur.fetchall()

    conn.close()
    return data

def CheckStatusOrRealisticUser(id):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute("SELECT login FROM users where login=" + id + " AND status=1;")
    data = cur.fetchall()

    conn.close()
    if data:
        return False
    else:
        return True