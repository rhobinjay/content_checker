from content_checker import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    contentintegratedlabs = db.relationship('ContentIntegratedLab', backref='user', lazy=True)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instruction = db.Column(db.String(20), nullable=False)
    answer = db.Column(db.String(20), nullable=False)
    contentintegratedlabs = db.relationship('ContentIntegratedLab', backref='task', lazy=True)


class ContentIntegratedLab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    user_answer = db.Column(db.String(20), nullable=True)
    score = db.Column(db.Integer, nullable=False, default=0)
