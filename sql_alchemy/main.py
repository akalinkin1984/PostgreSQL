import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Stock, Shop, Sale
import os
import json


driver_db = input('Введите название СУБД: ')
login = input('Введите имя пользователя: ')
password = input('Введите пароль: ')
host = input('Введите host сервера: ')
port = input('Введите порт сервера: ')
name_db = input('Введите название БД: ')

DSN = f'{driver_db}://{login}:{password}@{host}:{port}/{name_db}'

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

path = os.getcwd() + '\\tests_data.json'

Session = sessionmaker(bind=engine)
session = Session()

with open(path, 'r') as f:
    data = json.load(f)

for s in data:
    model = s.get('model').capitalize()
    session.add(eval(model)(id=s.get('pk'), **s.get('fields')))
session.commit()

input_publisher = input('Введите имя или id издателя(1-4): ')

if input_publisher.isdigit():
    res = (session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
           .join(Publisher, Book.publishers)
           .join(Stock, Book.stocks)
           .join(Shop, Stock.shops)
           .join(Sale, Stock.sales)
           .filter(Publisher.id == input_publisher)).all()
else:
    res = (session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
           .join(Publisher, Book.publishers)
           .join(Stock, Book.stocks)
           .join(Shop, Stock.shops)
           .join(Sale, Stock.sales)
           .filter(Publisher.name == input_publisher)).all()

if res:
    for book, shop, price, date in res:
        print(f'{book:40}| {shop:10}| {price:10}| {date:25}|')
else:
    print('Такого издателя нет в БД!')

session.close()
