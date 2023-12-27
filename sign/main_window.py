import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_main_2 import Ui_MainWindow as Ui_MainWindow_2
from login_window import loginWindow

class Main_Window(QMainWindow, Ui_MainWindow_2):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)
        self.main=Ui_MainWindow_2()
        self.loginwindow= loginWindow() 
        #self.main.login_Button.clicked.connect(self.login_open)  
        self.loginwindow.show()   
        
        self.signup_Button.clicked.connect(self.open_signup)

    def login_open(self):
        pass

    def open_signup(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = Main_Window()
    app_window.show()
    sys.exit(app.exec_())

