from tkinter import *

from methods.AddBook import *
from methods.DeleteBook import *
from methods.ViewBooks import *
from methods.IssueBook import *
from methods.ReturnBook import *

from methods.Images.images import set_backgroundImage


# intializing tkinter
root = Tk()
root.title("Library")
root.minsize(width=400,height=400) 
root.geometry("650x500")

#setting image background
img,root = set_backgroundImage(root) 
    #img is returned bc it is a local variable used by mainloop. 
    #Meanwhile, img gets redundant (if not returned) as python garbage collects it, on function end.

#Heading
headingFrame = Frame(root, bg="#f42f20",bd=5)
headingFrame.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.14)

headingLabel = Label(
    headingFrame, 
    text="Welcome to \n Kv6-Jaipur Library Portal", 
    bg='black', 
    fg='white', 
    font=('Courier',15)
    )
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

#buttons
btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop() #run tkinter
