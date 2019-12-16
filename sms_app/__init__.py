from sms_app.config import config_env_files
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# this path works locally
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.environ.get('HOME') + '/short-message-survey/survey.db'
# this path works on Heroku, but we can't use this
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.environ.get('HOME') + '/survey.db'
# this path should work for the heroku postgres database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://eylbtbwiiflsbs:37a255cd11e961e584be5952b2b272ffed0fd51ba0c2e29fc34743f439e82a24@ec2-174-129-255-69.compute-1.amazonaws.com:5432/d88o9to60oiug9'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

# still don't know how this works so don't know if I need it
#app.config['SECRET_KEY'] = '\x91V}\x10\x8d\xa3lC\xac\x8c.\xdb\xa6\xb1\xa6\xe8\\\xf4\x19\xc2\x05\xd5\xbc'
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

