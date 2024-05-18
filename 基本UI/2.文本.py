import sys 

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

if __name__  == "__main__":
    app = QApplication(sys.argv)

    # 设置窗口标题
    w = QWidget()

    w.setWindowTitle("第一个PyQt")

    # 下面创建一个Label（纯文本），在创建的时候指定父对象
    label = QLabel("账号: ")
    label.setParent(w)

    # 显示位置与大小：x,y,w,h
    label.setGeometry(20, 20, 30, 30)

    w.show()

    app.exec()