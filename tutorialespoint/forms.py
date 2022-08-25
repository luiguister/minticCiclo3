from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, SubmitField, SelectField, RadioField, StringField
from wtforms import validators, ValidationError
from wtforms.validators import DataRequired, Length

class ContactoForm(FlaskForm):
   
   name=StringField("Name Of Student", validators=[DataRequired(message="Please enter your name."), Length(min=8, max=10, message="El usuario debe dener maximo 8 caracteres")])
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address")
   
   email = StringField("Email", validators=[DataRequired(message="Please enter your email.")])
   
   Age = IntegerField("age")
   language = SelectField('Languages', choices = [('cpp', 'C++'), ('py', 'Python')])
   submit = SubmitField("Send")

