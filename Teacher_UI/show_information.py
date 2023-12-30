import sys
sys.path.append('/Users/onur/Documents/GitHub/school-management-system')

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from  Ui_teacher import  Ui_MainWindow
from Classes.user import User


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_Window,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Teacher Page")
        self.showMaximized()

        self.tabwidget.clicked.connect(self.show_information)
        
    def show_information(self):
        

        #email = self.login_email


        if email == users.txt(email):

            self.teacher_profil_name_edit.setText(self.name)
            self.teacher_profil_surname_edit.setText(self.surname)
            self.teacher_profil_birth_edit.seText()
            self.teacher_profil_email_edit.seText()
            self.teacher_profil_city_edit.seText()
            self.teacher_profil_tel_edit.seText()

            

        
        
        





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