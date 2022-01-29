import requests

geocoder_request = "https://geocode-maps.yandex.ru/1.x?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode='Хабаровс'&format=json"
geocoder_request2 = "https://geocode-maps.yandex.ru/1.x?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode='Уфа'&format=json"
geocoder_request3 = "https://geocode-maps.yandex.ru/1.x?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode='Нижний Новгород'&format=json"
geocoder_request4 = "https://geocode-maps.yandex.ru/1.x?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode='Калиниград'&format=json"

response = requests.get(geocoder_request)
response2 = requests.get(geocoder_request2)
response3 = requests.get(geocoder_request3)
response4 = requests.get(geocoder_request4)
if response:
    json_response = response.json()
    json_response2 = response2.json()
    json_response3 = response3.json()
    json_response4 = response4.json()
    okryg = json_response["response"]['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components'][1]['name']
    okryg2 = json_response2["response"]['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components'][1][
        'name']
    okryg3 = json_response3["response"]['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components'][1][
        'name']
    okryg4 = json_response4["response"]['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components'][1][
        'name']
    print("Хабаровск", okryg)
    print("Уфа", okryg2)
    print("Нижний Новгород", okryg3)
    print("Калининград", okryg4)
else:
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
