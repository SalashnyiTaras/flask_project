from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, equal_to, Email, DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label='Username: ', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email: ', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Enter your password: ', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='Confirm your password: ', validators=[equal_to(password1), DataRequired()])
    submit = SubmitField(label='Submit')

