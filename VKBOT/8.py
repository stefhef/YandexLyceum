import os
import random

import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from dotenv import load_dotenv

load_dotenv()


def main():
    TOKEN = os.environ.get('TOKEN_VK')

    vk_session_bot = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session_bot, 208852865)
    vk_bot = vk_session_bot.get_api()

    vk_session_user = vk_api.VkApi(os.environ.get('LOGIN'), os.environ.get('PASSWORD'))
    vk_session_user.auth()
    vk_user = vk_session_user.get_api()

    owner_id = -208852865
    album_id = 281566517

    photos = vk_user.photos.get(album_id=album_id, owner_id=owner_id)["items"]

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            random_photo = random.choice(photos)
            send_photo = f"photo{owner_id}_{random_photo['id']}"
            from_user = vk_user.users.get(user_ids=event.obj.message["from_id"], fields="city")[0]
            user_name = from_user["first_name"]

            vk_bot.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Привет, {user_name}",
                                 random_id=get_random_id(),
                                 attachment=send_photo)


if __name__ == '__main__':
    main()
