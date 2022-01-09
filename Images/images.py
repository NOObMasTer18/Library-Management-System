from pathlib import Path
import random

def getLibImage() -> Path:
    file_dir = Path(__file__).absolute().parent
    imagepaths = sorted(Path(file_dir).glob("*.jpeg"))

    chosed_path :Path = random.choice(imagepaths)
    
    return chosed_path

if __name__ == "__main__":
    x = getLibImage()
    print(x)
    
