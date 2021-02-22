from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection_page():
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
                            <h1 align="center">Анкета претендента <br> на участие в миссии</h1>
                            <div>
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <br></br>
                                    <input type="email" class="form-control" id="email" placeholder="Введите адрес электронной почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="school" name="school">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Какие у вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="work" id="ingeneer" value="ingeneer" checked>
                                          <label class="form-check-label" for="ingeneer">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="work" id="Пилот" value="pilot">
                                          <label class="form-check-label" for="pilot">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="work" id="Доктор" value="doctor">
                                          <label class="form-check-label" for="doctor">
                                            Доктор
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="work" id="Строитель" value="stroit">
                                          <label class="form-check-label" for="stroit">
                                            Строитель
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="gender" id="муж" value="муж" checked>
                                          <label class="form-check-label" for="муж">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="gender" id="жен" value="жен">
                                          <label class="form-check-label" for="жен">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="motive">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="motive" rows="3" name="motive"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="photo">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(f'Фамилия: {request.form["surname"]}')
        print(f'Имя: {request.form["name"]}')
        print(f'Адрес: {request.form["email"]}')
        print(f'Образование: {request.form["school"]}')
        print(f'Профессия: {request.form["work"]}')
        print(f'Пол: {request.form["gender"]}')
        print(f'Мотивация: {request.form["motive"]}')
        print(f'Фотография: {request.form["photo"]}')
        print(f'Контрольный вопрос: {"OK" if request.form["accept"] == "on" else "NO"}')
        return "Форма отправлена"

if __name__ == '__main__':
    print('http://127.0.0.1:8000/astronaut_selection')
    app.run(port=8000, host='127.0.0.1')
