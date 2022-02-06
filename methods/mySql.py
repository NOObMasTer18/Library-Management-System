from dotenv import load_dotenv
import pymysql
import os



# environment variables
load_dotenv()
user = os.getenv("User")
dbPassword = os.getenv("Password")
host = os.getenv("Host")
myDatabase=os.getenv("myDatabase")
table1 = os.getenv("table1")
table2 = os.getenv("table2")

#Constructs 
def get_connection() ->  pymysql.connect:
    connection = pymysql.connect(
        host=host,
        user=user,
        password=dbPassword,
    )
    
    return connection

def get_connectionAndCursor() -> tuple[pymysql.connect.cursor,pymysql.connect]:
    connection = get_connection()
    connection.ping()
    cursor = connection.cursor()
    cursor.execute(f"use {myDatabase};")
    return connection,cursor

def initialize():
    """Initializes database and tables by checking and
    creating database and tables if not existed already."""
    
    hasmyDatabase = False
    hastable1 = False
    hastable2 = False

    connection,cursor = get_connectionAndCursor()
    
    cursor.execute("show databases;")
    result=cursor.fetchall()
    print(result)
    for x in range(len(result)):
        if myDatabase is not None:
            if myDatabase in result[x]:
                
                hasmyDatabase = True
                print(f"Database named {myDatabase} found!")
                break
    if hasmyDatabase:
        cursor.execute(f"use {myDatabase};")
        cursor.execute(f"show tables;")
        result = cursor.fetchall()
        for x in range(len(result)):
            if table1 in result[x]:
                hastable1 = True
                print(f"table named {table1} found!")
            if table2 in result[x]:
                hastable2 = True 
                print(f"table named {table2} found!")

    if not hasmyDatabase:
        print("creating database...")
        cursor.execute(f"create database {myDatabase};")
        print(f"database {myDatabase} created.")
    cursor.execute(f"use {myDatabase}")
    if not hastable1:
        print("creating table...")
        cursor.execute(f"create table {table1}(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));")
        print(f"table {table1} created.")
    if not hastable2:
        print("creating table...")
        cursor.execute(f"create table {table2}(bid varchar(20) primary key, issuedto varchar(30));")
        print(f"table {table2} created.")

if __name__ == "__main__":
    connection,cursor = get_connectionAndCursor()
    cursor.execute("select version()")
    for x in cursor:
        print(f"Connected successfully with MySql{x}!")

