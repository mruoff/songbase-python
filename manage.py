##file needed to manage and run code without the debug/ how you run a flask script

from flask_script import Manager
from songbase import app
from songbase import app, db, Artist, Song

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    coldplay = Artist(name='Coldplay', about='Coldplay is a British rock band.')
    maroon5 = Artist(name='Maroon 5', about='Maroon 5 is an American pop rock band.')
    song1 = Song(name='yellow', year=2004, lyrics='blah blah', artist=coldplay)
    db.session.add(coldplay)
    db.session.add(maroon5)
    db.session.commit()


if __name__=='__main__':
    manager.run()
