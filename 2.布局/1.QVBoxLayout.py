import sys 
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QGroupBox, QMainWindow
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(300, 300)
        self.setWindowTitle("垂直布局")

        # 垂直布局
        layout = QVBoxLayout()

        # 按钮1
        layout.addStretch(1)
        btn1 = QPushButton("按钮1")
        layout.addWidget(btn1)

        # 按钮2
        layout.addStretch(1)
        btn2 = QPushButton("按钮2")
        layout.addWidget(btn2)

        # 按钮3
        layout.addStretch(1)
        btn3 = QPushButton("按钮3")
        layout.addWidget(btn3)

        layout.addStretch(2)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    w = MyWindow()
    w.show()

    app.exec()


