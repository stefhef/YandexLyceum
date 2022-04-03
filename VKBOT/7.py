import os
import vk_api
from dotenv import load_dotenv

load_dotenv()


def main(owner_id, album_id):
    vk_session_user = vk_api.VkApi(os.environ.get('LOGIN'), os.environ.get('PASSWORD'))
    try:
        vk_session_user.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk_user = vk_session_user.get_api()

    photos = vk_user.photos.get(album_id=album_id, owner_id=owner_id)["items"]
    for photo in photos:
        for size in photo.get('sizes', None):
            print(f"{size.get('width', None)}X{size.get('height', None)} Url:{size.get('url', None)}")
        print()
    print()


if __name__ == '__main__':
    owner_id = -208852865
    album_id = 281566517
    main(owner_id, album_id)
