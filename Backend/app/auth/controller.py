from flask import Blueprint, request, url_for, render_template, flash, session, redirect, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_required, login_user, LoginManager
from models import Users
from app import db, app
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

auth = Blueprint('auth', __name__, url_prefix='/auth')
jwt = JWTManager(app)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json()
        username = data['username']
        full_name = data['fullname']
        email = data['email']
        password = generate_password_hash(data['password'])
        check_email = Users.query.filter_by(email=email).first()

        check_username = Users.query.filter_by(username=username).first()

        if check_username is not None:
            return 'Username Already Used'

        elif check_email is not None:
            return 'Email Already Used'

        else:
            user = Users(full_name=full_name, username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            return jsonify({
                "token" : create_access_token(identity=user.username)
            })


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        email = data['email']
        password = data['password']
        
        check_email = Users.query.filter_by(email=email).first()
        if check_email is None:
            return 'Incorrect Details'
        else:
            verify_password = check_password_hash(check_email.password, password)
            if verify_password is False:
                return 'Incorrect Details'
            else:
                user = check_email
                return jsonify({
                    "token" : create_access_token(identity=user.username)
                })

