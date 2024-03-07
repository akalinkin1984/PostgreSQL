import psycopg2


def create_db(conn):
    """
    Функция, создающая структуру БД (таблицы).
    """
    with conn.cursor() as cur:
        # cur.execute('''
        #             DROP TABLE phones;
        #             DROP TABLE clients;
        #             ''')
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS clients(
                        id_client SERIAL PRIMARY KEY,
                        first_name VARCHAR(40) NOT NULL,
                        last_name VARCHAR(40) NOT NULL,
                        email VARCHAR(80) UNIQUE NOT NULL
                                                        );
                    ''')

        cur.execute('''
                    CREATE TABLE IF NOT EXISTS phones(
                        id_phone SERIAL PRIMARY KEY,
                        id_client INTEGER NOT NULL REFERENCES clients(id_client),
                        phone INTEGER UNIQUE
                                                    );
                    ''')

        conn.commit()


def add_client(conn, first_name, last_name, email, phone=None):
    """
    Функция, позволяющая добавить нового клиента.
    """
    with conn.cursor() as cur:
        cur.execute('''
                    INSERT INTO clients(first_name, last_name, email)
                    VALUES(%s, %s, %s);
                    ''', (first_name, last_name, email))

        cur.execute('''
                    SELECT id_client FROM clients
                    WHERE email = %s;
                    ''', (email, ))

        id_client = cur.fetchone()[0]

        cur.execute('''
                    INSERT INTO phones(id_client, phone)
                    VALUES(%s, %s);
                    ''', (id_client, phone))

        conn.commit()


def add_phone(conn, id_client, phone):
    """
    Функция, позволяющая добавить телефон для существующего клиента.
    """
    with conn.cursor() as cur:
        cur.execute('''
                    INSERT INTO phones(id_client, phone)
                    VALUES(%s, %s);
                    ''', (id_client, phone))

        conn.commit()


def change_client(conn, id_client, first_name=None, last_name=None, email=None, phone=None):
    """
    Функция, позволяющая изменить данные о клиенте.
    """
    with conn.cursor() as cur:
        cur.execute('''
                    UPDATE clients
                    SET first_name = %s, last_name = %s, email = %s
                    WHERE id_client = %s;
                    ''', (first_name, last_name, email, id_client))

        cur.execute('''
                    SELECT id_phone, phone FROM phones 
                    WHERE id_client = %s;
                    ''', (id_client, ))

        phones_list = cur.fetchall()

        if (len(phones_list) == 1) and (phones_list[0][1] is None):
            print('У клиента нет телефонов!')
        if (len(phones_list) == 1) and (phones_list[0][1] is not None):
            cur.execute('''
                        UPDATE phones
                        SET phone = %s
                        WHERE id_client = %s;
                        ''', (phone, id_client))
        elif len(phones_list) > 1:
            print('У клиента несколько телефонов. Для изменения введите id нужного номера телефона. Доступные варианты:')
            for id_num, number in phones_list:
                print(f'id {id_num} - номер {number}')
            question = input('Введите id номера телефона который хотите изменить: ')
            cur.execute('''
                        UPDATE phones
                        SET phone = %s
                        WHERE id_phone = %s;
                        ''', (phone, question))

        conn.commit()


def delete_phone(conn, id_client, phone):
    """
    Функция, позволяющая удалить телефон для существующего клиента.
    """
    with conn.cursor() as cur:
        cur.execute('''
                    DELETE FROM phones
                    WHERE id_client = %s AND phone = %s;
                    ''', (id_client, phone))

        conn.commit()


def delete_client(conn, id_client):
    """
    Функция, позволяющая удалить существующего клиента.
    """
    with conn.cursor() as cur:
        cur.execute('''
                    DELETE FROM phones
                    WHERE id_client = %s;
                    ''', (id_client, ))

        cur.execute('''
                    DELETE FROM clients
                    WHERE id_client = %s;
                    ''', (id_client, ))

        conn.commit()


def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    """
    Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
    """
    def answer_func(func):
        if func is not None:
            id_client, name, surname = func
            print(f'Найдет клиент с id - {id_client}, имя - {name}, фамилия - {surname}.')
        else:
            print('Клиент не найден!')

    with conn.cursor() as cur:
        if email:
            cur.execute('''
                        SELECT id_client, first_name, last_name FROM clients 
                        WHERE email = %s;
                        ''', (email, ))
            answer_func(cur.fetchone())

        elif phone:
            cur.execute('''
                        SELECT c.id_client, c.first_name, c.last_name FROM clients AS c
                        JOIN phones AS p ON c.id_client = p.id_client
                        WHERE p.phone = %s
                        ''', (phone, ))
            answer_func(cur.fetchone())

        elif last_name or first_name:
            cur.execute('''
                        SELECT id_client, first_name, last_name FROM clients 
                        WHERE last_name = %s OR first_name = %s;
                        ''', (last_name, first_name))
            answer_func(cur.fetchone())

        else:
            print('Некорректно вызвана функция find_client!')


if __name__ == '__main__':
    database = input('Введите название БД: ')
    user = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')

    conn = psycopg2.connect(database=database, user=user, password=password)

    create_db(conn)

    add_client(conn, 'Вася', 'Пупкин', 'pupok@mail.ru', 555555)
    add_client(conn, 'Петя', 'Пистолетов', 'pistol@yandex.ru', 335566)
    add_client(conn, 'Федя', 'Бутылкин', 'bottle@yandex.ru', 222222)
    add_client(conn, 'John', 'Арбузов', 'arbuz@rambler.ru', 335778)
    add_client(conn, 'Оля', 'Свистунова', 'svistok@rambler.ru', 959595)
    add_client(conn, 'Вера', 'Шапочкина', 'shapka@mail.ru')

    add_phone(conn, 1, 232323)
    add_phone(conn, 3, 444444)

    change_client(conn, 1, 'Вася', 'Пупкин', 'pupok@mail.ru', 101010)
    change_client(conn, 4, 'John', 'Персиков', 'persik@rambler.ru', 202020)
    change_client(conn, 6, 'Верочка', 'Шапочкина', 'shapka55@mail.ru')

    delete_phone(conn, 1, 55555)
    delete_phone(conn, 3, 444444)

    delete_client(conn, 1)
    delete_client(conn, 6)

    find_client(conn, last_name='Свистунова', email='svistok@rambler.ru')
    find_client(conn, phone=222222)
    find_client(conn)
    find_client(conn, 'Вася', 'Пупкин', 'pupok@mail.ru')

    conn.close()
