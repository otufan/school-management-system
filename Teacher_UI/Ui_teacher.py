# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/onur/Documents/GitHub/school-management-system/Teacher_UI/teacher.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1912, 1078)
        MainWindow.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"background-color: rgb(248, 255, 246);\n"
"background-color: rgb(233, 235, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(252, 255, 240);\n"
"background-color: rgb(255, 253, 248);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1111, 80))
        self.frame.setStyleSheet("background-color: rgb(255, 234, 254);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.date_label = QtWidgets.QLabel(self.frame)
        self.date_label.setGeometry(QtCore.QRect(20, 20, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.date_label.setFont(font)
        self.date_label.setObjectName("date_label")
        self.welkome_label = QtWidgets.QLabel(self.frame)
        self.welkome_label.setGeometry(QtCore.QRect(740, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.welkome_label.setFont(font)
        self.welkome_label.setObjectName("welkome_label")
        self.user_name_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.user_name_lineEdit.setGeometry(QtCore.QRect(840, 30, 113, 22))
        self.user_name_lineEdit.setObjectName("user_name_lineEdit")
        self.teacher_label = QtWidgets.QLabel(self.frame)
        self.teacher_label.setGeometry(QtCore.QRect(1000, 0, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.teacher_label.setFont(font)
        self.teacher_label.setObjectName("teacher_label")
        self.to_do_list_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.to_do_list_pushButton.setGeometry(QtCore.QRect(20, 680, 191, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.to_do_list_pushButton.setFont(font)
        self.to_do_list_pushButton.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.to_do_list_pushButton.setObjectName("to_do_list_pushButton")
        self.to_do_list_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.to_do_list_tableWidget.setGeometry(QtCore.QRect(20, 730, 531, 192))
        self.to_do_list_tableWidget.setRowCount(6)
        self.to_do_list_tableWidget.setColumnCount(7)
        self.to_do_list_tableWidget.setObjectName("to_do_list_tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.to_do_list_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.to_do_list_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.to_do_list_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.to_do_list_tableWidget.setHorizontalHeaderItem(3, item)
        self.announcements_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.announcements_pushButton.setGeometry(QtCore.QRect(20, 150, 171, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.announcements_pushButton.setFont(font)
        self.announcements_pushButton.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.announcements_pushButton.setObjectName("announcements_pushButton")
        self.announcements_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.announcements_textEdit.setGeometry(QtCore.QRect(260, 130, 641, 71))
        self.announcements_textEdit.setObjectName("announcements_textEdit")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(890, 450, 73, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(980, 450, 110, 22))
        self.dateEdit_2.setMaximumDate(QtCore.QDate(2023, 12, 31))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.schedule_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.schedule_tabWidget.setGeometry(QtCore.QRect(20, 280, 591, 301))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schedule_tabWidget.setFont(font)
        self.schedule_tabWidget.setObjectName("schedule_tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.schedule_tableWidget = QtWidgets.QTableWidget(self.tab)
        self.schedule_tableWidget.setGeometry(QtCore.QRect(10, 60, 521, 192))
        self.schedule_tableWidget.setRowCount(5)
        self.schedule_tableWidget.setColumnCount(7)
        self.schedule_tableWidget.setObjectName("schedule_tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setHorizontalHeaderItem(3, item)
        self.schedule_tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.attandance_tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.attandance_tableWidget.setGeometry(QtCore.QRect(40, 60, 281, 192))
        self.attandance_tableWidget.setRowCount(5)
        self.attandance_tableWidget.setColumnCount(4)
        self.attandance_tableWidget.setObjectName("attandance_tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.attandance_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.attandance_tableWidget.setHorizontalHeaderItem(1, item)
        self.lesson_comboBox = QtWidgets.QComboBox(self.tab_2)
        self.lesson_comboBox.setGeometry(QtCore.QRect(50, 20, 73, 22))
        self.lesson_comboBox.setObjectName("lesson_comboBox")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.tab_2)
        self.dateEdit_3.setGeometry(QtCore.QRect(150, 20, 110, 22))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.schedule_tabWidget.addTab(self.tab_2, "")
        self.meeting_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.meeting_tabWidget.setGeometry(QtCore.QRect(630, 280, 551, 321))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.meeting_tabWidget.setFont(font)
        self.meeting_tabWidget.setObjectName("meeting_tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.meeting_tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.meeting_tableWidget.setGeometry(QtCore.QRect(10, 80, 521, 181))
        self.meeting_tableWidget.setRowCount(5)
        self.meeting_tableWidget.setColumnCount(5)
        self.meeting_tableWidget.setObjectName("meeting_tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.meeting_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.meeting_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.meeting_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.meeting_tableWidget.setHorizontalHeaderItem(3, item)
        self.meeting_tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.meeting_comboBox = QtWidgets.QComboBox(self.tab_4)
        self.meeting_comboBox.setGeometry(QtCore.QRect(30, 30, 73, 22))
        self.meeting_comboBox.setObjectName("meeting_comboBox")
        self.dateEdit_4 = QtWidgets.QDateEdit(self.tab_4)
        self.dateEdit_4.setGeometry(QtCore.QRect(150, 30, 110, 22))
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.meeting_attandance_tableWidget = QtWidgets.QTableWidget(self.tab_4)
        self.meeting_attandance_tableWidget.setGeometry(QtCore.QRect(40, 80, 271, 192))
        self.meeting_attandance_tableWidget.setRowCount(3)
        self.meeting_attandance_tableWidget.setColumnCount(4)
        self.meeting_attandance_tableWidget.setObjectName("meeting_attandance_tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.meeting_attandance_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.meeting_attandance_tableWidget.setHorizontalHeaderItem(1, item)
        self.meeting_tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1912, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.schedule_tabWidget.setCurrentIndex(1)
        self.meeting_tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.date_label.setText(_translate("MainWindow", "Date"))
        self.welkome_label.setText(_translate("MainWindow", "Welkome"))
        self.teacher_label.setText(_translate("MainWindow", "Teacher"))
        self.to_do_list_pushButton.setText(_translate("MainWindow", "To-Do-List"))
        item = self.to_do_list_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Assignet To"))
        item = self.to_do_list_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Task Name"))
        item = self.to_do_list_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Due Date"))
        item = self.to_do_list_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        self.announcements_pushButton.setText(_translate("MainWindow", "Announcements"))
        item = self.schedule_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Lesson Name"))
        item = self.schedule_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.schedule_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Begin Time"))
        item = self.schedule_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "End Time"))
        self.schedule_tabWidget.setTabText(self.schedule_tabWidget.indexOf(self.tab), _translate("MainWindow", "Schedule"))
        item = self.attandance_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Student Name"))
        item = self.attandance_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Attanded/Missed"))
        self.schedule_tabWidget.setTabText(self.schedule_tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Attandance"))
        item = self.meeting_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Meeting Subject"))
        item = self.meeting_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.meeting_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "BeginTime"))
        item = self.meeting_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "End Time"))
        self.meeting_tabWidget.setTabText(self.meeting_tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Mentor_Meeting"))
        item = self.meeting_attandance_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Student Name"))
        item = self.meeting_attandance_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Attanded/Missed"))
        self.meeting_tabWidget.setTabText(self.meeting_tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Meeting_Attandance"))
