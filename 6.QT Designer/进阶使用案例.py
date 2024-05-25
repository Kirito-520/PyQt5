import sys

from PyQt5.QtWidgets import * 
from PyQt5 import uic


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("E://学习/pyqt5/qt-designer/login.ui")
        #print(self.ui.__dict__)

        # 提取要操作的控件
        self.user_name_qwidget = self.ui.lineEdit 
        self.user_password_qwidget = self.ui.lineEdit_2
        self.login_btn = self.ui.pushButton 
        self.forget_password = self.ui.pushButton_2 
        self.textBrowser = self.ui.textBrowser 

        # 绑定信号与槽函数
        self.login_btn.clicked.connect(self.login)

    def login(self):
        user_name = self.user_name_qwidget.text()
        password = self.user_password_qwidget.text()
        if user_name == "admin" and password == "123456":
            self.textBrowser.setText("欢迎 %s" % user_name)
            self.textBrowser.repaint()
        else:
            self.textBrowser.setText("用户名或密码错误...请重试")
            self.textBrowser.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    app.exec()