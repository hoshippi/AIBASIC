
from .app import app
from flask import Flask, render_template, redirect, request

#URL mapping
@app.route("/",methods=["GET","POST"])
def index():
    user = "Takahiro Hoshino"
    informations = [
        {"id":1, "name":"Jan", "address": "Cebu", "status":"Active"},
        {"id":2, "name":"Takahiro Hoshino", "address": "Kanagawa", "status":"Inactive"},
        {"id":3, "name":"Hiroki Azeyanagi", "address": "Chiba", "status":"Active"},
        {"id":4, "name":"Ayaka Ishikawa", "address": "Tokyo", "status":"Active"}
    ]
    if request.method == "POST":
        return f"id : {len(informations)+1} name : {'name'} , address : {'address'} , status : {'status'}"
    return render_template("dashboard.html", user=user, informations=informations)

@app.route("/student")
def student():
    students = [
        {"id":1, "name":"Jan", "address": "Cebu", "status":"Active"},
        {"id":2, "name":"Takahiro Hoshino", "address": "Kanagawa", "status":"Inactive"},
        {"id":3, "name":"Hiroki Azeyanagi", "address": "Chiba", "status":"Active"},
        {"id":4, "name":"Ayaka Ishikawa", "address": "Tokyo", "status":"Active"}
    ]
    return render_template("student/student.html", students=students)

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
    return render_template("teacher/teacher.html", teachers=teachers)