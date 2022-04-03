import os
from datetime import timedelta, timezone, datetime
import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from dotenv import load_dotenv

load_dotenv()


def main():

    TOKEN = os.environ.get('TOKEN_VK')

    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 208852865)
    vk = vk_session.get_api()

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            message = event.obj.message.get('text').lower()
            if 'время' in message or 'число' in message or 'дата' in message or 'день' in message:
                dt = datetime.now(timezone(timedelta(hours=3)))

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=dt.strftime('Дата, время и день недели в Москве: %d.%m.%Y %H:%M:%S %A'),
                                 random_id=get_random_id())
            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Могу подсказать дату, время и день недели в Москве. Для этого напишите одно "
                                         "из следующих слов: «время», «число», «дата», «день»",
                                 random_id=get_random_id())


if __name__ == '__main__':
    main()
