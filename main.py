import os
import sys
import sqlite3

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from forms.main_form import Ui_MainWindow
from add_change import AddChangeWindow
from export import export_phones


class PhoneDirectory(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.phone_numbers = None
        self.additional_info = None
        self.additional_info_dictionary = {'FIO': '', 'City': '', 'Address': '', 'Comment': '', 'Info': ''}
        self.all_data = {}
        self.setupUi(self)
        self.con = sqlite3.connect('./database/phone_directory.db')
        self.btn_add.clicked.connect(self.add_contact)
        self.btn_change.clicked.connect(self.add_change)
        self.btn_delete.clicked.connect(self.delete_contact)
        self.all_info_table.cellClicked.connect(self.table_checked)
        self.btn_export.clicked.connect(self.export)
        # self.all_info_table.ite.connect(self.phones_view)
        self.add_window = None
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icon.png"))
        self.setWindowIcon(icon)
        self.phones_view()

    def add_contact(self):
        self.add_window = AddChangeWindow('Добавление контакта')
        self.add_window.show()

    def add_change(self):
        self.add_window = AddChangeWindow('Изменение контакта', 'Изменить')
        self.add_window.show()

    def phones_view(self):
        cursor = self.con.cursor()
        data_from_base = cursor.execute('''SELECT users.id, users.fio, users.birthday,
                                        phones.phone_number, types_of_number.id 
                                FROM directory
                                JOIN users ON users.id = directory.user_id 
                                JOIN phones ON phones.id = directory.phone_id
                                JOIN types_of_number ON types_of_number.id = phones.type_id
                                GROUP BY users.fio ORDER BY users.fio
                                ''').fetchall()
        for item in data_from_base:
            element_data = {'id': item[0], 'birthday': item[2], 'phones': []}
            self.all_data[item[1]] = element_data
        self.phone_numbers = cursor.execute('''SELECT users.fio, phones.phone_number, types_of_number.id
                                            FROM directory 
                                            JOIN users ON users.id = directory.user_id
                                            JOIN phones ON phones.id = directory.phone_id
                                            JOIN types_of_number ON types_of_number.id = phones.type_id''').fetchall()
        for item in self.phone_numbers:
            self.all_data[item[0]]['phones'].append((item[1], item[2]))
        self.additional_info = cursor.execute('''SELECT * FROM users ORDER BY users.fio''').fetchall()
        cursor.close()
        data_to_table_widget = []
        for key, item in self.all_data.items():
            element = [key, item['birthday'], '', '', '']
            for phone_number in item['phones']:
                if phone_number[1] == 1:
                    element[2] = phone_number[0]
                elif phone_number[1] == 2:
                    element[3] = phone_number[0]
                elif phone_number[1] == 3:
                    element[4] = phone_number[0]
            data_to_table_widget.append(element)
        for items in range(len(data_to_table_widget)):
            self.all_info_table.setRowCount(len(data_to_table_widget))
            for j, elem in enumerate(data_to_table_widget[items]):
                self.all_info_table.setItem(items, j, QtWidgets.QTableWidgetItem(elem))

    def delete_contact(self):
        current_user = self.all_info_table.selectedItems()
        print(current_user[0].text())

    def table_checked(self):
        row_index = self.all_info_table.currentRow()
        self.additional_info_dictionary['FIO'] = self.additional_info[row_index][1]
        self.additional_info_dictionary['City'] = self.additional_info[row_index][3]
        self.additional_info_dictionary['Address'] = self.additional_info[row_index][4]
        self.additional_info_dictionary['Comment'] = self.additional_info[row_index][5]
        self.additional_info_dictionary['Info'] = self.additional_info[row_index][6]
        self.city_edit.setText(self.additional_info_dictionary['City'])
        self.address_edit.setText(self.additional_info_dictionary['Address'])
        self.comment_text.setText(self.additional_info_dictionary['Comment'])
        self.additional_info_text.setText(self.additional_info_dictionary['Info'])
        contact_phones = self.all_data[self.additional_info[row_index][1]]['phones']
        phones_to_contact_table = []
        for item in contact_phones:
            elem = []
            if item[1] == 1:
                elem.append('Мобильный')
                elem.append(item[0])
            elif item[1] == 2:
                elem.append('Рабочий')
                elem.append(item[0])
            elif item[1] == 3:
                elem.append('Домашний')
                elem.append(item[0])
            phones_to_contact_table.append(elem)
        phones_to_contact_table.sort()
        for items in range(len(phones_to_contact_table)):
            self.contact_table.setRowCount(len(phones_to_contact_table))
            for j, elem in enumerate(phones_to_contact_table[items]):
                self.contact_table.setItem(items, j, QtWidgets.QTableWidgetItem(elem))
        self.phones_view()

    def export(self):
        export_phones()
        reply = QtWidgets.QMessageBox.information(None, 'Успешное завершение!',
                                               'Экспорт успешно завершен!',
                                               QtWidgets.QMessageBox.Yes)
        if reply == QtWidgets.QMessageBox.Yes:
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PhoneDirectory()
    ex.show()
    sys.exit(app.exec())
