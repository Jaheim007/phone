import sys 
from PyQt5.QtWidgets import QMainWindow, QApplication
from Widget.command import AccountPage_Phone

 
def main():
    app = QApplication(sys.argv)
    home = AccountPage_Phone()
    home.show()
    app.exec_()


if __name__ == '__main__':
    main()

