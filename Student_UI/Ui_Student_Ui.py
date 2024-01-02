# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/onur/Documents/GitHub/school-management-system/Student_UI/Student_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color: rgb(187, 62, 3);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 1031, 911))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(0, 95, 115);\n"
"border-color: rgb(148, 210, 189);\n"
"color: rgb(155, 34, 38);")
        self.tabWidget.setObjectName("tabWidget")
        self.student_main = QtWidgets.QWidget()
        self.student_main.setObjectName("student_main")
        self.student_main_name = QtWidgets.QLabel(self.student_main)
        self.student_main_name.setGeometry(QtCore.QRect(40, 20, 401, 50))
        self.student_main_name.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.student_main_name.setFont(font)
        self.student_main_name.setStyleSheet("color: rgb(238, 155, 0);")
        self.student_main_name.setObjectName("student_main_name")
        self.student_main_date = QtWidgets.QLabel(self.student_main)
        self.student_main_date.setGeometry(QtCore.QRect(680, 20, 250, 50))
        self.student_main_date.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.student_main_date.setFont(font)
        self.student_main_date.setStyleSheet("color: rgb(238, 155, 0);")
        self.student_main_date.setObjectName("student_main_date")
        self.label_main_announcements = QtWidgets.QLabel(self.student_main)
        self.label_main_announcements.setGeometry(QtCore.QRect(30, 90, 200, 40))
        self.label_main_announcements.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_main_announcements.setFont(font)
        self.label_main_announcements.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_main_announcements.setObjectName("label_main_announcements")
        self.announcements_textBrowser = QtWidgets.QTextBrowser(self.student_main)
        self.announcements_textBrowser.setGeometry(QtCore.QRect(30, 140, 721, 192))
        self.announcements_textBrowser.setObjectName("announcements_textBrowser")
        self.tabWidget.addTab(self.student_main, "")
        self.student_profile = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(17)
        self.student_profile.setFont(font)
        self.student_profile.setObjectName("student_profile")
        self.label_profile_name = QtWidgets.QLabel(self.student_profile)
        self.label_profile_name.setGeometry(QtCore.QRect(40, 39, 200, 51))
        self.label_profile_name.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_name.setFont(font)
        self.label_profile_name.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_name.setObjectName("label_profile_name")
        self.label_profile_surname = QtWidgets.QLabel(self.student_profile)
        self.label_profile_surname.setGeometry(QtCore.QRect(40, 100, 200, 50))
        self.label_profile_surname.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_surname.setFont(font)
        self.label_profile_surname.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_surname.setObjectName("label_profile_surname")
        self.label_profile_birth = QtWidgets.QLabel(self.student_profile)
        self.label_profile_birth.setGeometry(QtCore.QRect(40, 170, 200, 50))
        self.label_profile_birth.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_birth.setFont(font)
        self.label_profile_birth.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_birth.setObjectName("label_profile_birth")
        self.label_profile_mail = QtWidgets.QLabel(self.student_profile)
        self.label_profile_mail.setGeometry(QtCore.QRect(40, 230, 200, 50))
        self.label_profile_mail.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_mail.setFont(font)
        self.label_profile_mail.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_mail.setObjectName("label_profile_mail")
        self.label_profile_city = QtWidgets.QLabel(self.student_profile)
        self.label_profile_city.setGeometry(QtCore.QRect(40, 290, 200, 50))
        self.label_profile_city.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_city.setFont(font)
        self.label_profile_city.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_city.setObjectName("label_profile_city")
        self.label_profile_tel = QtWidgets.QLabel(self.student_profile)
        self.label_profile_tel.setGeometry(QtCore.QRect(40, 340, 200, 50))
        self.label_profile_tel.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_tel.setFont(font)
        self.label_profile_tel.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_tel.setObjectName("label_profile_tel")
        self.student_profil_name_edit = QtWidgets.QTextEdit(self.student_profile)
        self.student_profil_name_edit.setGeometry(QtCore.QRect(250, 30, 321, 50))
        self.student_profil_name_edit.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.student_profil_name_edit.setFont(font)
        self.student_profil_name_edit.setStyleSheet("color: rgb(238, 155, 0);")
        self.student_profil_name_edit.setReadOnly(True)
        self.student_profil_name_edit.setOverwriteMode(False)
        self.student_profil_name_edit.setObjectName("student_profil_name_edit")
        self.student_profil_surname_edit = QtWidgets.QTextEdit(self.student_profile)
        self.student_profil_surname_edit.setGeometry(QtCore.QRect(250, 90, 321, 50))
        self.student_profil_surname_edit.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.student_profil_surname_edit.setFont(font)
        self.student_profil_surname_edit.setStyleSheet("color: rgb(238, 155, 0);")
        self.student_profil_surname_edit.setReadOnly(True)
        self.student_profil_surname_edit.setOverwriteMode(False)
        self.student_profil_surname_edit.setObjectName("student_profil_surname_edit")
        self.student_profil_birth_edit = QtWidgets.QTextEdit(self.student_profile)
        self.student_profil_birth_edit.setGeometry(QtCore.QRect(250, 160, 321, 50))
        self.student_profil_birth_edit.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.student_profil_birth_edit.setFont(font)
        self.student_profil_birth_edit.setStyleSheet("color: rgb(238, 155, 0);")
        self.student_profil_birth_edit.setReadOnly(True)
        self.student_profil_birth_edit.setOverwriteMode(False)
        self.student_profil_birth_edit.setObjectName("student_profil_birth_edit")
        self.student_profil_mail_edit = QtWidgets.QTextEdit(self.student_profile)
        self.student_profil_mail_edit.setGeometry(QtCore.QRect(250, 220, 321, 50))
        self.student_profil_mail_edit.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.student_profil_mail_edit.setFont(font)
        self.student_profil_mail_edit.setStyleSheet("color: rgb(238, 155, 0);")
        self.student_profil_mail_edit.setReadOnly(True)
        self.student_profil_mail_edit.setOverwriteMode(False)
        self.student_profil_mail_edit.setObjectName("student_profil_mail_edit")
        self.student_profil_city_edit = QtWidgets.QTextEdit(self.student_profile)
        self.student_profil_city_edit.setGeometry(QtCore.QRect(250, 280, 321, 50))
        self.student_profil_city_edit.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.student_profil_city_edit.setFont(font)
        self.student_profil_city_edit.setStyleSheet("color: rgb(238, 155, 0);")
        self.student_profil_city_edit.setReadOnly(False)
        self.student_profil_city_edit.setOverwriteMode(False)
        self.student_profil_city_edit.setObjectName("student_profil_city_edit")
        self.student_profil_tel_edit = QtWidgets.QTextEdit(self.student_profile)
        self.student_profil_tel_edit.setGeometry(QtCore.QRect(250, 340, 321, 50))
        self.student_profil_tel_edit.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.student_profil_tel_edit.setFont(font)
        self.student_profil_tel_edit.setStyleSheet("color: rgb(238, 155, 0);")
        self.student_profil_tel_edit.setReadOnly(False)
        self.student_profil_tel_edit.setOverwriteMode(False)
        self.student_profil_tel_edit.setObjectName("student_profil_tel_edit")
        self.update_information_Button = QtWidgets.QPushButton(self.student_profile)
        self.update_information_Button.setGeometry(QtCore.QRect(410, 410, 161, 32))
        self.update_information_Button.setObjectName("update_information_Button")
        self.tabWidget.addTab(self.student_profile, "")
        self.student_plan = QtWidgets.QWidget()
        self.student_plan.setObjectName("student_plan")
        self.label_plan_lesson = QtWidgets.QLabel(self.student_plan)
        self.label_plan_lesson.setGeometry(QtCore.QRect(40, 30, 200, 50))
        self.label_plan_lesson.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_plan_lesson.setFont(font)
        self.label_plan_lesson.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_plan_lesson.setObjectName("label_plan_lesson")
        self.label_plan_mentor = QtWidgets.QLabel(self.student_plan)
        self.label_plan_mentor.setGeometry(QtCore.QRect(540, 30, 300, 50))
        self.label_plan_mentor.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_plan_mentor.setFont(font)
        self.label_plan_mentor.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_plan_mentor.setObjectName("label_plan_mentor")
        self.student_plan_lesson_list = QtWidgets.QTableWidget(self.student_plan)
        self.student_plan_lesson_list.setGeometry(QtCore.QRect(50, 90, 441, 501))
        self.student_plan_lesson_list.setObjectName("student_plan_lesson_list")
        self.student_plan_lesson_list.setColumnCount(0)
        self.student_plan_lesson_list.setRowCount(0)
        self.student_plan_mentor_list = QtWidgets.QTableWidget(self.student_plan)
        self.student_plan_mentor_list.setGeometry(QtCore.QRect(520, 90, 451, 501))
        self.student_plan_mentor_list.setObjectName("student_plan_mentor_list")
        self.student_plan_mentor_list.setColumnCount(0)
        self.student_plan_mentor_list.setRowCount(0)
        self.tabWidget.addTab(self.student_plan, "")
        self.student_to_do = QtWidgets.QWidget()
        self.student_to_do.setObjectName("student_to_do")
        self.tasks_tableWidget = QtWidgets.QTableWidget(self.student_to_do)
        self.tasks_tableWidget.setGeometry(QtCore.QRect(100, 90, 651, 192))
        self.tasks_tableWidget.setObjectName("tasks_tableWidget")
        self.tasks_tableWidget.setColumnCount(0)
        self.tasks_tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.student_to_do, "")
        self.student_attendance = QtWidgets.QWidget()
        self.student_attendance.setObjectName("student_attendance")
        self.label_lesson_status = QtWidgets.QLabel(self.student_attendance)
        self.label_lesson_status.setGeometry(QtCore.QRect(40, 30, 400, 50))
        self.label_lesson_status.setMinimumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_lesson_status.setFont(font)
        self.label_lesson_status.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_lesson_status.setObjectName("label_lesson_status")
        self.student_attendance_lesson_list = QtWidgets.QTextEdit(self.student_attendance)
        self.student_attendance_lesson_list.setGeometry(QtCore.QRect(40, 90, 450, 500))
        self.student_attendance_lesson_list.setMinimumSize(QtCore.QSize(450, 500))
        self.student_attendance_lesson_list.setStyleSheet("color: rgb(238, 155, 0);")
        self.student_attendance_lesson_list.setObjectName("student_attendance_lesson_list")
        self.label_mentor_status = QtWidgets.QLabel(self.student_attendance)
        self.label_mentor_status.setGeometry(QtCore.QRect(540, 21, 480, 50))
        self.label_mentor_status.setMinimumSize(QtCore.QSize(480, 50))
        self.label_mentor_status.setMaximumSize(QtCore.QSize(480, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_mentor_status.setFont(font)
        self.label_mentor_status.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_mentor_status.setObjectName("label_mentor_status")
        self.student_attendance_mentor_list = QtWidgets.QTextEdit(self.student_attendance)
        self.student_attendance_mentor_list.setGeometry(QtCore.QRect(540, 90, 450, 500))
        self.student_attendance_mentor_list.setMinimumSize(QtCore.QSize(450, 500))
        self.student_attendance_mentor_list.setStyleSheet("color: rgb(238, 155, 0);")
        self.student_attendance_mentor_list.setObjectName("student_attendance_mentor_list")
        self.tabWidget.addTab(self.student_attendance, "")
        self.student_dance = QtWidgets.QWidget()
        self.student_dance.setObjectName("student_dance")
        self.chat_list = QtWidgets.QComboBox(self.student_dance)
        self.chat_list.setGeometry(QtCore.QRect(30, 30, 230, 50))
        self.chat_list.setMinimumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chat_list.setFont(font)
        self.chat_list.setStyleSheet("color: rgb(238, 155, 0);")
        self.chat_list.setObjectName("chat_list")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.student_chat_message_panel = QtWidgets.QTextEdit(self.student_dance)
        self.student_chat_message_panel.setGeometry(QtCore.QRect(290, 70, 700, 421))
        self.student_chat_message_panel.setMinimumSize(QtCore.QSize(700, 0))
        self.student_chat_message_panel.setMaximumSize(QtCore.QSize(700, 16777215))
        self.student_chat_message_panel.setStyleSheet("background-color: rgb(233, 216, 166);")
        self.student_chat_message_panel.setObjectName("student_chat_message_panel")
        self.student_chat_message = QtWidgets.QTextEdit(self.student_dance)
        self.student_chat_message.setGeometry(QtCore.QRect(290, 530, 700, 100))
        self.student_chat_message.setMinimumSize(QtCore.QSize(700, 100))
        self.student_chat_message.setMaximumSize(QtCore.QSize(700, 100))
        self.student_chat_message.setStyleSheet("background-color: rgb(233, 216, 166);")
        self.student_chat_message.setObjectName("student_chat_message")
        self.student_chat_send_button = QtWidgets.QPushButton(self.student_dance)
        self.student_chat_send_button.setGeometry(QtCore.QRect(50, 530, 200, 100))
        self.student_chat_send_button.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.student_chat_send_button.setFont(font)
        self.student_chat_send_button.setStyleSheet("color: rgb(238, 155, 0);\n"
"background-color: rgb(148, 210, 189);")
        self.student_chat_send_button.setObjectName("student_chat_send_button")
        self.tabWidget.addTab(self.student_dance, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.student_main_name.setText(_translate("MainWindow", "HOŞGELDİN AHMET"))
        self.student_main_date.setText(_translate("MainWindow", "26/12/2023"))
        self.label_main_announcements.setText(_translate("MainWindow", "Announcements"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.student_main), _translate("MainWindow", "Main"))
        self.label_profile_name.setText(_translate("MainWindow", "Name :"))
        self.label_profile_surname.setText(_translate("MainWindow", "Surname :"))
        self.label_profile_birth.setText(_translate("MainWindow", "Date of Birth :"))
        self.label_profile_mail.setText(_translate("MainWindow", "E-Mail :"))
        self.label_profile_city.setText(_translate("MainWindow", "City :"))
        self.label_profile_tel.setText(_translate("MainWindow", "Tel :"))
        self.update_information_Button.setText(_translate("MainWindow", "Update Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.student_profile), _translate("MainWindow", "Profile"))
        self.label_plan_lesson.setText(_translate("MainWindow", "Lesson Plan"))
        self.label_plan_mentor.setText(_translate("MainWindow", "Mentor Meeting Plan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.student_plan), _translate("MainWindow", "Lesson / Mentor Plan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.student_to_do), _translate("MainWindow", "To do List"))
        self.label_lesson_status.setText(_translate("MainWindow", "Lesson Attendance Status"))
        self.label_mentor_status.setText(_translate("MainWindow", "Mentor Meeting Attendance Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.student_attendance), _translate("MainWindow", "Attendance Status"))
        self.chat_list.setItemText(0, _translate("MainWindow", "Please Select Person:"))
        self.chat_list.setItemText(1, _translate("MainWindow", "None"))
        self.chat_list.setItemText(2, _translate("MainWindow", "None"))
        self.chat_list.setItemText(3, _translate("MainWindow", "None"))
        self.chat_list.setItemText(4, _translate("MainWindow", "None"))
        self.chat_list.setItemText(5, _translate("MainWindow", "None"))
        self.chat_list.setItemText(6, _translate("MainWindow", "None"))
        self.chat_list.setItemText(7, _translate("MainWindow", "None"))
        self.chat_list.setItemText(8, _translate("MainWindow", "None"))
        self.chat_list.setItemText(9, _translate("MainWindow", "None"))
        self.chat_list.setItemText(10, _translate("MainWindow", "None"))
        self.student_chat_send_button.setText(_translate("MainWindow", "SEND"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.student_dance), _translate("MainWindow", "Chat"))
