import sqlite3
from flask import Flask
app = Flask(__name__)

# DATABASE
# agentData-> agent_id,password
# TodoList-> TodoId, agent_id, TodoString 

# Schema
def createTodoApp():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs TodoList (TodoId TEXT PRIMARY KEY , agent_id TEXT, TodoString TEXT)")
    conn.commit()
    conn.close()

def insertTodo(agent_id,TodoString):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT COUNT(DISTINCT TodoId) from TodoList")
    r=cur.fetchone
    TodoNo=r['COUNT(DISTINCT TodoId)']
    cur.execute("INSERT INTO TodoList VALUES (?,?,?)",(TodoNo, agent_id,TodoString))
    conn.commit()
    conn.close()

# Connects to DB
def connect():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs agentData (agent_id TEXT PRIMARY KEY , password TEXT)")
    conn.commit()
    conn.close()
# Register
def insertAgent(agent_id,password):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO agentData VALUES (?,?)",(agent_id,password))
    conn.commit()
    conn.close()
# Login
def loginAgent(agent_id="",password=""):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT * from agentData where agentId=? and password=?",agent_id,password)
    r=cur.fetchone()
    if(r['agent_id']==agent_id and r['password']==password):
        print("LOGGED IN!")
    conn.close()
    

# FLASK API 
@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()

