from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from content_checker.config import Testing

db = SQLAlchemy()


# class TestingSetup:

#     config = config.Testing

#     def setup(self, app):
#         with app.app_context():
#             from content_checker.models import User, Task, ContentIntegratedLab

#             db.create_all()

#             for user in ["ben", "john", "peter"]:
#                 db.session.add(User(username=user))

#             for instruction, answer in zip(
#                 ["Who?", "What?", "When?"], ["answer who", "answer what", "answer when"]
#             ):
#                 db.session.add(Task(instruction=instruction, answer=answer))

#             db.session.commit()

#             for user in User.query.all():
#                 for task in Task.query.all():
#                     db.session.add(
#                         ContentIntegratedLab(
#                             user=user, task=task, user_answer=None, score=0
#                         )
#                     )

#             db.session.commit()


def create_app(config=Testing):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    # TestingSetup().setup(app)

    from content_checker.main.routes import main
    from content_checker.content.routes import content

    app.register_blueprint(main)
    app.register_blueprint(content)

    return app

