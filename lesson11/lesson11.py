import argparse
import requests
import sqlalchemy
import random
from sqlalchemy import create_engine, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, Session, sessionmaker

parser = argparse.ArgumentParser()

first_currency = parser.add_argument('-f',
                                     '--first_currency',
                                     type=str,
                                     help='Enter a first_currency')
second_currency = parser.add_argument('-s',
                                      '--second_currency',
                                      type=str,
                                      help='Enter a second_currency')
number = parser.add_argument('-n',
                             '--number',
                             type=int,
                             help='Enter a number')

args = parser.parse_args()



def connect(response):
    lst = response.json()
    lst1 = []
    lst2 = []
    for val in lst:
        lst1.append(val.get('Cur_Abbreviation'))
        lst2.append(val.get('Cur_OfficialRate'))
    list_currency = {key: value for key, value in zip(lst1, lst2)}

    return list_currency


def converter(list_currency, f, n, s):
    if s == 'RUB':
        result = (list_currency[f] * n) / list_currency[s] * 100
    elif f == 'RUB':
        result = (list_currency[f] * n) / list_currency[s] / 100
    elif s == 'BYN':
        result = n * list_currency[s]
    elif f == 'BYN':
        result = n / list_currency[s]
    else:
        result = (list_currency[f] * n) / list_currency[s]
    return round(result, 2)


# def export_to_db(link, f, n, s):
#     db = create_engine(link)
#     base = declarative_base()
#
#     class HistoryConverter(base):
#         __tablename__ = "converter"
#
#         id = Column(Integer, primary_key=True)
#         first_currency = Column(String(3))
#         number = Column(Float())
#         second_currency = Column(String(3))
#
#     base.metadata.create_all(db)
#     Session = sessionmaker(db)
#     session = Session()
#     history = HistoryConverter(first_currency=f, number=n, second_currency=s)
#     session.add(history)
#     session.commit()
#     session.close()


response = requests.get('http://www.nbrb.by/api/exrates/rates?periodicity=0')
link = 'postgresql://postgres:Vlad2010@localhost:5432/testdb'
f = args.first_currency
s = args.second_currency
n = args.number
list_currency = connect(response)
result = converter(list_currency, f, n, s)
# export_to_db(link, f, n, s)
print(result)
