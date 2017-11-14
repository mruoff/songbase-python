from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yolo'

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
    if request.method == 'POST':s
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
