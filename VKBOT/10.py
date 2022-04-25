from datetime import datetime
import os
import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from dotenv import load_dotenv

load_dotenv()


def main():
    session_storage = {}

    TOKEN = os.environ.get('TOKEN_VK')

    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 208852865)
    vk = vk_session.get_api()

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            message = event.obj.message.get('text').lower()
            user_id = event.obj.message['from_id']

            if user_id not in users:
                vk.messages.send(user_id=user_id,
                                 message="Могу сказать в какой день недели была та или иная дата. Введите дату в "
                                         "формате YYYY-MM-DD",
                                 random_id=get_random_id())
                users.append(user_id)
            else:
                week = datetime.strptime(message, '%Y-%m-%d')
                vk.messages.send(user_id=user_id,
                                 message=weeks.get(week.weekday(), 'Неизвестно'),
                                 random_id=get_random_id())


if __name__ == '__main__':
    main()
