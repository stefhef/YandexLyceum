import os
import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from dotenv import load_dotenv
import wikipedia


load_dotenv()


def main():
    users = []

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
                                 message="Что хотите узнать?",
                                 random_id=get_random_id())
                users.append(user_id)
            else:
                vk.messages.send(user_id=user_id,
                                 message=wikipedia.summary(message, sentences=2),
                                 random_id=get_random_id())
                users.remove(user_id)


if __name__ == '__main__':
    wikipedia.set_lang("ru")
    main()
