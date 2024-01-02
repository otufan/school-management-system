import sys
import os
sys.path.append(os.getcwd())

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Teacher_UI.Ui_teacher import *
from Classes.task import Task
from Classes.user import *
from Teacher_UI.CreateLesson import *
from Teacher_UI.CreateMentor import *
from Teacher_UI.LessonAttendance import *
from Teacher_UI.MentorAttendance import *

class Main_Window(QMainWindow, Ui_MainWindow):


    def __init__(self):
        super(Main_Window,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Teacher Page")

        User.set_currentuser("admin@example.com")
        #self.current_user = Authentication.get_current_user()
        self.current_user_email = 'created@example.com'
        #self.load_tasks(current_user.email)

        #hide admin tab if user is not admin
        tab_widget = self.tabWidget
        if User._current_user.user_type != "admin":
            tab_widget.removeTab(6)

        self.display_announcements()
        self.display_announcement_to_delete()

        self.show_information()
        
        self.load_tasks(self.current_user_email)
        #initial values of task create form
        self.assignee_input_combo.addItem("")
        self.assignee_input_combo.addItems(User.get_emails_for_task_assign())
        self.due_date_input.setDate(QtCore.QDate(1000, 1, 1))

        #signal to create task button
        self.create_task_button.clicked.connect(self.create_task)

        self.show_Lesson_Schedule()
        self.show_Mentor_Schedule()

        self.create_lesson.clicked.connect(self.open_create_lesson)
        self.create_mentor.clicked.connect(self.open_create_mentor)
        self.lesson_att_insert.clicked.connect(self.show_lesson_attendance_page)
        self.mentor_att_insert.clicked.connect(self.show_mentor_attendance_page)  
        
        self.create_announcement_button.clicked.connect(self.create_announcement)

        self.delete_announcement_button.clicked.connect(self.delete_announcement)
        #self.teacher_profil_city_edit.textChanged.connect(self.on_city_changed)
        #self.teacher_profil_tel_edit.textChanged.connect(self.on_tel_changed)

    def on_city_changed(self):
        new_city = self.teacher_profil_city_edit.toPlainText()
        User.update_user_information(User._current_user.email, city=new_city)
        self.showUpdateAlert("City is updated")

    def on_tel_changed(self):
        new_tel = self.teacher_profil_tel_edit.text()
        updated_info = {"phone_number": new_tel }
        User.update_user_information(User._current_user.email, **updated_info)
        self.showUpdateAlert("Phone number is updated")

    def display_announcement_to_delete(self):
        user = User._current_user
        announcements_to_delete = User.get_announcements_to_delete(user.email, user.user_type)
        self.announcement_to_delete_combobox.clear()
        self.announcement_to_delete_combobox.addItem("")
        for announcement in announcements_to_delete:
            self.announcement_to_delete_combobox.addItem(announcement['announcement'])
        pass

    def show_information(self):
        user = User._current_user
        self.teacher_profil_name_edit.setText(user.name)
        self.teahcer_profil_surname_edit.setText(user.surname)
        self.teacher_profil_birth_edit.setText(user.birthdate)
        self.teacher_profil_mail_edit.setText(user.email)
        self.teacher_profil_city_edit.setText(user.city)
        self.teacher_profil_tel_edit.setText(user.phone_number)

    def delete_announcement(self):
        announcement = self.announcement_to_delete_combobox.currentText()
        if announcement != "":
            User.delete_announcement(announcement)
            self.announcement_to_delete_combobox.setCurrentIndex(0)
            self.display_announcements()
            self.showUpdateAlert(f"{announcement} is deleted!")

        else:
            self.showUpdateAlert("Please select announcement to delete!")
        

    def create_announcement(self):
        text = self.announcement_lineEdit.text()
        email = User._current_user.email
        if text != "":
            success, message = User.create_announcement(text, email)
            if success:
                self.display_announcements()
                self.display_announcement_to_delete()
                self.showUpdateAlert(f"{message}")
            else:
                self.showUpdateAlert(f"{message}")
        
        else:
            self.showUpdateAlert(f"Announcement text cannot be empty!")
        
        
    def display_announcements(self):
        # Get announcements
        announcements = User.get_announcements()

        if announcements is None or not announcements:
            print("No announcement found.")
            formatted_announcements = "No announcement"
        else:
            # Format announcements with gaps
            formatted_announcements = "<hr>".join(
        f"<p style='font-size:14pt;'>{announcement['announcement']}</p>"
        f"<p style='font-size:12pt; font-style:italic;'>Announcement by {announcement['created_by']} ({announcement['timestamp']})</p>"
        for announcement in announcements
    )

        # Set the formatted text in the QTextBrowser
        self.announcement_textbrowser.setHtml(formatted_announcements)

    def open_create_lesson(self):

        self.open_create_lesson_window = CreateLesson()
        self.open_create_lesson_window.show()

    def open_create_mentor(self):

        self.open_create_mentor_window = CreateMentor()
        self.open_create_mentor_window.show()

    def show_lesson_attendance_page(self):

        self.open_lesson_attendance_window = LessonAttendance()
        self.open_lesson_attendance_window.show()

    def show_mentor_attendance_page(self):

        self.open_lesson_attendance_window = MentorAttendance()
        self.open_lesson_attendance_window.show()

    def refresh_lesson(self):

        teacher_plan_tab = self.findChild(QTableWidget, 'teacher_plan_lesson')
        table = User.get_LessonSchedule() 

       
        if isinstance(table, QTableWidget):
            teacher_plan_tab.clear()  

           
            teacher_plan_tab.setColumnCount(table.columnCount())
            teacher_plan_tab.setRowCount(table.rowCount())

            for i in range(table.rowCount()):
                for j in range(table.columnCount()):
                    item = table.item(i, j)
                    if item is not None:
                        teacher_plan_tab.setItem(i, j, QTableWidgetItem(item.text()))
            teacher_plan_tab.update()

    def refresh_mentor(self):

        teacher_plan_tab = self.findChild(QTableWidget, 'teacher_plan_mentoring')
        teacher_plan_tab.clearContents()
        self.show_Mentor_Schedule()   

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

    def show_Lesson_Schedule(self):

        teacher_plan_tab = self.findChild(QTableWidget, 'teacher_plan_lesson')
        table = User.get_LessonSchedule()
        layout = QVBoxLayout()
        layout.addWidget(table)        
        teacher_plan_tab.setLayout(layout)
      

    def show_Mentor_Schedule(self):

        teacher_plan_tab = self.findChild(QTableWidget, 'teacher_plan_mentoring')    
        table = User.get_Mentor_Schedule()
        layout = QVBoxLayout()
        layout.addWidget(table)        
        teacher_plan_tab.setLayout(layout)
  
    def show_Lesson_Attendance(self):

        teacher_lesson_attendance = self.findChild(QTableView, 'teacher_attendance_lesson')
        table = User.get_Lesson_Attendance()
        layout = QVBoxLayout()
        layout.addWidget(table)
        teacher_lesson_attendance.setLayout(layout)

    def show_Mentor_Attendance(self):

        teacher_mentor_attendance = self.findChild(QTableView, 'teacher_attendance_mentor')
        table = User.get_Mentor_Attendance()
        layout = QVBoxLayout()
        layout.addWidget(table)        
        teacher_mentor_attendance.setLayout(layout)

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

