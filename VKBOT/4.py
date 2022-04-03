import os

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
            from_user = vk.users.get(user_ids=event.obj.message["from_id"], fields="city")[0]
            user_name = from_user["first_name"]
            user_city = from_user.get("city", None)
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"Привет, {user_name}",
                             random_id=get_random_id())
            if user_city:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Как поживает {user_city['title']}?",
                                 random_id=get_random_id())


if __name__ == '__main__':
    main()
