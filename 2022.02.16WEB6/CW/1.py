from flask import Flask, url_for, request

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


@app.route("/promotion_image")
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                    <title>Рекламаная компания</title>
                  </head>
                  <body>
                  <h1>Жди нас Марс</h1>
                  <img src="{url_for('static', filename='img/mars.jpg')}" alt="Здесь должен быть Марс, но его выкрали">
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    
                    <div class="alert alert-success" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-info" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 align="centre">Анкета претендента</h1>
                            <h2 align="midle">на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" aria-describedby="surnameHelp" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" aria-describedby='nameHelp' placeholder="Введите имя" name="name">
                                    <p></p>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Базовое</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее специальное</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     
                                     <div class="form-group">
                                        <fieldset>
                                        <legend>Какие у вас есть профессии?</legend>
                                          <div>
                                             <input type="checkbox" id="ing-res" name="prof" value="ing-res">
                                             <label for="ing-res">Инженер-исследоватль</label>
                                          </div>
                                          <div>
                                             <input type="checkbox" id="ing-bui" name="prof" value="ing-bui">
                                             <label for="ing-bui">Инженер-строитель</label>
                                          </div>
                                          <div>
                                             <input type="checkbox" id="plane" name="prof" value="plane">
                                             <label for="plane">Пилот</label>
                                          </div>
                                          <div>
                                             <input type="checkbox" id="meteo" name="prof" value="meteo">
                                             <label for="meteo">Метеоролог</label>
                                          </div>
                                          <div>
                                             <input type="checkbox" id="med" name="prof" value="med">
                                             <label for="med">Врач</label>
                                          </div>
                                        </fieldset>
                                    </div>
                                     
                                     <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                     
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите приянть участие в миссии?</label>
                                        <textarea class="form-control" id="why" rows="3" name="about"></textarea>
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
