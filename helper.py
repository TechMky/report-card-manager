from typing import List
from rich.console import Console
from rich.table import Table
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

        if index == ReportCard.INDEX_EXAM_NAME:
            queryList.append(ReportCard.exam_name.ilike(f"%{ param }%"))

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

def pretty_print_report_card(result: List[ReportCard] ):

    console = Console()
    # extract this to a helper function afterwards
    table = Table(show_header=True, header_style="bold green")
    table.add_column("ID")
    table.add_column("Exam Name")
    table.add_column("Student Name")
    table.add_column("Admission Number")
    table.add_column("Class - Section")
    table.add_column("Percentage")
    
    for report_card in result:

        # can optimize to use a single loop
        max_total_marks = sum([ subject.max_marks for subject in report_card.report_card_subjects ])
        obtained_marks = sum([ subject.marks for subject in report_card.report_card_subjects ])

        percentage = (obtained_marks / max_total_marks) * 100
        percentage = str(round(percentage, 2)) + ' %'

        table.add_row(

            str(report_card.report_card_id), 
            report_card.exam_name,
            report_card.student_name, 
            report_card.student_addmission_number, 
            f"{report_card.student_class} - {report_card.student_section}", 
            percentage

        )

    console.print(table)