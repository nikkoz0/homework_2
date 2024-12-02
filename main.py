import sys
from random import randint
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic


class Homework(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        uic.loadUi('homework_2.ui', self)
        self.pushButton.clicked.connect(self.push)

    def push(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(QColor(255, 255, 0))
            r = randint(1, 200)
            painter.drawEllipse(200, 60, r, r)
            r_1 = randint(1, 200)
            painter.drawEllipse(400, 60, r_1, r_1)
            painter.end()
        self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    play = Homework()
    play.show()
    sys.exit(app.exec())
