#from flask_script import Manager
import click
from flask_migrate import Migrate, MigrateCommand
from flask_migrate import upgrade as upgrade_database
from sms_app import db, parsers, prepare_app
#from sms_app import app, db, parsers, prepare_app


#prepare_app(environment='development')
app = prepare_app()

from sms_app import views

migrate = Migrate(app, db)

#manager = Manager(app)
#manager.add_command('db', MigrateCommand)

#app.run()



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

#def dbseed():
#    with open('survey.json') as survey_file:
#        db.save(parsers.survey_from_json(survey_file.read()))
           
#surveys = [open('survey.json'), open('survey2.json'), open('survey3.json'), open('survey4.json')]

#@manager.command     
#def dbseed():
#    for survey in surveys:
#        with survey as survey_file:
#            db.save(parsers.survey_from_json(survey_file.read()))  
                      
#@manager.command
#def dbseed():
#    with open('survey.json') as survey_file:
#        db.save(parsers.survey_from_json(survey_file.read()))
        
#cli.add_command()
@app.cli.command
def dbseed():
    with open('survey.json') as survey_file:
        db.save(parsers.survey_from_json(survey_file.read()))
           
#if __name__ == "__main__":
#    manager.run()

if __name__ == "__main__":
    cli()
    app.run()

