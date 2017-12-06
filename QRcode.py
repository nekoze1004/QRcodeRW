from pyzbar.pyzbar import decode
import webbrowser, os, sys, cv2, qrcode, tkinter.filedialog


# QRコードをGUIで選択する
def fileSelect():
    fileType = [("*.jpg", "*.png")]
    initialDir = os.path.abspath(os.path.dirname(__file__) + "/result")
    fileName = tkinter.filedialog.askopenfile(filetypes=fileType, initialdir=initialDir)
    return fileName


# QRコードを読み込む
def readQR():
    imgPath = fileSelect()
    try:
        img = cv2.imread(imgPath.name)
        data = decode(img)
        print(data[0][0].decode("utf-8"))
        try:
            # 文字の先頭4文字がhttpならURLとして処理する
            if data[0][0][:4].decode("utf-8") == "http":
                url = data[0][0].decode("utf-8")
                # webブラウザで開く
                webbrowser.open(url)
        except UnicodeDecodeError:  # URLでなければ、なにもしない
            pass
    except AttributeError:
        # 画像が読み込めないエラーが発生したら
        print("画像が見つかりませんでした")


# 入力された文字に応じてQRコードを生成する
def writeQR():
    print("QRコードにしたい文字列を入力")
    qrStr = input(">>> ")
    QR = qrcode.make(qrStr)
    # QRコードのファイル名を決める
    fileName = URL2FileName(qrStr)
    print(fileName)
    QR.save("result/" + fileName + ".png")
    QR.show()


def URL2FileName(str):
    result = str.replace("\\", "").replace("/", "_").replace("*", "") \
        .replace(":", "").replace("?", "").replace("\"", "") \
        .replace("<", "").replace(">", "").replace("|", "")
    return result


def isR(str):
    if str == "r":
        return 0
    elif str == "R":
        return 0
    elif str == "w":
        return 1
    elif str == "W":
        return 1
    elif str == "e":
        return 3
    else:
        return 4


if __name__ == "__main__":
    while True:
        print("QRコード、読むか書くか R or W")
        rw = input(">>> ")
        if isR(rw) == 0:
            readQR()
        elif isR(rw) == 1:
            writeQR()
        elif isR(rw) == 3:
            sys.exit()
