import sqlite3
import csv


def export_phones():
    con = sqlite3.connect('database/phone_directory.db')
    cursor = con.cursor()
    data = cursor.execute('''SELECT users.fio, users.birthday, users.city, users.address,
                            phones.phone_number, types_of_number.type_of_number 
                            FROM directory
                            JOIN users ON users.id = directory.user_id 
                            JOIN phones ON phones.id = directory.phone_id
                            JOIN types_of_number ON types_of_number.id = phones.type_id
                            ORDER BY users.fio
                            ''').fetchall()
    result_dictionary = {}
    for element in data:
        if f'{element[0]}' not in result_dictionary:
            result_dictionary[f'{element[0]}'] = (element[4], element[5])
        else:
            result_dictionary[f'{element[0]}'] += (element[4], element[5])
    with open('export.csv', mode="w", encoding='utf-8') as export_file:
        file_writer = csv.writer(export_file, delimiter=';', lineterminator="\r")
        file_writer.writerow(["Фамилия Имя", "Номер телефона", "Тип контакта"])
        for key, data in result_dictionary.items():
            row = [key]
            for item in data:
                row.append(item)
            file_writer.writerow(row)
    con.close()

