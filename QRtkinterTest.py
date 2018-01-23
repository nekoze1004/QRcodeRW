from tkinter import *
import cv2, datetime, os


# 初期化？　保存先と探索先が無いなら作る
def initialize():
    if not (os.path.exists("./result")):
        os.mkdir("./result")


# ファイルの保存を行う関数
def fileWrite(img):
    today = datetime.datetime.today()
    print(today.strftime("%Y%m%d%H%M%S"))
    imgName = "./result/" + today.strftime("%Y%m%d%H%M%S")
    cv2.imwrite(imgName + ".png", img)


def captchaVideo():
    cap = cv2.VideoCapture(0)

    cv2.namedWindow("capVideo", cv2.WINDOW_AUTOSIZE)

    while True:
        ret, image = cap.read()

        if ret == False:
            continue

        cv2.imshow("capVideo", image)

        k = cv2.waitKey(33)

        if k == ord("s"):
            fileWrite(image)
        elif k >= 0:
            break

    cv2.destroyAllWindows()


def mainWIndow():
    root = Tk()
    root.title("QRcodeRW")
    root.readprofile(0, 0)
    root.geometry("400x300+10+10")

    cameraButton = Button(root, text="カメラ", command=captchaVideo)
    cameraButton.pack()

    root.mainloop()


if __name__ == "__main__":
    initialize()
    mainWIndow()
