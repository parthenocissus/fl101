from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hedgehog Street'


@app.route('/test/')
def hello_world_test():
    return 'Hedgehog Street 2'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
