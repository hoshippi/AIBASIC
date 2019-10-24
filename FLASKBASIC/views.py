
from .app import app
from .database import db
from flask import Flask, render_template, redirect, request, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User

# ここでformsすべてをインポートしないのは、formsに今後何か追加でclassを作ったときなどに、全部インポートしてしまうのを防ぐため。
from .forms import UserRegistrationForm, InformationForm, StudentInformationForm, TeacherInformataionForm


@app.route("/",methods=["GET","POST"])
def index():
    user = "Takahiro Hoshino"
    form = InformationForm()
    informations = [
        {"id":1, "name":"Jan", "address": "Cebu", "status":"Active"},
        {"id":2, "name":"Takahiro Hoshino", "address": "Kanagawa", "status":"Inactive"},
        {"id":3, "name":"Hiroki Azeyanagi", "address": "Chiba", "status":"Active"},
        {"id":4, "name":"Ayaka Ishikawa", "address": "Tokyo", "status":"Active"}
    ]
    if request.method == "POST":
        return f"id : {len(informations)+1} name : {'name'} , address : {'address'} , status : {'status'}"
    return render_template("dashboard.html", user=user, informations=informations, form=form)

@app.route("/student")
def student():
    students = [
        {"id":1, "name":"Jan", "address": "Cebu", "status":"Active"},
        {"id":2, "name":"Takahiro Hoshino", "address": "Kanagawa", "status":"Inactive"},
        {"id":3, "name":"Hiroki Azeyanagi", "address": "Chiba", "status":"Active"},
        {"id":4, "name":"Ayaka Ishikawa", "address": "Tokyo", "status":"Active"}
    ]
    form = StudentInformationForm()
    return render_template("student/student.html", students=students, form=form)

@app.route("/schedule")
def schedule():
    schedules = [
        {"month":10, "date":15, "year":2019, "address": "Cebu", "status":"scheduled"},
        {"month":11, "date":12, "year":2019, "address": "Tokyo", "status":"scheduled"},
        {"month":12, "date":27, "year":2019, "address": "Kyoto", "status":"canceled"},
        {"month":1, "date":15, "year":2020, "address": "London", "status":"scheduled"}
    ]
    return render_template("schedule/schedule.html", schedules = schedules )

@app.route("/teacher")
def teacher():
    teachers = [
        {"id":1, "name":"Jan", "address": "Cebu", "status":"Active"},
        {"id":2, "name":"Takahiro Hoshino", "address": "Kanagawa", "status":"Inactive"},
        {"id":3, "name":"Hiroki Azeyanagi", "address": "Chiba", "status":"Active"},
        {"id":4, "name":"Ayaka Ishikawa", "address": "Tokyo", "status":"Active"}
    ]
    form = TeacherInformataionForm()
    return render_template("teacher/teacher.html", teachers=teachers, form=form)

@app.route("/users")
def list_users():
    # get all the users from the database ordered by id
    users = User.query.order_by(User.id.desc()).all()
    return render_template("user/index.html", users=users)

@app.route("/user/create", methods=["GET", "POST"])
def add_user():
    form = UserRegistrationForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method="sha256")
        new_user = User(username=form.username.data, firstname=form.firstname.data, lastname=form.lastname.data, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()
        flash("New User added successfully.")

        return redirect(url_for("list_users"))

    return render_template("user/create.html", form=form)

