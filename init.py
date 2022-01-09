from tkinter import *
from dotenv import load_dotenv
import pymysql
import os


# environment variables
load_dotenv()
mysqldbPassword = os.getenv("Password")
mydatabase="kv6library"


def get_cursor() ->  pymysql.connect:
    con = pymysql.connect(host="localhost",user="root",password=mysqldbPassword,database=mydatabase)
    
    return con