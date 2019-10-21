#all the connection of database 
#database configuration


import os

from os.path import join,dirname
#dotenvというライブラリを使って、".env"をロードする
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__),".env")

class DebelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}/{database}?character=utf8".format(**{
        "user":os.environ.get("MYSQL_USER") or "root",
        "password":os.environ.get("MYSQL_PASSWORD") or "",
        "host":os.environ.get("DB_HOST") or "localhost",
        "database":os.environ.get("MYSQL_DATABASE") or "ems_db"
    })

    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_ECHO = False


Config = DebelopmentConfig