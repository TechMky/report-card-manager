from models import ReportCard
from db import Session
from helper import get_query_from_student_search_params, pretty_print_report_card
from sqlalchemy import and_


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

    pretty_print_report_card(result)