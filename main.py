import os
from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
# from AddBook import *
# from DeleteBook import *
# from ViewBooks import *
# from IssueBook import *
from dotenv import load_dotenv
# extras
from init import get_cursor

con = get_cursor()
cor = con.cursor()

print("Great success!")
