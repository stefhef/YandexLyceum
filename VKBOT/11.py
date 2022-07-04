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




if __name__ == '__main__':
    main()
