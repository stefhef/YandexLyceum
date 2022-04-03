from flask import Flask, url_for, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static\\img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return render_template('form.html', image=url_for('static', filename='img/standart.png'))
    elif request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save('static\\img', filename)
        print(filename)
        return render_template('form.html', image=url_for('static/img', filename=file.filename))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
