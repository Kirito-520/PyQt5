import sys 
from PyQt5.QtWidgets import QApplication, QLabel, QWidget 

class MyWnd(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel("这是文字！！")
        label.setStyleSheet("font-size:30px;color:red")
        label.setParent(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWnd()
    w.setWindowTitle("qwidget")
    w.show()

    app.exec()