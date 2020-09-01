# helper functions

def get_choice_from_menu(menu: str, handlers: dict):
    print(menu)
    choice = input("Enter your Option: ")
    while (choice not in handlers.keys()):
        print('Invalid Option')
        choice = input("Enter your Option: ")
    
    return choice