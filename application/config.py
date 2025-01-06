import os

class LocalDev():
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite3'
    JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY')
    UPLOAD_FOLDER='uploads'