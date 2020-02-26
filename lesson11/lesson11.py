
import argparse
import requests
import sqlalchemy
import random

import converter
import export_to_db
import connect

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


response = requests.get('http://www.nbrb.by/api/exrates/rates?periodicity=0')

f = args.first_currency
s = args.second_currency
n = args.number
list_currency = connect.connect(response)
result = converter.converter(list_currency, f, n, s)
export_to_db.export_to_db(f, n, s)
print(result)
