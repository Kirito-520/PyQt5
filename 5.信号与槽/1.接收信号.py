import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 改变当前的widget的宽和高
        self.resize(500, 300)
        # 创建爱一个按钮
        btn = QPushButton("点我点我", self)
        # 设置窗口的位置、宽高
        btn.setGeometry(200, 200, 100, 30)
        # 将按钮被点击时触发信号与我们定义的函数进行绑定
        btn.clicked.connect(self.click_my_btn)

    def click_my_btn(self, arg):
        # 槽函数，点击按钮则调用该函数
        # 这里的参数正好是信号发送时传递的参数
        print("你点击了按钮！", arg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()

    app.exec()