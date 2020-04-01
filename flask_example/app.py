import http
import os
import flask
import flask_marshmallow
import flask_sqlalchemy
import flask_wtf
import wtforms
from flask import render_template
from wtforms import validators
import requests

app = flask.Flask(__name__)

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

    return round(result,2)


@app.route('/')
def home():
    name = 'VV'
    return flask.render_template('home.html', name=name)


app.config['SECRET_KEY'] = 'random_string_for_safe'


class CreateProductForm(flask_wtf.FlaskForm):
    first_currency = wtforms.StringField(
        'first_currency',
        validators=[
            validators.DataRequired(),
            validators.Length(min=2, max=20),
        ]
    )
    number = wtforms.FloatField(
        'number',
        validators=[validators.DataRequired()]
    )
    second_currency = wtforms.StringField(
        'second_currency',
        validators=[
            validators.DataRequired(),
            validators.Length( max=3)
        ]
    )

    submit = wtforms.SubmitField('result')


@app.route('/add_product/', methods=['GET', 'POST'])
def add_product():
    a = ''
    form = CreateProductForm()
    if form.validate_on_submit():
        flask.flash("Product successfully added", "success")
        result = converter(list_currency,form.first_currency.data,form.number.data, form.second_currency.data)
        a = result
    return flask.render_template('product_form.html', form=form,a=a)


response = requests.get('http://www.nbrb.by/api/exrates/rates?periodicity=0')
link = 'postgresql://postgres:Vlad2010@localhost:5432/testdb'
list_currency = connect(response)
print(list_currency)


if __name__ == '__main__':
    app.run(debug=True)
