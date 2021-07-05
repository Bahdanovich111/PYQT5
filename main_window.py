import sys, datetime, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton
import parsing


class Ui_Form(QWidget):
    def setupUi(self, Pogoda):
        # Pogoda.setObjectName("ПОГОДА")
        Pogoda.resize(1400, 900)
        Pogoda.setStyleSheet("background-color: #FFDEAD")
        # self.date = QtWidgets.QLabel(Pogoda)
        # self.date.setGeometry(QtCore.QRect(420, 29, 341, 71))
        # self.date.setStyleSheet("color: #e0bd3f;\n"
        #                          "font: 26pt \"MS Shell Dlg 2\";\n"
        #                          "font: 28pt \"MS Shell Dlg 2\";\n"
        #                          "background-color: #b0e0e6;\n"
        #                          "border: none\n"
        #                          "")
        # self.label.setWordWrap(False)
        # self.label.setObjectName("label")
        self.gismet_value = QtWidgets.QLabel(Pogoda)
        self.gismet_value.setGeometry(QtCore.QRect(380, 240, 720, 71))
        self.gismet_value.setStyleSheet("color: #e0bd3f;"
                                        # "font: 10pt \"MS Shell Dlg 2\";\n"
                                        "font: 28pt \"MS Shell Dlg 2\";\n"
                                        "background-color: #b0e0e6;"
                                        "border: 4px solid orange;\n"
                                        "border-radius:30px;"
                                        "")
        self.gismet = QtWidgets.QLabel(Pogoda)
        self.gismet.setGeometry(QtCore.QRect(50, 240, 250, 71))
        self.gismet.setStyleSheet("color: #e0bd3f;"
                                  # "font: 26pt \"MS Shell Dlg 2\";\n"
                                  "font: 28pt;"
                                  "background-color: #b0e0e6;"
                                  "border: none"
                                  "")
        # self.label_2.setWordWrap(False)
        # self.label_2.setObjectName("label_2")
        self.yandex_value = QtWidgets.QLabel(Pogoda)
        self.yandex_value.setGeometry(QtCore.QRect(380, 400, 720, 71))
        self.yandex_value.setStyleSheet("color: #e0bd3f;"
                                        "font: 28pt \"MS Shell Dlg 2\"\"center\";\n"
                                        "background-color: #b0e0e6;"
                                        "border: 4px solid orange;\n"
                                        "border-radius:30px;"
                                        "")
        self.yandex = QtWidgets.QLabel(Pogoda)
        self.yandex.setGeometry(QtCore.QRect(50, 400, 250, 71))
        self.yandex.setStyleSheet("color: #e0bd3f;\n"
                                  "font: 26pt \"MS Shell Dlg 2\";\n"
                                  "font: 28pt \"MS Shell Dlg 2\"\"center\";\n"
                                  "background-color: #b0e0e6;\n"
                                  "border: none\n"
                                  "")
        self.pogoda_value = QtWidgets.QLabel(Pogoda)
        self.pogoda_value.setGeometry(QtCore.QRect(380, 560, 720, 71))
        self.pogoda_value.setStyleSheet("color: #e0bd3f;\n"
                                        "font: 26pt \"MS Shell Dlg 2\";\n"
                                        "font: 28pt \"MS Shell Dlg 2\"\"center\";\n"
                                        "background-color: #b0e0e6;\n"
                                        "border: 4px solid orange;\n"
                                        "border-radius:30px;"
                                        "")
        self.pogoda = QtWidgets.QLabel(Pogoda)
        self.pogoda.setGeometry(QtCore.QRect(50, 560, 250, 71))
        self.pogoda.setStyleSheet("color: #e0bd3f;\n"
                                  "font: 26pt \"MS Shell Dlg 2\";\n"
                                  "font: 28pt \"MS Shell Dlg 2\"\"center\";\n"
                                  "background-color: #b0e0e6;\n"
                                  "border: none\n"
                                  "")

        # self.label_3.setWordWrap(False)
        # self.label_3.setObjectName("label_3")
        self.sity = QtWidgets.QLabel(Pogoda)
        self.sity.setGeometry(QtCore.QRect(530, 140, 341, 71))
        self.sity.setStyleSheet("color: #e0bd3f;\n"
                                "font: 26pt \"MS Shell Dlg 2\";\n"
                                "font: 28pt \"MS Shell Dlg 2\";\n"
                                "background-color: #b0e0e6;\n"
                                "border-radius:30px;"
                                "")

        self.dateEdit = QtWidgets.QDateEdit(Pogoda)
        self.dateEdit.setGeometry(QtCore.QRect(575, 29, 250, 50))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setStyleSheet("font: 25pt;")
        # self.label_4.setWordWrap(False)
        # self.sity.setObjectName("label_4")

        self.retranslateUi(Pogoda)
        # makeRequest()
        QtCore.QMetaObject.connectSlotsByName(Pogoda)

    def retranslateUi(self, Pogoda):
        _translate = QtCore.QCoreApplication.translate
        Pogoda.setWindowTitle(_translate("Form", "Погода"))
        # date = datetime.date.today()
        # self.date.setText(_translate("Form", f"   {datetime.date.today()}"))
        rt = (parsing.makeRequest())
        self.gismet_value.setText(
            _translate("Form", f"{rt[0]}°C  ветер:{rt[1][0]}  влажность:{rt[2]}"))  # вытянуть gis_
        self.gismet_value.adjustSize()
        self.pogoda_value.setText(_translate("Form", f"{rt[3][0]}°C  ветер:{rt[4][0]}  влажность:{rt[5][0]} "))
        self.pogoda_value.adjustSize()
        # rt = parsing.makeRequest()
        print(rt)
        # self.label_2.setText()
        self.gismet.setText(_translate("Form", "GISMETIO"))
        self.yandex_value.setText(_translate("Form", f"{rt[6]}°C  ветер:{rt[7]}м/с  влажность:{rt[8]}"))
        self.yandex_value.adjustSize()
        self.yandex.setText(_translate("Form", "YANDEX.BY"))
        self.pogoda.setText(_translate("Form", "POGODA.BY"))
        self.sity.setText(_translate("Form", "****минск****"))

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     Pogoda = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Pogoda)
#     Pogoda.show()
#
#
#     sys.exit(app.exec_())
# def pusk():
# app = QtWidgets.QApplication(sys.argv)
# Pogoda = QtWidgets.QWidget()
# ui = Ui_Form()
# ui.setupUi(Pogoda)
# Pogoda.show()
# sys.exit(app.exec_())
