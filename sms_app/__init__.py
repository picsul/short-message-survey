from sms_app.config import config_env_files
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

import os


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.environ.get('HOME') + '/short-message-survey/survey.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.environ.get('HOME') + '/survey.db'
app.config['SECRET_KEY'] = '\x91V}\x10\x8d\xa3lC\xac\x8c.\xdb\xa6\xb1\xa6\xe8\\\xf4\x19\xc2\x05\xd5\xbc'
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

