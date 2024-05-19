import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("计算器")

        # 准备数据 
        data = {
            0: ["7", "8", "9", "+", "("],
            1: ["4", "5", "6", "-", ")"],
            2: ["1", "2", "3", "*", "<-"],
            3: ["0", ".", "=", "/", "C"]
        }

        layout = QVBoxLayout()

        edit = QLineEdit()
        edit.setPlaceholderText("请输入内容：")
        layout.addWidget(edit)

        grid = QGridLayout()

        # 循环创建追加进去
        for line_number, line_data in data.items():
            for col_number, number in enumerate(line_data):
                btn = QPushButton(number)
                grid.addWidget(btn, line_number, col_number)

        # 把网格布局追加到容器中
        layout.addLayout(grid)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()