# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'phone.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(832, 657)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.background_img = QLabel(self.centralwidget)
        self.background_img.setObjectName(u"background_img")
        self.background_img.setGeometry(QRect(-10, 0, 861, 661))
        self.background_img.setPixmap(QPixmap(u":/images/Static/abstract_background_with_modern_gradient-01_4x.webp"))
        self.background_img.setScaledContents(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 120, 191, 61))
        self.label.setStyleSheet(u"font: 17pt \"Avenir\";\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 240, 191, 61))
        self.label_2.setStyleSheet(u"font: 17pt \"Avenir\";\n"
"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 350, 191, 61))
        self.label_3.setStyleSheet(u"font: 17pt \"Avenir\";\n"
"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 30, 181, 71))
        self.label_4.setStyleSheet(u"font: 25 20pt \"Avenir\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.nom_line = QLineEdit(self.centralwidget)
        self.nom_line.setObjectName(u"nom_line")
        self.nom_line.setGeometry(QRect(200, 170, 381, 41))
        self.number_line = QLineEdit(self.centralwidget)
        self.number_line.setObjectName(u"number_line")
        self.number_line.setGeometry(QRect(200, 400, 381, 41))
        self.prenom_line = QLineEdit(self.centralwidget)
        self.prenom_line.setObjectName(u"prenom_line")
        self.prenom_line.setGeometry(QRect(200, 290, 381, 41))
        self.valide_btn = QPushButton(self.centralwidget)
        self.valide_btn.setObjectName(u"valide_btn")
        self.valide_btn.setGeometry(QRect(310, 480, 121, 51))
        self.valide_btn.setStyleSheet(u"background-color: #2B60DE;\n"
"font: 16pt \"Avenir\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.valide_btn.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.valide_btn.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.background_img.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Nom</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Prenom</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Num\u00e9ro de t\u00e9l\u00e9phone</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Information</span></p></body></html>", None))
        self.valide_btn.setText(QCoreApplication.translate("MainWindow", u"Valide", None))
    # retranslateUi

