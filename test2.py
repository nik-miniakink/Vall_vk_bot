import base as bg
from datetime import datetime

now = datetime.now()
noun = True
def month_game():
    for game in bg.games:
        begin_date = game['дата'].split("-")
        begin_date = begin_date[0].split('.')
        date_of_game = datetime(2020, int(begin_date[1]), int(begin_date[0]))

        if now.month == date_of_game.month:

            print(game)

        if date_of_game.month > now.month and noun:
            noun = False
            print('no game')


def near_games():
    for game in bg.games:
        begin_date = game['дата'].split("-")
        begin_date = begin_date[0].split('.')
        date_of_game = datetime(2020, int(begin_date[1]), int(begin_date[0]))
        #n = datetime.now()
        #print(date_of_game)
        #print(datetime.now())

        if date_of_game > datetime.now():
            r = date_of_game - datetime.now()
            print(r)
            message1 = f'Ближайшая игра "{game["название"]}" будет {game["дата"]}, ' \
                        f'в городе {game["город"].title()}, организаторы {game["орагнизаторы"]}.'
            message2 = f'До игры осталось {r.days} дней.'
            print(message1)
            print(message2)

near_games()