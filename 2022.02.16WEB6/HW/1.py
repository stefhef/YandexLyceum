from flask import Flask, url_for, request, render_template

app = Flask(__name__)
data = {'Марс': ['Эта планета близка к земли', 'Есть вода и ресурсы', 'Небольшое МП', 'Она просто красивая, красная',
                 "Хочу туда"],
        'Земля': ['Мы тут живём', 'И ещё много все', 'Очень много', 'Воды', 'И тчо-то ещё'],
        'Венера': ['Что-то', 'Не, я действительно мало знаю', 'Очень мало', 'Я тупой(((((', 'Ну и ладно'],
        'Солнышко': ['Тёплое', 'Очень тёпленькое', 'Крайне тёпленькое', 'Солнышко)))))', 'Большое'],
        'Уран': ['Маленькое', 'Далёкое', 'Не хочу думать', 'Вообще не хочу', 'Ну и хватит']}


@app.route('/')
def path():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    global data
    lst = data.get(planet_name, 'Земля')
    return render_template('planet.html', data=lst, planet_name=planet_name)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level: int, rating: float):
    return render_template('result.html', nickname=nickname, level=level, rating=rating)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
