import pickle
import module_task_2

data = []


def save_table(data):
    try:
        fileName = "таблица_pickle.pickle"
        if fileName.isdigit():
            raise Exception('Неверно введено название файла')
        with open("таблица_pickle.pickle", 'wb') as file_pickle:
            pickle.dump(data, file_pickle)
    except IOError:
        print('Неверно введено название файла')


def load_table():
    fileName = "таблица_pickle.pickle"
    if fileName.isdigit():
        raise Exception('Неверно введено название файла')
    with open("таблица_pickle.pickle", 'rb') as file_pickle:
        global data
        data = pickle.load(file_pickle)
        return data


def get_rows_by_number(start, stop=0, copy_table=False):
    return module_task_2.get_rows_by_number(data, start, stop, copy_table)


def get_rows_by_index(*vals, copy_table=False):
    return module_task_2.get_rows_by_index(*vals, data=data, copy_table=False)


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
