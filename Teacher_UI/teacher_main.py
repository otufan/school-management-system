import sys
sys.path.append('/Users/onur/Documents/GitHub/school-management-system')

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_teacher import *
from Classes.task import Task
#from Classes.authentication import Authentication

class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_Window,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Teacher Page")

        #current_user = Authentication.get_current_user()
        #self.load_tasks(current_user.email)
        self.load_tasks('created@example.com')

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