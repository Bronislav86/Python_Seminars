from date_create import *

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
        for contact in enumerate(contacts_list, 1):
            print(*contact)
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