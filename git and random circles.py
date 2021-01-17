import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame
from PyQt5.QtGui import QColor, QPainter
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 700, 700)
        self.draw_button = QPushButton('Нарисовать\nокружность', self)
        self.draw_button.setStyleSheet(
            'background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.99005, y2:0.972, stop:0.129353 rgba(167, 124, 217, 255), stop:1 rgba(255, 255, 255, 255));font: italic 14pt "Palatino Linotype";')
        self.draw_button.move(240, 620)
        self.draw_button.resize(161, 61)
        self.draw_button.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        self.x, self.y = int(self.width()), int(self.height())
        self.radius = randint(0, int((self.x + self.y) / 4))
        self.color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        qp.setBrush(self.color)
        qp.drawEllipse(randint(0, int(self.x / 2)), randint(0, int(self.y / 2)),
                       self.radius, self.radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())