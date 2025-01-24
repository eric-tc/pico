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
    #Questa pws non può essere randomica altrimenti gunicorn con il multithread ne crea una diversa
    # per ogni thread creando problemi di validazione csrf
    app.config['SECRET_KEY'] = "#ekqk3DEgqwer)=90mlw@"
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

    from .models import User
    
    print("CREATE DB")
    #Handled with migration command DO NOT USE
    # with app.app_context():
    #     db.create_all()
    
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
    
    #TODO da rivedere con HTTPS problemi con validazione csrf da gunicorn con worker multipli
    app.config['PREFERRED_URL_SCHEME'] = 'http'
    app.config['WTF_CSRF_ENABLED'] = True
    app.config['WTF_CSRF_SSL_STRICT'] = False

    return app

my_app= create_app()


@my_app.context_processor
def utility_processor():
    return dict(zip=zip)

# Questo comando serve per creare il db con i dati di default 
# viene chiamto con il comando flask insert-db
@my_app.cli.command("insert-db")
def insert_db():
    with my_app.app_context():    
        print("INSEIRMENTO DATI DI DEFAULT")
        NotificationStatus.insert_rows()
        PathologyType.insert_rows()
        PathologyStatus.insert_rows()
        Pathology.insert_rows()
        EmailStatus.insert_rows()
        ControlStatus.insert_rows()