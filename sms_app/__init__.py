from sms_app.config import config_env_files
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_migrate import upgrade as upgrade_database
import os
import tomllib
import click

db = SQLAlchemy()

def save_and_commit(item):
    db.session.add(item)
    db.session.commit()
    
db.save = save_and_commit

def prepare_app(p_db=db):
    app = Flask(__name__)
    app.config.from_object(config_env_files["new"])
    p_db.init_app(app)
    from . import views
    app.register_blueprint(views.bp)
    return app

app = prepare_app()

with open("config.toml", "rb") as f:
   confi = tomllib.load(f)

#from . import views
#from . import question_view
#from . import answer_view
#from . import survey_view

migrate = Migrate(app, db)

#from . import views
import sms_app.parsers

@app.cli.command("dbseed")
def dbseed():
    with open('survey.json') as survey_file:
        db.save(parsers.survey_from_json(survey_file.read()))

if __name__ == "__main__":
    cli()
