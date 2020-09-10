from models import ReportCard
from db import Session
from helper import get_choice_from_menu
from rich.console import Console
from rich.table import Column, Table

def view_by_name():
    pass

def view_report_card():

    view_submenu ='''
        
        1. View By Student's Name
        2. View By Student's Admission No
        3. View By Class & Section

        '''

    view_handler = {
        "1": view_by_name
    }
    
    submenu_choice = get_choice_from_menu(view_submenu, view_handler)
    
    view_handler[submenu_choice]()


def view_by_name():
    name = input("Enter Student's Name: ")

    session = Session()
    sql_query = session.query(ReportCard).filter(ReportCard.student_name.ilike(f"%{name}%"))
    
    result = sql_query.all()

    if not result:
        print("Not Found")
        return

    console = Console()
    # extract this to a helper function afterwards
    table = Table(show_header=True, header_style="bold green")
    table.add_column("ID")
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
            report_card.student_name, 
            report_card.student_addmission_number, 
            f"{report_card.student_class} - {report_card.student_section}", 
            percentage

        )

    console.print(table)