import os
import sys
import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from forms.change_contact import Ui_Form
from forms.add_contact_window import Ui_Dialog


class AddContact(QDialog, Ui_Dialog):
    def __init__(self):
        super(AddContact, self).__init__()
        cursor = sqlite3.connect('database/phone_directory.db')
        self.setupUi(self)
        list_of_types = cursor.execute('''SELECT * FROM types_of_number''').fetchall()
        self.comboBox.addItems(list(map(lambda x: x[1], list_of_types)))
        self.comboBox.setCurrentIndex(0)
        self.btn_add.clicked.connect(self.run)
        self.btn_cancel.clicked.connect(self.cancel)
        cursor.close()

    def run(self):
        self.exec()
        contact_type = self.comboBox.currentText()
        contact_number = self.line_phonenumber.text()
        self.close()
        return self.view_data(contact_type, contact_number)

    def view_data(self, contact_type, contact_number):
        return contact_type, contact_number

    def cancel(self):
        self.close()
        return None


    # def number(self, contact_type=1, contact_number=1):
    #     print(contact_type, contact_number)

    def cancel(self):
        self.close()
