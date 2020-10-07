import logging
import names
from random import randint, random
import pyinputplus
from models import ReportCard, ReportCardSubject
from config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, with_expression

LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(message)s"


engine = create_engine(DATABASE_URL)


Session = sessionmaker(bind=engine)

def init_db():
    # setup db logging
    handler = logging.FileHandler('sql.log')
    handler.setFormatter(logging.Formatter(LOG_FORMAT))

    sql_logger = logging.getLogger('sqlalchemy.engine')
    sql_logger.setLevel(logging.DEBUG)
    sql_logger.addHandler(handler)

    #initialize tables in the database using the models
    ReportCard.__table__.create(bind=engine, checkfirst=True)
    ReportCardSubject.__table__.create(bind=engine, checkfirst=True)

def seed_database():
    """
    docstring
    """

    choice = pyinputplus.inputYesNo(prompt='Are you sure you want to delete all records?')

    if choice == 'no':
        print("Skipping Delete...")
        return


    session = Session()

    rows_deleted = session.query(ReportCard).delete()
    session.commit()

    print(f'Deleted {rows_deleted} records')

    #TODO add code to insert records with little randomness

    NO_OF_RECORDS = pyinputplus.inputInt(prompt='Enter the Number of records to be added (default: 50): ', default=50)

    exam_names = ['SA 1', 'FA 2', 'SA 2', 'UNIT 1']
    section = ['A', 'B', 'C', 'D']
    class_name = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    
    report_cards = []

    while NO_OF_RECORDS != 0:
        NO_OF_RECORDS -= 1

        gender = random() > 0.5 if 'male' else 'female' 
        report_card_dict = {
            "exam_name" : exam_names[randint(0, len(exam_names) - 1)],
            "student_name" : names.get_full_name(gender),
            "student_addmission_number": randint(1111, 9999),
            "student_class": class_name[randint(0, len(class_name) - 1)],
            "student_section": section[randint(0, len(section) - 1)],
        }

        no_of_subject = randint(1, 5)

        subject_names = ['Maths', 'English', 'Science', 'Hindi', 'History']

        report_card_subject_list = []
        for subject_number in range(no_of_subject):
            
            report_card_subject_dict = {
                "subject_name": subject_names.pop(),
                "marks": randint(1, 100),
                "max_marks": 100,
            }

            report_card_subject = ReportCardSubject(**report_card_subject_dict)
            report_card_subject_list.append(report_card_subject)

        report_card_dict["report_card_subjects"] = report_card_subject_list

        report_cards.append(ReportCard(**report_card_dict))


    #finally insert in the database

    session = Session()
    #TODO bulk insert is not adding child records only parent records are being inserted
    # session.bulk_save_objects(report_cards) 
    session.add_all(report_cards) 
    session.commit()
    print('Records Added')