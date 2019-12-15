from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_migrate import upgrade as upgrade_database
from sms_app import app, db, parsers, prepare_app
#from sms_app.scheduling import the_schedule
from apscheduler.schedulers.background import BackgroundScheduler
from sms_app.send_sms import outgoing_sms

from flask_apscheduler import APScheduler

prepare_app(environment='development')
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


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


@manager.command
def dbseed():
    with open('survey.json') as survey_file:
        db.save(parsers.survey_from_json(survey_file.read()))

#def run_schedule():        
#    while 1:
#        the_schedule.run_pending()
#        time.sleep(1)       
        
if __name__ == "__main__":
    #t = Thread(target=run_schedule)
    #t.start()  
    #scheduler = BackgroundScheduler()
    #scheduler.add_job(outgoing_sms, 'interval', minutes=1, args = ['+15172400923', 'Lets see if this works'])
    #scheduler.start()
    
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    
    app.apscheduler.add_job(outgoing_sms, 'interval', minutes=1, args = ['+15172400923', 'Lets see if this works'])

    manager.run()
