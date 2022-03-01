import requests


cities = tuple(map(str.strip, input().split(',')))
cords = list()
for city in cities:
    geocoder_request = f"https://geocode-maps.yandex.ru/1.x?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode='{city}'&format=json"
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        width = float(json_response["response"]['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')[1])
        cords.append((city, width))
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")

print(min(cords, key=lambda x: x[1])[0])
