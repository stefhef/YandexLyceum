from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def path():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <title>Колонизация Марса</title>
                  </head>
                  <body>
                    <p>Человечество вырастает из детства.
<br>Человечеству мала одна планета.
<br>Мы сделаем обитаемыми безжизненные пока планеты.
<br>И начнем с Марса!
<br>Присоединяйся!</p>
                  </body>
                </html>'''


@app.route("/image_mars")
def image_mars():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" alt="Здесь должен быть Марс, но его выкрали">
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
