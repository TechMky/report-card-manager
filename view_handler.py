from models import ReportCard
from db import Session
from helper import get_query_from_student_search_params
from sqlalchemy import and_
from rich.console import Console
from rich.table import Column, Table


def view_report_card():

    # create an empty string list
    search_params = [ '' ] * 4

    search_params[ReportCard.INDEX_NAME] = input("Enter Name: ")
    search_params[ReportCard.INDEX_ADM_NO] = input("Enter Admission Number: ")
    search_params[ReportCard.INDEX_CLASS] = input("Enter Class: ")
    search_params[ReportCard.INDEX_SECTION] = input("Enter Section: ")

    query = get_query_from_student_search_params(search_params)

    session = Session()
    sql_query = session.query(ReportCard).filter( and_( *query ) )
    
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