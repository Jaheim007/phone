# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/phone.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 657)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_img = QtWidgets.QLabel(self.centralwidget)
        self.background_img.setGeometry(QtCore.QRect(-10, 0, 861, 661))
        self.background_img.setText("")
        self.background_img.setPixmap(QtGui.QPixmap(":/images/Static/abstract_background_with_modern_gradient-01_4x.webp"))
        self.background_img.setScaledContents(True)
        self.background_img.setObjectName("background_img")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 120, 191, 61))
        self.label.setStyleSheet("font: 17pt \"Avenir\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 240, 191, 61))
        self.label_2.setStyleSheet("font: 17pt \"Avenir\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 350, 191, 61))
        self.label_3.setStyleSheet("font: 17pt \"Avenir\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 30, 181, 71))
        self.label_4.setStyleSheet("font: 25 20pt \"Avenir\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.nom_line = QtWidgets.QLineEdit(self.centralwidget)
        self.nom_line.setGeometry(QtCore.QRect(200, 170, 381, 41))
        self.nom_line.setObjectName("nom_line")
        self.number_line = QtWidgets.QLineEdit(self.centralwidget)
        self.number_line.setGeometry(QtCore.QRect(200, 400, 381, 41))
        self.number_line.setObjectName("number_line")
        self.prenom_line = QtWidgets.QLineEdit(self.centralwidget)
        self.prenom_line.setGeometry(QtCore.QRect(200, 290, 381, 41))
        self.prenom_line.setObjectName("prenom_line")
        self.valide_btn = QtWidgets.QPushButton(self.centralwidget)
        self.valide_btn.setGeometry(QtCore.QRect(310, 480, 121, 51))
        self.valide_btn.setStyleSheet("background-color: #2B60DE;\n"
"font: 16pt \"Avenir\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.valide_btn.setDefault(True)
        self.valide_btn.setFlat(False)
        self.valide_btn.setObjectName("valide_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">Nom</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">Prenom</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">Num??ro de t??l??phone</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Information</span></p></body></html>"))
        self.valide_btn.setText(_translate("MainWindow", "Valide"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
