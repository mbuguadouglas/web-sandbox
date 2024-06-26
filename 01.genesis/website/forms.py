from flask_wtf import FlaskForm
from wtforms import Form,StringField,EmailField,PasswordField,BooleanField,SubmitField,FileField,TextAreaField
from wtforms.validators import  InputRequired,Length,EqualTo,DataRequired
from flask_wtf.file import FileRequired

class SignUpForm(FlaskForm):
    """
    class inherits from FlaskForms to define attributes of the Signup form
    # discovered wtforms->Form does not capture data at all.
    # always use flask_wtf->FlaskForm instead
    """
    email = EmailField('Email Address', validators=[InputRequired(),
        Length(10,40)])
    username = StringField('Username', validators=[InputRequired(),
        Length(3,15)])
    password = PasswordField('Password', validators=[InputRequired(),
        Length(5,20)])
    confirm_password = PasswordField('Confirm Password',validators=[
        InputRequired(),EqualTo('password',message=
            ('Oops! It looks like your passwords do not match. Try again?'))])
    profile_pic = FileField('Choose Avatar', validators=[FileRequired()])
    remember_me = BooleanField('Remember Me?')
    signup = SubmitField('Submit')


class LoginForm(FlaskForm):
    """
    class inherits from FlaskForm to define attributes of Login form class
    """
    email = EmailField('Email Address', validators=[InputRequired(),Length(10,40)])
    password = PasswordField('Password', validators=[InputRequired(),Length(7,20)])
    remember_me = BooleanField('Remember Me?')
    login =  SubmitField('Login')

class NoteForm(FlaskForm):
    """
    class inherits from FlskForm to defines attributes of Notes adding forms
    """
    title = StringField('Select a title for your note', validators=[Length(min=2,max=100)])
    content = TextAreaField('Give a description of the Note', validators=[Length(min=5,max=1000)])
    submit = SubmitField('Submit')


class UpdateForm(FlaskForm):
    """
    class inherits from FlskForm to defines attributes of Notes updating forms
    """
    new_title = StringField('Update the title field',validators=[Length(max=100)])
    new_content = StringField('Update the content field',validators=[Length(max=1000)])
    update = SubmitField('Submit')
