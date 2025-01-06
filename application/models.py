from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    active=db.Column(db.Boolean, nullable=False)
    gender=db.Column(db.String(120), nullable=False)
    age=db.Column(db.Integer, nullable=False)
    height=db.Column(db.Integer, nullable=False)
    smoke=db.Column(db.Boolean, nullable=False)
    drink=db.Column(db.Boolean, nullable=False)
    location=db.Column(db.String(120), nullable=False)
    interested=db.Column(db.String(120), nullable=False)
    reported=db.Column(db.Integer, nullable=False)
    valid_user=db.Column(db.Boolean, nullable=False)

    #relationships
    genres=db.relationship('Genre', secondary='user_genre', backref='users')
    matches=db.relationship('Match', foreign_keys='Match.user1_id', backref='user1_matches')
    preferences=db.relationship('UserMoviePreference', backref='user')
    chats=db.relationship('Chat', foreign_keys='Chat.sender_id', backref='sender')

    
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre = db.Column(db.String(80), unique=True, nullable=False)


user_genres=db.Table('user_genre',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key=True)
)


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user2_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    matched_on = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(50), nullable=False, default='pending')  # pending, accepted, declined



class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    release_year = db.Column(db.Integer)
    rating = db.Column(db.Float)



class UserMoviePreference(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    preference_level = db.Column(db.String(50), nullable=False, default='like')  # like, love, dislike

    movie = db.relationship('Movie', backref='user_preferences')



class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    is_read = db.Column(db.Boolean, default=False)



class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reporter_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reported_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reason = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    resolved = db.Column(db.Boolean, default=False)



##Relationships Overview

#  User ⇄ Genre → Many-to-Many (user_genres)
#  User ⇄ Match → One-to-Many (matches)
#  User ⇄ Movie → Many-to-Many (UserMoviePreference)
#  User ⇄ Chat → One-to-Many (chats)
#  User ⇄ Report → One-to-Many (Report)

