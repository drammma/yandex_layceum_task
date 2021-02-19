from flask import Flask

app = Flask(__name__)

PAGES = ['http://127.0.0.1:8080/index', 'http://127.0.0.1:8080/promotion', 'http://127.0.0.1:8080/image_mars']

@app.route('/')
def main_page():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index_page():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion_page():
    countdown_list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                      'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(countdown_list)

@app.route('/image_mars')
def greeting_page():
    return """<!doctype html>
                <html lang="en">
                    <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.jpg" alt="картинка планеты">
                    <br>Вот она, красная планета</br>
                  </body>
                </html>"""

if __name__ == '__main__':
    print(*PAGES, sep='\n')
    app.run(port=8080, host='127.0.0.1')