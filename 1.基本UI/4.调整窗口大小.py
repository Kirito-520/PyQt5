import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("第一个PyQt5")

    # 窗口大小
    w.resize(300, 300)

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()