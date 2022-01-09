from tkinter import *
from dotenv import load_dotenv
import pymysql
import os


# environment variables
load_dotenv()
mysqldbPassword = os.getenv("Password")
mydatabase="kv6library"


# functions
def get_connection() ->  pymysql.connect:
    connection = pymysql.connect(host="localhost",user="root",password=mysqldbPassword,database=mydatabase)
    
    return connection

def get_cursor() -> pymysql.connect.cursor:
    connection = get_connection()
    connection.ping()
    cursor = connection.cursor()
    return cursor


# Check
if __name__ == "__main__":
    cursor = get_cursor()
    cursor.execute("select version()")
    for x in cursor:
        print(f"Connected successfully with MySql{x}!")