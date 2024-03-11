import os
import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Stock, Shop, Sale


driver_db = input('Введите название СУБД: ')
login = input('Введите имя пользователя: ')
password = input('Введите пароль: ')
host = input('Введите host сервера: ')
port = input('Введите порт сервера: ')
name_db = input('Введите название БД: ')

DSN = f'{driver_db}://{login}:{password}@{host}:{port}/{name_db}'

engine = sqlalchemy.create_engine(DSN)

path = os.getcwd() + '\\tests_data.json'

answer = input('Введите имя или id издателя: ')

Session = sessionmaker(bind=engine)
session = Session()


def entering_data(file, sess):
    with open(file, 'r') as f:
        data = json.load(f)

    for s in data:
        model = s.get('model').capitalize()
        sess.add(eval(model)(id=s.get('pk'), **s.get('fields')))
    sess.commit()


def getting_data(input_publisher, sess):
    res = (sess.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
           .join(Publisher, Book.publisher)
           .join(Stock, Book.stocks)
           .join(Shop, Stock.shop)
           .join(Sale, Stock.sales))

    if input_publisher.isdigit():
        res = res.filter(Publisher.id == input_publisher).all()
    else:
        res = res.filter(Publisher.name == input_publisher).all()

    if res:
        for book, shop, price, date in res:
            print(f'{book:40}| {shop:10}| {price:10}| {date:25}|')
    else:
        print('Такого издателя нет в БД!')


if __name__ == '__main__':
    create_tables(engine)
    entering_data(path, session)
    getting_data(answer, session)


session.close()
