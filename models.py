from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # Relationships
    skills = db.relationship('Skill', backref='user', lazy=True, cascade="all, delete")
    matches_initiated = db.relationship('Match', foreign_keys='Match.user_id', backref='initiator', lazy=True, cascade="all, delete")
    matches_received = db.relationship('Match', foreign_keys='Match.matched_with', backref='receiver', lazy=True, cascade="all, delete")
    sessions = db.relationship('SessionSchedule', backref='user', lazy=True, cascade="all, delete")

    def __repr__(self):
        return f"<User {self.id}, Username: {self.username}, Email: {self.email}>"

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Skill {self.name}, Category: {self.category}, User ID: {self.user_id}>"
    
class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(100), nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    matched_with = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  

    user = db.relationship('User', foreign_keys=[user_id], backref='initiated_matches', cascade="all, delete")
    matched_user = db.relationship('User', foreign_keys=[matched_with], backref='received_matches', cascade="all, delete")

    def __repr__(self):
        return f"<Match User {self.user_id} with {self.matched_with} for {self.skill_name}>"

class SessionSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Session {self.session_name} on {self.date}, User ID: {self.user_id}>"