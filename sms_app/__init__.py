from sms_app.config import config_env_files
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
#from . import views


#app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
#app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()

def prepare_app(p_db=db):
    app = Flask(__name__)
    app.config.from_object(config_env_files["new"])
    p_db.init_app(app)
    # load views by importing them
    return app

#app.run()
app = prepare_app()
#migrate = Migrate(app, db)

from . import views



def save_and_commit(item):
    db.session.add(item)
    db.session.commit()
db.save = save_and_commit

