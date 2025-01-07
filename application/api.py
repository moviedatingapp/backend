from flask_restful import Resource
from flask import jsonify, request, current_app
from werkzeug.security import generate_password_hash
from application.models import AuthUser, UserProfile,Genre, Match, Movie, UserMoviePreference, Chat, Report
import bcrypt
from flask_jwt_extended import create_access_token, get_jwt,jwt_required, get_jwt_identity
from application.models import db
import jwt
import os, json
from application.config import LocalDev
from werkzeug.utils import secure_filename
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


class SignUp(Resource):
    def post(self):
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        username=data.get('username')
        password = data.get('password')

        if email=="" or username=="" or password=="":
            return jsonify({'message': 'Please fill all the fields'}), 400
        
        existing_user = AuthUser.query.filter(
        (AuthUser.email == email) | (AuthUser.username == username)
    ).first()
    
        if existing_user:
            return jsonify({'message': 'User with this email or username already exists'}), 400
        
        hashed_password = generate_password_hash(password)
        new_user = AuthUser(name=name, username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({'message': 'User signed up successfully'}), 201