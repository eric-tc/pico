# models.py

from flask_login import UserMixin
from . import db
from datetime import datetime
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime
from .internal_data import CONTROLS,PATHOLOGY_TYPE,PATHOLOGY,NOTIFICATION_STATUS,EMAIL_STATUS,CONTROL_STATUS,PATHOLOGY_STATUS
from sqlalchemy.dialects.postgresql import JSONB

class User(UserMixin, db.Model):

    
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(300))
    name = db.Column(db.String(120))
    role = db.Column(db.Integer)
    phone = db.Column(db.String(20))
    sx_dx_hand = db.Column(db.String(10))
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
                print(row.value)
                id,name,timeline,form,enum,pre_options= row.value
                new_instance = cls(name=name)
                db.session.add(new_instance)
            
            # Commit the changes
            db.session.commit()
        else:
            print(f"The table {cls.__tablename__} is not empty. Rows were not inserted.")


"""
Tabella per gestire lo stato di una patologia

1: Prima intervento
2: Trattamento
3: Post Intervento

"""
class PathologyStatus(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120))


    @classmethod
    def insert_rows(cls):
        # Create and insert a new row for each value in the list
        if db.session.query(cls).count() == 0:
            for row in PATHOLOGY_STATUS:
                id,name= row.value
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
    
    #Valore utilizzato per salvare a db quale tipo di sotto patologia è stato selezionato
    #Utilzzato inoltre per capire se la patologia ha un post trattamento diverso in termini di settimane
    id_pathology_type= db.Column(db.Integer,db.ForeignKey('pathology_type.id'),nullable=False)
    pathology_type = db.relationship('PathologyType', foreign_keys=[id_pathology_type])
    
    #Tiene traccia dello stato della patologia (PRE,TRATTAMENTO PROGRAMMATO,POST)
    id_pathology_status= db.Column(db.Integer,db.ForeignKey('pathology_status.id'),nullable=False)
    pathology_status = db.relationship('PathologyStatus', foreign_keys=[id_pathology_status])

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    #Tiene traccia della riga del database da cui è stato creato il record.
    #Solitamente fa riferimento al controllo con next_control_number=0. 
    # Cioè il controllo iniziale di inserimento terapia
    id_created_from = db.Column(db.Integer, nullable=True)
    #Data in cui è stato fissato intervento 
    surgery_date = db.Column(db.DateTime,nullable=True)
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
    
    mpcj=db.Column(JSONB)
    pipj= db.Column(JSONB)
    dipj=db.Column(JSONB)
    ipj=db.Column(JSONB)
    polso=db.Column(JSONB)
    vas=db.Column(db.Float)
    trapezio_metacarpale=db.Column(JSONB)
    forza=db.Column(JSONB)
    dash=db.Column(JSONB)
    prwhe=db.Column(JSONB)
    eaton_littler=db.Column(db.Integer)
    edema=db.Column(db.String(10))
    sensibilita_volare= db.Column(JSONB)
    sensibilita_dorsale= db.Column(JSONB)
    cicatrice= db.Column(JSONB)
    tutore = db.Column(db.String(10))
    altro = db.Column(JSONB)
    guarigione_ossea= db.Column(JSONB)
    concesso_inizio_mobilizzazione = db.Column(db.Integer)
    articolazione_stabile = db.Column(db.Integer)
    data_inizio_mobilizzazione = db.Column(db.DateTime,nullable=True)
    #Questo campo è utilizzato per salvare note solitamente su controlli creati dal fisioterapista
    note= db.Column(JSONB)
    #Campo utilizzati per salvare i diversi parametri 
    #in base alla tipologia di intervento selezionato
    pre_options = db.Column(JSONB)
    chirugico_options = db.Column(JSONB)
    #Ad esempio nello scafoide dopo 6 mesi devo aggiungere dei parametri aggiuntivi
    post_options= db.Column(JSONB)
    


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

        
    