from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class FormInicio(FlaskForm):
    nombre=StringField("usuario", validators=[DataRequired(message="Completa el campo nombre"), 
        Length(min=8, max=10, message="El usuario debe dener maximo 8 caracteres")])
    contraseña=PasswordField("contraseña", validators=[DataRequired(message="Complete la contraseña")])
    recordar=BooleanField("recordar usuario")
    enviar=SubmitField("iniciar sesion")