from delete_handlers import delete_report_card
from view_handler import view_report_card
from models import ReportCard, ReportCardSubject
from db import Session

def get_main_menu():
    menu = '''
    1. Add New Report Card
    2. Edit Report Card
    3. View Report Card
    4. Delete Report Card
    0. Exit
    '''
    
    return menu, get_handlers()

# handlers for the different options

def get_handlers():
    return {
        '1': add_report_card,
        '3': view_report_card,
        '4': delete_report_card,
    }

def add_report_card():
    report_card_dict = {
        "exam_name" : input("Enter Exam Name: "),
        "student_name" : input("Enter Student's Name: "),
        "student_addmission_number": input("Enter Student's Admission Number: "),
        "student_class": input("Enter Student's class: "),
        "student_section": input("Enter Student's section: "),
    }

    no_of_subject = int(input("How many subjects do you want to add ? "))
    
    if no_of_subject < 1:
        print("Report Card cannot be added with no subjects")
        return

    # get subject's data
    report_card_dict["report_card_subjects"] = get_report_card_subjects( no_of_subject )

    report_card = ReportCard(**report_card_dict)

    session = Session()
    session.add(report_card)
    session.commit()

    print("Report Card Added!!")


def get_report_card_subjects(subject_count: int):
    
    report_card_subject_list = []
    
    for subject_number in range(subject_count):
        
        report_card_subject_dict = {
            "subject_name": input(f"Enter Subject { subject_number + 1 }'s Name: "),
            "marks": float(input(f"Enter Subject { subject_number + 1 }'s marks obtained: ")),
            "max_marks": float(input(f"Enter Subject { subject_number + 1 }'s maximum marks: ")),
        }

        report_card_subject = ReportCardSubject(**report_card_subject_dict)

        report_card_subject_list.append(report_card_subject)
    
    return report_card_subject_list