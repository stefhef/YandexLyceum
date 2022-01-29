import requests

geocoder_request = "https://geocode-maps.yandex.ru/1.x?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode='Петровка," \
                   "38с9'&format=json "

response = requests.get(geocoder_request)
if response:
    json_response = response.json()
    toponym = json_response["response"]['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
        'GeocoderMetaData']['AddressDetails']['Country']['AdministrativeArea']['Locality']['Thoroughfare']['Premise'][
        'PostalCode']['PostalCodeNumber']
    print("Почтовый адрес", toponym)
else:
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
