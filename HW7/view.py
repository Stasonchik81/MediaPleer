def main_menu():

    print(f"**** Telephone directory *****\n"
          f"1. Show all contacts\n"
          f"2. Search contact\n"
          f"3. Add contact\n"
          f"4. Edit contact\n"
          f"5. Delete contact\n"
          f"6. Import contacts\n"
          f"7. Exit")
    return int(input('Choose menu item: '))

def input_name_for_searching():
    return input('Enter name for searching contact: ')

def input_countact_for_add():
    return input('Enter contact to record: ')

def input_contact_for_edit():
    return input('Which contact do you want to change? Enter: ')

def enter_changing():
    return input('Enter changing: ')

def input_name_for_delete():
    return input('Enter name to delete from the directory: ')

def input_exit():
    return input('Exit? Yes/No ')





