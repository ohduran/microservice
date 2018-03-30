from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(db.Model):
    """User table."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    tasks = db.relationship('Task', backref='author', lazy='dynamic')

    def __repr__(self):
        """print(User) method."""
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        """Generate a password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verify a password."""
        return check_password_hash(self.password_hash, password)


class Task(db.Model):
    """Task table."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        """print(User) method."""
        return '<Post {} - {}>'.format(self.title, self.description)
