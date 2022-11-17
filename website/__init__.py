from flask import Flask
from flask_mysqldb import MySQL, MySQLdb

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'airforce14'

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = '1874'
    app.config['MYSQL_DB'] = 'test1'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    mysql.init_app(app) 

    from .auth import auth
    from .views import views

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
