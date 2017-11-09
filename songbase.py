from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    #return '<h1>Misy Page on Python</h1>'
    return render_template('index.html')


@app.route('/user/<string:name>/')
def get_user(name):
        #return '<h1>hello %s your age is %d</h1>' % (name,3)
        return render_template('user.html', user_name=name)

@app.route('/songs')
def get_all_songs():
        songs = [
        'Back Where I Come From',
        'Happier',
        'All too Well'
        ]
        return render_template('songs.html', songs=songs)


if __name__ == '__main__':
    app.run()
