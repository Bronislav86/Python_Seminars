# Последовательностью Фибоначчи называется
# последовательность чисел a0 , a1, ..., an, ...,
# где a0  = 0, a1  = 1,
# ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# def fibonachchi(n):
#     if n in [1, 2]:
#         return 1
#     return fibonachchi(n - 1) + fibonachchi(n - 2)
# n = int(input())
# print(fibonachchi(n))

# --------------------------------------Задача31-----------------------------------------------

# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


# from random import randint
# import time

# n = int(input('Введите количество оценок: '))

# list_1 = [randint(1, 100000000) for _ in range(n)]
# #print(list_1)
# #print()
# start_1 = time.time()
# max_bal = max(list_1)
# min_bal = min(list_1)

# for i in range(len(list_1)):
#     if max_bal == list_1[i]:
#          list_1[i] = min_bal
# end_1 = time.time()
# #print(list_1)

# print(f'{end_1 - start_1}')
# #№2
# start_2 = time.time()

# list_1 = [randint(1, 100000000) for _ in range(n)]
# max_bal = list_1[0]
# min_bal = list_1[0]
# #list_max_point = []

# for el in set(list_1):
#     if max_bal < el:
#          max_bal = el
#     if el < min_bal:
#         min_bal = el
# #print(max_bal, min_bal)

# for i in range(len(list_1)):
#     if max_bal == list_1[i]:
#          list_1[i] = min_bal
# end_2 = time.time()
# #print(list_1)
# print(f'{end_2 - start_2}')

# #№3

# start_3 = time.time()

# list_1 = [randint(1, 100000000) for _ in range(n)]
# max_bal = list_1[0]
# min_bal = list_1[0]
# list_max_point = [0]

# for i in range(len(list_1)):
#     if max_bal < list_1[i]:
#          max_bal = list_1[i]
#          list_max_point = [i]
#     elif list_1[i] == max_bal:
#          list_max_point.append(i)

#     if list_1[i] < min_bal:
#         min_bal = list_1[i]
# #print(max_bal, min_bal)

# for i in list_max_point:
#     list_1[i] = min_bal

# end_3 = time.time()
# #print(list_1)
# print(f'{end_3 - start_3}')

# -------------------------------------Задача35-------------------------------

# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


# def prime_num(num):
#     for div in range(2, num):
#         if num % div == 0:
#             return False
#     return True

# num = int(input('Введите одно число: '))

# if prime_num(num) == True:
#     print('YES')
# else:
#     print('NO')

# №2

# def prime_num(num):
#     if num != 2 and num % 2 == 0:
#         return False
#     for div in range(3,int(num ** 0.5) + 1, 2):
#         if num % div == 0:
#             return False
#     return True

# #№3

# num=int(input("Введите число: "))
# print(prime_num(num))

# def prime_num(num):
#     if num != 2 and num % 2 == 0:
#         return False
#     for div in range(3,int(num ** 0,5) + 1, 2):
#         if num % div == 0:
#             return False
#     return True

# num = int(input('Введите одно число: '))

# if prime_num(num) == True:
#     print('YES')
# else:
#     print('NO')

# ----------------------------------------Задача 37-------------------------

# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def reverse_nums (n):
#     if n == 1:
#         return input('Введите число последовательности: ')
#     k = input('Введите число последовательности: ')
#     return f'{reverse_nums(n - 1)} {k}'

# num = int(input('Введиче количестиво чисел: '))
# print(reverse_nums(num))

# --------------------------------ДЗ----------------------------------------------

# Задача 1

# Напишите функцию f, которая на вход принимает два числа a и b,
# и возводит число a в целую степень b с помощью рекурсии.
# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8

# def f(a, b):
#     if b in [1]:
#         return a
#     return a * f(a, b - 1)


# a = 2
# b = 3
# print(f(a, b))

# Задача2

# def sum(a, b):
#     if b in [0]:
#         return a
#     return sum(a + 1, b - 1)

# a = 28
# b = 22
# print(sum(a, b))
