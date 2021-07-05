from main_window import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("погода.png"))
        self.label.move(0, 0)

        self.setGeometry(500, 100, 900, 800)
        self.setWindowTitle('Погода')

        self.ok_button = QPushButton('weather', self)
        self.ok_button.move(350, 700)
        self.ok_button.setFixedSize(200, 50)
        self.ok_button.clicked.connect(self.pus)
        self.show()


    def pus(self):
        #app = QtWidgets.QApplication(sys.argv)
        global Pogoda
        Pogoda = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Pogoda)
        ex.close()
        Pogoda.show()
        #sys.exit(app.exec_())

        # self.setWindowIcon(QIcon('terminate.png'))
    # def tre(self):
    #     print('clicked')



    # def makeRequest(self):
    #     return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
