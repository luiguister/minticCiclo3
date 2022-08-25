from flask import Flask, url_for, request, render_template
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/hola')
def hola():
    return 'hola mundo'

@app.route('/hola2')
@app.route('/hola2/<name>')
def hola2(name='Luis Guillermo'):
    return render_template('hola2.html', name=name)

@app.route('/login')
def login():
    return 'login'

"""@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()"""

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Luis Diaz'))

"""@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'"""

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

app.run(port=5000, debug=True)