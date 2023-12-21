# f = lambda x, y: x * y

# print(f(2, 3))

# #--------------------------------------------------------------------

# my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]


# res_list = list(filter(lambda x: x % 2 == 0, my_list))
# print(res_list)

# # for cur_orbit in res_list:
# #     print(cur_orbit, end=' ')
# # print()

# res_list=[]
# f = lambda x: x % 2 == 0
# for cur_orbit in my_list:
#     if f(cur_orbit):
#         res_list.append(cur_orbit)
# print(res_list)

# #-----------------------------------MAP-------------------------------

# es_list = list(map(lambda x: x ** 2 , my_list))
# print(res_list)

# res_list=[]
# f = lambda x: x ** 2
# for cur_orbit in my_list:
#     res_list.append(f(cur_orbit))
# print(res_list)

# #

# my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]

# numbers = input('Введите цифры через пробел').split()
# print(numbers)
# res_list = list(map(int , numbers))
# print(res_list)
# print([int(cur_orbit) for cur_orbit in numbers])

# -------------------------Задача 47-------------------

# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется
# множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а
# нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# transformation = lambda x: x

# values = [1, 23, 42, "asdfg"]
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print("ok")
# else:
#     print("fail")

# -------------------------Задача 49-----------------------------

# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь.
# Напишите функцию s(list_of_orbits), которая
# среди списка орбит планет найдет ту, по которой вращается самая
# далекая планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники были
# были запущены на круговые орбиты. Результатом функции должен быть
# кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты.
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей
# эллипса. При решении задачи используйте списочные выражения. Подсказка: проще
# всего будет найти эллипс в два шага: сначала вычислить самую большую площадь
# эллипса, а затем найти и сам эллипс, имеющий такую  площадь. Гарантируется,
# что самая далекая планета ровно одна

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*s(orbits))

# Вывод:
# 2.5 10

import math

# s = lambda cur_tuple: cur_tuple[0] * cur_tuple[1]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# max_s = s(orbits[0])
# index = 0

# for cur_orbit in orbits[1:]:
#     if cur_orbit[0] != cur_orbit[1]:
#         cur_s = s(cur_orbit)
#         if cur_s > max_s:
#             max_s = cur_s
#             index = cur_orbit
# print(*index)

# Вариант2


# def find_farther_orbit(list_of_orbits):
#     filter_orbits = list(filter(lambda cur_orbit: cur_orbit[0] != cur_orbit[1], list_of_orbits))
#     tuple_s = list(map(lambda cur_orbit: cur_orbit[0] * cur_orbit[1], filter_orbits))
#     max_s = max(tuple_s)
#     i_max_s = tuple_s.index(max_s)
#     return filter_orbits[i_max_s]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farther_orbit(orbits))

# ----------------------Задача 52----------------------------

# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, и
# возвращают True, если это так. Если значение характеристики для разных
# объектов отличается - то False. Для пустого набора объектов, функция должна
# возвращать True. Аргумент characteristic - это функция, которая принимает
# объект и вычисляет его характеристику.
# Ввод:							        Вывод:
# values = [0, 2, 10, 6]				same
# if same_by(lambda x: x % 2, values):
# 	print(‘same’)
# else:
# 	print(‘different’)


# def same_by(characteristic, objects):
#     if not objects:
#         return True
#     result = list(map(characteristic, objects))
#     print(result)
#     return all(result) == any(result)


# values = [1, 15, 8, 9]

# if same_by(lambda x: x % 2 == 1, values):
#     print("same")
# else:
#     print("different")

# Вариант2


# def same_by(characteristic, objects):
#     if not objects:
#         return True
#     result = set(map(characteristic, objects))
#     print(result)
#     return len(result) == 1


# values = [1, 15, 3, 9]

# if same_by(lambda x: x % 2 == 1, values):
#     print("same")
# else:
#     print("different")

# Вариаент3

