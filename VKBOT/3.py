import os
import vk_api
from dotenv import load_dotenv

load_dotenv()


def main():


    login, password = os.environ.get('LOGIN'), os.environ.get('PASSWORD')
    # login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    upload = vk_api.upload.VkUpload(vk_session)

    types_photo = ['jpg', 'png', 'gif']
    photos = tuple(filter(lambda x: x.split('.')[-1] in types_photo, os.listdir('static/img')))

    album_id = 281566517
    group_id = 208852865
    for photo in photos:
        upload.photo(f'static\\img\\{photo}', album_id=album_id, group_id=group_id)


if __name__ == '__main__':
    main()
