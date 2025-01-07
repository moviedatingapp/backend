from application.models import db,AuthUser
from main import create_app
import bcrypt
from datetime import datetime
app=create_app()


db.create_all()  # when app has app.app_context()
db.session.commit()