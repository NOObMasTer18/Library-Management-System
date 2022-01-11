import random
from tkinter import Canvas, Tk,PhotoImage
from pathlib import Path
from PIL import Image,ImageTk

def getLibImage() -> Path:
    file_dir = Path(__file__).absolute().parent
    imagepaths = sorted(Path(file_dir).glob("*.jpeg"))

    chosed_path :Path = random.choice(imagepaths)
    
    return chosed_path

def set_backgroundImage(root: Tk) -> tuple[PhotoImage,Tk]:
    # background image
    imgPath = getLibImage()
    same=True
    n=0.25
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
    return img,root



if __name__ == "__main__":
    x = getLibImage()
    print(x)
    
