from flask_restful import Resource
from flask import jsonify, request, current_app
from application.models import User, Genre, Match, Movie, UserMoviePreference, Chat, Report
import bcrypt
from flask_jwt_extended import create_access_token, get_jwt,jwt_required, get_jwt_identity
from application.models import db,User
import jwt
import os,json
from application.config import LocalDev
from werkzeug.utils import secure_filename
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from datetime import datetime, timedelta