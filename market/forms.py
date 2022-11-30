from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import Length,Email, EqualTo, DataRequired

class RegisterForm(FlaskForm):
    # username
    username = StringField(label='User Name:', validators=[Length(min=2,max=30,message="lol no name")])
    # email
    email_address = StringField(label='Email Address:', validators=[Email("yo add a message")])
    # pass1
    password1 = PasswordField(label='Password:', validators=[Length(min=6)])
    # pass2
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1', "djwad")])
    # submit
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    # username
    username = StringField(label='User Name:', validators=[DataRequired()])
    # pass
    password = PasswordField(label='Password:', validators=[DataRequired()])
    # submit
    submit = SubmitField(label='Login')