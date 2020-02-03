import vk_api
from vk_api.upload import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from random import randint
import weather as w
import sec_and_pass as p


"""Модуль для авторизации в API VK
token: уникальный токен, для подключения от именни сообщества, текущий токен имеет все права
vk_session: авторизация в ВК для сообщества, с использованием токена"""

token = p.token
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()


def random_id():
    """случайное число, для присваивания номера сообщению при отправки, во избежании повтора отправки сообщения"""
    random_noun = 0
    random_noun += randint(0, 10000000)
    return random_noun


longpoll = VkBotLongPoll(vk_session, group_id=p.id)
send_photo = VkUpload(vk_session)  # присваиваю короткое имя для модуля VkUpload


def wait_message():
    """Ожидание события loongpool если событие 'сообщение, то забираем текст сообщения'"""
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            message = event.object.message['text']
            global user_id
            global peer_id
            user_id = event.message.from_id
            peer_id = event.message.peer_id
            return message



def send_message_png(list_query):
    """формирование картинки с прогнозом погоды и отправка ее в ответ"""
    """в list_query содержится город, далее идет проверка, если город кончается на 'е', то отрезаем ее формируем"""
    citi = list_query[-1]
    temp = citi[-1:]
    if temp == 'е':
        citi = citi[:-1]

    # используя VK.api для питона вызываю метод отправки фото в сообщении photo_messages
    get_photo = send_photo.photo_messages(w.make_weather_image(citi))
    photo = get_photo[0]  # достаю словарь с параметрами формирования и отпавки сообщения из списка
    # формирую параметр attachment для vk.api
    attac = 'photo' + '{}_{}'.format(photo["owner_id"], photo["id"])
    if peer_id != user_id:  # если сообщение пришло  от чата 2000000001, значит это сообщение из чата
        vk.messages.send(      # и поэтому параметр user_id не нужен для отправки сообщения
            #user_id=user_id,
            message=f'Погода в {list_query[-1].title()} как ты хотел, дорогой! ',
            random_id=random_id(),
            peer_id=peer_id,
            attachment=attac
        )
    else:
        vk.messages.send(
            user_id=user_id,
            message=f'Погода в {list_query[-1].title()} как ты хотел, дорогой! ',
            random_id=random_id(),
            peer_id=peer_id,
            attachment=attac
        )


def send_message(message_ans):
    """функция отправки тестового сообщение метом апи вконтакте"""
    if peer_id != user_id:  # если сообщение пришло от 2000000001, значит это сообщение из чата
        vk.messages.send(      # и поэтому параметр user_id не нужен для отправки сообщения
            # user_id=user_id,
            message=message_ans,
            random_id=random_id(),
            peer_id=peer_id
        )
    else:
        vk.messages.send(
            user_id=user_id,
            message=message_ans,
            random_id=random_id(),
            peer_id=peer_id
        )