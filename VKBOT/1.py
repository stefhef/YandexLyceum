import vk_api
import datetime
from dotenv import load_dotenv

load_dotenv()

def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод wall.get
    response = vk.wall.get(count=5, offset=1)
    if response['items']:
        for item in response['items']:
            print(item['text'])
            print(datetime.datetime.utcfromtimestamp(int(item['date'])))


if __name__ == '__main__':
    main()
