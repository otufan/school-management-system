import sys
sys.path.append("C:/Users/omert/OneDrive/Desktop/Pyhton HM/school-management-system")
from Classes.user import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from Ui_Student_Ui import *
from Classes.task import Task
#from Classes.authentication import Authentication


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_Window,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Student Page")

        #current_user = Authentication.get_current_user()
        #self.load_tasks(current_user.email)
        self.load_tasks('assigned@example.com')
        self.show_Lesson_Schedule
        self.show_Mentor_Schedule

    def load_tasks(self, email):
        tasks = Task.retrieve_task_per_assignee(email)
        print(tasks)

        if tasks is None or not tasks:
            print("No tasks found.")
            return

        table_widget = self.findChild(QTableWidget, 'tasks_tableWidget')
        table_widget.setRowCount(len(tasks))
        table_widget.setColumnCount(6)

        headers = ["Task Name", "Due Date", "Assigned To", "Created By", "Status", "Created"]
        table_widget.setHorizontalHeaderLabels(headers)
        
        # Set the combo box delegate for the "Status" column (column index 4)
        table_widget.setItemDelegateForColumn(4, ComboBoxDelegate())

        # Populate the table
        for row, task in enumerate(tasks):
            table_widget.setItem(row, 0, QTableWidgetItem(task.task_name))
            table_widget.setItem(row, 1, QTableWidgetItem(task.due_date))
            table_widget.setItem(row, 2, QTableWidgetItem(task.assigned_to_email))
            table_widget.setItem(row, 3, QTableWidgetItem(task.created_by))
            
            # Create a QTableWidgetItem for the "Status" column
            status_item = QTableWidgetItem(task.status)
            status_item.setData(Qt.UserRole, task)

            table_widget.setItem(row, 4, status_item)
            table_widget.setItem(row, 5, QTableWidgetItem(task.created))

        # Connect the itemDoubleClicked signal to a slot
        table_widget.itemDoubleClicked.connect(self.on_item_double_clicked)

    def on_item_double_clicked(self, item):
        # Prevent editing for certain columns
        if item.column() in [0, 1, 2, 3, 5]:
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Clear the editable flag
        else:
            item.setFlags(item.flags() | Qt.ItemIsEditable)  # Set the editable flag

    def show_Lesson_Schedule(self):

        #student_plan_tab = self.findChild(QWidget, 'student_plan')
        student_plan_tab = self.findChild(QTableWidget, 'student_plan_lesson_list')
        print('BURADA')

        table = self.create_table(User.get_LessonSchedule(), 'student_plan_lesson_list')
        table_layout = student_plan_tab.layout()
        table_layout.addWidget(table)

    def show_Mentor_Schedule(self):

        student_plan_tab = self.findChild(QWidget, 'student_plan')
    
        table = self.create_table(User.get_Mentor_Schedule(), 'student_plan_mentor_list')
        table_layout = student_plan_tab.layout()
        table_layout.addWidget(table)

    def create_table(self, infos, table_name):

        table = self.findChild(QTableWidget, table_name)
        table.setRowCount(len(infos))
        table.setColumnCount(len(infos[0]))

        if table_name == 'student_plan_lesson_list':
            table.setHorizontalHeaderLabels(['Lesson Date','Lesson Name','Lesson Start Time','Lesson Finish Time'])
        else:
            table.setHorizontalHeaderLabels(['Mentoring Date','Mentoring Subject','MEntoring Start Time','Mentoring Finish Time'])

        for row_index, row_info in enumerate(infos):
            for column_index, info in enumerate(row_info):
                infos.setItem(row_index, column_index, QTableWidgetItem(info))

        infos.resizeColumnsToContents()

        return table


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

    def setModelData(self, editor, model, index):
        if index.column() == 4:
            value = editor.currentText()
            model.setData(index, value, role=Qt.EditRole)

            row = index.row()
            task_name = model.data(model.index(row, 0), role=Qt.DisplayRole)
            created_by = model.data(model.index(row, 3), role=Qt.DisplayRole)
            new_status = editor.currentText()

            Task.update_task_status(task_name, created_by, new_status)

            # Show an alert
            self.showUpdateAlert(task_name, new_status)

    def showUpdateAlert(self, task_name, new_status):
        message = f"Task:  {task_name} status is updated to: {new_status}"
        QMessageBox.information(None, "Item Updated", message, QMessageBox.Ok)

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









