# Starters
from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
from pathlib import Path
# from methods.AddBook import *
# from methods.DeleteBook import *
# from methods.ViewBooks import *
# from methods.IssueBook import *
#extras
from Images.images import set_backgroundImage,getLibImage

#init
from init import get_cursor



cursor = get_cursor()


# intializing tkinter
root = Tk()
root.title("Library")
root.minsize(width=400,height=400) 
root.geometry("600x500")

imgPath = getLibImage()
same=True
n=0.25
# Adding a background image
background_image =Image.open(imgPath)
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 

img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill="both")


root.mainloop() #run tkinter