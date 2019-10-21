# all the code for the database are going to be here

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    # 一種のインポート。すでに定義されているデータ構造をそのまま映してくる的なやつ
    Migrate(app,db)

    return db
    