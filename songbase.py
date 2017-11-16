import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yolo'


# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

# define database tables
class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)
    songs = db.relationship('Song', backref='artist')


@app.route('/artist')
def artists():
    #return '<h1>Misy Page on Python</h1>'
    return render_template('artist-all.html')


class Song(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    year = db.Column(db.Integer)
    lyrics = db.Column(db.Text)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))

@app.route('/artist/add', methods=['GET', 'POST'])
def add_artists():
    if request.method == 'GET':
        return render_template('artist-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        about = request.form['about']

        # insert the data into the database
        artist = Artist(name=name, about=about)
        db.session.add(artist)
        db.session.commit()
        return redirect(url_for('show_all_artists'))

@app.route('/')
def home():
    #return '<h1>Misy Page on Python</h1>'
    return render_template('index.html')



##this is how you get the forms to run!!!!!
@app.route('/form-demo', methods=['GET', 'POST'])
def form_demo():
    if request.method == 'GET':
        first_name = request.args.get('first_name')
        if first_name:
            return render_template('form-demo.html', first_name=first_name)
        else:
            first_name = session.get('first_name')
            return render_template('form-demo.html', first_name=first_name)
    if request.method == 'POST':
        session['first_name'] = request.form['first_name']
        return redirect(url_for('form_demo'))
        ##return render_template('form-demo.html', first_name=first_name)

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
