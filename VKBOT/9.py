import os
from flask import Flask, url_for, request, render_template
from vk_api import vk_api

app = Flask(__name__)

login, password = os.environ.get('LOGIN'), os.environ.get('PASSWORD')
# login, password = LOGIN, PASSWORD
vk_session = vk_api.VkApi(login, password)
try:
    vk_session.auth()
except vk_api.AuthError as error_msg:
    print(error_msg)
    exit()
vk = vk_session.get_api()


@app.get('/vk_stat/<int:group_id>')
def vk_stat(group_id):
    global vk
    out = {'cities': [],
           'ages': {'12-18': 0,
                    '18-21': 0,
                    '21-24': 0,
                    '24-27': 0,
                    '27-30': 0,
                    '30-35': 0,
                    '35-45': 0,
                    '45-100': 0}}
    #  , stats_groups='reach'
    try:
        responce = vk.stats.get(group_id=group_id, interval='all')[0]
    except vk_api.exceptions.ApiError as error_msg:
        return error_msg
    out['likes'] = responce.get('activity', {}).get('likes', 0)
    out['comments'] = responce.get('activity', {}).get('comments', 0)
    out['subscribed'] = responce.get('activity', {}).get('subscribed', 0)
    for item in responce.get('reach', {}).get('age', {}):
        out['ages'][item['value']] = item['count']
    for citie in responce.get('reach', {}).get('cities', {}):
        out['cities'].append(citie['name'])
    return render_template('vk_stat.html', out=out)


# if __name__ == '__main__':
    # app.run(port=8080, host='127.0.0.1')
