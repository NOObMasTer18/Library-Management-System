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
root.geometry("650x500")

#setting image background
img,root = set_backgroundImage(root) 
    #img is returned bc it is a local variable used by mainloop. 
    #Meanwhile, img gets redundant as python garbage collects it, on function end.

#frame
headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.14)
headingLabel = Label(headingFrame1, text="Welcome to \n Kv6-Jaipur Library Portal", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

root.mainloop() #run tkinter