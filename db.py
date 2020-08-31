from config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, with_expression

import logging

handler = logging.FileHandler('sql.log')
handler.setLevel(logging.DEBUG)
logging.getLogger('sqlalchemy').addHandler(handler)

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    rs = conn.execute('SHOW DATABASES;')
    for row in rs:
        print(row)

Session = sessionmaker(bind=engine)

