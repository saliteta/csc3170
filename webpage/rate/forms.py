from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from rate.models import User
#to link the backend databse to the front end design


class Register_form(FlaskForm):
    #want to catch the error when it violate the database constrain early in the 
    # falsk will automatically generate the validate syntax for you if your function start with validate_
    # flask will automatically check the field after the underscore
    # following the convention is important
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username = username_to_check.data).first()
        if user: # if user is not none
            raise ValidationError('User name is already exist! Please Try a diffrent user name')
    
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address = email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email already exist, please change to another one')
    


    username = StringField(label = 'User Name:', validators=[Length(min = 2, max = 30), DataRequired()])#label will give the secondary title of the field
    #using the length to limit the min and max
    email_address = StringField(label = 'Email Adress:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label = 'Password:', validators=[Length(min = 6), DataRequired()])
    password2 = PasswordField(label = 'Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label = 'Create Account')


class Login_form(FlaskForm):

    username = StringField(label = 'User Name:', validators=[Length(min = 2, max = 30), DataRequired()])#label will give the secondary title of the field
    password = PasswordField(label = 'Password:', validators=[Length(min = 6), DataRequired()])
    submit = SubmitField(label = 'Login')

class Rate_form(FlaskForm):
    #can be changed as rated content
    Difficulty = StringField(label = 'Difficult from low to high ,5 as the highest', validators=[Length(min = 1, max = 1), DataRequired()])#label will give the secondary title of the field
    Quality = StringField(label = 'Teaching quality from low to high, 5 as the highest', validators=[Length(min = 1, max = 1), DataRequired()])
    submit = SubmitField(label = 'Submmit Rate!')

class Rerate_form(FlaskForm):
    #can be changed as rated content
    
    submit = SubmitField(label = 'Submmit Rerate form!')

