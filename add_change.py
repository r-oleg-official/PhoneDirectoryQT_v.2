import os
import sys
import sqlite3

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow
from forms.change_contact import Ui_Form
from add_contact import AddContact


class AddChangeWindow(QMainWindow, Ui_Form):
    def __init__(self, title='Заголовок', btn_text='Добавить', data=None):
        super().__init__()
        self.add_contact_window = None
        self.setupUi(self)
        self.list_of_numbers = []
        self.birthday_edit.setDate(QtCore.QDate.currentDate())
        self.setWindowTitle(title)
        self.btn_move.setText(btn_text)
        self.btn_move.clicked.connect(self.move_some)
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_add_contact.clicked.connect(self.add_contact)

    def add_contact(self):
        self.list_of_numbers.append(AddContact().run())
        print(self.list_of_numbers)
        for items in range(len(self.list_of_numbers)):
            self.contact_table.setRowCount(len(self.list_of_numbers))
            for j, elem in enumerate(self.list_of_numbers[items]):
                self.contact_table.setItem(items, j, QtWidgets.QTableWidgetItem(elem))

    def move_some(self):
        con = sqlite3.connect('database/phone_directory.db')
        cursor = con.cursor()
        fio = f'{self.line_surname.text()} {self.line_name.text()} {self.line_third.text()}'
        birthday = self.birthday_edit.dateTime().toString('dd.MM.yyyy')
        city = self.line_city.text()
        address = self.line_address.text()
        comment = self.line_comment.text()
        info = self.additional_info_text.toPlainText()
        # phone = input('Введите номер телефона: ')
        # phone_type = cursor.execute('''SELECT id, type_of_number FROM types_of_number ''').fetchall()
        # print('Выберите тип контакта:')
        # for i in range(len(phone_type)):
        #     print(f'{phone_type[i][0]}. {phone_type[i][1]}')
        # contact_type = int(input())
        print(self.list_of_numbers)
        check_contact = '''SELECT id, fio FROM users WHERE fio = ?'''
        check_user_data = cursor.execute(check_contact, (fio,)).fetchone()
        contact_type, phone = None, None

        if check_user_data:
            reply = QtWidgets.QMessageBox.question(None, 'Указанный контакт обнаружен!',
                                                   'Обновить информацию?',
                                                   QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.No:
                return
            else:
                print(self.list_of_numbers)
                for item in self.list_of_numbers:
                    if item[0] == 'Мобильный':
                        contact_type = 1
                    elif item[0] == 'Рабочий':
                        contact_type = 2
                    elif item[0] == 'Домашний':
                        contact_type = 3
                    phone = item[1]
                    phone_add_query = '''INSERT INTO phones (phone_number, type_id) VALUES (?, ?);'''
                    cursor.execute(phone_add_query, (phone, contact_type))
                    con.commit()
                    phone_id_query = '''SELECT id FROM phones WHERE phone_number = ?'''
                    phone_id_data = cursor.execute(phone_id_query, (phone,)).fetchone()
                    add_contact = '''INSERT INTO directory (phone_id, user_id) VALUES (?, ?)'''
                    cursor.execute(add_contact, (phone_id_data[0], check_user_data[0]))
                    con.commit()
        else:
            user_add_query = '''INSERT INTO users (fio, birthday, city, address, comment, info) 
                            VALUES (?, ?, ?, ?, ?, ?);'''
            data = (fio, birthday, city, address, comment, info)
            cursor.execute(user_add_query, data)
            con.commit()
            for item in self.list_of_numbers:
                if item[0] == 'Мобильный':
                    contact_type = 1
                elif item[0] == 'Рабочий':
                    contact_type = 2
                elif item[0] == 'Домашний':
                    contact_type = 3
                phone = item[1]
                phone_add_query = '''INSERT INTO phones (phone_number, type_id) VALUES (?, ?);'''
                cursor.execute(phone_add_query, (phone, contact_type))
                con.commit()
            user_id_query = '''SELECT id FROM users WHERE fio = ?'''
            user_id_data = cursor.execute(user_id_query, data[0]).fetchone()
            phone_id_query = '''SELECT id FROM phones WHERE phone_number = ?'''
            phone_id_data = cursor.execute(phone_id_query, (phone,)).fetchone()
            add_contact = '''INSERT INTO directory (phone_id, user_id) VALUES (?, ?)'''
            cursor.execute(add_contact, (phone_id_data[0], user_id_data[0]))
            con.commit()
        self.close()
        con.close()

    def cancel(self):
        self.close()
