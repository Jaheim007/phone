from tkinter import messagebox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem, QAbstractItemView, QMessageBox
from Widget.phone import Ui_MainWindow
import sqlite3
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient

class AccountPage_Phone(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.valide_btn.clicked.connect(self.database)
        
    def database(self):       
        db = sqlite3.connect("phonedata.db")
        dictornary = {
            "nom": self.nom_line.text(),
            "prenom": self.prenom_line.text(),
            "phone_number":self.number_line.text()
        }
        if self.nom_line.text() == "" or self.prenom_line.text() == "" or self.number_line.text() =="":    
            QMessageBox.warning(self, "Error", "Veuillez saisir vos infomations")
            
        else:            
            data = db.cursor()
            data.execute("""CREATE TABLE IF NOT EXISTS Phonedata(
                            nom text, 
                            prenom text,
                            phone_number text
                        )""")
            data.execute("INSERT INTO Phonedata VALUES (:nom, :prenom, :phone_number)", dictornary)
            db.commit()
            db.close()
            
            # auth_user_name = 'ACdcfbf10879c8edc8a3668e785ff1adac'
            # auth_password = '0941c1842c353b04fcb722507c2365f4'
            # use_hmac_authentication = False

            # client = MessageMediaMessagesClient(auth_user_name, auth_password, use_hmac_authentication)
            # messages_client = client.messages

            # body_value = {
            #     "messages":[
            #         {
            #             "content":"My first message",
            #             "destination_number": self.number_line.text() 
            #         }
            #     ]
            # }

            # body = body_value

            # result = messages_client.send_messages(body)
            
            self.nom_line.clear()
            self.prenom_line.clear()
            self.number_line.clear()
        