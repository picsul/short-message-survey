from sms_app import app, db

class Survey(db.Model):
    __tablename__ = 'surveys'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    questions = db.relationship('Question', backref='survey', lazy='dynamic')

    def __init__(self, title):
        self.title = title

    @property
    def has_questions(self):
        return self.questions.count() > 0


class Question(db.Model):
    __tablename__ = 'questions'

    TEXT = 'text'
    NUMERIC = 'numeric'
    BOOLEAN = 'boolean'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    kind = db.Column(db.Enum(TEXT, NUMERIC, BOOLEAN,
                             name='question_kind'))
    test = db.Column(db.String)
    yes = db.Column(db.Integer)
    no = db.Column(db.integer)
    survey_id = db.Column(db.Integer, db.ForeignKey('surveys.id'))
    answers = db.relationship('Answer', backref='question', lazy='dynamic')

    def __init__(self, content, test, yes, no, kind=TEXT):
        self.content = content
        self.test = test
        self.yes = yes
        self.no = no
        self.kind = kind


    def next(self):
        return self.survey.questions\
                    .filter(Question.id > self.id)\
                    .order_by('id').first()

class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    session_id = db.Column(db.String, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    survey_id = db.Column(db.String, db.ForeignKey('instances.sid'))

    @classmethod
    def update_content(cls, session_id, question_id, content):
        existing_answer = cls.query.filter(Answer.session_id == session_id and
                                           Answer.question_id == question_id).first()
        existing_answer.content = content
        db.session.add(existing_answer)
        db.session.commit()

    def __init__(self, content, question, session_id, instance):
        self.content = content
        self.question = question
        self.session_id = session_id
        self.instance = instance
        
class Number(db.Model):
    __tablename__ = 'numbers'
    
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    code = db.Column(db.String, nullable=False, server_default = 'NA')
    week = db.Column(db.String, nullable=False, server_default = 'NA')

    def __init__(self, number, name, code, week):
        self.number = number
        self.name = name
        self.code = code
        self.week = week
        
class Instance(db.Model):
    __tablename__ = 'instances'
    
    sid = db.Column(db.String, primary_key=True)
    assign = db.Column(db.String, nullable = False)
    
    answers = db.relationship('Answer', backref='instance', lazy='dynamic')
    
    def __init__(self, sid, assign):
        self.sid = sid
        self.assign = assign

