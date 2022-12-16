import controller
import data_base

def users_choise_menu(command:int):
    if command == 1:
        data_base.show_contacts()
    elif command == 2:
        data_base.search_contact()
    elif command == 3:
        data_base.add_contact()
    elif command == 4:
        data_base.edit_contact()
    elif command == 5:
        data_base.delete_contact()
    elif command == 6:
        data_base.import_contacts()
    elif command == 7:
        data_base.exit_from_programm()





