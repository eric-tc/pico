# init.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from .config import BaseConfig
import os
from enum import Enum

from flask_wtf import FlaskForm, CSRFProtect
from flask_cors import CORS
from flask_caching import Cache

from flask_migrate import Migrate

#ROLE 1 = DOCTOR
#ROLE 2 = PATIENT

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
boostrap= None
csrf = None
chace = None

#Tutte le volte che aggiungo una nuova tabella devo importarla qui
# per essere tracciata dalle migrazioni
from .models import User,\
DoctorPatient,\
DoctorCurrentPathology,\
Notification,\
PathologyData,\
PathologyType,\
PathologyStatus,\
Pathology,\
EmailStatus,\
ControlStatus,\
NotificationStatus

def create_app():
    global csrf
    global cache

    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config["CACHE_TYPE"] = "SimpleCache"
    app.config["CACHE_DEFAULT_TIMEOUT"] = 60
    
    csrf = CSRFProtect(app)
    CORS(app)
    
    @app.template_filter('format_date')
    def format_date(value, format='%Y-%m-%d'):
        return value.strftime(format)

    app.jinja_env.filters['format_date'] = format_date

    db.init_app(app)
    #Migrazioni
    migrate = Migrate(app, db)
    
    #Init Cache
    cache = Cache(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # from .models import User
    
    # print("CREATE DB")
    # with app.app_context():
    #     db.create_all()
    
    # @login_manager.user_loader
    # def load_user(user_id):
    #     # since the user_id is just the primary key of our user table, use it in the query for the user
    #     return User.query.get(int(user_id))

    # # blueprint for auth routes in our app
    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint)

    # # blueprint for non-auth parts of app
    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    # from .doctor import doctor as doctor_blueprint
    # app.register_blueprint(doctor_blueprint)

    # from .patient import patient as patient_blueprint
    # app.register_blueprint(patient_blueprint)
    
    return app

my_app= create_app()