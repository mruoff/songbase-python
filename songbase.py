from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Misy Page on Python</h1>'


@app.route('/user/<string:name>/')
def get_user(name):
        return '<h1>hello %s your age is %d</h1>' % (name,3)


if __name__ == '__main__':
    app.run()
