from tkinter import *
from pyzbar.pyzbar import decode
import webbrowser, os, sys, cv2, qrcode, tkinter.filedialog




# 初期化？　保存先と探索先が無いなら作る
def initialize():
    if not (os.path.exists("./result")):
        os.mkdir("./result")


def start_Button():
        pass


def mainWindow():
    root = Tk()
    root.title("QRcodeRW")
    root.readprofile(0, 0)
    root.geometry("400x300+10+10")

    radioButtonVal = IntVar()
    radioButtonVal.set(99)

    titleLabel = Label(root, text="QRコードReader＆Writer", font=("", 15))
    R_rButton = Radiobutton(root, text="読み込む", variable=radioButtonVal, value=0)
    W_rButton = Radiobutton(root, text="書き出す", variable=radioButtonVal, value=1)
    startButton = Button(root, text="開始", command=start_Button)

    titleLabel.place(x=10, y=20)
    R_rButton.place(x=10, y=50)
    W_rButton.place(x=10, y=70)
    startButton.place(x=150, y=70)

    root.mainloop()


if __name__ == "__main__":
    initialize()
    mainWindow()
