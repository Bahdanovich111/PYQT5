import sys, datetime, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton
import parsing


class Ui_Form(QWidget):
    def setupUi(self, Pogoda):
        # Pogoda.setObjectName("ПОГОДА")
        Pogoda.resize(750, 650)
        Pogoda.setStyleSheet("background-color: #FFDEAD")
        self.label = QtWidgets.QLabel(Pogoda)
        self.label.setGeometry(QtCore.QRect(210, 29, 341, 71))
        self.label.setStyleSheet("color: #e0bd3f;\n"
                                 "font: 26pt \"MS Shell Dlg 2\";\n"
                                 "font: 28pt \"MS Shell Dlg 2\";\n"
                                 "background-color: #1d1c21;\n"
                                 "border: none\n"
                                 "")
        # self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Pogoda)
        self.label_2.setGeometry(QtCore.QRect(100, 140, 585, 71))
        self.label_2.setStyleSheet("color: #e0bd3f;\n"
                                   "font: 26pt \"MS Shell Dlg 2\";\n"
                                   "font: 28pt \"MS Shell Dlg 2\";\n"
                                   "background-color: #1d1c21;\n"
                                   "border: none\n"
                                   "")
        # self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Pogoda)
        self.label_3.setGeometry(QtCore.QRect(100, 300, 585, 71))
        self.label_3.setStyleSheet("color: #e0bd3f;\n"
                                   "font: 26pt \"MS Shell Dlg 2\";\n"
                                   "font: 28pt \"MS Shell Dlg 2\"\"center\";\n"
                                   "background-color: #1d1c21;\n"
                                   "border: none\n"
                                   "")
        # self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Pogoda)
        self.label_4.setGeometry(QtCore.QRect(220, 510, 321, 61))
        self.label_4.setStyleSheet("color: #e0bd3f;\n"
                                   "font: 26pt \"MS Shell Dlg 2\";\n"
                                   "font: 28pt \"MS Shell Dlg 2\";\n"
                                   "background-color: #1d1c21;\n"
                                   "border: none\n"
                                   "")
        # self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Pogoda)
        # makeRequest()
        QtCore.QMetaObject.connectSlotsByName(Pogoda)

    def retranslateUi(self, Pogoda):
        _translate = QtCore.QCoreApplication.translate
        Pogoda.setWindowTitle(_translate("Form", "Погода"))
        # date = datetime.date.today()
        self.label.setText(_translate("Form", f"   {datetime.date.today()}"))
        rt = (parsing.makeRequest())
        self.label_2.setText(_translate("Form", f"Температура сейчас:{rt}"))  # вытянуть gis_
        # rt = parsing.makeRequest()
        # print(rt)
        # self.label_2.setText()
        self.label_3.setText(_translate("Form", "           GISMETIO"))
        self.label_4.setText(_translate("Form", "      минск"))


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     Pogoda = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Pogoda)
#     Pogoda.show()
#
#
#     sys.exit(app.exec_())
#def pusk():
    # app = QtWidgets.QApplication(sys.argv)
    # Pogoda = QtWidgets.QWidget()
    # ui = Ui_Form()
    # ui.setupUi(Pogoda)
    # Pogoda.show()
    # sys.exit(app.exec_())



