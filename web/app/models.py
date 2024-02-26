# models.py

from flask_login import UserMixin
from . import db
from datetime import datetime
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime
from .internal_data import CONTROLS,PATHOLOGY_TYPE,PATHOLOGY,NOTIFICATION_STATUS,EMAIL_STATUS,CONTROL_STATUS

class User(UserMixin, db.Model):

    
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(300))
    name = db.Column(db.String(120))
    role = db.Column(db.Integer)
    #new_instance = YourModel(doctor_ids=[1, 2, 3, 4, 5])
    doctor_ids = db.Column(ARRAY(db.Integer))


class Pathology(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120))


    @classmethod
    def insert_rows(cls):
        # Create and insert a new row for each value in the list
        if db.session.query(cls).count() == 0:
            for row in PATHOLOGY:
                id,name,timeline= row.value
                new_instance = cls(name=name)
                db.session.add(new_instance)
            
            # Commit the changes
            db.session.commit()
        else:
            print(f"The table {cls.__tablename__} is not empty. Rows were not inserted.")



class PathologyType(db.Model):
   
    
    id = db.Column(db.Integer,primary_key=True)
    type=db.Column(db.Integer) 
    name = db.Column(db.String(120))
    
    @classmethod
    def insert_rows(cls):
        # Create and insert a new row for each value in the list
        if db.session.query(cls).count() == 0:
            for row in PATHOLOGY_TYPE:

                id,type,name= row.value
                new_instance = cls(name=name,type=type.value[0])
                db.session.add(new_instance)
            
            # Commit the changes
            db.session.commit()
        else:
            print(f"The table {cls.__tablename__} is not empty. Rows were not inserted.")


