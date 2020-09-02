import logging
from config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, with_expression

LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(message)s"

handler = logging.FileHandler('sql.log')
handler.setFormatter(logging.Formatter(LOG_FORMAT))

sql_logger = logging.getLogger('sqlalchemy.engine')
sql_logger.setLevel(logging.DEBUG)
sql_logger.addHandler(handler)

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    rs = conn.execute('SHOW DATABASES;')
    for row in rs:
        print(row)

Session = sessionmaker(bind=engine)

