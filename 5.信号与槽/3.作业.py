import sys
from PyQt5.QtWidgets import QApplication, QDial, QSpinBox, QWidget, QHBoxLayout, QVBoxLayout 
from PyQt5.QtCore import pyqtSignal 

class MyWindow(QWidget):
    my_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500, 300)

        container = QHBoxLayout()

        v_layout = QVBoxLayout()
        self.qdial = QDial(self) 
        self.qdial.setRange(0, 100)
        self.qdial.setNotchesVisible(True) # 显示刻度
        self.qdial.valueChanged.connect(self.onDialValueChanged)
        v_layout.addWidget(self.qdial)


        v_layout2 = QVBoxLayout()
        self.spinbox = QSpinBox(self)
        self.spinbox.valueChanged.connect(self.onSpinValueChanged)
        v_layout2.addWidget(self.spinbox)
       

        container.addLayout(v_layout)
        container.addLayout(v_layout2)

        self.setLayout(container)

    def onDialValueChanged(self, value):
        self.spinbox.setValue(value)

    def onSpinValueChanged(self,value):
        self.qdial.setValue(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()

    app.exec()