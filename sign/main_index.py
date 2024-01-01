import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_main_2 import Ui_MainWindow as Ui_MainWindow_2
from Ui_main_3 import Ui_MainWindow as Ui_MainWindow_3

class Main_Window(QMainWindow, Ui_MainWindow_2):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)
        self.login_Button.clicked.connect(self.open_login)
        self.signup_Button.clicked.connect(self.open_signup)

    def open_login(self):
        self.ui_main_3_window = QtWidgets.QMainWindow()
        self.ui_main_3 = Ui_MainWindow_3()
        self.ui_main_3.setupUi(self.ui_main_3_window)
        self.ui_main_3_window.show()
        
        uic.loadUi('./school-management-system/sign/main_2.ui', self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = Main_Window()
    app_window.show()
    sys.exit(app.exec_())
