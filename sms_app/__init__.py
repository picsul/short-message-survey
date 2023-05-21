from sms_app.config import config_env_files
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_migrate import upgrade as upgrade_database
import os
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
    return app

app = prepare_app()

# register blueprint with views
from .views import bp
app.register_blueprint(bp)
from .question_view import question_bp
app.register_blueprint(question_bp)
from .survey_view import survey_bp
app.register_blueprint(survey_bp)
from .answer_view import answer_bp
app.register_blueprint(answer_bp)
from .controller_view import controller_bp
app.register_blueprint(controller_bp)

migrate = Migrate(app, db)

import sms_app.parsers

@app.cli.command("dbseed")
def dbseed():
    with open('survey.json') as survey_file:
        db.save(parsers.survey_from_json(survey_file.read()))

if __name__ == "__main__":
    cli()
