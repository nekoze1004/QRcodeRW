from tkinter import *
from pyzbar.pyzbar import decode
import webbrowser, os, sys, cv2, qrcode, tkinter.filedialog


# 初期化？　保存先と探索先が無いなら作る
def initialize():
    if not (os.path.exists("./result")):
        os.mkdir("./result")


def mainWindow():
    def start_Button():
        print(radioButtonVal.get())
        if radioButtonVal.get() == 0:
            consoleText.set("Read")
        elif radioButtonVal.get() == 1:
            consoleText.set("Write")
        else:
            consoleText.set("うんこ")

    def changeConsoleText(event):
        text = consoleText.get()
        consoleCanvas.coords(cID, text)

    root = Tk()
    root.title("QRcodeRW")
    root.readprofile(0, 0)
    root.geometry("400x300+10+10")

    radioButtonVal = IntVar()
    radioButtonVal.set(99)
    consoleText = StringVar()
    consoleText.set("")

    titleLabel = Label(root, text="QRコードReader＆Writer", font=("", 15))
    R_rButton = Radiobutton(root, text="読み込む", variable=radioButtonVal, value=0)
    W_rButton = Radiobutton(root, text="書き出す", variable=radioButtonVal, value=1)
    startButton = Button(root, text="開始", command=start_Button)
    previewCanvas = Canvas(root, width=128, height=128)
    previewCanvas.create_rectangle(0, 0, 128, 128, fill='green')
    consoleCanvas = Canvas(root, width=370, height=130)
    consoleCanvas.create_rectangle(0, 0, 370, 130, fill="red")
    # ここ2行がわからない consoleCanvas内のTextを変えたい
    cID = consoleCanvas.create_text(10, 10)
    consoleCanvas.tag_bind(cID, '<Return>', changeConsoleText)

    titleLabel.place(x=10, y=20)
    R_rButton.place(x=10, y=50)
    W_rButton.place(x=10, y=70)
    startButton.place(x=150, y=70)
    previewCanvas.place(x=250, y=20)
    consoleCanvas.place(x=10, y=160)

    root.mainloop()


if __name__ == "__main__":
    initialize()
    mainWindow()
