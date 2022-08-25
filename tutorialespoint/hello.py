import os
from flask import Flask, redirect, url_for, request, render_template, make_response, session, escape, abort, flash, g
from werkzeug.utils import secure_filename
import sqlite3 as sql
from forms import ContactoForm
from datetime import datetime

path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app = Flask(__name__)
app.secret_key = 'any random string'


@app.route('/')
def hello_world():
   return 'hello world'
app.add_url_rule('/', 'hello', hello_world)

@app.route('/ruta')
def ruta():
   return 'ruta'

#routes
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

#building
@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

#HTTP Methods
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

#Templates
@app.route('/template')
def template():
   return '<html><body><h1>Hello World template</h1></body></html>'

@app.route('/template2/<user>')
def template2(user):
   return render_template('hello.html', name = user)

@app.route('/template3/<int:score>')
def template3(score):
   return render_template('hello.html', marks = score)

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

#Static Files
@app.route("/static")
def index():
   return render_template("index.html")

#Sending Form Data to Template
@app.route('/student')
def student():
   return render_template('student.html')

@app.route('/result2',methods = ['POST', 'GET'])
def result2():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

#cookies
@app.route('/cookie')
def cookie():
   return render_template('login2.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
      user = request.form['nm']
   
      resp = make_response(render_template('readcookie.html'))
      resp.set_cookie('userID', user)
   
   return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'

#Sessions
@app.route('/sessions')
def sesiones():
   if 'username' in session:
      username = session['username']
      return 'Logged in as ' + username + '<br>' + \
            "<b><a href = '/logoutSession'>click here to log out</a></b>"
   return "You are not logged in <br><a href = '/loginSession'></b>" + \
      "click here to log in</b></a>"

@app.route('/loginSession', methods = ['GET', 'POST'])
def loginSession():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('sesiones'))
   return '''
	
   <form action = "" method = "post">
      <p><input type = text name = username></p>
      <p><input type = submit value = Login></p>
   </form>
	'''

@app.route('/logoutSession')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('sesiones'))

# Redirect & Errors
@app.route('/redireccionar')
def redireccionar():
   return render_template('log_in.html')

@app.route('/loginRedirect',methods = ['POST', 'GET'])
def loginRedirect():
   if request.method == 'POST':
      if request.form['username'] == 'admin' :
         return redirect(url_for('successRedirect'))
      else:
         abort(415)
   else:
      return redirect(url_for('redireccionar'))

@app.route('/successRedirect')
def successRedirect():
   return 'logged in successfully'

#Message Flashing
@app.route('/flashing')
def indexFlash():
   return render_template('indexFlash.html')

@app.route('/loginFlash', methods = ['GET', 'POST'])
def loginFlash():
   error = None
   
   if request.method == 'POST':
      if request.form['username'] != 'admin' or \
         request.form['password'] != 'admin':
         error = 'Invalid username or password. Please try again!'
      else:
         flash('You were successfully logged in')
         return redirect(url_for('indexFlash'))
			
   return render_template('loginFlash.html', error = error)

#WTF
@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactoForm()
   if form.validate_on_submit():
      return redirect(url_for("success2"))
   else:
      flash('All fields are required.')
      return render_template('contact.html', form = form)

@app.route('/success')
def success2():
    return render_template("success.html")

#sqlite
@app.route('/home')
def home():
   return render_template('base.html')

@app.route('/enternew')
def new_student():
   return render_template('estudiante.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("resultado.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall()
   return render_template("list.html",rows = rows)

#sijax

#datetime
def format_datetime(value, format="%d-%m-%Y"):
    if value is None:
        return ""
    return datetime.strptime(value,"%Y-%m-%d").strftime(format)

#configured Jinja2 environment with user defined
app.jinja_env.filters['date_format']=format_datetime

@app.route("/fecha")
def fecha():
    data={'cdate':'2022-01-17'}
    return render_template("fecha.html",row=data)

 
if __name__ == '__main__':
   app.run(port=5000, debug=True)