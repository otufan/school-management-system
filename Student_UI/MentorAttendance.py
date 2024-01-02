import sys, os
sys.path.append(os.getcwd())

from Classes.user import User
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtGui import *

class MentorAttendance(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mentor Attendance Window")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.table_view = QTableView()
        layout.addWidget(self.table_view)

        self.show_Mentor_Attendance()

    def show_Mentor_Attendance(self):
        table_lesson = User.get_Mentor_Attendance_Student("ada@demirci.com")
        layout = QVBoxLayout()
        layout.addWidget(table_lesson)
        self.table_view.setLayout(layout)


def mentor_attendance():
    app = QApplication(sys.argv)
    pencere = MentorAttendance()
    pencere.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    mentor_attendance()