#------------------Задача 55----------------------------
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например
# имя или фамилию человека) Использование функций. Ваша программа не должна быть линейной

# Этапы работы
# 1. Создать тел. справочник контакт:           ++++
#     - открыть файл в режиме добавления (а)    ++++
# 2. Добавить контакт:                          ++++
#     - запросить информацию у пользователя     ++++
#     - подготовить в необходимом формате       ++++
#     - открыть файл в режиме добавления (а)    ++++
#     - добавить контакт в файл                 ++++
# 3. Вывести данные из файла на экран:          ++++
#     - открыть файл в режиме чтения (r)        ++++
#     - вывевести данные на экран               ++++
# 4. Поиск данных:                              ++++
#     - запросить вариант поиска                ++++
#     - запросить данные у пользователя для поиска  ++++
#     - открыть файл в режиме чтения (r)        ++++
#     - сохранить данные в переменную           ++++
#     - осуществить поиск                       ++++
#     -вывести инфо на экран                    ++++
# 5. Реализовать UI:                            ++++
#     - Вывести варианты меню                   ++++
#     - Получение запроса пользователя          ++++
#     - Реализация запроса пользователя         ++++
#     - Выход                                   ++++
# 6. Копирование данных из одного файла в другой:
#     - добавить вариант копирования в меню     ++++
#     - вывести отформатированный список контактов  ++++
#     - запросить у пользователя данные для копирования   
#     - открыть исходный файл в режиме чтения(r)
#     - сохранить данные в переменную
#     - открыть новый файл в который будем копировать
#     - осуществить копирование
#     - вывести данныеб хранящиеся в новом файле
    
def input_name():
    return input('Введите имя: ')

def input_surname():
    return input('Введите фамилию: ')

def input_patronymic():
    return input('Введите отчество: ')

def input_phone():
    return input('Введите номер телефона: ')

def input_address():
    return input('Введите адрес: ')

def create_contact():
    name = input_name()
    surnname = input_surname()
    partonymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    
    return f'{surnname} {name} {partonymic} {phone}\n{address}\n\n'

def add_contact(contact):
    with open('Phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)

def show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        for contact in contacts_list:
            print(contact)
        #print(file.read().rstrip())

def search_contact():
    print(
            'Возможные варианты поиска:\n'
            '1. По Фамилии\n'
            '2. По Имени\n'
            '3. По Отчеству\n'
            '4. По Номеру телефона\n'
            '5. По Городу\n'
        )
    var_search = input('Выберите вариант поиска: ')
    
    while var_search not in ('1', '2', '3', '4', '5'):
            print('Некорректные данные, нужно ввести число комманды')
            var_search = input('Введите вариант поиска: ')
            
    index_var = int(var_search) - 1
    search = input('Введите данные для поиска: ')
    
    with open('Phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n', ' ').split()
        if search in contact_lst[index_var]:
            print(contact_str)
            
def create_favorites_contact_list():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        for contact in enumerate(contacts_list, 1):
            print(*contact)

    print('Выберите номер контакта для копирования: ', end='')
    contact_number = int(input())
    tuple_contacts_list = enumerate(contacts_list, 1)

    for cur_contact in tuple_contacts_list:
        if contact_number > len(contacts_list):
            print('Такого контакта не существует')
            contact_number = int(input('Выберите контакт из списка: '))
        if int(cur_contact[0]) == contact_number:
            with open('favorites_contacts.txt', 'a', encoding='UTF-8') as file:
                file.write(f'{cur_contact[1]}\n\n')
            
    print()
    print(f'Контакт:\n\n{cur_contact[1]}\n\nуспешно добавлен в Избранные.')
    print()
    print('Список контаков Избранные:\n')
    
    with open('favorites_contacts.txt', 'r', encoding='UTF-8') as file:
        fav_contacts_list = file.read().rstrip().split('\n\n')
        for contact in fav_contacts_list:
            print(contact)

def interface():
    with open('Phonebook.txt', 'a', encoding='UTF-8'):
        pass
    
    command = '-1'
    while command != '5':
        print('Возможные варианты взаимодействия:\n'
              '1. Добавить контакт\n'
              '2. Вывести на экран\n'
              '3. Поиск контакта\n'
              '4. Добавить контакт в Избранные\n'
              '5. Выход из программы')

        command = input('Введите номер действия: ')

        while command not in ('1', '2', '3', '4', '5'):
            print('Некорректные данные, нужно ввести число комманды')
            command = input('Введите номер действия: ')

        match command:
            case '1':
                add_contact(create_contact())
            case '2':
                show_info()
            case '3':
                search_contact()
            case '4':
                create_favorites_contact_list()
            case '5':
                print('Всего хорошего!')

interface()

# Дописать в меню вывод списка избранных  контактов!