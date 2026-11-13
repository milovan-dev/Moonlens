from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

from wtforms import PasswordField

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Lozinka', validators=[DataRequired()])
    submit = SubmitField('Prijavi se')

class PhotoForm(FlaskForm):
    title = StringField('Naslov fotografije', validators=[DataRequired()])
    description = TextAreaField('Opis')
    category = SelectField('Kategorija', choices=[
        ('krstenje', 'Krštenje'),
        ('rodjendan', 'Rođendani'),
        ('prom', 'Prom'),
        ('women', 'Women'),
        ('man', 'Man'),
        ('model', 'Model'),
        ('arhitektura','Arhitektura'),
        ('priroda','Priroda')
    ], validators=[DataRequired()])
    photo = FileField('Izaberi sliku', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png', 'webp'], 'Dozvoljene su samo slike!')
    ])
    submit = SubmitField('Objavi fotografiju')