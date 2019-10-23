# in this file, you are going to make the structure of the database that you want to make. migrate it from here's configuration

from datetime import datetime
from FLASKBASIC.database import db

#db.Model はdbはSQLAlchemyクラスのinstanceであるため、そのModelメソッドを使っているという意味。
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    #Pythonコード内では、文字型をVARCHARではなくString
    username = db.Column(db.String(20),nullable=False)
    firstname = db.Column(db.String(40),nullable=False)
    lastname = db.Column(db.String(40),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)