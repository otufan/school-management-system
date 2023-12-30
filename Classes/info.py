import sys
sys.path.append('/Users/onur/Documents/GitHub/school-management-system')

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_teacher import *


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_Window,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Teacher Page")
        self.showMaximized()

       # self.info_button.clicked.connect(self.show_information)
        
    # def show_information(self):
        name = self.user_name_lineEdit.text()
        surname = self.user_surname_lineEdit.text()
        birtdate = self.user_birtdate_lineEdit.text()
        email = self.user_email_lineEdit.text()
        city = self.user_city_lineEdit.text()
        tel = self.user_tel_lineEdit.text()










if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = Main_Window()    
    widget = QtWidgets.QStackedWidget()
    
    widget.addWidget(app_window)
    widget.show()
    try:
        sys.exit(app.exec_())

    except:
        print("Exiting")