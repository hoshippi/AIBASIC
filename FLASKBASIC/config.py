#all the settings to connect to the database
#database configuration

#↓OSによってロケーションを指定できるように（ディレクトリの指定の仕方がOSによって違う）
import os

from os.path import join,dirname
#dotenvというライブラリを使って、".env"をロードする
from dotenv import load_dotenv

#join()を使って、この"config.py"と.envを指定し、つなげている
dotenv_path = join(dirname(__file__),".env")


class DevelopmentConfig:
    #DEBUG = TRUE だと、エラーが起こった時にエラーを表示してくれる。プロダクションステイとだとこれをオフにして、ユーザーにはエラーを表示しない
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(**{
        "user":os.environ.get("MYSQL_USER") or "test",
        "password":os.environ.get("MYSQL_PASSWORD") or "test",
        "host":os.environ.get("DB_HOST") or "docker_mysql",
        "database":os.environ.get("MYSQL_DATABASE") or "ems_db"
    })

    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_ECHO = False

    SECRET_KEY = os.urandom(24)

#instance or object ↓ 両方の呼び方がある
Config = DevelopmentConfig