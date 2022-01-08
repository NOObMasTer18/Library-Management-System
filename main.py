import os
from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
# import pymysql
# from AddBook import *
# from DeleteBook import *
# from ViewBooks import *
# from IssueBook import *
from dotenv import load_dotenv
# Add your own database name and password here to reflect in the code
load_dotenv()

mysqldbPassword = os.getenv("Password")
print(mysqldbPassword)

#ho gya kya ?