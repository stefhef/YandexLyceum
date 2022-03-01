from io import BytesIO
import requests
from PIL import Image


url = "https://static-maps.yandex.ru/1.x/?ll=29.966103,59.948612&z=10&l=map&pl=30.281647,59.949763,30.254073,59.958695,30.215311,59.965928,29.912984,59.891145"
response = requests.get(url)
Image.open(BytesIO(response.content)).show()
