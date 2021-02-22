from flask import Flask, url_for

app = Flask(__name__)

PAGES = ['http://127.0.0.1:8080/index', 'http://127.0.0.1:8080/promotion', 'http://127.0.0.1:8080/image_mars',
         'http://127.0.0.1:8080/promotion_image']


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
def image_mars_page():
    return """<!doctype html>
                <html lang="en">
                    <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1 align="center">Жди нас, Марс</h1>
                    <p align="center"><img align="center" src="/static/img/planet.png" width="550" height="400" alt="картинка планеты"></p>
                    <p align="center">Вот она какая, красная планета</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image_page():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                        <h1 align="center">Жди нас, Марс</h1>

                        <p align="center"><img align="center" src="/static/img/planet.png" width="550" height="350" alt="картинка планеты"></p>
                        <div align="center" class="alert alert-primary" role="alert">
                          Человечество вырастает из детства.
                        </div>
                        <div align="center" class="alert alert-success" role="alert">
                          Человечеству мала одна планета.
                        </div>
                        <div align="center" class="alert alert-secondary" role="alert">
                          Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div align="center" class="alert alert-warning" role="alert">
                          И начнем с Марса!
                        </div>
                        <div align="center" class="alert alert-danger" role="alert">
                          Присоединяйся!
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    print(*PAGES, sep='\n')
    app.run(port=8080, host='127.0.0.1')
