import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_main_2 import Ui_MainWindow as Ui_MainWindow_2
from Ui_main_3 import Ui_main_3

class Main_Window(QMainWindow, Ui_MainWindow_2):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("School Info")
        
        self.login_Button.clicked.connect(self.open_login)
        self.signup_Button.clicked.connect(self.open_signup)

    def open_login(self):
        self.setter = Setter_Window()
        self.setter.show()
        self.hide()

    def open_signup(self):
        pass

class Setter_Window(QMainWindow, Ui_main_3):
    def __init__(self):
        super(Setter_Window, self).__init__()
        self.setupUi(self)
        self.set_seconds_Button.clicked.connect(self.time_setter)
        self.seconds = self.seconds_spinBox.value()

    def time_setter(self):
        self.seconds = self.seconds_spinBox.value()
        self.hide()
        # Ana pencereyi göstermek için:
        app_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = Main_Window()
    app_window.show()
    sys.exit(app.exec_())

