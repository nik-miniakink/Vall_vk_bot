import requests
import base
import urllib
from urllib.request import urlretrieve
"""модуль работы с погодой для бота вконтакте"""

url_w = 'http://wttr.in'  # url сайта с погодой, который формирует ответ на запрос о погоде


"""Формирование запросов к сайту о погоде. Справка по параметрам http://wttr.in/:help """
parameters = {
    'M': '',
    'p': 'p',
    '3': '',
    'q': '',
    'm': '',
    'F': '',
    'transparency': '200',
    'lang': 'ru',
    'png': '.png'


}

def weather(citi):
    """отправка запроса с именем города и параметрами и получение адреса *.png файла с прогнозом погоды"""
    url = f'{url_w}/{citi}.png'
    weather_photo_url = requests.get(url, params=parameters)
    return weather_photo_url.url



def make_weather_image(citi):
    """сохраение картинки с прогнозом погоды на свой сервер, в папку с проектом."""
    """Файл перезаписывается при каждом создании запроса погоды"""
    destination = 'forecast.png'
    urlretrieve(weather(citi), destination)
    return destination









    




