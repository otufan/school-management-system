import sys
sys.path.append('/Users/onur/Documents/GitHub/school-management-system')

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_teacher import *
from Classes.task import Task


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_Window,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Teacher Page")
        self.showMaximized()


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