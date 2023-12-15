import re
import math

symbols = {
    "плюс": "+",
    "минус": "-",
    "умножить": "*",
}
dct_1 = {ch: ch1 for ch1, ch in enumerate(
    'один два три четыре пять шесть семь восемь девять десять одиннадцать двенадцать тринадцать четырнадцать пятнадцать шестнадцать семнадцать восемнадцать девятнадцать'.split(),
    1)}
dct_10 = {ch: 10 * ch1 for ch1, ch in
          enumerate(' двадцать тридцать сорок пятьдесят шестьдесят семьдесят восемьдесят девяносто'.split(), 2)}
dct_100 = {ch: 100 * ch1 for ch1, ch in
           enumerate('сто двести триста четыреста пятьсот шестьсот семьсот восемьсот девятьсот'.split(), 1)}
o_dct = {**symbols, **dct_1, **dct_10, **dct_100}

yravn = input('Введите ваше уравнение, а мы все решим ;): ').lower()

new_yravn = []
for i in yravn.split():  # убираем НА из умножения
    if i != 'на':
        new_yravn.append(i)
d = 0
for i in new_yravn:  # находим цифры и знаки
    if type(o_dct[i]) == int:
        d += o_dct[i]
    else:
        rez = d
        oper = o_dct[i]
        d = 0

if oper == '+':  # реализовываем операции
    rez += d
elif oper == '-':
    rez -= d
else:
    rez *= d

dct_text = {ch: ch1 for ch1, ch in o_dct.items()}

text = []
if rez < 0:  # отдельные случаи (уход в отрицательные числа) и ноль
    text.append('минус')
    rez *= -1
elif rez == 0:
    text.append('ноль')