"""

Classe che contiene tutti i dati degli interventi

"""
class PathologyData(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    
    id_doctor = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    doctor = db.relationship('User', foreign_keys=[id_doctor])
    
    id_patient = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    patient = db.relationship('User', foreign_keys=[id_patient])
    
    id_pathology= db.Column(db.Integer,db.ForeignKey('pathology.id'),nullable=False)
    pathology = db.relationship('Pathology', foreign_keys=[id_pathology])
    
    id_pathology_type= db.Column(db.Integer,db.ForeignKey('pathology_type.id'),nullable=False)
    pathology_type = db.relationship('PathologyType', foreign_keys=[id_pathology_type])

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    #Data prossimo incontro
    next_control_date= db.Column(db.DateTime,nullable=False)
    #Ora prossimo incontro
    next_control_time= db.Column(db.String(10),nullable=False)
    next_control_number= db.Column(db.Integer,nullable=False)
    #1= se il paziente ha confermato la data della prossima visita
    is_date_accepted = db.Column(db.Integer,default=0)
    #Gestione email per controllo
    email_status= db.Column(db.Integer, default=0)
    email_sent_date=db.Column(db.DateTime,default=None)
    email_confirmed_date= db.Column(db.DateTime,default=None)
    #identifica se i dati sono già stati inseriti e non è possibile cambiarli
    
    id_control_status = db.Column(db.Integer,db.ForeignKey('control_status.id'),nullable=False)
    control_status = db.relationship('ControlStatus', foreign_keys=[id_control_status])
    

    #I valori di queste variabili devono corrispondere ai valori di RIZOARTROSI_CONTROLS dentro internal Data.
    #In questo modo posso accedere a queste variabili utilizzando setattr(myinstance,RIZOARTROSI_CONTROLS....value)  
    nprs_vas=db.Column(db.Integer)
    prom_aprom_mcpj= db.Column(db.Integer)
    prom_aprom_ipj=db.Column(db.Integer)
    abduzione=db.Column(db.Integer)
    anteposizione=db.Column(db.Integer)
    kapandji=db.Column(db.Integer)
    pinch=db.Column(db.Integer)
    grip=db.Column(db.Integer)
    dash=db.Column(db.Integer)
    prwhe=db.Column(db.Integer)
    eaton_littler=db.Column(db.Integer)
    tipo_cicatrice= db.Column(db.String(100))
    stato_cicatrice = db.Column(db.String(100))
    modena = db.Column(db.String(100))

    #Campi utilizzati per salvare i diversi parametri 
    #in base alla tipologia di intervento selezionato
    field1 = db.Column(db.String(30))
    field2 = db.Column(db.String(30))
    field3 = db.Column(db.String(30))
    field4 = db.Column(db.String(30))
    field5 = db.Column(db.String(30))
    


"""
Classe per tenere traccia relazione paziente dottore
Un dottore può avere più pazienti in cura.

Uno stesso paziente può avere più dottori nello stesso momento?
"""
class DoctorPatient(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    id_doctor = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    doctor = db.relationship('User', foreign_keys=[id_doctor])
    id_patient = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    patient = db.relationship('User', foreign_keys=[id_patient])

    # Adding a unique constraint on column1 and column2
    __table_args__ = (
        UniqueConstraint('id_doctor', 'id_patient'),
    )

"""
Tiene traccia quali pazienti ha in cura e per quali patologie.
Questa tabella si riempe solo quando un dottore ha creato una cura 
per uno specifico paziente dopo che sono diventati amici.
"""

class DoctorCurrentPathology(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    id_doctor = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    doctor = db.relationship('User', foreign_keys=[id_doctor])
    id_patient = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    patient = db.relationship('User', foreign_keys=[id_patient])
    #Corrisponde all'id della patologia nella tabella pathology
    id_pathology = db.Column(db.Integer)
    id_pathology_row=db.Column(db.Integer)    
    id_pathology_type= db.Column(db.Integer)

    # Adding a unique constraint on column1 and column2
    __table_args__ = (
        UniqueConstraint('id_doctor', 'id_patient',"id_pathology","id_pathology_type"),
    )


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_doctor = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    doctor = db.relationship('User', foreign_keys=[id_doctor])
    id_patient = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    patient = db.relationship('User', foreign_keys=[id_patient])
    status = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

"""
Classe utilizzata per salvare lo stato del controllo

1 Active. Significa che il controllo è stato inserito a database
2 Closed. Significa che un medico ha inserito i dati del controllo. 
3 Expired. Significa che il paziente non si è presentato e il sistema ha chiuso in automatico 
il controllo dopo x settimane

"""
class ControlStatus(db.Model):
    

    id = db.Column(db.Integer, primary_key=True)
    control_name= db.Column(db.String(50), nullable=False)

    @classmethod
    def insert_rows(cls):
        # Create and insert a new row for each value in the list
        if db.session.query(cls).count() == 0:
            for member in CONTROL_STATUS:
                new_instance = cls(control_name=member.value[1])
                db.session.add(new_instance)
            
            # Commit the changes
            db.session.commit()
        else:
            print(f"The table {cls.__tablename__} is not empty. Rows were not inserted.")

class EmailStatus(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    status_name= db.Column(db.String(50), nullable=False)

    @classmethod
    def insert_rows(cls):
        # Create and insert a new row for each value in the list
        if db.session.query(cls).count() == 0:
            for member in EMAIL_STATUS:
                new_instance = cls(status_name=member.value[1])
                db.session.add(new_instance)
            
            # Commit the changes
            db.session.commit()
        else:
            print(f"The table {cls.__tablename__} is not empty. Rows were not inserted.")

class NotificationStatus(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    status_name= db.Column(db.String(50), nullable=False)

    @classmethod
    def insert_rows(cls):
        # Create and insert a new row for each value in the list
        if db.session.query(cls).count() == 0:
            for member in NOTIFICATION_STATUS:
                new_instance = cls(status_name=member.value[1])
                db.session.add(new_instance)
            
            # Commit the changes
            db.session.commit()
        else:
            print(f"The table {cls.__tablename__} is not empty. Rows were not inserted.")

        
    