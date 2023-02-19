import click
from flask_migrate import Migrate, MigrateCommand
from flask_migrate import upgrade as upgrade_database
from sms_app import db, parsers, prepare_app
#from sms_app import app, db, parsers, prepare_app

#prepare_app(environment='development')
app = prepare_app()

from sms_app import views

#with app.app_context()
migrate = Migrate(app, db)

#migrate = Migrate()
#migrate.init_app(app, db)

#@manager.command
#def test():
#    """Run the unit tests."""
#    import sys
#    import unittest
#    prepare_app(environment='test')
#    upgrade_database()
#    tests = unittest.TestLoader().discover('.', pattern="*_tests.py")
#    test_result = unittest.TextTestRunner(verbosity=2).run(tests)

#    if not test_result.wasSuccessful():
#        sys.exit(1)
        
@app.cli.command("dbseed")
def dbseed():
    with open('survey.json') as survey_file:
        db.save(parsers.survey_from_json(survey_file.read()))
         
if __name__ == "__main__":
    cli()
    app.run()
