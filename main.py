# Starters
from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
from pathlib import Path
# from methods.AddBook import *
# from methods.DeleteBook import *
# from methods.ViewBooks import *
# from methods.IssueBook import *
#extras
from Images.images import set_backgroundImage

#init
from init import get_cursor


cursor = get_cursor()

# intializing tkinter
root = Tk()
root.title("Library")
root.minsize(width=400,height=400) 
root.geometry("600x500")

#setting image background
img,root = set_backgroundImage(root) 
    #img is returned bc it is a local variable used by mainloop. 
    #Meanwhile img gets redundant as python garbage collects it on function end.

root.mainloop() #run tkinter