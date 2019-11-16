from flask import Flask

app = Flask(__name__)


@app.route('/flasktest/')
def flasktest():
    return 'Hedgehog Street 2'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("80"))
