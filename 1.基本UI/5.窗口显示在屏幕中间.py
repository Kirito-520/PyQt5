import sys 

from PyQt5.QtWidgets import QApplication , QWidget, QDesktopWidget

if __name__  == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("第一个PyQt5")

    w.resize(300, 300)

    # 调整窗口在屏幕中央显示
    center_pointer = QDesktopWidget().availableGeometry().center()
    x = center_pointer.x()
    y = center_pointer.y()
    print(w.frameGeometry())
    print(w.frameGeometry().getRect())
    print(type(w.frameGeometry().getRect()))
    old_x, old_y, width, height = w.frameGeometry().getRect()
    w.move(x - width / 2 , y - height / 2)

    w.show()

    app.exec()

