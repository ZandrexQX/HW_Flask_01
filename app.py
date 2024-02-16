from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    context = {
        'title': 'Интернет-магазин',
        'name': 'Zandrex'
    }
    return render_template('base.html', **context)


if __name__ == '__main__':
    app.run(debug=True)