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

