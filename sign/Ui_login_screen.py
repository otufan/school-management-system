# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/onur/Documents/GitHub/school-management-system/sign/login_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 500)
        Form.setMinimumSize(QtCore.QSize(600, 500))
        Form.setMaximumSize(QtCore.QSize(600, 500))
        Form.setStyleSheet("background-color: rgb(10, 98, 38);")
        self.enter_Button = QtWidgets.QPushButton(Form)
        self.enter_Button.setGeometry(QtCore.QRect(370, 330, 100, 50))
        self.enter_Button.setMinimumSize(QtCore.QSize(100, 50))
        self.enter_Button.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.enter_Button.setFont(font)
        self.enter_Button.setStyleSheet("background-color: rgb(249, 186, 50);\n"
"border-color: rgb(0, 0, 0);")
        self.enter_Button.setObjectName("enter_Button")
        self.email_label = QtWidgets.QLabel(Form)
        self.email_label.setGeometry(QtCore.QRect(50, 160, 150, 30))
        self.email_label.setMinimumSize(QtCore.QSize(150, 30))
        self.email_label.setMaximumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("background-color: rgb(249, 186, 50);")
        self.email_label.setObjectName("email_label")
        self.password_label = QtWidgets.QLabel(Form)
        self.password_label.setGeometry(QtCore.QRect(50, 240, 150, 30))
        self.password_label.setMinimumSize(QtCore.QSize(150, 30))
        self.password_label.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("background-color: rgb(249, 186, 50);")
        self.password_label.setObjectName("password_label")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(220, 240, 250, 30))
        self.password.setMinimumSize(QtCore.QSize(250, 30))
        self.password.setMaximumSize(QtCore.QSize(250, 30))
        self.password.setStyleSheet("background-color: rgb(249, 186, 50);")
        self.password.setMaxLength(8)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.email = QtWidgets.QLineEdit(Form)
        self.email.setGeometry(QtCore.QRect(220, 160, 250, 30))
        self.email.setMinimumSize(QtCore.QSize(250, 30))
        self.email.setMaximumSize(QtCore.QSize(250, 30))
        self.email.setStyleSheet("background-color: rgb(249, 186, 50);")
        self.email.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.email.setObjectName("email")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.enter_Button.setText(_translate("Form", "Enter"))
        self.email_label.setText(_translate("Form", "E-mail Adress:"))
        self.password_label.setText(_translate("Form", "Password:"))
