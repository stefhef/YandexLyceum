from io import BytesIO
import requests
from PIL import Image


url = "https://static-maps.yandex.ru/1.x/?ll=37.617617,55.755811&z=10&l=sat,skl&pt=37.440343,55.817824,pm2rdm~37.560161,55.791477,pm2dgm~37.553728,55.715742,pm2ywm"
response = requests.get(url)
Image.open(BytesIO(response.content)).show()
