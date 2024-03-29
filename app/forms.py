from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, TextAreaField, TextField, SelectField, validators
from wtforms.validators import InputRequired, Email, DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class ProfileForm(FlaskForm):
    firstname = TextField('First Name', validators=[DataRequired()])
    lastname = TextField('Last Name', validators=[DataRequired()])
    location = TextField('Location', validators=[DataRequired()])
    email = TextField('Email', validators=[DataRequired(), Email()])
    biography = TextAreaField('Biography', validators=[DataRequired()])
    gender = SelectField(u'Gender', choices=[('',''), ('Male', 'Male'), ('Female', 'Female')], validators=[validators.DataRequired()])
    photo = FileField('Profile Picture', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])
    