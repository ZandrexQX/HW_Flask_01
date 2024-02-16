from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    context = {
        'title': 'Интернет-магазин',
    }
    return render_template('main.html', **context)


@app.route('/computers/')
def computers():
    context = {
        'title': 'Компьютеры',
    }
    return render_template('computers.html', **context)


@app.route('/noutebook/')
def noutebooks():
    context = {
        'title': 'Ноутбуки',
    }
    return render_template('noutebook.html', **context)


@app.route('/telephones/')
def telephones():
    context = {
        'title': 'Телефоны',
    }
    return render_template('telephone.html', **context)


if __name__ == '__main__':
    app.run(debug=True)