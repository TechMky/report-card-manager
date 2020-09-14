from models import ReportCard
# helper functions

def get_choice_from_menu(menu: str, handlers: dict):
    print(menu)
    choice = input("Enter your Option: ")
    while (choice not in handlers.keys()):
        print('Invalid Option')
        choice = input("Enter your Option: ")
    
    return choice


def get_query_from_student_search_params(search_params: list):
    queryList = []

    for index,param in enumerate(search_params):
        
        if len(param) == 0:
            continue

        # index 0 is name
        if index == ReportCard.INDEX_NAME:
            queryList.append(ReportCard.student_name.ilike(f"%{ param }%"))

        # index 1 is admision number
        if index == ReportCard.INDEX_CLASS:
            queryList.append(ReportCard.student_class.ilike(f"{ param }"))
        
        if index == ReportCard.INDEX_SECTION:
            queryList.append(ReportCard.student_section.ilike(f"{ param }"))
        
        if index == ReportCard.INDEX_ADM_NO:
            queryList.append(ReportCard.student_addmission_number == param)

    return queryList