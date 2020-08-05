import datetime
import random
import string

from flask import Flask, send_file, send_from_directory

app = Flask('app')


@app.route('/')
def hello():
    return 'Hello'


@app.route('/now')
def now():
    return str(datetime.datetime.now())


@app.route('/gen_password')
def gen_password():
    return ''.join([
        random.choice(string.ascii_lowercase)
        for _ in range(10)
    ])


@app.route('/get_requirements')
def get_requirements():
    return send_file('./requirements.txt')

@app.route('/get_requirements2')
def get_requirements2():
    return send_from_directory('./', 'requirements.txt', as_attachment=True)


if __name__ == '__main__':
    app.run()


