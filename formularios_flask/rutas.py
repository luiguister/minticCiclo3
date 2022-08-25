from urllib import request
from flask import Flask, redirect, render_template, url_for, flash
from formularios import FormInicio
from settings.config import configuracion

app=Flask(__name__)

app.config.from_object(configuracion)

@app.route('/')
@app.route('/index')
def index():
    lista=["lunes", "martes", "Miercoles"]
    return render_template('index.html', lista=lista, titulo="Inicio de la app")

@app.route('/login', methods=['GET', 'POST'])
def login():
    formulario=FormInicio()
    if formulario.validate_on_submit():
        flash("Se solicita inicio de sesion por el usuario {}, recordar={}"
        .format(formulario.nombre.data, formulario.recordar.data))
        return redirect(url_for("logueado"))
    return render_template('inicio.html',form=formulario, titulo="Inicio del login")

@app.route('/logueado')
def logueado():
    return render_template("logueado.html")

app.run(port=5000, debug=True)