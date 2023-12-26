import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        
        uic.loadUi('./school-management-system/sign/main_2.ui', self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())