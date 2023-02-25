from sms_app.config import config_env_files
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_migrate import upgrade as upgrade_database
import os
import tomllib
import click
from flask import Blueprint

db = SQLAlchemy()

def prepare_app(p_db=db):
    app = Flask(__name__)
    app.config.from_object(config_env_files["new"])
    p_db.init_app(app)
    return app

app = prepare_app()

#from manage import db_bp

db_bp = Blueprint('dbstuff', __name__)

app.register_blueprint(db_bp)

with open("config.toml", "rb") as f:
    confi = tomllib.load(f)

migrate = Migrate(app, db)

from . import views

def save_and_commit(item):
    db.session.add(item)
    db.session.commit()
db.save = save_and_commit
