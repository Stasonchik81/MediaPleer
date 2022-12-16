import view

def show_contacts():
    with open('Telephone_directory.csv', 'r', encoding='UTF8') as td:
        phone = td.read()
        print(phone)

def search_contact():
    search_name = view.input_name_for_searching()
    with open ('Telephone_directory.csv', 'r', encoding='UTF8') as td:
        for i in td:
            if search_name in i:
                print(i)
            else:
                print('Contact not find.')
                break

def search_contact_for_edit():
    search_name = view.input_name_for_delete()
    with open ('Telephone_directory.csv', 'r', encoding='UTF8') as td:
        for i in td:
            if search_name in i:
                return i
            else:
                print('Contact not find.')
                break


def add_contact():
    contact = view.input_countact_for_add()
    with open('Telephone_directory.csv', 'a', encoding='UTF8') as td:
        td.write(f'\n{contact}')
    show_contacts()

def edit_contact():
    search_name = search_contact_for_edit()
    print(search_name)
    new_data = view.enter_changing()
    with open('Telephone_directory.csv', 'r', encoding='UTF8') as td:
        phone = td.read()
        phone = phone.replace(search_name, new_data)

    with open('Telephone_directory.csv','w+',encoding='UTF8') as dt:
        dt.write(phone)

def delete_contact():
    search_name = search_contact_for_edit()
    print(search_name)

    with open('Telephone_directory.csv', 'r', encoding='UTF8') as td:
        phone = td.read()
        phone = phone.replace(search_name, ' ')

    with open('Telephone_directory.csv', 'w+', encoding='UTF8') as dt:
        dt.write(phone)

def import_contacts():
    with open('Telephone_directory.csv', 'r', encoding='UTF8') as td:
        phone = td.read()
    with open('Telephone_directory.txt', 'w', encoding='UTF8') as dt:
        dt.write(phone)

def exit_from_programm():
    answer = view.input_exit()
    if answer == 'Yes':
        exit()











