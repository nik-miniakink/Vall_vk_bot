import peewee
from base_pg import *
from base import *

"""Модуль для работы с функционалом peewee. Тут представленны функции для работы с таблицами PostgreSQL """

if __name__ == '__main__':
    try:
        pg_db.connect()
        AmigosBase.create_table()
    except peewee.InternalError as px:  # Проверка на ошибку подключения. Если будет ошибка, то вернется код ошибки
        print(str(px))

    try:
        Games.create_table()
    except peewee.InternalError as px:
        print(str(px))


def add_unit(vk_id, name, nic, rang):  # функция добавления члена команды в таблицу amigos_base
    row = AmigosBase(
        vk_id=vk_id,
        name=name.lower(),
        nic=nic.lower().strip(),
        rang=rang.lower().strip()
    )
    row.save()


def make_games_table(date, citi, title, orgs):  # функция добавления игры  в таблицу games
    row = Games(
        date=date,
        citi=citi.lower().strip(),
        title=title,
        orgs=orgs
    )
    row.save()


def find_all_units():  # функция для работы с таблицей amigos_base. Возвращает всю таблицу amigos_base
    return AmigosBase.select()


def get_game():  # функция для работы с таблицей Games. Возвращает всю таблицу Games
    return Games.select()

# def transf_game_info():
#     """Функция для перевода всей базы игр из рукописной базы в таблицу PGSQL
#     скорее всего кроме 2020 года, больше использоваться не будет"""
#     for game in games:
#         date=game['дата']
#         citi=game['город']
#         title=game['название']
#         orgs=game['орагнизаторы']
#         make_games_table(date, citi, title, orgs)
