from pyzbar.pyzbar import decode
from PIL import Image
import webbrowser
import tkinter.filedialog
import cv2
import os


def fileSelect():
    fType = [("*.jpg", "*.png")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    fileName = tkinter.filedialog.askopenfile(filetypes=fType, initialdir=iDir)
    return fileName


if __name__ == "__main__":
    imgPath = fileSelect()
    print(imgPath.name)
    img = cv2.imread(imgPath.name)
    data = decode(img)

    try:
        if data[0][0][:4].decode("utf-8") == "http":
            url = data[0][0].decode("utf-8")
            webbrowser.open(url)
    except UnicodeDecodeError:
        print(data[0][0].decode("utf-8"))
