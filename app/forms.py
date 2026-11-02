from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

from wtforms import PasswordField

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Lozinka', validators=[DataRequired()])
    submit = SubmitField('Prijavi se')

class PhotoForm(FlaskForm):
    title = StringField('Naslov slike', validators=[DataRequired()])
    description = TextAreaField('Opis')
    category = StringField('Kategorija', validators=[DataRequired()], default='General')
    image = FileField('Slika', validators=[
        DataRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Dozvoljene su samo slike (jpg, jpeg, png)!')
    ])
    submit = SubmitField('Sačuvaj sliku')