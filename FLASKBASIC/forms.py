from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired, Email, Length

from flask_wtf import FlaskForm


# flask自体にformを作る機能がある。
# バックエンド（サーバー側プログラム）で作る利点は、ユーザー側に意図的に変えられない点。
# 
class UserRegistrationForm(FlaskForm):
    username= StringField("Username", validators=[InputRequired(), Length(min=6, max=20)])
    firstname= StringField("Firstname",validators=[InputRequired()])
    lastname= StringField("Lastname",validators=[InputRequired()])
    password= PasswordField("Password", validators=[InputRequired(), Length(min=6, max=12)])


class InformationForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired(), Length(min=6, max=20)])
    address = StringField("Adress", validators=[InputRequired()])
    status = SelectField("Status", choices=[("1","Active"),("0","Inactive")])


class StudentInformationForm(FlaskForm):
    student_name = StringField("Name", validators=[InputRequired(), Length(min=6, max=20)])
    address = StringField("Adress", validators=[InputRequired()])
    status = SelectField("Status", choices=[("1","Active"),("0","Inactive")])
    school_year = SelectField("Schoolyear", choices=[("1","1st Grade"),("2","2nd Grade"),("3","3rd Grade"),("4","4th Grade")])

class TeacherInformataionForm(FlaskForm):
    teacher_name = StringField("Name", validators=[InputRequired(), Length(min=6, max=20)])
    address = StringField("Address", validators=[InputRequired()])
    status = SelectField("Status", choices=[("1","Active"),("0","Inactive")])