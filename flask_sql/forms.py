from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Producto(FlaskForm):
    codigo=StringField('id', validators=[DataRequired()])
    nombre=StringField('Nombre', validators=[DataRequired()])
    precio=StringField('Precio', validators=[DataRequired()])
    cantidad=StringField('Cantidad', validators=[DataRequired()])
    enviar=SubmitField('Agregar Producto')