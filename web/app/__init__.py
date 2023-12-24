# init.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from .config import BaseConfig
import os
from enum import Enum

from flask_wtf import FlaskForm, CSRFProtect
#ROLE 1 = DOCTOR
#ROLE 2 = PATIENT

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
boostrap= None
csrf = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    app.config['SECRET_KEY'] = os.urandom(24)
    
    
    csrf = CSRFProtect(app)

    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    
    print("CREATE DB")
    with app.app_context():
        db.create_all()
    
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .doctor import doctor as doctor_blueprint
    app.register_blueprint(doctor_blueprint)

    from .patient import patient as patient_blueprint
    app.register_blueprint(patient_blueprint)
    
    return app

my_app= create_app()