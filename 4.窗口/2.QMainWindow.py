import sys 
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel("这是文字")
        label.setStyleSheet("font-size:30px;color:red")

        # 调用父类的menubar，从而对菜单栏进行操作
        menu = self.menuBar()
        menu.setNativeMenuBar(False)

        file_menu = menu.addMenu("文件")
        file_menu.addAction("新建")
        file_menu.addAction("打开")
        file_menu.addAction("保存")

        edit_menu = menu.addMenu("编辑")
        edit_menu.addAction("复制")
        edit_menu.addAction("粘贴")
        edit_menu.addAction("剪切")

        # 设置中心内容设置
        self.setCentralWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.setWindowTitle("我是窗口标题")
    w.show()

    app.exec()