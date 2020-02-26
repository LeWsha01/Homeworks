from sqlalchemy import create_engine, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, Session, sessionmaker

link = 'postgresql://postgres:Vlad2010@localhost:5432/testdb'

db = create_engine(link)
base = declarative_base()


class HistoryConverter(base):
    __tablename__ = "converter"

    id = Column(Integer, primary_key=True)
    first_currency = Column(String(3))
    number = Column(Float())
    second_currency = Column(String(3))


base.metadata.create_all(db)


def export_to_db(f, n, s):
    Session = sessionmaker(db)
    session = Session()
    history = HistoryConverter(first_currency=f, number=n, second_currency=s)
    session.add(history)
    session.commit()
    session.close()
