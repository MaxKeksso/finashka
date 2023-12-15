import csv
import module_task_2

data = []


def save_table(external_data=None):
    global data
    if external_data == None:
        external_data = data
    try:
        with open("таблица_csv.csv", 'w', encoding='UTF-8', newline='') as file_csv:
            file = "таблица_csv.csv"
            csv_w = csv.writer(file_csv, dialect='excel', delimiter=';')
            for i in external_data:
                csv_w.writerow(i)
        if '.csv' not in file:
            raise Exception('Неверно введено название файла')
    except IOError:
        print('Неверно введено название файла')


def load_table():
    global data
    try:
        fileName = "таблица_csv.csv"
        if fileName.isdigit():
            raise Exception('Неверно введено название файла')
        with open(fileName, 'r', encoding='UTF-8') as file_csv:
            csv_r = csv.reader(file_csv, dialect='excel', delimiter=';')
            for row in csv_r:
                data.append(row)
    except FileNotFoundError:
        print('Запрашиваемый файл не найден')


def get_rows_by_number(start, stop=0, copy_table=False):
    return module_task_2.get_rows_by_number(data, start, stop, copy_table)


def get_rows_by_index(*vals, copy_table=False):
    return module_task_2.get_rows_by_index(*vals, data=data, copy_table=copy_table)


def get_column_types(by_number=True):
    return module_task_2.get_column_types(data, by_number)


def set_column_types(types_dict, by_number=True):
    return module_task_2.set_column_types(types_dict, data, by_number)


def get_values(column=0):
    return module_task_2.get_values(data, column)


def set_values(*values, column=0):
    return module_task_2.set_values(*values, data=data, column=column)


def get_value(column=0):
    return module_task_2.get_value(data, column)


def set_value(value, column=0):
    return module_task_2.set_value(value, data, column=column)


def print_table(external_data=None):
    if external_data:
        module_task_2.print_table(external_data)
    else:
        module_task_2.print_table(data)