l = 100
while l:  # перевод числа в его разряды
    if rez > l - 1:
        if rez > 20:
            text.append(dct_text[rez // l * l])
            rez %= l
        else:
            text.append(dct_text[rez])
            l = 0
    l //= 10

print(' '.join(text))  # вывод результата
#
# if 'степени' in operands:  # done
#     # 2**4 23**2
#     step_left_part = operands[:operands.index('в')]
#     step_right_part = operands[operands.index('степени') + 1:]
#
#     for i in range(len(step_left_part)):
#         step_left_array.append(numbers[step_left_part[i]])
#     step_left_rez = sum(step_left_array)
#
#     for i in range(len(step_right_part)):
#         step_right_array.append(numbers[step_right_part[i]])
#     step_right_rez = sum(step_right_array)
#
#     step_rez = step_left_rez ** step_right_rez
#
#     if 0 <= step_rez <= 19:
#         print(numbers[str(step_rez)])
#     elif step_rez > 19 and step_rez % 10 == 0:
#         print(numbers[str(step_rez)])
#     else:
#         for i in range(len(str(step_rez))):
#             array.append(int(str(step_rez)[i]) * (10 ** (len(str(step_rez)) - i - 1)))
#         for el in array:
#             ans_1 += numbers[str(el)] + ' '
#         print(ans_1)
#
# if 'делить' in operands and 'синус' not in operands and 'косинус' not in operands and 'тангенс' not in operands:  # done
#     # print(41.31/17, 41.31/5.28, 11/10, 41/17.28)
#     for i in range(0, operands.index('делить')):
#         if operands[i] in numbers:
#             left_part.append(numbers[operands[i]])
#     for i in range(operands.index('делить') + 1, len(operands)):
#         if operands[i] in numbers:
#             right_part.append(numbers[operands[i]])
#
#     if ',' in left_part:
#         num_1 = sum(left_part[:left_part.index(',')])
#         num_2 = sum(left_part[left_part.index(',') + 1:])
#         if len(str(num_2)) == 2:
#             num_2 = num_2 / 100
#         if len(str(num_2)) == 1:
#             num_2 = num_2 / 10
#         ans_del_1 = num_1 + num_2
#     else:
#         ans_del_1 = sum(left_part)
#
#     if ',' in right_part:
#         num_3 = sum(right_part[:right_part.index(',')])
#         num_4 = sum(right_part[right_part.index(',') + 1:])
#         if len(str(num_4)) == 2:
#             num_4 = num_4 / 100
#         if len(str(num_4)) == 1:
#             num_4 = num_4 / 10
#         ans_del_2 = num_3 + num_4
#     else:
#         ans_del_2 = sum(right_part)
#
#     rez = round(ans_del_1 / ans_del_2, 3)
#
#     if '.' in str(rez):
#         left_rez, right_rez = str(rez).split('.')
#         left_rez = int(left_rez)
#         right_rez = int(right_rez)
#
#         if 0 <= left_rez <= 19:
#             total = numbers[str(left_rez)]
#             if total == 'две':
#                 total = 'два'
#             if total == 'одна':
#                 total = 'один'
#         elif left_rez > 19 and left_rez % 10 == 0:
#             total = numbers[str(left_rez)]
#             if total == 'две':
#                 total = 'два'
#             if total == 'одна':
#                 total = 'один'
#         else:
#             for i in range(len(str(left_rez))):
#                 array.append(int(str(left_rez)[i]) * (10 ** (len(str(left_rez)) - i - 1)))
#             for el in array:
#                 ans_rez_1 += numbers[str(el)] + ' '
#             total = ans_rez_1
#             if total == 'две':
#                 total = 'два'
#             if total == 'одна':
#                 total = 'один'
#
#         if 0 <= right_rez <= 19:
#             total_2 = numbers[str(right_rez)]
#         elif right_rez > 19 and right_rez % 10 == 0:
#             total_2 = numbers[str(right_rez)]
#         else:
#             for i in range(len(str(right_rez))):
#                 array.append(int(str(right_rez)[i]) * (10 ** (len(str(right_rez)) - i - 1)))
#             for el in array:
#                 ans_rez_2 += numbers[str(el)] + ' '
#             total_2 = ans_rez_2
#
#     if total_2.count(' ') == 0 and ('одна' in total_2):
#         ans_total = total + ' и ' + total_2 + ' десятая'
#     elif total_2.count(' ') == 0:
#         ans_total = total + ' и ' + total_2 + ' десятых'
#     elif total_2.count(' ') == 2 and ('одна' in total_2):
#         ans_total = total + ' и ' + total_2 + 'сотая'
#     elif total_2.count(' ') == 2:
#         ans_total = total + ' и ' + total_2 + 'сотых'
#
#     elif total_2.count(' ') == 3 and ('одна' in total_2):
#         ans_total = total + ' и ' + total_2 + 'тысячная'
#     elif total_2.count(' ') == 3:
#         ans_total = total + ' и ' + total_2 + 'тысячных'
#
#     print(ans_total)
#
# if 'синус' in operands:  # done
#     if 'делить' in operands:  # синус от пи делить на четыре
#         left_part = operands[operands.index('от') + 1:operands.index('делить')]
#         right_part = operands[operands.index('на') + 1:]
#
#         for i in range(len(left_part)):
#             left_array.append(numbers[left_part[i]])
#         total_left = sum(left_array)
#
#         for i in range(len(right_part)):
#             right_array.append(numbers[right_part[i]])
#         total_right = sum(right_array)
#
#         rez = round(math.sin(total_left / total_right), 3)
#
#         if '.' in str(rez):
#             left_rez, right_rez = str(rez).split('.')
#             left_rez = int(left_rez)
#             right_rez = int(right_rez)
#
#             if 0 <= left_rez <= 19:
#                 total = numbers[str(left_rez)]
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             elif left_rez > 19 and left_rez % 10 == 0:
#                 total = numbers[str(left_rez)]
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             else:
#                 for i in range(len(str(left_rez))):
#                     array.append(int(str(left_rez)[i]) * (10 ** (len(str(left_rez)) - i - 1)))
#                 for el in array:
#                     ans_rez_1 += numbers[str(el)] + ' '
#                 total = ans_rez_1
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             if 0 <= right_rez <= 19:
#                 total_2 = numbers[str(right_rez)]
#
#             elif right_rez > 19 and right_rez % 10 == 0:
#                 total_2 = numbers[str(right_rez)]
#
#             else:
#                 for i in range(len(str(right_rez))):
#                     array.append(int(str(right_rez)[i]) * (10 ** (len(str(right_rez)) - i - 1)))
#                 for el in array:
#                     ans_rez_2 += numbers[str(el)] + ' '
#                 total_2 = ans_rez_2
#
#             if 'ноль' in total_2:
#                 total_2 = total_2[:total_2.index('ноль')] + total_2[total_2.index('ноль') + 4:]
#
#             if total_2.count(' ') == 0 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + ' десятая'
#
#             elif total_2.count(' ') == 0:
#                 ans_total = total + ' и ' + total_2 + ' десятых'
#
#             elif total_2.count(' ') == 2 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + 'сотая'
#
#             elif total_2.count(' ') == 2:
#                 ans_total = total + ' и ' + total_2 + 'сотых'
#
#             elif total_2.count(' ') == 3 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + 'тысячная'
#
#             elif total_2.count(' ') == 3:
#                 ans_total = total + ' и ' + total_2 + 'тысячных'
#
#             print(ans_total)
#
#     if 'умножить' in operands:  # синус от двадцать пять умножить на двадцать девять
#         left_part = operands[operands.index('от') + 1:operands.index('умножить')]
#         right_part = operands[operands.index('на') + 1:]
#
#         for i in range(len(left_part)):
#             left_array.append(numbers[left_part[i]])
#         total_left = sum(left_array)
#
#         for i in range(len(right_part)):
#             right_array.append(numbers[right_part[i]])
#         total_right = sum(right_array)
#
#         rez = round(math.sin(total_left * total_right), 3)
#
#         if '.' in str(rez):
#             left_rez, right_rez = str(rez).split('.')
#             left_rez = int(left_rez)
#             right_rez = int(right_rez)
#
#             if 0 <= left_rez <= 19:
#                 total = numbers[str(left_rez)]
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             elif left_rez > 19 and left_rez % 10 == 0:
#                 total = numbers[str(left_rez)]
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             else:
#                 for i in range(len(str(left_rez))):
#                     array.append(int(str(left_rez)[i]) * (10 ** (len(str(left_rez)) - i - 1)))
#                 for el in array:
#                     ans_rez_1 += numbers[str(el)] + ' '
#                 total = ans_rez_1
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             if 0 <= right_rez <= 19:
#                 total_2 = numbers[str(right_rez)]
#
#             elif right_rez > 19 and right_rez % 10 == 0:
#                 total_2 = numbers[str(right_rez)]
#
#             else:
#                 for i in range(len(str(right_rez))):
#                     array.append(int(str(right_rez)[i]) * (10 ** (len(str(right_rez)) - i - 1)))
#                 for el in array:
#                     ans_rez_2 += numbers[str(el)] + ' '
#                 total_2 = ans_rez_2
#
#             if 'ноль' in total_2:
#                 total_2 = total_2[:total_2.index('ноль')] + total_2[total_2.index('ноль') + 4:]
#
#             if total_2.count(' ') == 0 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + ' десятая'
#
#             elif total_2.count(' ') == 0:
#                 ans_total = total + ' и ' + total_2 + ' десятых'
#
#             elif total_2.count(' ') == 2 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + 'сотая'
#
#             elif total_2.count(' ') == 2:
#                 ans_total = total + ' и ' + total_2 + 'сотых'
#
#             elif total_2.count(' ') == 3 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + 'тысячная'
#
#             elif total_2.count(' ') == 3:
#                 ans_total = total + ' и ' + total_2 + 'тысячных'
#
#             print(ans_total)
#
# if 'косинус' in operands:  # done
#     if 'делить' in operands:  # косинус от пятнадцать делить на двадцать три
#         left_part = operands[operands.index('от') + 1:operands.index('делить')]
#         right_part = operands[operands.index('на') + 1:]
#
#         for i in range(len(left_part)):
#             left_array.append(numbers[left_part[i]])
#         total_left = sum(left_array)
#
#         for i in range(len(right_part)):
#             right_array.append(numbers[right_part[i]])
#         total_right = sum(right_array)
#
#         rez = round(math.cos(total_left / total_right), 3)
#
#         if '.' in str(rez):
#             left_rez, right_rez = str(rez).split('.')
#             left_rez = int(left_rez)
#             right_rez = int(right_rez)
#
#             if 0 <= left_rez <= 19:
#                 total = numbers[str(left_rez)]
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             elif left_rez > 19 and left_rez % 10 == 0:
#                 total = numbers[str(left_rez)]
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             else:
#                 for i in range(len(str(left_rez))):
#                     array.append(int(str(left_rez)[i]) * (10 ** (len(str(left_rez)) - i - 1)))
#                 for el in array:
#                     ans_rez_1 += numbers[str(el)] + ' '
#                 total = ans_rez_1
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             if 0 <= right_rez <= 19:
#                 total_2 = numbers[str(right_rez)]
#
#             elif right_rez > 19 and right_rez % 10 == 0:
#                 total_2 = numbers[str(right_rez)]
#
#             else:
#                 for i in range(len(str(right_rez))):
#                     array.append(int(str(right_rez)[i]) * (10 ** (len(str(right_rez)) - i - 1)))
#                 for el in array:
#                     ans_rez_2 += numbers[str(el)] + ' '
#                 total_2 = ans_rez_2
#
#             if 'ноль' in total_2:
#                 total_2 = total_2[:total_2.index('ноль')] + total_2[total_2.index('ноль') + 4:]
#
#             if total_2.count(' ') == 0 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + ' десятая'
#
#             elif total_2.count(' ') == 0:
#                 ans_total = total + ' и ' + total_2 + ' десятых'
#
#             elif total_2.count(' ') == 2 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + 'сотая'
#
#             elif total_2.count(' ') == 2:
#                 ans_total = total + ' и ' + total_2 + 'сотых'
#
#             elif total_2.count(' ') == 3 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + 'тысячная'
#
#             elif total_2.count(' ') == 3:
#                 ans_total = total + ' и ' + total_2 + 'тысячных'
#
#             print(ans_total)
#
#     if 'умножить' in operands:  # косинус от пятнадцать умножить на три
#         left_part = operands[operands.index('от') + 1:operands.index('умножить')]
#         right_part = operands[operands.index('на') + 1:]
#
#         for i in range(len(left_part)):
#             left_array.append(numbers[left_part[i]])
#         total_left = sum(left_array)
#
#         for i in range(len(right_part)):
#             right_array.append(numbers[right_part[i]])
#         total_right = sum(right_array)
#
#         rez = round(math.cos(total_left * total_right), 3)
#
#         if '.' in str(rez):
#             left_rez, right_rez = str(rez).split('.')
#             left_rez = int(left_rez)
#             right_rez = int(right_rez)
#
#             if 0 <= left_rez <= 19:
#                 total = numbers[str(left_rez)]
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             elif left_rez > 19 and left_rez % 10 == 0:
#                 total = numbers[str(left_rez)]
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             else:
#                 for i in range(len(str(left_rez))):
#                     array.append(int(str(left_rez)[i]) * (10 ** (len(str(left_rez)) - i - 1)))
#                 for el in array:
#                     ans_rez_1 += numbers[str(el)] + ' '
#                 total = ans_rez_1
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             if 0 <= right_rez <= 19:
#                 total_2 = numbers[str(right_rez)]
#
#             elif right_rez > 19 and right_rez % 10 == 0:
#                 total_2 = numbers[str(right_rez)]
#
#             else:
#                 for i in range(len(str(right_rez))):
#                     array.append(int(str(right_rez)[i]) * (10 ** (len(str(right_rez)) - i - 1)))
#                 for el in array:
#                     ans_rez_2 += numbers[str(el)] + ' '
#                 total_2 = ans_rez_2
#
#             if 'ноль' in total_2:
#                 total_2 = total_2[:total_2.index('ноль')] + total_2[total_2.index('ноль') + 4:]
#
#             if total_2.count(' ') == 0 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + ' десятая'
#
#             elif total_2.count(' ') == 0:
#                 ans_total = total + ' и ' + total_2 + ' десятых'
#
#             elif total_2.count(' ') == 2 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + 'сотая'
#
#             elif total_2.count(' ') == 2:
#                 ans_total = total + ' и ' + total_2 + 'сотых'
#
#             elif total_2.count(' ') == 3 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + 'тысячная'
#
#             elif total_2.count(' ') == 3:
#                 ans_total = total + ' и ' + total_2 + 'тысячных'
#
#             print(ans_total)
#
# if 'тангенс' in operands:  # done
#     if 'делить' in operands:  # тангенс от пятнадцать делить на двадцать три
#         left_part = operands[operands.index('от') + 1:operands.index('делить')]
#         right_part = operands[operands.index('на') + 1:]
#
#         for i in range(len(left_part)):
#             left_array.append(numbers[left_part[i]])
#         total_left = sum(left_array)
#
#         for i in range(len(right_part)):
#             right_array.append(numbers[right_part[i]])
#         total_right = sum(right_array)
#
#         rez = round(math.tan(total_left / total_right), 3)
#
#         if '.' in str(rez):
#             left_rez, right_rez = str(rez).split('.')
#             left_rez = int(left_rez)
#             right_rez = int(right_rez)
#
#             if 0 <= left_rez <= 19:
#                 total = numbers[str(left_rez)]
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             elif left_rez > 19 and left_rez % 10 == 0:
#                 total = numbers[str(left_rez)]
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             else:
#                 for i in range(len(str(left_rez))):
#                     array.append(int(str(left_rez)[i]) * (10 ** (len(str(left_rez)) - i - 1)))
#                 for el in array:
#                     ans_rez_1 += numbers[str(el)] + ' '
#                 total = ans_rez_1
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             if 0 <= right_rez <= 19:
#                 total_2 = numbers[str(right_rez)]
#
#             elif right_rez > 19 and right_rez % 10 == 0:
#                 total_2 = numbers[str(right_rez)]
#
#             else:
#                 for i in range(len(str(right_rez))):
#                     array.append(int(str(right_rez)[i]) * (10 ** (len(str(right_rez)) - i - 1)))
#                 for el in array:
#                     ans_rez_2 += numbers[str(el)] + ' '
#                 total_2 = ans_rez_2
#
#             if 'ноль' in total_2:
#                 total_2 = total_2[:total_2.index('ноль')] + total_2[total_2.index('ноль') + 4:]
#
#             if total_2.count(' ') == 0 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + ' десятая'
#
#             elif total_2.count(' ') == 0:
#                 ans_total = total + ' и ' + total_2 + ' десятых'
#
#             elif total_2.count(' ') == 2 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + 'сотая'
#
#             elif total_2.count(' ') == 2:
#                 ans_total = total + ' и ' + total_2 + 'сотых'
#
#             elif total_2.count(' ') == 3 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + 'тысячная'
#
#             elif total_2.count(' ') == 3:
#                 ans_total = total + ' и ' + total_2 + 'тысячных'
#
#             print(ans_total)
#
#     if 'умножить' in operands:  # тангенс от пятнадцать умножить на тридцать
#         left_part = operands[operands.index('от') + 1:operands.index('умножить')]
#         right_part = operands[operands.index('на') + 1:]
#
#         for i in range(len(left_part)):
#             left_array.append(numbers[left_part[i]])
#         total_left = sum(left_array)
#
#         for i in range(len(right_part)):
#             right_array.append(numbers[right_part[i]])
#         total_right = sum(right_array)
#
#         rez = round(math.tan(total_left * total_right), 3)
#
#         if '.' in str(rez):
#             left_rez, right_rez = str(rez).split('.')
#             left_rez = int(left_rez)
#             right_rez = int(right_rez)
#
#             if 0 <= left_rez <= 19:
#                 total = numbers[str(left_rez)]
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             elif left_rez > 19 and left_rez % 10 == 0:
#                 total = numbers[str(left_rez)]
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             else:
#                 for i in range(len(str(left_rez))):
#                     array.append(int(str(left_rez)[i]) * (10 ** (len(str(left_rez)) - i - 1)))
#                 for el in array:
#                     ans_rez_1 += numbers[str(el)] + ' '
#                 total = ans_rez_1
#                 if total == 'две':
#                     total = 'два'
#                 if total == 'одна':
#                     total = 'один'
#
#             if 0 <= right_rez <= 19:
#                 total_2 = numbers[str(right_rez)]
#
#             elif right_rez > 19 and right_rez % 10 == 0:
#                 total_2 = numbers[str(right_rez)]
#
#             else:
#                 for i in range(len(str(right_rez))):
#                     array.append(int(str(right_rez)[i]) * (10 ** (len(str(right_rez)) - i - 1)))
#                 for el in array:
#                     ans_rez_2 += numbers[str(el)] + ' '
#                 total_2 = ans_rez_2
#
#             if 'ноль' in total_2:
#                 total_2 = total_2[:total_2.index('ноль')] + total_2[total_2.index('ноль') + 4:]
#
#             if total_2.count(' ') == 0 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + ' десятая'
#
#             elif total_2.count(' ') == 0:
#                 ans_total = total + ' и ' + total_2 + ' десятых'
#
#             elif total_2.count(' ') == 2 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + 'сотая'
#
#             elif total_2.count(' ') == 2:
#                 ans_total = total + ' и ' + total_2 + 'сотых'
#
#             elif total_2.count(' ') == 3 and ('одна' in total_2):
#                 ans_total = total + ' и ' + total_2 + 'тысячная'
#
#             elif total_2.count(' ') == 3:
#                 ans_total = total + ' и ' + total_2 + 'тысячных'
#
#             print(ans_total)
#
# if 'перестановка' in operands:  # перестановка с числом шесть
#     part = operands[operands.index('числом') + 1:]
#     for i in range(len(part)):
#         array.append(numbers[part[i]])
#     total = sum(array)
#     rez = math.factorial(total)
#
#     if 0 <= rez <= 19:
#         print(numbers[str(rez)])
#     elif rez > 19 and rez % 100 == 0:
#         print(numbers[str(rez)])
#     else:
#         for i in range(len(str(rez))):
#             rez_array.append(int(str(rez)[i]) * (10 ** (len(str(rez)) - i - 1)))
#         if rez_array[-1] == 0:
#             rez_array = rez_array[:-1]
#         if rez_array[-2] == 0:
#             rez_array = rez_array[:-2] + rez_array[-1:]
#         for el in rez_array:
#             rez_ans += numbers[str(el)] + ' '
#         print(rez_ans)
#
# if 'размещений' in operands:  # размещений из три по два
#     upper_part = operands[operands.index('из') + 1:operands.index('по')]
#     lower_part = operands[operands.index('по') + 1:]
#
#     for i in range(len(upper_part)):
#         upper_array.append(numbers[upper_part[i]])
#     total_upper = sum(upper_array)
#
#     for i in range(len(lower_part)):
#         lower_array.append(numbers[lower_part[i]])
#     total_lower = sum(lower_array)
#     rez = round((math.factorial(total_upper)) / (math.factorial(total_upper - total_lower)))
#
#     if 0 <= rez <= 19:
#         print(numbers[str(rez)])
#     elif rez > 19 and rez % 100 == 0:
#         print(numbers[str(rez)])
#     else:
#         for i in range(len(str(rez))):
#             rez_array.append(int(str(rez)[i]) * (10 ** (len(str(rez)) - i - 1)))
#         if rez_array[-1] == 0:
#             rez_array = rez_array[:-1]
#         if rez_array[-2] == 0:
#             rez_array = rez_array[:-2] + rez_array[-1:]
#         for el in rez_array:
#             rez_ans += numbers[str(el)] + ' '
#         print(rez_ans)
#
# if 'сочетаний' in operands:  # сочетаний из три по пять
#     upper_part = operands[operands.index('из') + 1:operands.index('по')]
#     lower_part = operands[operands.index('по') + 1:]
#
#     for i in range(len(upper_part)):
#         upper_array.append(numbers[upper_part[i]])
#     total_upper = sum(upper_array)
#
#     for i in range(len(lower_part)):
#         lower_array.append(numbers[lower_part[i]])
#     total_lower = sum(lower_array)
#     rez = round(
#         (math.factorial(total_lower)) / ((math.factorial(total_lower - total_upper)) * (math.factorial(total_upper))))
#
#     if 0 <= rez <= 19:
#         print(numbers[str(rez)])
#     elif rez > 19 and rez % 100 == 0:
#         print(numbers[str(rez)])
#     else:
#         for i in range(len(str(rez))):
#             rez_array.append(int(str(rez)[i]) * (10 ** (len(str(rez)) - i - 1)))
#         if rez_array[-1] == 0:
#             rez_array = rez_array[:-1]
#         if rez_array[-2] == 0:
#             rez_array = rez_array[:-2] + rez_array[-1:]
#         for el in rez_array:
#             rez_ans += numbers[str(el)] + ' '
#         print(rez_ans)
