import sys
import re

sys.path.append("C:/Users/ahmet/Documents/GitHub/school-management-system")


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_teacher import *
from Classes.task import Task
from Classes.user import *
from Teacher_UI.CreateLesson import *
from Teacher_UI.CreateMentor import *
#from Classes.authentication import Authentication

class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self): 
        super(Main_Window,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Teacher Page")

        #self.current_user = Authentication.get_current_user()
        self.current_user_email = 'created@example.com'
        #self.load_tasks(current_user.email)
        
        self.load_tasks(self.current_user_email)
        #initial values of task create form
        self.assignee_input_combo.addItem("")
        self.assignee_input_combo.addItems(User.get_emails_for_task_assign())
        self.due_date_input.setDate(QtCore.QDate(1000, 1, 1))

        #signal to create task button
        self.create_task_button.clicked.connect(self.create_task)

        self.create_lesson.clicked.connect(self.open_create_lesson)
        self.create_mentor.clicked.connect(self.open_create_mentor)

        self.create_teacher_account_button.clicked.connect(self.check_enter_signup)

    def check_enter_signup(self):
        name = self.teacher_name_admin.text()
        surname = self.teache_surname_admin.text()
        birthday = self.teacher_birthdate_admin.date().toString(QtCore.Qt.ISODate) #ISO standart for Date
        city = self.teacher_city_admin.text()
        email = self.teacher_email_admin.text()
        phone_number=self.teacher_tel_admin.text()
        password = self.teacher_password_admin.text()
        if (name == '' or surname == '' or birthday=='' or city == '' or email == '' or password == ''):
            self.ui_main_3_window.statusBar().showMessage("Please fill in the blanks!", 2000)
        elif not self.is_valid_email(email):
            self.ui_main_3_window.statusBar().showMessage("Please enter a valid email address!", 2000)
        elif not self.is_valid_password(password):
            self.ui_main_3_window.statusBar().showMessage("Please enter a valid password!", 2000)
        else:
            self.create_Teacher(name, surname,email, birthday, city,phone_number, password)

    def is_valid_email(self, email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email)
    
    def is_valid_password(self,password):
        password = self.teacher_password_admin.text()

        if len(password) <= 8 and any(c.isalpha() for c in password) and any(c.isdigit() for c in password) and any(c.isascii() and not c.isalnum() for c in password):
            return True
        else:
            return False
    
    def create_Teacher(self,name, surname, email, birthday, city,phone_number, password):
        if not User.email_exists(email):
            User.create_user(name, surname, email, birthday, city, phone_number, password, user_type="teacher")
            print("User created successfully.")
        else:
            QMessageBox.warning(None, 'Warning', f'The email {email} already exists.', QMessageBox.Ok)

    def open_create_lesson(self):

        self.open_create_lesson_window = CreateLesson()
        self.open_create_lesson_window.show()

    def open_create_mentor(self):

        self.open_create_mentor_window = CreateMentor()
        self.open_create_mentor_window.show()


    def create_task(self):
        task_name = self.task_name_input.text()
        due_date = self.due_date_input.date().toString("dd/MM/yyyy")
        assignee = self.assignee_input_combo.currentText()

        if task_name != "" and assignee != "":
            Task.create_task(task_name,due_date,assignee,self.current_user_email)
            print("Task is created", task_name, due_date, assignee)
            self.load_tasks(self.current_user_email)

            self.assignee_input_combo.setCurrentIndex(0)
            self.task_name_input.setText("")
        else:
            self.showUpdateAlert(f"Task Name and Assignee cannot be empty")
        

    def load_tasks(self, email):
        tasks = Task.retrieve_task_per_creator(email)
        print(tasks)

        if tasks is None or not tasks:
            print("No tasks found.")
            return

        task_widget = self.findChild(QTableWidget, 'tasks_tableWidget')
        print("taskwidget created")
        task_widget.setRowCount(len(tasks))
        task_widget.setColumnCount(6)

        headers = ["Task Name", "Due Date", "Assigned To", "Created By", "Status", "Created"]
        task_widget.setHorizontalHeaderLabels(headers)
        
        # Set the combo box delegate for the "Status" column (column index 4)
        task_widget.setItemDelegateForColumn(4, ComboBoxDelegate())

        # Populate the table
        for row, task in enumerate(tasks):
            task_widget.setItem(row, 0, QTableWidgetItem(task.task_name))
            task_widget.setItem(row, 1, QTableWidgetItem(task.due_date))
            task_widget.setItem(row, 2, QTableWidgetItem(task.assigned_to_email))

            task_widget.setItem(row, 3, QTableWidgetItem(task.created_by))
            
            # Create a QTableWidgetItem for the "Status" column
            status_item = QTableWidgetItem(task.status)
            status_item.setData(Qt.UserRole, task)

            task_widget.setItem(row, 4, status_item)
            task_widget.setItem(row, 5, QTableWidgetItem(task.created))
        print("tasks printed in table")
        # Connect the itemDoubleClicked signal to a slot
        task_widget.itemDoubleClicked.connect(self.on_item_double_clicked)
        print("double click signal connected")
        # Connect the itemChanged signal to a slot for handling updates
        task_widget.itemChanged.connect(self.on_item_changed)
        print("item changed signal connected")

    def on_item_double_clicked(self, item):
        # Prevent editing for certain columns
        if item.column() in [0,2, 3, 5]:
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Clear the editable flag
        else:
            item.setFlags(item.flags() | Qt.ItemIsEditable)  # Set the editable flag

    def on_item_changed(self, item):
        row = item.row()
        col = item.column()
        # print(item.row(), item.column())
        if item.tableWidget().item(row, 2) is not None:
            task_name_ilk = item.tableWidget().item(row, 0).text()
            assigned_to_email = item.tableWidget().item(row, 2).text()
            new_value = item.text()
            print("new value: ", new_value)

            if 1 == 0:  # Task Name column
                if Task.update_task_teacher(task_name_ilk, assigned_to_email, task_name=new_value):
                    self.showUpdateAlert(f"Task name is updated to {new_value}")
                else:
                    print("Task not updated.")
            elif col == 1:  # Due Date column
                if Task.update_task_teacher(task_name_ilk, assigned_to_email, due_date=new_value):
                    self.showUpdateAlert(f"Due date is updated to {new_value}")
                else:
                    print("Task not updated.")
            elif col == 4:  # Status column
                if Task.update_task_teacher(task_name_ilk, assigned_to_email, status=new_value):
                    self.showUpdateAlert(f"Status is updated to {new_value}")
                else:
                    print("Task not updated.")
            else:
                # Handle the case where the item was not edited
                print("Item not edited.")
        else:
            print("Item is None.")


    
    def showUpdateAlert(self, alert):
        message = alert
        QMessageBox.information(None, "Item Updated", message, QMessageBox.Ok)

class ComboBoxDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        if index.column() == 4:
            combo_box = QComboBox(parent)
            combo_box.addItems(["Open", "In Progress", "Completed"])
            return combo_box
        return None

    def setEditorData(self, editor, index):
        value = index.model().data(index, role=Qt.DisplayRole)
        editor.setCurrentText(value)


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