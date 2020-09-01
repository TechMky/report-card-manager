def get_main_menu():
    menu = '''
    1. Add New Report Card
    2. Edit Report Card
    3. View Report Card
    0. Exit
    '''
    
    return menu, get_handlers()

# handlers for the different options

def get_handlers():
    return {
        '1': add_report_card
    }

def add_report_card():
    pass