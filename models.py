from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey, Sequence
from sqlalchemy.sql.sqltypes import Float, Integer, String


Base = declarative_base()

class ReportCard(Base):

    INDEX_EXAM_NAME = 0
    INDEX_NAME = 1
    INDEX_ADM_NO = 2
    INDEX_CLASS = 3
    INDEX_SECTION = 4

    __tablename__ = 'report_card'
    report_card_id = Column(Integer, Sequence('report_card_id'), primary_key=True)
    exam_name = Column(String(255))
    student_name = Column(String(255))
    student_addmission_number = Column(String(255))
    student_class = Column(String(50))
    student_section = Column(String(10))
    report_card_subjects = relationship('ReportCardSubject', backref='report_card', lazy=True, passive_deletes=True, cascade='all, delete, delete-orphan')


class ReportCardSubject(Base):
    __tablename__ = 'report_card_subject'
    report_card_subject_id = Column(Integer, Sequence('report_card_subject_id'), primary_key=True)
    report_card_id = Column(Integer, ForeignKey('report_card.report_card_id', ondelete="CASCADE"))
    subject_name = Column(String(255))
    marks = Column(Float)
    max_marks = Column(Float)
