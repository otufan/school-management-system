import sys
sys.path.append("C:/Users/MainUser/Desktop/tech_groupproject/school-management-system")
import re
import json
import pandas as pd
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_main_2 import Ui_MainWindow as Ui_MainWindow_2
from Ui_login_screen import Ui_Form as Ui_MainWindow_3
from Ui_signup_screen import Ui_Form as Ui_MainWindow_4
from Classes.user import User
from Student_UI.student_main import Main_Window as Ui_MainWindow_5
from Teacher_UI.teacher_main import Main_Window as Ui_MainWindow_6



class Main_Window(QMainWindow, Ui_MainWindow_2):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)
        self.resize(640,480)       
        self.setWindowTitle("School Info")
        self.login_Button.clicked.connect(self.open_login)
        self.login_Button.clicked.connect(self.close)
        self.signup_Button.clicked.connect(self.open_signup)
        self.signup_Button.clicked.connect(self.close)
        
        
    
    def create_Student(self,name, surname, email, birthday, city,phone_number, password):
        if not User.email_exists(email):
            User.create_user(name, surname, email, birthday, city, phone_number, password, user_type="student")
            print("User created successfully.")
            # Close this window after saving the user
            self.ui_main_3_window.close()
            # Open the login screen
            self.open_login()
        else:
            QMessageBox.warning(None, 'Warning', f'The email {email} already exists.', QMessageBox.Ok)
            
        #User.create_user(name, surname, email, birthday, city, phone_number, password, user_type="student")
               
        #Call the create_user function from Classes user.py file.
        
        #_name = name
        #_surname = surname
        #_birthday = birthday
        #_city = city
        #_email = email
        #_password = password
        
        #student_data = {
        #    "name": _name,
         #   "surname": _surname,
          #  "birthday": _birthday,
           # "city": _city,
            #"email": _email,
            #"password": _password
        #}

        #try:
            #with open("C:/Users/MainUser/Desktop/tech_groupproject/school-management-system/data/student.txt", "r") as file:
            #    students = json.load(file)
        #except FileNotFoundError:
        #    students = []

       # students.append(student_data)

       # with open("C:/Users/MainUser/Desktop/tech_groupproject/school-management-system/data/student.txt", "w") as file:
        #    json.dump(students, file, indent=2)


    

    def is_valid_email(self, email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email)
    
    def is_valid_password(self,password):
        password = self.ui_main_3.password.text()

        if len(password) <= 8 and any(c.isalpha() for c in password) and any(c.isdigit() for c in password) and any(c.isascii() and not c.isalnum() for c in password):
            return True
        else:
            return False
    def is_equal_password(self,password,repassword):
        password = self.ui_main_3.password.text()
        repassword= self.ui_main_3.repassword.text()
        if password == repassword:
            return True
        else:
            return False
        
    def check_enter(self):
        email = self.ui_main_3.email.text()
        password = self.ui_main_3.password.text()
        if (email == '' or password == ''):
            self.ui_main_3_window.statusBar().showMessage("Please fill in the blanks!", 2000)
        elif not self.is_valid_email(email):
            self.ui_main_3_window.statusBar().showMessage("Please enter a valid email address!", 2000)
        elif not self.is_valid_password(password):
            self.ui_main_3_window.statusBar().showMessage("Please enter a valid password!", 2000)
        else:
            user_data = User.login(email, password)
            if user_data:
                # successful enter for users
                user_type = user_data.get('user_type')
                User.set_currentuser(email)
                self.open_main_window(user_type)
                
            else:
                self.ui_main_3_window.statusBar().showMessage("Invalid email or password!", 2000)

    def open_main_window(self, user_type):
        if user_type == 'admin':
            # Admin ekranını aç
            print("Opening admin main window...")
            # Örneğin:
            # admin_window = AdminMainWindow()
            # admin_window.show()
        elif user_type == 'teacher':
            # Open teacher UI
            self.ui_main_3_window = QtWidgets.QMainWindow()
            self.ui_main_3 = Ui_MainWindow_6()
            self.ui_main_3.setupUi(self.ui_main_3_window)
            self.ui_main_3_window.show()
            self.ui_main_3_window.resize(440,400)
        elif user_type == 'student':
            self.ui_main_3_window = QtWidgets.QMainWindow()
            self.ui_main_3 = Ui_MainWindow_5()
            self.ui_main_3.setupUi(self.ui_main_3_window)
            self.ui_main_3_window.show()
            self.ui_main_3_window.resize(440,400)
        else:
            print("Unknown user type!")

            
    def check_enter_signup(self):
        name = self.ui_main_3.name.text()
        surname = self.ui_main_3.surname.text()
        birthday = self.ui_main_3.birthday.date().toString(QtCore.Qt.ISODate) #ISO standart for Date
        city = self.ui_main_3.city.text()
        email = self.ui_main_3.email.text()
        phone_number=self.ui_main_3.phone_number.text()
        password = self.ui_main_3.password.text()
        repassword = self.ui_main_3.repassword.text()
        if (name == '' or surname == '' or birthday=='' or city == '' or email == '' or password == '' or repassword == ''):
            self.ui_main_3_window.statusBar().showMessage("Please fill in the blanks!", 2000)
        elif not self.is_valid_email(email):
            self.ui_main_3_window.statusBar().showMessage("Please enter a valid email address!", 2000)
        elif not self.is_valid_password(password):
            self.ui_main_3_window.statusBar().showMessage("Please enter a valid password!", 2000)
        elif not self.is_equal_password(password, repassword):
            self.ui_main_3_window.statusBar().showMessage("Please check your password!", 2000)
        else:
            self.create_Student(name, surname,email, birthday, city,phone_number, password)
            
    def open_login(self):
        self.ui_main_3_window = QtWidgets.QMainWindow()
        self.ui_main_3 = Ui_MainWindow_3()
        self.ui_main_3.setupUi(self.ui_main_3_window)
        self.ui_main_3_window.show()
        self.ui_main_3_window.resize(440,400)
        self.ui_main_3.enter_Button.clicked.connect(self.check_enter) 
         
            
    def open_signup(self):
        self.ui_main_3_window = QtWidgets.QMainWindow()
        self.ui_main_3 = Ui_MainWindow_4()
        self.ui_main_3.setupUi(self.ui_main_3_window)
        self.ui_main_3_window.show()
        self.ui_main_3_window.resize(440,400)
        self.ui_main_3.sign_Button.clicked.connect(self.check_enter_signup)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = Main_Window()
    app_window.show()
    sys.exit(app.exec_())

