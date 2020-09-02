import logging
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
