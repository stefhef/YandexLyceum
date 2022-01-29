import requests

geocoder_request = "https://geocode-maps.yandex.ru/1.x?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode='Хабаровс'&format=json"
geocoder_request2 = "https://geocode-maps.yandex.ru/1.x?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode='Красная площадь, 1'&format=json"
geocoder_request3 = "https://geocode-maps.yandex.ru/1.x?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode='Красная площадь, 1'&format=json"
geocoder_request4 = "https://geocode-maps.yandex.ru/1.x?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode='Красная площадь, 1'&format=json"

response = requests.get(geocoder_request)
if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    toponym_coodrinates = toponym["Point"]["pos"]
    print('Исторический музей города Москвы имеет адрес: "' + toponym_address + '" и координаты:', toponym_coodrinates)
else:
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
