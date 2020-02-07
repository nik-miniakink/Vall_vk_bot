import vk_interaction as vk_i
from vk_interaction import *  # никогда так нельзя импортировать делать, но сейчас я так хочу
from datetime import datetime
import base as bg
from operations import *


def check_message():
    """функция ожидания события, прихода сообщения"""
    message = wait_message()  # данная функция находится в модуле vk_interaction.py wait_message()
    appeal_to_vall = ['велл', 'вэлл']  # список для проверки, что сообщение адресовано Велл
    message_as_list = (message.split()).lower  # превращение строки сообщения в список в нижнем регистре
    if message_as_list[0] in appeal_to_vall:  # проверка, что начало сообщения содержит обращение к Велл
        check_what_wont(message_as_list)
    else:
        vk_i.send_message('А вы к кому сейчас обращаетесь?')  # или тут принт? или отправить сообщение через VK?


def check_what_wont(message):
    """Проверка того, что спрашивается в сообщении"""
    hello = ['привет', 'дела?', 'здравствуй', 'дела']
    weather = ['погода', 'прогноз', 'погоды', 'погоду']
    schedule = {1: 'когда ближайшая БИ?', 2: 'игры в этом месяце', 3: 'оставшиеся игры?', }
    who_are_you = ['расскажи о себе', 'расскажи о себе.']  # повторяющиеся значения
    list_query = ' '.join(message)  # Зачем ведь она у нас изначально есть  в виде message bp ghtlsleotq aeyrwbb

    for message in hello:
        if message in message:
            talk_messages(message)

    for message in weather:
        if message in message:
            return vk_i.send_message_png(message)

    for key, value in schedule.items():
        if value in list_query:
            if key == 1:
                near_games()
            elif key == 2:
                mounthly_games()
            #else:
             #  № тут должна быть функция выводящая оставщиеся игр

    if list_query in who_are_you:
        about_vell()


def talk_messages(dialog):
    """Функция для поболтать. Это для оживления Велл ;) """
    if dialog == 'привет':
        vk_i.send_message('Привет мой дорогой!')
    elif dialog == 'дела?':
        vk_i.send_message('У меня великолепно! Я живу!')
    elif dialog == 'здравствуй':
        vk_i.send_message('Доброго времени суток, мой хороший!')


def near_games():
    """формирование ответа на вопрос, когда ближайшая БИ"""
    games = get_game()
    for game in games:
        begin_date = game.date.split("-")
        begin_date = begin_date[0].split('.')
        date_of_game = datetime(2020, int(begin_date[1]), int(begin_date[0]))

        if date_of_game > datetime.now():
            r = date_of_game - datetime.now()
            message1 = f'Ближайшая игра "{game.title}" будет {game.date}, ' \
                       f'в городе {game.citi.title()}, организаторы {game.orgs}.'
            message2 = f'До игры осталось {r.days} дней.'
            return vk_i.send_message(message1), vk_i.send_message(message2)


def mounthly_games():
    """ поиск и ответ какие  игры будут в этом месяце"""
    now = datetime.now()
    noun = True
    vk_i.send_message('В этом месяце')
    games=get_game()
    for game in games:
        begin_date = game.date.split("-")
        begin_date = begin_date[0].split('.')
        date_of_game = datetime(2020, int(begin_date[1]), int(begin_date[0]))

        if now.month == date_of_game.month:
            vk_i.send_message(f'"{game.title}" будет в {game.date}, '
                              f'в городе {game.citi.title()}, организаторы {game.orgs}.')

        if date_of_game.month > now.month and noun:
            noun = False
            vk_i.send_message('Нет игр!')


def about_vell():
    vk_i.send_message(bg.about_Vell[0])
    vk_i.send_message(bg.about_Vell[1])
    vk_i.send_message(bg.about_Vell[2])
    vk_i.send_message(bg.about_Vell[3])
    # send_message(bg.about_Vell[4])
    # send_message(bg.about_Vell[5])


while True:
    check_message()
