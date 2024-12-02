import sys
from random import randint
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPainter, QColor
from homework_3 import Ui_MainWindow


class Homework(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.pushButton.clicked.connect(self.push)

    def push(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            r = randint(1, 200)
            painter.drawEllipse(200, 60, r, r)
            r_1 = randint(1, 200)
            painter.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            painter.drawEllipse(400, 60, r_1, r_1)
            painter.end()
        self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    play = Homework()
    play.show()
    sys.exit(app.exec())
