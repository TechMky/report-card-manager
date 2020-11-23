from models import ReportCard
from db import Session
from helper import get_query_from_student_search_params, pretty_print_report_card, pretty_print_report_card_with_subject
from sqlalchemy import and_
import pyinputplus as pyinp

def get_user_input_query():
    # create an empty string list
    search_params = [ '' ] * 5

    search_params[ReportCard.INDEX_EXAM_NAME] = input("Enter Exam Name: ")
    search_params[ReportCard.INDEX_NAME] = input("Enter Student Name: ")
    search_params[ReportCard.INDEX_ADM_NO] = input("Enter Admission Number: ")
    search_params[ReportCard.INDEX_CLASS] = input("Enter Class: ")
    search_params[ReportCard.INDEX_SECTION] = input("Enter Section: ")

    return search_params

def view_report_card(mode='view'):

    search_parameters = get_user_input_query()

    query = get_query_from_student_search_params(search_parameters)

    session = Session()
    sql_query = session.query(ReportCard).filter( and_( *query ) )
    
    result = sql_query.all()

    if not result:
        print("No Records Found!")
        return []

    pretty_print_report_card(result)
    
    session.close()

    if mode != 'view':
        return result

    # this block executes only if mode is view
    report_card_id = pyinp.inputInt(prompt='Enter Report Card ID for more details: ', greaterThan=0)

    found_report_card = None
    for report_card in result:
        if report_card.report_card_id == report_card_id:
           found_report_card = report_card

    if not found_report_card:
        print(f'Report Card wit ID {report_card_id} Not Found in the above table') 
        return
    
    pretty_print_report_card_with_subject(found_report_card)
