import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget 

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()

    w.setWindowTitle("This is my icon")

    # 设置图标
    w.setWindowIcon(QIcon("pyqt5/icon/icon1.jpg"))

    w.show()
    
    # 运行循环
    app.exec()