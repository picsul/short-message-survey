from sms_app.config import config_env_files
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)

def prepare_app(environment='development', p_db=db):
    #app.config.from_object(config_env_files[environment])
    p_db.init_app(app)
    # load views by importing them
    from . import views
    return app


def save_and_commit(item):
    db.session.add(item)
    db.session.commit()
db.save = save_and_commit

