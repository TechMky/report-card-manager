from db import Session
from view_handler import view_report_card

import pyinputplus as pyip

def delete_report_card():
    
    #call this so the records are fetched to show to the user
    result = view_report_card()

    no_of_records = len(result)

    if no_of_records == 0:
        print("No Records Found To Delete")
        return

    choice = pyip.inputYesNo(prompt=f"Found { no_of_records }. Are you sure you want to delete all of the above? (yes/no)")
    
    if choice == 'no':
        print("Skipping Delete...")
        return

    session = Session()
    session.delete(result)
    session.commit()

    print(f"Deleted { no_of_records } records")
    return

