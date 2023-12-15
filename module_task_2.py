def get_rows_by_number(data, start, stop=None, copy_table=False):
    if start < 0 or start >= len(data):
        raise ValueError("Неверный номер строки")
    if copy_table:
        res = []
        for i in range(start - 1, stop if stop != 0 and stop is not None else len(data) - 1):
            res.append(data[i])
        return res
    else:
        if stop is None or stop == 0:
            return data[start - 1:]
        else:
            return data[start - 1: stop]


def get_rows_by_index(*vals, data, copy_table=False):
    # if type(vals) != str:
    #     raise TypeError('Неверные значения. В данной таблице значения должны быть строкой')
    list = []
    for i in data:
        if i[0] in vals:
            list.append(i[:] if copy_table else i)
    return list


def get_column_types(data, by_number=True):
    # if by_number != True or by_number != False:
    #     raise ValueError('by_number должен быть либо True, либо False')
    d = {}
    if by_number:
        for i, s in enumerate(data[1]):
            if type(s) == str:
                if s.isnumeric():
                    d[i + 1] = int
                elif s.isnumeric() and '.' in s:
                    d[i + 1] = float
                elif s == "True" or s == "False":
                    d[i + 1] = bool
                else:
                    d[i + 1] = str
            else:
                d[i + 1] = type(s)
    else:
        for i, s in enumerate(data[1::]):
            ind = 0
            for val in s:
                if type(val) == str:
                    if val.isnumeric():
                        d[data[0][ind]] = int
                    elif '.' in val:
                        d[data[0][ind]] = float
                    elif val == 'True' or val == 'False':
                        d[data[0][ind]] = bool
                    else:
                        d[data[0][ind]] = str
                else:
                    d[data[0][ind]] = type(val)
                ind += 1
    return d


def set_column_types(types_dict, data, by_number=True):
    # if len(types_dict) != len(data[0]):
    #     raise Exception('У нас всего 5 столбцов!')
    for col in types_dict.keys():
        if by_number:
            column = col
            col_type = types_dict[column]
        else:
            column = data[0].index(col)
            col_type = types_dict[list(types_dict.keys())[column]]
        for row in data:
            if data[0] == row:
                continue
            if col_type == 'str':
                row[column] = str(row[column])
            if col_type == 'int':
                row[column] = int(row[column])
            if col_type == 'float':
                row[column] = float(row[column])
            if col_type == 'bool':
                row[column] = True if row[column] == "True" else False

    return data


def get_values(data, column=0):
    # if column < 0 or column >= len(data[0]):
    #     raise ValueError("Неверный номер столбца")
    list = []
    if type(column) == str:
        for header in data[0]:
            if header in data[0]:
                if header == column:
                    index = data[0].index(header)
                    for spisok in data:
                        list.append(spisok[index])
                    return list
                else:
                    continue
            else:
                return 'Такого названия в таблице нет'
    else:
        for spisok in data:
            list.append(spisok[column])
        return list


def set_values(*values, data, column=0):
    # if column < 0 or column >= len(data[0]):
    #     raise ValueError("Неверный номер столбца")
    list = get_values(data, column)
    head = list[0]
    for index, value in enumerate(values):
        if value != head:
            list[index + 1] = value
        else:
            continue
    return list


def get_value(data, column=0):
    # if column < 0 or column >= len(data[0]):
    #     raise ValueError("Неверный номер столбца")
    list = []
    if type(column) == str:
        for header in data[0]:
            if header in data[0]:
                if header == column:
                    index = data[0].index(header)
                    list.append(header)
                    for value in data[1]:
                        if data[1].index(value) == index:
                            list.append(value)
                        else:
                            continue
                    return list
                else:
                    continue
            else:
                return 'Такого названия в таблице нет'
    else:
        list.append(f'Столбец номер {column}: ')
        for value in data[1]:
            if data[1].index(value) == column:
                list.append(value)
        return list


def set_value(value, data, column):
    # if column < 0 or column >= len(data[0]):
    #     raise ValueError("Неверный номер столбца")
    # if type(value) != int or type(value) != str or type(value) != float or type(value) != bool:
    #     raise Exception('Такой тип таблица не поддерживает')
    list = get_value(data, column)
    list[1] = value
    return list


def print_table(data):
    if data == [] or data == None:
        raise Exception('Проверьте data, видимо она пустая')
    for row in data:
        print(*row, sep=' ')
