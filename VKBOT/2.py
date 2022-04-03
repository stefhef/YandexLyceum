import vk_api
import os

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

    vk = vk_session.get_api()

    response = vk.friends.get(fields='nickname, bdate')
    friends = sorted(list(map(lambda x: (x['last_name'], x['first_name'], x.get('bdate', '')), response['items'])))
    for friend in friends:
        print(*friend)


if __name__ == '__main__':
    main()
