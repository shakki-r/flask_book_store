from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def home():
#     return '<h1> hello </h1>'


@app.route('/shakkir')
def shakkir():
    return '<h2>this is shakkir </h2>'


# variable passing using string

@app.route('/profile/<username>')
def profile_name(username):
    return '<h1> username is : %s </h1>' % username


# variable passing integer
@app.route('/id/<int:id>')
def id_display(id):
    return '<h1> id is %d </h1>' % id


# value passing template and if condition
@app.route('/profile/template_name/<username>')
def template_value_passing(username):
    return render_template('index.html', username=username, value=6)


# for loop

@app.route('/names')
def name_display():
    names = ['manu', 'shakkir', 'fathih', 'vivak', 'asif', 'shameel', 'abu']
    length = len(names)
    return render_template('names.html', names=names, len=length)


# object rendering
@app.route('/')
def movie():
    movie_details = [{'name': 'The Alchemist', 'author': 'Paulo Coelho',
                      'img': 'https://m.media-amazon.com/images/I/81fiotccNCL._AC_UF1000,1000_QL80_.jpg'},
                     {'name': 'Atomic Habits', 'author': 'James Clear',
                      'img': 'https://jamesclear.com/wp-content/uploads/2023/05/atomic-habits-dots.png'},
                     {'name':
                          'ആടുജീവിതം', 'author': ' Benyamin',
                      'img': 'https://m.media-amazon.com/images/I/71qifrtz+yL._AC_UF894,1000_QL80_.jpg'},

                     ]
    return render_template('movie.html', movie=movie_details)


app.run(debug=True)
