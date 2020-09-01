from helper import get_choice_from_menu
from main_menu import get_main_menu


#main menu
main_menu, main_menu_handlers = get_main_menu()
main_menu_choice = get_choice_from_menu(main_menu, main_menu_handlers)

# whatever be the choice handle it accordingly
main_menu_handlers[main_menu_choice]()
