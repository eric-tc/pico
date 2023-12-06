# models.py

from flask_login import UserMixin
from . import db
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(120))
    role = db.Column(db.Integer)

def create_phatology_data():

    existing_data= Phatology.query.first()
    if not existing_data:
        #Create all Pathology
        rizoartrosi= Phatology(name="Rizoartrosi")




class Phatology(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120))

"""
This class will contains all data releated to
doctor patients and all value from rizoartrosi based on
different timestamp

"""
class Rizoartrosi(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    doctor = db.Column(db.Integer)
    patient = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    #Parametri
    nprs_vas=db.Column(db.Integer)
    prom_arom_mcpj= db.Column(db.Integer)
    prom_arom_Ipj=db.Column(db.Integer)
    abduction=db.Column(db.Integer)
    anterposition=db.Column(db.Integer)
    kapandji=db.Column(db.Integer)
    pinch=db.Column(db.Integer)
    grip=db.Column(db.Integer)
    dash=db.Column(db.Integer)
    prwhe=db.Column(db.Integer)
    Eaton_littler=db.Column(db.Integer)
    scar_status= db.Column(db.String(100))
    scar_type = db.Column(db.String(100))
    

    

