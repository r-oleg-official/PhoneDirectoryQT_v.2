# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\add_contact.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(499, 82)
        Dialog.setMinimumSize(QtCore.QSize(499, 82))
        Dialog.setMaximumSize(QtCore.QSize(499, 82))
        Dialog.setStyleSheet("background:rgb(102, 207, 255)")
        self.lbl_phonenumber = QtWidgets.QLabel(Dialog)
        self.lbl_phonenumber.setGeometry(QtCore.QRect(237, 20, 88, 16))
        self.lbl_phonenumber.setObjectName("lbl_phonenumber")
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_cancel.setGeometry(QtCore.QRect(380, 50, 105, 23))
        self.btn_cancel.setStyleSheet("background:rgb(0, 85, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 75 9pt \"Arial\";")
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_add = QtWidgets.QPushButton(Dialog)
        self.btn_add.setGeometry(QtCore.QRect(270, 50, 105, 23))
        self.btn_add.setStyleSheet("background:rgb(0, 85, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 75 9pt \"Arial\";")
        self.btn_add.setObjectName("btn_add")
        self.lbl_type = QtWidgets.QLabel(Dialog)
        self.lbl_type.setGeometry(QtCore.QRect(10, 20, 73, 16))
        self.lbl_type.setObjectName("lbl_type")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(88, 20, 131, 18))
        self.comboBox.setStyleSheet("background:rgb(255, 255, 255)")
        self.comboBox.setObjectName("comboBox")
        self.line_phonenumber = QtWidgets.QLineEdit(Dialog)
        self.line_phonenumber.setGeometry(QtCore.QRect(330, 20, 161, 21))
        self.line_phonenumber.setStyleSheet("background:rgb(255, 255, 255)")
        self.line_phonenumber.setObjectName("line_phonenumber")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавление контакта"))
        self.lbl_phonenumber.setText(_translate("Dialog", "Номер телефона:"))
        self.btn_cancel.setText(_translate("Dialog", "Отменить"))
        self.btn_add.setText(_translate("Dialog", "Добавить"))
        self.lbl_type.setText(_translate("Dialog", "Тип контакта:"))
