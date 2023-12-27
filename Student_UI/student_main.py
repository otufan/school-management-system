import sys
sys.path.append('/Users/onur/Documents/GitHub/school-management-system')

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
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

            print("Before setting UserRole:", task)
            status_item.setData(Qt.UserRole, task)
            print("After setting UserRole:", task)

            table_widget.setItem(row, 4, status_item)

            table_widget.setItem(row, 5, QTableWidgetItem(task.created))

class ComboBoxDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        combo_box = QComboBox(parent)
        # Add items to the combo box
        combo_box.addItems(["Open", "In Progress", "Completed"])  # Add your status options
        return combo_box

    def setEditorData(self, editor, index):
        value = index.model().data(index, role=Qt.DisplayRole)
        editor.setCurrentText(value)

    def setModelData(self, editor, model, index):
        value = editor.currentText()
        model.setData(index, value, role=Qt.EditRole)

        # Update the data in the JSON file
        row = index.row()

        # Retrieve task_name, due_date, and created_by attributes
        task_name = model.data(model.index(row, 0), role=Qt.DisplayRole)
        due_date = model.data(model.index(row, 1), role=Qt.DisplayRole)
        created_by = model.data(model.index(row, 3), role=Qt.DisplayRole)
        # Get the new value selected in the combo box
        new_status = editor.currentText()


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