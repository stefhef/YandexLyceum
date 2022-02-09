from io import BytesIO

import requests
from PIL import Image

API_KEY = "40d1649f-0493-4b70-98ba-98533de7710b"


def geocode(address):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": API_KEY,
        "geocode": address,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        raise f"""Ошибка выполнения запроса: {response.url}
HTTP статус: {response.status_code}({response.reason})"""

    json_response = response.json()
    return json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]


def get_ll_spn(address):
    toponym = geocode(address)
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    ll = ','.join((toponym_longitude, toponym_lattitude))

    envelope = toponym["boundedBy"]['Envelope']
    l, b = envelope['lowerCorner'].split(' ')
    r, t = envelope["upperCorner"].split(' ')
    dx, dy = str(abs(float(l) - float(r)) / 2), str(abs(float(b) - float(t)) / 2)
    spn = ','.join((dx, dy))
    return ll, spn


def get_nearst_object(ll, spn, map_type="map", add_params=None):
    map_params = {
        "ll": ll,
        "spn": spn,
        "l": map_type,
        "pt":  f"{ll},pm2rdm"
    }

    if isinstance(add_params, dict):
        map_params.update(add_params)

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    return response


def show_map(response):
    Image.open(BytesIO(
        response.content)).show()
