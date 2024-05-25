import sys 
import os 
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = uic.loadUi("E:/学习/pyqt5/qt-designer/qt_designer_demo.ui")
    ui.show()
    app.exec()