# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()


# string = "a a a b c a a d c d d"
# print(string)
# splited_list = string.split()
# print(splited_list)
# print()
# uniq_symbols = dict()

# for symbol in splited_list:
#     if symbol not in uniq_symbols:
#         uniq_symbols[symbol] = 0
#         print(symbol, end=" ")
#     else:
#         uniq_symbols[symbol] += 1
#         print(f'{symbol}_{uniq_symbols[symbol]}', end=' ')
#     #print(uniq_symbols)
            
# Вариант2

# string = "a a a b c a a d c d d"
# splited_list = string.split()
# print(splited_list)
# print()
# uniq_symbols = dict()
# result = ''

# for symbol in splited_list:
#     if symbol not in uniq_symbols:
#         uniq_symbols[symbol] = 0
#         result += symbol + ' '
#     else:
#         uniq_symbols[symbol] += 1
#         result += f'{symbol}_{uniq_symbols[symbol]} '
# print(result. strip())
            
#Вариант3

# string = "a a a b c a a d c d d"
# splited_list = string.split()
# print(splited_list)
# print()
# uniq_symbols = dict()
# result = ''

# for symbol in splited_list: #Здесь symbol - это ключ словаря uniq_symbols
#     if symbol not in uniq_symbols:
#         result += symbol + ' '
#     else:
#         result += f'{symbol}_{uniq_symbols[symbol]} '
#     uniq_symbols[symbol] = uniq_symbols.get(symbol, 0) + 1 #Здесь объявили ключ словаря
# print(result. strip())
  
#-------------------------Задача27---------------------------

# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
  
# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea"
# listed_text = text.lower().split()
# print(listed_text)
# set_words = set(listed_text)
# print(set_words)
# print()
# print(len(set_words))

# print(len(set(text.lower().split())))

#---------------------------------Задача 29--------------------------------------------------

# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Примечание: Программные коды на следующих
# слайдах

#Ваня
# n = int(input())
# max_number = n  #ошибка
# while n != 0:
#     n = int(input())
#     if max_number < n:  #ошибка
#         max_number = n
# print(max_number)

#Петя
# n = int(input())
# max_number = -1
# while n != 0:#
#     if max_number < n:
#         max_number = n#
#     n = int(input())#
# print(max_number)# 
      
#-----------------ДЗ - Задача 1-------------------------------------------------      
      
# var2 = '1 2 3'
# var3 = '1 2 3 4'

# var2 = '5 6 7 8' 
# var3 = '6 7 8 9'

# var2 = '1'
# var3 = '3 4 5 6'                 
            
# var2 = '10 20 30 40 50'
# var3 = '10 20 30 40 50'
# var2_listed = var2.split()
# var3_listed = var3.split()

# planty2 = set(var2_listed)
# planty3 = set(var3_listed)

# intersection = planty2.intersection(planty3)
# list_intersection = list(intersection)
# print(*sorted(list_intersection))

#---------------------Задача2-------------------------------------------

# arr = [5, 8, 6, 4, 9, 2, 7, 3]

# max = 0
# res = 0

# for i in range(-1, len(arr) - 1):
#     res = arr[i] + arr[i - 1] + arr[i + 1]
#     if res > max:    
#         max = res
# print(max)