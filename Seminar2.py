# Задача 9
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1

# n = int(input('введите число: '))
# number = 1
# fact = 1
# # Вариант 1
# while n > 0:
#     fact = fact * number
#     number += 1
#     n -= 1
# print(fact)

# # Вариант 2

# while number <= n:
#     fact = fact * number
#     number += 1
# print(fact)

# # Вариант 2

# n = int(input('введите число: '))

# fact = 1

# while n > 1:
#     fact *= n
#     n -= 1
# print(fact)

#----------------------------------------------Задача 11----------------------------------------

# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1

# n = int(input("Введите число больше 1: "))
# count = 4
# fib1 = 1
# fib2 = 1
# fib_res = 1

# while fib_res < n:
#     fib1 = fib2
#     fib2 = fib_res
#     fib_res = fib1 + fib2
#     count += 1
    
# if fib_res == n:
#     print(count)
# else:
#     print(-1)
    
# Множественное присванивание!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
# n = int(input("Введите число больше 1: "))
# count = 4
# fib2 = 2
# fib_res = 1

# while fib_res < n:
#     fib2,fib_res = fib_res,fib2 + fib_res                                                       #ВОТ ЗДЕСЬ ОНО!!!5
#     count += 1
    
# if fib_res == n:
#     print(count)
# else:
#     print(-1)

#--------------------------Задача 13-----------------------------------------------------

# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50

#import random                                                       #ЗДЕСЬ ИСПОЛЬЗУЕМ РАНДОМ!!!!!!!!!!!!!

# num = int(input("Введите количество дней от 1 до 100: "))
# temp = 0
# max_count = 0
# count = 0

# for i in range(num):
#     #temp = int(input())
#     temp = random.randint(-50, 50)
#     print(temp, end=" ")
#     if temp > 0:
#         count += 1
#         if max_count < count:
#             max_count = count
#     else:
#         count = 0
# print()
# print(max_count)
        
#-------ВАРИАНТ 2--------

# num = int(input("Введите количество дней от 1 до 100: "))
# temp = 0
# max_count = 0
# count = 0

# for i in range(num):
#     #temp = int(input())
#     temp = random.randint(-50, 50)
#     print(temp, end=" ")
#     if temp > 0:
#         count += 1
#     else:
#         if max_count < count:
#             max_count = count
#         count = 0
# if max_count < count:
#     max_count = count
# print()
# print(max_count)

#--------------------------------------ЗАДАЧА 15-------------------------------------------

# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

#from random import randint

# n = int(input("Введите количество арбузов: "))
# count = 0
# max_wheight = 0
# min_wheight = 1000

#Вариант 1

# while count < n:
#     wheigth = randint(1, 10)
#     print(wheigth, end=' ')
#     if wheigth >= max_wheight:
#         max_wheight = wheigth
#     elif wheigth < max_wheight:
#         min_wheight = wheigth
#     count +=1

# print()
# print(min_wheight, end=' ')
# print(max_wheight, end=' ')

# #Вариант 2
# n = int(input("Введите количество арбузов: "))
# max_wheight = 0
# min_wheight = 1000

# for _ in range(n):
#     wheigth = randint(1, 10)
#     print(wheigth, end=' ')
#     if wheigth > max_wheight:
#         max_wheight = wheigth
#     elif wheigth < min_wheight:
#         min_wheight = wheigth
# print()
# print(min_wheight, end=' ')
# print(max_wheight, end=' ')

# #Вариант 3
# n = int(input("Введите количество арбузов: "))
# wheigth = randint(0, 100)
# max_wheight = wheigth
# min_wheight = wheigth

# for _ in range(n - 1):
#     wheigth = randint(1, 100)
#     print(wheigth, end=' ')
#     max_wheight = max(max_wheight, wheigth)
#     min_wheight = min(min_wheight, wheigth)
# print()
# print(min_wheight, end=' ')
# print(max_wheight, end=' ')


        
