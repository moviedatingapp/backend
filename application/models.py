from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


### Authentication User Model ###
class AuthUser(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relationship to UserProfile (One-to-One)
    profile = db.relationship('UserProfile', backref='auth_user', uselist=False)


### User Profile Model ###
class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('auth_user.id'), nullable=False, unique=True)
    
    active = db.Column(db.Boolean, nullable=False, default=True)
    gender = db.Column(db.String(120))
    age = db.Column(db.Integer)
    height = db.Column(db.Integer)
    smoke = db.Column(db.Boolean)
    drink = db.Column(db.Boolean)
    location = db.Column(db.String(120))
    interested = db.Column(db.String(120))
    reported = db.Column(db.Integer, default=0)
    valid_user = db.Column(db.Boolean, default=True)

    # Relationships
    genres = db.relationship('Genre', secondary='user_genre', backref='users')
    matches = db.relationship('Match', foreign_keys='Match.user1_id', backref='user1_matches')
    preferences = db.relationship('UserMoviePreference', backref='user')
    chats = db.relationship('Chat', foreign_keys='Chat.sender_id', backref='sender')


### Genre Table ###
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre = db.Column(db.String(80), unique=True, nullable=False)


user_genres = db.Table(
    'user_genre',
    db.Column('user_id', db.Integer, db.ForeignKey('user_profile.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key=True)
)


### Match Table ###
class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)
    user2_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)
    matched_on = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(50), nullable=False, default='pending')  # pending, accepted, declined


### Movie Table ###
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    release_year = db.Column(db.Integer)
    rating = db.Column(db.Float)


### User Movie Preference ###
class UserMoviePreference(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    preference_level = db.Column(db.String(50), nullable=False, default='like')  # like, love, dislike

    movie = db.relationship('Movie', backref='user_preferences')


### Chat Table ###
class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    is_read = db.Column(db.Boolean, default=False)


### Report Table ###
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reporter_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)
    reported_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)
    reason = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    resolved = db.Column(db.Boolean, default=False)

    