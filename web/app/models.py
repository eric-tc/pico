# models.py

from flask_login import UserMixin
from . import db
from datetime import datetime
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime

print("READ MODEL")
class User(UserMixin, db.Model):

    
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(300))
    name = db.Column(db.String(120))
    role = db.Column(db.Integer)
    #new_instance = YourModel(doctor_ids=[1, 2, 3, 4, 5])
    doctor_ids = db.Column(ARRAY(db.Integer))

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


"""
Classe per tenere traccia relazione paziente dottore
Un dottore può avere più pazienti in cura.

Uno stesso paziente può avere più dottori nello stesso momento?

"""
class DoctorPatient(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    id_doctor = db.Column(db.Integer)
    id_patient = db.Column(db.Integer)

    # Adding a unique constraint on column1 and column2
    __table_args__ = (
        UniqueConstraint('id_doctor', 'id_patient'),
    )
    

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_doctor = db.Column(db.Integer)
    doctor_name= db.Column(db.String(50))
    id_patient = db.Column(db.Integer)
    status = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)



class NotificationStatus(db.Model):
    status_list=["sent","approved","to be eliminated"]
    id = db.Column(db.Integer, primary_key=True)
    status_name= db.Column(db.String(50), nullable=False)

    @classmethod
    def insert_rows(cls):
        # Create and insert a new row for each value in the list
        if db.session.query(cls).count() == 0:
            for value in cls.status_list:
                new_instance = cls(status_name=value)
                db.session.add(new_instance)
            
            # Commit the changes
            db.session.commit()
        else:
            print(f"The table {cls.__tablename__} is not empty. Rows were not inserted.")

        
    