from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)


app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

from content_checker import routes

##################################################
# Setup database
##################################################
from content_checker.models import User, Task, ContentIntegratedLab
db.create_all()

questions_answers = [
    ('Create an FDB with the following schema', 'fdb schema'),
    ('', ''),
    ('', ''),
    ('', ''),
    ('', ''),
    ('', ''),

]

for user in ['ben', 'john', 'peter']:
    db.session.add(User(username=user))

for instruction, answer in zip(['Who?', 'What?', 'When?'], ['answer who', 'answer what', 'answer when']):
    db.session.add(Task(instruction=instruction,answer=answer))

db.session.commit()


for user in User.query.all():
    for task in Task.query.all():
        db.session.add(ContentIntegratedLab(user=user, task=task, user_answer=None, score=0))

db.session.commit()
