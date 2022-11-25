import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow


class Okr(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Git и желтые окружности')
        self.pushButton.clicked.connect(self.yell)

    def yell(self):
        self.repaint()

    def paintEvent(self, event):
        self.do_paint = True
        qp = QPainter()
        qp.begin(self)
        c = QColor(255,255,0)
        qp.setBrush(c)
        s = random.randint(16, 100)
        qp.drawEllipse(random.randint(0, self.size().width()) - (s // 2), random.randint(0, self.size().height()) - (s // 2), s, s)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Okr()
    ex.show()
    sys.exit(app.exec())