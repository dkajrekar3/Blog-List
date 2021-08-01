
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'd948313194e3fb1627c6b428a800bc5b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db=SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from bloglist import routes