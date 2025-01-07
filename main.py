from flask import Flask, jsonify
from application.models import db, AuthUser, UserProfile, Genre, Match, Movie, UserMoviePreference, Chat, Report
from application.config import LocalDev
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from application.api import SignUp

app = None
api = None

def create_app():
    
    app=Flask(__name__)

    app.config.from_object(LocalDev)

    
    #models.py and db.sqlite3 to be coionected
    # app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'

    #Models.py and main.py connrcted
    db.init_app(app)   # to connect db object to app db object === app
    app.app_context().push()  # to modify database 
   # security ko app se connect

    api=Api(app)


    

    return app, api


app, api=create_app()



CORS(app)
jwt=JWTManager(app)

api.add_resource(SignUp, '/signup')

if __name__=='__main__':
    print("hello working")
    print("tatti")
    print("gbfgbf")
    app.run(debug=True,port=5000)