# def same_by(characteristic, objects):
#     result = list(filter(characteristic, objects))
#     print(result)
#     return result == objects or not result


# values = [1, 2, 4, 6, 5]

# if same_by(lambda x: x % 2 == 0, values):
#     print("same")
# else:
#     print("different")

# ---------------------------------------------------------Про Any и All--------------------------

# print(all([True, True, True, True]))
# print(all([True, False, True, True]))
# print(all([False, False, False, False]))
# print()
# print(any([True, True, True, True]))
# print(any([True, False, True, True]))
# print(any([False, False, False, False]))
# print()
# print(all([1, 2, 3, 4]))
# print(all([1, 0, 3, 4]))
# print(all([0, 0, 0, 0]))
# print()
# print(any([1, 2, 3, 4]))
# print(any([1, 0, 3, 4]))
# print(any([0, 0, 0, 0]))
# print()
# print(all(['dfg', 'sdf', 'sdf', 'cvb']))
# print(all(['dfg', '', 'sdf', 'cvb']))
# print(all(['', '', '', '']))
# print()
# print(any(['dfg', 'sdf', 'sdf', 'cvb']))
# print(any(['dfg', '', 'sdf', 'cvb']))
# print(any(['', '', '', '']))
# print()
# print(all([[''], ('',), {''}, ['']]))
# print(all([[''], [], [''], ['']]))
# print(all([{}, {}, {}, []]))
# print()
# print(any([[''], ('',), {''}, ['']]))
# print(any([[''], [], [''], ['']]))
# print(any([{}, {}, {}, []]))
# print()

# ------------------------------------------------------------------------------------------------

# Д О П Ы #
# a = "Python"
# b = "Hello World!"
# z = "Привет меня зовут Вася!"

# # print(a, b, z)
# # print(a, b, z, sep="-||-")
# # print(a, b, z, sep="-||-", end=" The End")

# print(a, end=" ")
# print(b, end="\t")
# print(z)


# name = "John"
# print(f'Hi, {name}.')  #- Hi, John.
# print('Hi, %s.' % name)  #- Hi, John
# print('{} Hi, {}'.format(name[:2], name))  #- Hi, {name}
# print('{b} Hi, {a}'.format(b=name[:2], a=name))  #- Hi, {name}


# import copy

# my_list_1 = [123,234,3456,678,789, [111,222,[11,22,33],333,444]]
# print(f'{my_list_1 =}')
# my_list_2 = my_list_1
# print(f'{my_list_2 =}')
# print()
# my_list_2[1] = 0
# print(f'{my_list_1 =}')
# print(f'{my_list_2 =}')
# print()

# my_list_3 = my_list_1.copy()
# print(f'{my_list_1 =}')
# print(f'{my_list_3 =}')
# print()
# my_list_3[2] = 999999
# print(f'{my_list_1 =}')
# print(f'{my_list_3 =}')
# my_list_3[-1][2][1] = 'XXXX'
# print(f'{my_list_1 =}')
# print(f'{my_list_3 =}')

# my_list_4 = my_list_1[:]

# my_list_5 = copy.deepcopy(my_list_1)
# print(f'{my_list_1 =}')
# print(f'{my_list_5 =}')
# print()
# my_list_5[2] = 777777
# print(f'{my_list_1 =}')
# print(f'{my_list_5 =}')
# my_list_5[-1][2][1] = '~~~~~~'
# print(f'{my_list_1 =}')
# print(f'{my_list_5 =}')



# q,*w, e = (11, 22, 33, 44, 55)
# print(q)
# print(w)
# print(e)

# q,*w, e = (11, 22, 33)
# print(q)
# print(w)
# print(e)

# q,*w, e = (11, 22)
# print(q)
# print(w)
# print(e)

# my_list = [(1,2,3,4,5), (11,22,33), (111,222)]
# for q,w,*e in my_list:
#     print(q,w,e, sep=' -\\- ')