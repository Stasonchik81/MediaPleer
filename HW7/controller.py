import view
import funcs

def button_click():
    while True:
        command = view.main_menu()
        print(command)
        funcs.users_choise_menu(command)



