from flask import Flask

app = Flask(__name__)

PAGES = ['http://127.0.0.1:8081/index', 'http://127.0.0.1:8081/promotion', 'http://127.0.0.1:8081/image_mars']

@app.route('/')
def main_page():
    return "Миссия Марса"


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
                    <h1 align="center">Жди нас, Марс!</h1>
                    <p align="center"><img align="center" src="/static/img/planet.png" width="550" height="400" alt="картинка планеты"></p>
                    <p align="center">Вот она какая, красная планета</p>
                  </body>
                </html>"""

if __name__ == '__main__':
    print(*PAGES, sep='\n')
    app.run(port=8081, host='127.0.0.1')