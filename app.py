def get_main_menu():
    menu = '''
    1. Add New Report Card
    2. Edit Report Card
    3. View Report Card
    0. Exit
    '''
    valid_options = ['1','2','3','0']
    return menu, valid_options



#main menu
main_menu, options = get_main_menu()
print(main_menu)
choice = input("Enter your Option: ")

#validate choice will extract to a function after wards
while (choice not in options):
    print('Invalid Option')
    choice = input("Enter your Option: ")

