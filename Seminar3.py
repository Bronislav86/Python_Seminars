# --------------------------Задача17--------------------------

# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# from random import randint

# size = int(input('ВВЕДИТЕ РАЗМЕР СПИСКА: '))
# #list_1 = [i for i in range(size)]
# list_1 = []

# # for _ in range(size):
# #     list_1.append(randint(-5, 5))

# list_2 = [randint(-5, 5) for _ in range(size)]
# print(list_2)

# my_set = set(list_2)
# print(my_set, '\n', len(my_set))
# print()
# print(len(set(list_2)))

# print(len(set([randint(-5, 5) for _ in range(size)])))

# ---------------------------------Задача19--------------------------

# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# from random import randint

# k = int(input('Введите коэффициент сдвига: '))

# list_2 = [i for i in range(1, randint(7, 10))]
# print(list_2)
# #print(list_2.pop())                                    #смотрим как работает поп

# for _ in range(k):
#     last_num = list_2.pop()
#     list_2.insert(0, last_num)
# print(list_2)

# #Вариант2

# print(list_2[-k:] + list_2[:-k])

# ---------------------------------Задача 21----------------------------------------------------

# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# list_dicts = [
#     {"V": "S001", "VIII": "S007"},
#     {"V": "S002"},
#     {"VI": "S001"},
#     {"VI": "S005"},
#     {"VII": "S005"},
#     {"V": "S009"},
#     {"VIII": "S007"},
# ]

# uniq_values = set()

# for cur_dict in list_dicts:
#     for key in cur_dict:
#         uniq_values.add(cur_dict[key].strip())
# print(uniq_values)

# Вариант2

# uniq_values = set()

# for cur_dict in list_dicts:
#     for key in cur_dict.keys():
#         uniq_values.add(cur_dict[key].strip())
# print(uniq_values)

# Вариант3

# uniq_values = set()

# for cur_dict in list_dicts:
#     for value in cur_dict.values():
#         uniq_values.add(value.strip())
# print(uniq_values)

# Вариант4

# uniq_values = set()

# for cur_dict in list_dicts:
#         uniq_values.add(*cur_dict.values())
# print(uniq_values)

# Вариант5

# uniq_values = set()

# for cur_dict in list_dicts:
#         uniq_values.update(cur_dict.values())
# print(uniq_values)

# ---------------------------------Задача

# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# array = [0, -1, 5, 2, 3]
# count = 0

# for i in range(len(array) - 1):
#     if array[i] < array[i + 1]:
#         count += 1
# print(count)

# print(sum([1 for i in range(len(array) - 1) if array[i] < array[i + 1]]))

# list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
# k = 10

# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 8 #8

# list_1 = [1, 2, 3, 4, 5]
# k = 6

# ---------------------------------ДОМАШНЕЕ ЗАДАНИЕ--------------------------------------------

# list_1 = [1, 12, 6, 7, 8, 15]
# k = 11
# plus_diff_value = 1
# minus_diff_value = -2

# m = abs(k - list_1[0])  # модуль числа
# print(m)
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)

# for i in list_1:
#     difference = k - i
#     print(difference, end="||")
#     if difference == 0:
#         digit = i
#     if difference < 0 and difference >= minus_diff_value:
#         plus_diff_value = difference
#         digit = i
#     if difference > 0 and difference <= plus_diff_value:
#         minus_diff_value = difference
#         digit = i
# print()
# print(f"!-{digit}-!")

# print(sum([1 for i in list_1 if i == k]))

# -----------------------ЗАДАЧА ПРО СКРАБЛ-----------------------------------

#k = "ноутбук"
#k = 'laptop' # 10
#k = 'ящерица' #22
k = 'lizard' # 16
dictionary = {
    "a": 1,
    "e": 1,
    "i": 1,
    "o": 1,
    "u": 1,
    "l": 1,
    "n": 1,
    "s": 1,
    "t": 1,
    "r": 1,
    "а": 1,
    "в": 1,
    "е": 1,
    "и": 1,
    "н": 1,
    "о": 1,
    "р": 1,
    "с": 1,
    "т": 1,
    "d": 2,
    "g": 2,
    "д": 2,
    "к": 2,
    "л": 2,
    "м": 2,
    "п": 2,
    "у": 2,
    "b": 3,
    "c": 3,
    "m": 3,
    "p": 3,
    "б": 3,
    "г": 3,
    "ё": 3,
    "ь": 3,
    "я": 3,
    "f": 4,
    "h": 4,
    "v": 4,
    "w": 4,
    "y": 4,
    "й": 4,
    "ы": 4,
    "k": 5,
    "ж": 5,
    "з": 5,
    "х": 5,
    "ц": 5,
    "ч": 5,
    "j": 8,
    "x": 8,
    "ш": 8,
    "э": 8,
    "ю": 8,
    "q": 10,
    "z": 10,
    "ф": 10,
    "щ": 10,
    "ъ": 10,
}

k = k.lower()
summa = 0
for key, value in dictionary.items():
    for j in k:
        if key == j:
            summa += value
print(summa)
