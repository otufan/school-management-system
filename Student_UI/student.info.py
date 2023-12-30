import sys
sys.path.append('/Users/onur/Documents/GitHub/school-management-system')

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_Student_Ui import *
from Classes.user import user


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_Window,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Student Page")







        if email == users.txt(email):


            self.student_profil_name_edit.setText(self.name)
            self.student_attendance_profil_surname_edit.setText(self.surname)
            self.student_profil_birth_edit.seText()
            self.student_profil_email_edit.seText()
            self.student_profil_city_edit.seText()
            self.student_profil_tel_edit.seText()







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
