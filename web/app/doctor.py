from flask import Blueprint, render_template,request,jsonify,redirect, url_for, flash,session,make_response
from flask_login import login_required, current_user
from .internal_data import ROLE,NOTIFICATION_STATUS,PATHOLOGY_KEY_SELECTION_FORM,PATHOLOGY,CONTROL_STATUS,EMAIL_STATUS,PATHOLOGY_TYPE,DoctorData,RizoartrosiControlsTimeline,CONTROLS,PATHOLOGY_STATUS,CacheDataDoctor,CONTROLSNUMBER
from .models import User,DoctorPatient,Notification,PathologyData,PathologyType,Pathology
from .internal_data import FratturaMetaCarpaleTimeline,FrattureFalangeProssimaleTimeline
from . import db,csrf,cache
from sqlalchemy import cast, Integer,func
from .doctor_forms import MedicalTreatmentForm,PreTreamentForm,PostTreatmentForm,TreatmentForm,CustomControlForm
import datetime
from datetime import datetime, timedelta,time
from .mutils import get_date,get_date_from_datetime,get_pathology_enum,pathology_set_next_control,getDateInYMD
from werkzeug.security import generate_password_hash
import json
from .internal_data import get_pathology_type_dict,EVENT_DAYS
from .query_sql import select_next_treatments
import sys
from weasyprint import HTML
from .settings_form import SettingsFormDoctor
from .internal_data_enum_pathologies import DASH_ENUM_FIFTH,DASH_ENUM_FOURTH,DASH_ENUM_SECOND,DASH_ENUM_THIRD,DASH_ENUM_FIRST,DASH_ENUM_SIXTH

#TEST

from .doctor_forms import DashFormTest

doctor = Blueprint('doctor', __name__)

import os

PDF_DIRECTORY = 'app/static/pdf_files/'
if not os.path.exists(PDF_DIRECTORY):
    os.makedirs(PDF_DIRECTORY)

def remove_session_data():
    
    cache.delete(CacheDataDoctor.CALENDAR_EVENTS.value)
    


@doctor.route('/profile')
@login_required
def profile():

    remove_session_data()

    patients_list=(
    db.session.query(DoctorPatient, User.name,User.surname)
    .join(User, DoctorPatient.id_patient == User.id)
    .filter(DoctorPatient.id_doctor == current_user.id).order_by(User.id.asc())
    .order_by(User.surname.asc()).all()
    )
    

    print(patients_list)

    #Ritorna tutti le patologie aggiunte dal dottore per le quali non è ancora stato fissato intervento
    #(pathology_row,patient_name,pathology_name)
    interventi_da_fissare= db.session.query(PathologyData,User.name,User.surname,Pathology.name)\
    .join(User, PathologyData.id_patient == User.id)\
    .join(Pathology,PathologyData.id_pathology==Pathology.id)\
    .filter(PathologyData.id_doctor == current_user.id , PathologyData.id_pathology_status==PATHOLOGY_STATUS.PRIMA.value[0],PathologyData.id_control_status==CONTROL_STATUS.ACTIVE.value[0]).order_by(PathologyData.created_at.asc()).all()
    print("INTERVENTI DA FISSARE")
    print(interventi_da_fissare)


    # 2 recupero gli interventi di diversi pazienti più vicini alla data attuale
    next_treatments=[]
    # for patient_query in patients_list:
    #     #in base all'id paziente 
    #     print("value")
    #     doctorPatient, name = patient_query

    #     #recupero tutte le patologie a cui il paziente è associato il dottore
    #     select_next_treatments(doctorPatient.id_patient,next_treatments)


            
    return render_template('doctor/profile.html', 
                           name=current_user.name,
                           patients_list=patients_list,
                           interventi_da_fissare=interventi_da_fissare, 
                           next_treatments=next_treatments)
                          

"""
Route usata per settare i parametri del dottore. Come Email, cambio password, ecc

"""
@doctor.route('/settings_doctor',methods=["GET","POST"])
@login_required
def settings_doctor():

    form = SettingsFormDoctor()
    user_data = User.query.get(current_user.id)
    
    if form.validate_on_submit():
        print(form.email.data)
        user_data.name = form.name.data
        #check if form.password.data is not empty
        if form.password.data:
            user_data.password = generate_password_hash(form.password.data)
        user_data.phone = form.phone.data
        db.session.commit()
        flash('Cambio Dati effettuato con successo')
        return redirect(url_for('doctor.profile'))
    

    form.email.data= user_data.email
    form.name.data= user_data.name
    form.phone.data= user_data.phone
    #retrieve data from db and assign to form

    
    

    return render_template('doctor/settings_doctor.html', form=form,name=current_user.name)


"""
Ajax request to send notification to patient

"""
@doctor.route('/send_patient_notification',methods=["POST"])
@login_required
def send_patient_notification():

    print("DATA JSON")
    csrf.protect()

    print("DATA JSON")
    patient_id = request.json.get('patient_id')
    
    new_link = Notification(id_doctor=current_user.id,
                            id_patient=patient_id,
                            status=NOTIFICATION_STATUS.SENT.value[0])
    db.session.add(new_link)
    db.session.commit()


    if True:
        return jsonify({"success":"associato"})
    else:
        return jsonify({'error': 'User not found'}), 404
    

"""
Route to show all patient available

"""
@doctor.route('/patients_list')
@login_required
def patients_list():

    patients_list= User.query.filter_by(role=ROLE.PATIENT.value).all()

    return render_template('doctor/patients_list.html',patients_list=patients_list)


# -------------------------ROUTE PER DEFINIRE un nuovo controllo paziente---------------------------------------------------


"""
Inserimento della patologia nella fase PRE INTERVENTO e ritorno in home

"""
@doctor.route('/parameters_pre_treatment_selection/<patient_id>/<patient_name>/<pathology_id>',methods=["GET","POST"])
@login_required
def parameters_pre_treatment_selection(patient_id,patient_name,pathology_id):

    
    print("PARAMETERS_PRE_TREATMENT_SELECTION")
    
    print(patient_id)
    print(patient_name)
    print(pathology_id)


    pre_controls_map=None
    #Form per la selezione dei parametri della patologia
    pre_controls_form=None

    form= PreTreamentForm()
    controls_map=None
    
    #In base alla patologia selezionata ritorno le terapie associate a quella patologia
    for pathology in PATHOLOGY:
        if pathology.value[0] == int(pathology_id):
            
            controls_map,pre_controls_map= pathology.value[2].get_pre()
            if(pathology.value[5] is not None):
                pre_controls_form= pathology.value[5]()
            print("CONTROLS MAP")
            print(controls_map)
            break
    
    
    if request.method == 'POST':
        
        precontrols_data=None
        if(pre_controls_form is not None):
            precontrols_data= pre_controls_form.data

            if "csrf_token" in precontrols_data:
                precontrols_data.pop("csrf_token")

        data_frattura = request.form.get(CONTROLS.DATA_FRATTURA.value[1])
        
        mpcj_data,\
        pipj_data,\
        dipj_data,\
        ipj_data,\
        trapezio_metacarpale,\
        polso,\
        vas_data,\
        forza,\
        dash_data,\
        prwhe_data,\
        eaton_littler_data,\
        edema_data,\
        sensibilita_volare_data,\
        sensibilita_dorsale_data,\
        cicatrice,\
        tutore_data,\
        altro_data = pathology.value[2].process_parameters(controls_map=controls_map,
                                              form=form)
        

        # Form was submitted
        # Access form data
        new_entry = PathologyData(
        id_doctor=current_user.id,
        id_pathology=pathology_id,  
        id_pathology_type=pathology_id, # Non conosco ancora il tipo di intervento che sceglierà il dottore
        id_pathology_status= PATHOLOGY_STATUS.PRIMA.value[0], 
        id_patient=patient_id,  
        next_control_date=datetime(1970, 1, 1) if not data_frattura else get_date(data_frattura),
        next_control_time= "12:00",
        is_date_accepted= 0,
        next_control_number=0,
        id_control_status=CONTROL_STATUS.ACTIVE.value[0],  # Replace with the actual value
        mpcj=mpcj_data,
        pipj=pipj_data,
        dipj=dipj_data,
        ipj=ipj_data,
        polso=polso,
        vas=vas_data,
        trapezio_metacarpale=trapezio_metacarpale,
        forza=forza,
        dash=dash_data,
        prwhe=prwhe_data,
        eaton_littler=eaton_littler_data,
        edema=edema_data,
        sensibilita_volare=sensibilita_volare_data,
        sensibilita_dorsale=sensibilita_dorsale_data,
        cicatrice=cicatrice,
        tutore=tutore_data,
        altro=altro_data,
        chirugico_options=  None,
        pre_options= json.dumps(precontrols_data) if precontrols_data else None
        )
        
        db.session.add(new_entry)

        # Commit the session to persist the changes to the database
        db.session.commit()

        return redirect(url_for('doctor.profile'))



    return render_template('doctor/trattamenti/parameters_pre_treatment_selection.html',doctor_id=current_user.id,
                            patient_name=patient_name,
                            patient_id=patient_id,
                            pathology=PATHOLOGY,
                            form_keys=PATHOLOGY_KEY_SELECTION_FORM,
                            form=form,
                            controls_map=controls_map,
                            controls_map_pre=pre_controls_map,
                            pre_controls_form=pre_controls_form
                          )



"""
Route che crea nella tabella patology data una riga con la patologia inserita

"""
@doctor.route('/insert_pre_medical_treatment/<patient_id>/<patient_name>/>',methods=["GET","POST"])
@login_required
def insert_pre_medical_treatment(patient_id,patient_name):

    print("INSERT_PRE_MEDICAL_TREATMENT")
    
    if request.method == 'POST':
        
        pathology_id = request.form.get("pathology")
        print(pathology_id)
        #in base alla patologia selezionata creo dei campi da compilare e alcuni vuoti
        # return render_template('doctor/pre_treatment/parameters_pre_treatment_selection.html',
        #                        doctor_id=current_user.id,
        #                        patient_id=patient_id,
        #                        patient_name=patient_name)

        return redirect(url_for('doctor.parameters_pre_treatment_selection', 
                        patient_id=patient_id, 
                        patient_name=patient_name, 
                        pathology_id=pathology_id))
    


    return render_template('doctor/insert_pre_medical_treatment.html',doctor_id=current_user.id,
                            patient_name=patient_name,
                            patient_id=patient_id,
                            pathology=PATHOLOGY,
                            form_keys=PATHOLOGY_KEY_SELECTION_FORM
                          )


@doctor.route('/medical_treatment/',methods=["POST"])
@login_required
def medical_treatment():


    #session.pop(DoctorData.OPTIONS_FIELD.value, None)
    #POSSO ELIMINARE?
    medicalForm= MedicalTreatmentForm()

    # session[DoctorData.ID_PATIENT.value]=patient_id
    # #Quando crea un nuovo controllo l'appuntamento successivo è sempre il secondo
    # session[DoctorData.NUM_CONTROL.value]= 1

    # print("PATIENT ID")
    # print(session.get(DoctorData.ID_PATIENT.value))

    patient_id= request.form.get('patient_id')
    pathology_id = request.form.get('pathology_id')
    patient_name = request.form.get('patient_name')
    row_id_to_update = request.form.get('row_id')


    print(f"PATIENT ID {patient_id}")
    print(f"PATHOLOGY ID {pathology_id}")
    print(f"PATIENT NAME {patient_name}")
    print(f"ROW ID {row_id_to_update}")

    #ogni chiave rappresenta id patologia
    #pathology_names_id_options,timeline_pathology = get_pathology_type_dict()

    # ritorna la pathologia selezionata
    pathology_enum = get_pathology_enum(pathology_id)
    form= pathology_enum.value[3]()


    if form.validate_on_submit():

   
        surgery_date = getDateInYMD(request.form.get("data_intervento"))
        
        pathology_id_type =None
        patholgy_id_label=None

        #Devo verificare enum per capire quale id patologia devo inserire
        for key in pathology_enum.value[4]:
            
            if(key.value[0] == request.form.get("treatment_options")):
                pathology_id_type= key.value[0]
                patholgy_id_label= key.value[1]
                break
        
        
        #Aggiornamento riga patologia con la data dell'intervento
        pathology_row_to_update = PathologyData.query.get(row_id_to_update)
        #Id tipo patologia
        pathology_row_to_update.id_pathology_type= pathology_id_type        
        pathology_row_to_update.id_control_status=CONTROL_STATUS.CLOSED.value[0]
        pathology_row_to_update.surgery_date= surgery_date
        pathology_row_to_update.id_pathology_status= PATHOLOGY_STATUS.DURANTE.value[0]

        form_data= form.data
        #Elimino i campi che non sono legati alla patologia per evitare di riempire troppo il db
        if "csrf_token" in form_data:
            form_data.pop("csrf_token")
        if "data_intervento" in form_data:
            form_data.pop("data_intervento")
        if "data_primo_controllo" in form_data:
            form_data.pop("data_primo_controllo")
        if "orario_primo_controllo" in form_data:
            form_data.pop("orario_primo_controllo")
        if "patient_id" in form_data:
            form_data.pop("patient_id")
        if "pathology_id" in form_data:
            form_data.pop("pathology_id")
        if "submit_chirurgico_form" in form_data:
            form_data.pop("submit_chirurgico_form")
        if "row_id" in form_data:
            form_data.pop("row_id")
        if "patient_name" in form_data:
            form_data.pop("patient_name")
        if "treatment_options" in form_data:
            form_data["treatment_options"]= patholgy_id_label

        pathology_row_to_update.chirugico_options= json.dumps(form_data)
        db.session.commit()

        # variabili comun a tutte le patologie
        data_prossimo_controllo=None
        orario_prossimo_controllo= None

        print(f"PATHOLOGY ID TYPE {pathology_id_type}")
        

        #Pathology_Enum è enum PATHOLOGY che contiene tutte le patologie. 
        # Il valore 2 ad esempio è RizoartrosiControlsTimeline.timeline che contiene le settimane dei controlli successivi 
        print(form.data_primo_controllo.data)
        print(form.orario_primo_controllo.data)
        print("VALORI FORM")
        #indica se è stata concordata la data con il paziente
        data_primo_controllo=form.data_primo_controllo.data
        orario_primo_controllo=form.orario_primo_controllo.data

        date_accepted_first_control=False
        if data_primo_controllo:
            date_accepted_first_control=True
        for control_number,weeks_to_add in enumerate(pathology_enum.value[2].getTimeline(pathology_id_type)):
            
            #Aggiungo i controlli solo se hanno una settimana maggiore di 0
            if(int(weeks_to_add)>0):
                
                data_prossimo_controllo=None
                orario_prossimo_controllo=None
                is_date_accepted=False
                if (date_accepted_first_control):
                    data_prossimo_controllo,orario_prossimo_controllo,is_date_accepted= pathology_set_next_control(data_primo_controllo,
                                                                                                            orario_primo_controllo,
                                                                                                            True,
                                                                                                            weeks_to_add,
                                                                                                            surgery_date)
                else:
                    data_prossimo_controllo,orario_prossimo_controllo,is_date_accepted= pathology_set_next_control(data_primo_controllo,
                                                                                                            orario_primo_controllo,
                                                                                                            False,
                                                                                                            weeks_to_add,
                                                                                                            surgery_date)
                # in ogni caso dopo il primo controllo il check della data non è più vero. 
                # I controlli successivi al primo non possono avere la data confermata                                                                                           
                date_accepted_first_control=False
                
                # I valori dei parametri sono tutti a None perchè il dottore li dovrà inserire al momento del controllo
                new_entry = PathologyData(
                    id_doctor=current_user.id,  # Replace with the actual doctor ID
                    id_pathology=pathology_id,  # Replace with the actual type ID
                    id_pathology_type=pathology_id_type, #TODO da cambiare con id patologia
                    id_patient=patient_id,  # Replace with the actual patient ID
                    id_pathology_status= PATHOLOGY_STATUS.DOPO.value[0],
                    id_created_from=row_id_to_update,
                    next_control_date=data_prossimo_controllo,
                    next_control_time= orario_prossimo_controllo,
                    is_date_accepted= is_date_accepted,
                    next_control_number=control_number, # il primo controllo ha sempre valore 0. Questo serve per recuperare il valore corretto dalla timeline
                    id_control_status=CONTROL_STATUS.ACTIVE.value[0],  # Replace with the actual value
                    surgery_date=surgery_date,
                    mpcj=None,
                    pipj=None,
                    dipj=None,
                    ipj=None,
                    polso=None,
                    vas=None,
                    trapezio_metacarpale=None,
                    forza=None,
                    dash=None,
                    prwhe=None,
                    eaton_littler=None,
                    edema=None,
                    cicatrice=None,
                    tutore=None,
                    altro=None,
                    chirugico_options= json.dumps({"row_id":row_id_to_update}) #inserisco la riga di riferimento della patologia
                    )
            

                        # Add the instance to the session
                db.session.add(new_entry)

        # Commit the session to persist the changes to the database
        db.session.commit()

        flash('Inserimento terapia con successo')
        return redirect(url_for('doctor.profile'))
            

    
    print(f"week to add {pathology_enum.value[2].weeks_to_first_control}")

    return render_template(f'doctor/pathologies/{pathology_enum.value[1]}.html',
                           doctor_id=current_user.id,
                           patient_id=patient_id,
                           pathology_id=pathology_id,
                           patient_name=patient_name,
                           row_id=row_id_to_update,
                           form=form,
                           week_to_add=pathology_enum.value[2].weeks_to_first_control)


"""
Route per insiere un controllo personalizzato in base alla patologia.
Questa route è chiamata dalla storia del paziente selezionando il bottone "Aggiungi Controllo"

Row_id: id della riga della tabella patology_data con next_control_number uguale a 0
   
"""

@doctor.route('/insert_custom_control/<row_id>',methods=["GET","POST"])
@login_required
def insert_custom_control(row_id):
    form= CustomControlForm()

    print(f"Row id {row_id}")

    if form.validate_on_submit():

        row_original_control = PathologyData.query.get(row_id)

        new_row = PathologyData(id_doctor= row_original_control.id_doctor,
                               id_patient= row_original_control.id_patient,
                               id_pathology= row_original_control.id_pathology,
                               id_pathology_type= row_original_control.id_pathology_type,
                               id_pathology_status= PATHOLOGY_STATUS.PERSONALE.value[0],
                               id_created_from= row_id,
                               next_control_number=-1,
                               note=json.dumps(form.note.data),
                               next_control_date= datetime.utcnow(),
                               next_control_time= "12:00",
                               id_control_status=CONTROL_STATUS.CLOSED.value[0],)
       
        db.session.add(new_row)
        db.session.commit()

        flash('Controllo inserito con successo')
        return redirect(url_for('doctor.profile'))
           


    return render_template('doctor/trattamenti/custom_control.html',form=form)


# ------------------------------ROUTE PER MOSTRARE LA STORIA DEL PAZIENTE-------------------------------
# In ogni route devo salvare id paziente selezionato e la pathology type nella sessione
# Non passo nessun parametro nella path. passo tutti i valori in Post con il form

"""
Route per mostrare tutti i pazienti associati al dottore e i rispettivi trattamenti eseguiti

"""
@doctor.route('/patient_treatment_list/<patient_id>/<patient_name>',methods=["GET"])
@login_required
def patient_treatment_list(patient_id,patient_name):

    #prendo tutti i pazienti associati al dottore e mi faccio ritornare le malattie
    
    print(f"PATIENT ID {patient_id}")
    session[DoctorData.ID_PATIENT.value]= patient_id

    

    #ciclo su tutte le tabelle delle malattie per farmi ritornare tutti gli interventi. Versione 1
    # Nella tabella doctor patient pathology recupero solo le tabelle che devo ciclare per recuperare la storia paziente

    pathology_list = (
    db.session.query(
        PathologyData.id_patient,
        User.name,
        User.surname,
        Pathology.id,
        Pathology.name,
        PathologyType.id,
        PathologyType.name,
        PathologyData.created_at,
        PathologyData.id
    )
    .join(Pathology, Pathology.id == PathologyData.id_pathology)
    .join(PathologyType, PathologyType.id == PathologyData.id_pathology_type)
    .join(User, User.id == PathologyData.id_patient)
    .filter(PathologyData.id_patient == patient_id, 
            PathologyData.next_control_number == 0)
    .all()
    )
    name=""
    surname=""
    for item in pathology_list:
        name=item[1]
        surname=item[2]
        break
    
    return render_template('doctor/patient_treatment_list.html',pathology_list=pathology_list,name=name,surname=surname)


"""
Route to show patient history
"""
@doctor.route('/patient_history/<id_pathology>/<id_pathology_type>/',methods=["GET"])
@login_required
def patient_history(id_pathology,id_pathology_type):
    
    print(session.get(DoctorData.ID_PATIENT.value))
    
   

    print("HISTORY PATIENT")
    print(id_pathology)
    print(id_pathology_type)

    all_pathology_row = db.session.query(PathologyData).filter(PathologyData.id_patient == session.get(DoctorData.ID_PATIENT.value),
                                          PathologyData.id_pathology==id_pathology ,
                                          PathologyData.id_pathology_type== id_pathology_type).order_by(PathologyData.next_control_date.asc()).all()
    
    #Associa ad ogni controllo la propria lista di controlli attivi 
    pathology_and_control_maps=[]

    for pathology_raw in all_pathology_row:

        #control_map = RizoartrosiControlsTimeline.get_controls(pathology_raw.next_control_number)
        control_map=None
        pathology_and_control_maps.append((pathology_raw,control_map))

    return render_template('patient_history.html',pathology_and_control_maps=pathology_and_control_maps,control_status_enum=CONTROL_STATUS)


"""
Questa route permette al dottore di creare istantaneamente il paziente e
associarlo senza passare dalle notifiche

"""

@doctor.route('/create_new_patient',methods=["GET"])
@login_required
def create_patient():
    
    return render_template("doctor/create_new_patient.html")

"""
Il metodo post serve per gestire i dati derivati dal form
"""
@doctor.route('/create_new_patient',methods=["POST"])
@login_required
def create_patient_post():

    email = request.form.get('email')
    surname = request.form.get('surname')   
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again  
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_patient = User(email=email, name=name, surname=surname, password=generate_password_hash(password),role=ROLE.PATIENT.value)

    # add the new user to the database
    db.session.add(new_patient)
    db.session.commit()

    if(new_patient):
            new_link = DoctorPatient(id_doctor=current_user.id, id_patient=new_patient.id)
            db.session.add(new_link)
            db.session.commit()

    return redirect(url_for('doctor.profile'))



# ----------------------------- CALENDARIO TRATTAMENTI POST OPERATORIO -------------------------------
# Serve per Cambiare data e ora del controllo
# Visualizza tutti i controlli successivi
# Permette di compilare il trattamento post operatorio quando si è vicini alla data
@doctor.route('/calendar',methods=["GET"])
@login_required
def calendar():

    #Abilitano click su evento del calendario
   
    return render_template("doctor/trattamenti/calendar.html",
                           days_before=EVENT_DAYS.DAYS_BEFORE.value,
                           days_after=EVENT_DAYS.DAYS_AFTER.value)


# Ritorna tutti i trattamenti di tutti i pazienti associati a quel dottore.
# Posso usare questi campi per popolare il calendario con diversi filtri

@doctor.route('/treatments_events')
@login_required
def get_events():


    #Prendo solo gli eventi entro tot mesi. Per rendere la query più veloce
    events = cache.get(CacheDataDoctor.CALENDAR_EVENTS.value)
    
    if(events):
        print(f"BYTES EVNET {sys.getsizeof(cache.get(CacheDataDoctor.CALENDAR_EVENTS.value))}")
        return jsonify(events)
    else:
    
        today = datetime.today()

        # 3 Mesi
        
        date_after_x_months = today + timedelta(days=EVENT_DAYS.MONTHS_TO_RETRIEVE.value*30)
        
        treatments= db.session.query(PathologyData,User.name,User.surname,Pathology.name)\
        .join(User,PathologyData.id_patient==User.id)\
        .join(Pathology,PathologyData.id_pathology==Pathology.id)\
        .filter(PathologyData.id_doctor == current_user.id,
                PathologyData.id_pathology_status==PATHOLOGY_STATUS.DOPO.value[0],
                PathologyData.next_control_date<date_after_x_months).all()
        
        events=[]

        #LEGENDA COLORI
        """
        isDateAccepted=0 -> colore grigio
        isDateAccepted=1 -> colore verde
        eventoPassato -> colore rosso

        """
        for treatment in treatments:
            event_dict={}

            pathology_row,patient_name,patient_surname,pathology_name = treatment
            #patient_name = "test"
            #pathology_name = "pathology_name"
            event_dict["title"]= f"{patient_name} {patient_surname} - {pathology_name}- {pathology_row.next_control_number}° controllo - {pathology_row.next_control_time}"
            event_dict["start"]= pathology_row.next_control_date.strftime("%Y-%m-%d") + "T" + pathology_row.next_control_time
            event_dict["id"]= pathology_row.id
            event_dict["closed"]=pathology_row.id_control_status
            

            if(pathology_row.is_date_accepted==0):
                event_dict["color"]= "#D3D3D3" 
            elif(pathology_row.is_date_accepted==1):
                event_dict["color"]= "#00FF00"

            if(pathology_row.id_control_status==CONTROL_STATUS.CLOSED.value[0]):
                event_dict["color"]= "#FF0000"

            events.append(event_dict)

        print(f"BYTES EVNET {sys.getsizeof(events)}")
        cache.set(CacheDataDoctor.CALENDAR_EVENTS.value,events)

        return jsonify(events)

"""
Al momento questa funzione è deprecata perchè già integrate nel calendario.
Questa è vantaggiosa solo se devo visionare il paziente.
"""
@doctor.route('/controls_for_day/<date>', methods=["GET", "POST"])
@login_required
def controls_for_day(date):
    selected_date = date
    interventions = []
    if selected_date:
        try:
            # Parsing la data in formato YYYY-MM-DD
            date_obj = datetime.strptime(selected_date, "%Y-%m-%d")
            # Query per recuperare gli interventi con surgery_date uguale alla data fornita
            results = db.session.query(PathologyData, User.name, Pathology.name) \
                .join(User, PathologyData.id_patient == User.id) \
                .join(Pathology, PathologyData.id_pathology == Pathology.id) \
                .filter(PathologyData.next_control_date != None) \
                .filter(func.date(PathologyData.next_control_date) == date_obj.date()) \
                .all()
            for row in results:
                pathology_data, patient_name, surgery_name = row
                code = None
                if getattr(pathology_data, 'id_control_status', None) == 2:
                    code = 2
                else:
                    current_date = datetime.now().date()
                    event_date = getattr(pathology_data, 'next_control_date', None)
                    days_before = EVENT_DAYS.DAYS_BEFORE.value
                    days_after = EVENT_DAYS.DAYS_AFTER.value
                    if event_date:
                        days_before_date = current_date - timedelta(days=int(days_before))
                        days_after_date = current_date + timedelta(days=int(days_after))
                        if days_before_date <= event_date.date() <= days_after_date:
                            code = 1
                        elif event_date.date() < current_date:
                            code = 2
                        elif event_date.date() > current_date:
                            code = 0
                interventions.append({
                    'id': pathology_data.id,
                    'patient_name': patient_name,
                    'surgery_name': surgery_name,
                    'code': code
                })
        except Exception as e:
            print(f"Errore nella ricerca: {e}")
    return render_template(
        'doctor/trattamenti/controls_for_day.html',
        interventions=interventions,
        selected_date=selected_date
    )


    

@doctor.route('/next_controls/<row_id>/<event_in_range>',methods=["GET","POST"])
@login_required
def event_details(row_id,event_in_range):
    """
    Route quando clicco su evento del calendario a cui passo la row_id della tabella patology_data

    row_id : id della riga della tabella patology_data
    event_in_range: indica se l'evento è nel range di compilazione
    """
    print(row_id)
    print("EVENT IN RANGE")
    print(event_in_range)

    form= PostTreatmentForm()

    controls_map=None
    week_to_add=None
    # Serve per impostare il valore di default per poi aggiungere le settimane
    data_intervento=None
    data_controllo=None
    pathology_db = db.session.query(PathologyData).filter(PathologyData.id==row_id).first()

    #Verifico se la data di inizio mobilizzazione è già stata inserita
    pathology_parent= db.session.query(PathologyData).filter(PathologyData.id==pathology_db.id_created_from).first()
    data_inizio_mobilizzazione=True
    if(pathology_parent):
        print("PATHOLOGY PARENT")
        print(pathology_parent.data_inizio_mobilizzazione)
        if(pathology_parent.data_inizio_mobilizzazione):
            #se ho già inserito la data di inizio mobilizzazione non posso più modificarla
            data_inizio_mobilizzazione=False

    #In base alla patologia selezionata ritorno le terapie associate a quella patologia
    for pathology in PATHOLOGY:
        if pathology.value[0] == int(pathology_db.id_pathology):
            
            #dizionario con i controlli attivi
            control_key= None
            #verifico i controlli. Se ho raggiunto il valore massimo usi next
            for value in CONTROLSNUMBER:
                if pathology_db.next_control_number >pathology.value[2].last_control_number_before_next:
                    control_key= "next"
                    break
                if value.value[0] == pathology_db.next_control_number:
                    control_key= value.value[1]
                    break
            
            print(f" NEXT CONTROL NUMBER {pathology_db.next_control_number}")
            print(f"CONTROL KEY {control_key}")

            param=None
            #In alcune patologie devo passare dei parametri per visualizzare correttamente i controlli
            if(pathology.value[2] is FratturaMetaCarpaleTimeline or pathology.value[2] is FrattureFalangeProssimaleTimeline):
                #devo recuperare la raw id dove sono salvati i dati. Nel controllo attuale non ci sono i paramteri
                #dell'intervento chirurgico
                print(pathology_db.chirugico_options)
                row_id= json.loads(pathology_db.chirugico_options)["row_id"]
                print(f"ROW ID {row_id}")
                pathology_data_original = db.session.query(PathologyData.chirugico_options).filter(PathologyData.id==row_id).first()
                print(pathology_data_original)
                if(pathology.value[2] is FratturaMetaCarpaleTimeline):
                    param= json.loads(pathology_data_original[0])["rottura_metacarpo"]
                elif(pathology.value[2] is FrattureFalangeProssimaleTimeline):
                    param= json.loads(pathology_data_original[0])["rottura_falange"]


            print(f"PARAM {param}")
            controls_map= getattr( pathology.value[2],"get_"+control_key,None)(pathology_db.id_pathology_type,param)
            
            print(f"CONTROLS MAP {controls_map}")
           
            #settimane 
            timeline= pathology.value[2].getTimeline(str(pathology_db.id_pathology_type))    
            
            print(f"TIMELINE {timeline}")
            #settimana in base al numero del controllo
            week_to_add= timeline[pathology_db.next_control_number]
            
            
            data_intervento= pathology_db.surgery_date
            data_controllo= pathology_db.next_control_date
            print(controls_map)
            print(week_to_add)
            print(data_intervento)
            print(data_controllo)
            break
    
    # Siccome alcune patologie possono avere un decorso diverso devo tenere in considerazione anche il pathology type
    

    if form.is_submitted():
        remove_session_data()
        #Verifico se utente ha cambiato data e ora del controllo successivo
        if form.submit_change_date.data:

            next_control_date= getDateInYMD(form.data_controllo.data)
            print(next_control_date)
            next_control_time= form.orario_controllo.data
            print(next_control_time)

            pathology_db.next_control_date= next_control_date
            if(next_control_time):
                pathology_db.next_control_time= next_control_time
            else:
                pathology_db.next_control_time= "12:00"
            pathology_db.is_date_accepted=1
            db.session.commit()
            return redirect(url_for('doctor.calendar'))
        
        if form.submit_form.data:
            print("SUBMIT FORM")
            print(form.data)

            #Creo il PDF Dai dati parsati del form submit

            html_content_original = form.hidden_html.data
            if html_content_original:
                try:
                    html_content = request.get_json(silent=True) or eval(html_content_original)

                    filename = f"report_{row_id}.pdf"
                    pdf_path = os.path.join(PDF_DIRECTORY, filename)
                    HTML(string=html_content.get("html")).write_pdf(pdf_path)
                except Exception as e:
                    print(f"Error parsing form data: {e}")
                    parsed_data = {}

            #Inserisco i dati a database della patologia inserita
            for key in controls_map.keys():
                
                #Remove csrf token 
                
                #Data frattura nei controlli non è conteggiata
                if(key != CONTROLS.DATA_FRATTURA.value[1] and key != CONTROLS.DATA_INIZIO_MOBILIZZAZIONE.value[1]):
                    mpcj_data,\
                    pipj_data,\
                    dipj_data,\
                    ipj_data,\
                    trapezio_metacarpale,\
                    polso,\
                    vas_data,\
                    forza,\
                    dash_data,\
                    prwhe_data,\
                    eaton_littler_data,\
                    edema_data,\
                    sensibilita_volare_data,\
                    sensibilita_dorsale_data,\
                    cicatrice,\
                    tutore_data,\
                    altro_data = pathology.value[2].process_parameters(controls_map=controls_map,
                                                        form=form)
                    
                    pathology_db.mpcj=mpcj_data
                    pathology_db.pipj=pipj_data
                    pathology_db.dipj=dipj_data
                    pathology_db.ipj=ipj_data
                    pathology_db.polso=polso
                    pathology_db.vas=vas_data
                    pathology_db.trapezio_metacarpale=trapezio_metacarpale
                    pathology_db.forza=forza
                    pathology_db.dash=dash_data
                    pathology_db.prwhe=prwhe_data
                    pathology_db.eaton_littler=eaton_littler_data
                    pathology_db.edema=edema_data
                    pathology_db.sensibilita_volare=sensibilita_volare_data
                    pathology_db.sensibilita_dorsale=sensibilita_dorsale_data
                    pathology_db.cicatrice=cicatrice
                    pathology_db.tutore=tutore_data
                    pathology_db.altro=altro_data

                if(key == CONTROLS.DATA_INIZIO_MOBILIZZAZIONE.value[1]):
                    if(form.data[key]):
                        data_inizio_mobilizzazione= getDateInYMD(form.data[key])
                        setattr(pathology_parent, key, data_inizio_mobilizzazione)
                    
            # una volta inserito i valori il controllo si chiude e non può essere modificato
            pathology_db.id_control_status= int(CONTROL_STATUS.CLOSED.value[0])
            pathology_db.date_insertion= datetime.utcnow()

            #Aggiornamento della row
            db.session.commit()

            print("SUBMITTED")
            print(form.data)
            print(form.errors)

            return redirect(url_for('doctor.calendar'))

    print("DATA INIZIO MOBILIZZAZIONE")
    print(data_inizio_mobilizzazione)
    return render_template('doctor/trattamenti/parameters_post_treatment_selection.html',
                           row_id=row_id,
                           form=form,
                           controls_map=controls_map,
                           week_to_add=week_to_add,
                           data_intervento=data_intervento,
                           data_controllo=data_controllo,
                           event_in_range=event_in_range,
                           data_inizio_mobilizzazione=data_inizio_mobilizzazione)





@doctor.route("/generate_pdf", methods=["POST"])
def generate_pdf():
    form_data = request.json  # Receive form data as JSON

    # Render the HTML template with form data
    rendered_html = render_template("general/control_pdf.html", form_data=form_data)

    # Generate the PDF
    pdf = HTML(string=rendered_html).write_pdf()

    # response = make_response(pdf)
    # response.headers["Content-Type"] = "application/pdf"
    # response.headers["Content-Disposition"] = "inline; filename=form_data.pdf"

    # Save the PDF on the server (optional)
    pdf_path = os.path.join(PDF_DIRECTORY, "generated_form_data.pdf")
    with open(pdf_path, "wb") as pdf_file:
        pdf_file.write(pdf)

    return jsonify({"message": "PDF generated", "pdf_filename": "generated_form_data.pdf"})


@doctor.route('/generate_page_pdf/<row_id>', methods=['POST'])
def generate_page_pdf(row_id):
    # Get the HTML content from the AJAX request
    data = request.get_json()
    html_content = data.get("html")

    patient_name = "Nome Paziente"
    #get currrent date
    current_date = datetime.now().strftime("%d/%m/%Y")

    #Get Patient Name
    Data= db.session.query(PathologyData.id,PathologyData.id_pathology,PathologyData.id_patient,User.name,Pathology.name)\
        .join(User,PathologyData.id_patient==User.id)\
        .join(Pathology,PathologyData.id_pathology==Pathology.id)\
        .filter(PathologyData.id == row_id).first()
                
    Id,IdPathology,IdPatient,PatientName,PathologyName= Data

    additional_html = f"""
    <div style="color: black; font-weight: bold;">
        <h1>Resoconto Terapia</h1>
        <p>Data Referto: {current_date} </p>
        <p>Nome: {PatientName} </p>
        <p>Patologia: {PathologyName} </p>
        
    </div>
    """
    full_html = additional_html +  html_content

    #print(html_content)
    print("Generate PDF")
    # Generate the PDF
    filename = f"report_{row_id}.pdf"
    pdf_path = os.path.join(PDF_DIRECTORY, filename)
    HTML(string=full_html).write_pdf(pdf_path)
    
    print("Finish PDF")
    
    # Return the filename for download
    return jsonify({"filename": filename})


from flask import Flask, send_from_directory, jsonify

@doctor.route('/download/',methods=["GET","POST"])   
def download_pdf():
    # Serve the generated PDF file for download
    return send_from_directory("static", "form.pdf", as_attachment=True)
    #return jsonify({"message": "PDF generated", "pdf_filename": "generated_form_data.pdf"})
# ROUTE DI TESTING

from wtforms.validators import DataRequired, Length,NumberRange

@doctor.route('/test_controls/',methods=["GET","POST"])
def test_controls():

    
    controls_map= {"mpcj":{"active":False,
                           "indices":[1,2]
                           }
                           ,
                   "pipj":{"active":False,
                           "indices":[3,4]
                           },
                   "dipj":{"active":False,
                           "indices":[2]
                           },
                   "ipj":{"active":False,
                           "indices":[1]
                           },
                   "polso":{"active":False,
                           "indices":[0]
                           },
                   "vas":{"active":False,
                           "indices":[0]
                           },
                   "trapezio_metacarpale":{"active":False,
                           "indices":[0]
                           },
                   "forza":{"active":False,
                           "indices":[0]
                           },
                    "dash": {"active":True,
                           "indices":[0],
                           "labels":{
                                "labels_1":[(label.value[1],label.value[0]) for label in DASH_ENUM_FIRST],
                                "labels_2":[(label.value[1],label.value[0]) for label in DASH_ENUM_SECOND],
                                "labels_3":[(label.value[1],label.value[0]) for label in DASH_ENUM_THIRD],
                                "labels_4":[(label.value[1],label.value[0]) for label in DASH_ENUM_FOURTH],
                                "labels_5":[(label.value[1],label.value[0]) for label in DASH_ENUM_FIFTH],
                                "labels_6":[(label.value[1],label.value[0]) for label in DASH_ENUM_SIXTH], 
                                }
                           },       
                    "prwhe":{"active":False,
                           "indices":[0]
                           },       
                    "eaton_littler":{"active":False,
                           "indices":[0]
                           },
                    "edema":{"active":False,
                           "indices":[0]
                           },
                    "cicatrice":{"active":False,
                           "indices":[0]
                           },           
                    "tutore":{"active":False,
                           "indices":[0]
                           },
                    "altro":{"active":False,
                           "indices":[0]
                           },
                    CONTROLS.GUARIGIONE_OSSEA.value[1]: {"active":False,
                                            "indices":[0]
                                            },
                    CONTROLS.CONCESSO_INIZIO_MOBILIZZAZIONE.value[1]: {"active":False,
                                                        "indices":[0]
                                                        },
                    CONTROLS.ARTICOLAZIONE_STABILE.value[1]: {"active":False,
                                               "indices":[0]
                                                },
                    CONTROLS.SENSIBILITA_VOLARE.value[1]: {"active":False,
                                               "indices":[0]
                                                },
                    CONTROLS.SENSIBILITA_DORSALE.value[1]: {"active":True,
                    "indices":[0]
                    }            
                   }
    
    form= TreatmentForm(controls_map=controls_map)

    if request.method == "POST":

        if form.validate_on_submit():
            
            print("VALIDATE ENTER")
            
            mpcj_data = {}
            if controls_map["mpcj"]["active"]:
                for index in controls_map["mpcj"]["indices"]:
                    # Dynamically retrieve the data for each subform
                    mpcj_data[int(index)] = {
                        'arom_estensione': form.mpcj[int(index)].arom_estensione.data,
                        'arom_flessione': form.mpcj[int(index)].arom_flessione.data,
                        'prom_estensione': form.mpcj[int(index)].prom_estensione.data,
                        'prom_flessione': form.mpcj[int(index)].prom_flessione.data
                    }

            print("MPCJ")
            print(mpcj_data)

            
            dipj_data = {}
            if controls_map["dipj"]["active"]:
                for index in controls_map["dipj"]["indices"]:
                    # Dynamically retrieve the data for each subform
                    dipj_data[int(index)] = {
                        'arom_estensione': form.dipj[int(index)].arom_estensione.data,
                        'arom_flessione': form.dipj[int(index)].arom_flessione.data,
                        'prom_estensione': form.dipj[int(index)].prom_estensione.data,
                        'prom_flessione': form.dipj[int(index)].prom_flessione.data
                    }
            print("DIPJ")
            print(dipj_data)

            
            pipj_data = {}
            if controls_map["pipj"]["active"]:
                for index in controls_map["pipj"]["indices"]:
                    # Dynamically retrieve the data for each subform
                    pipj_data[int(index)] = {
                        'arom_estensione': form.pipj[int(index)].arom_estensione.data,
                        'arom_flessione': form.pipj[int(index)].arom_flessione.data,
                        'prom_estensione': form.pipj[int(index)].prom_estensione.data,
                        'prom_flessione': form.pipj[int(index)].prom_flessione.data
                    }

            print("PIPJ")
            print(pipj_data)
            
            ipj_data = {}
            if controls_map["ipj"]["active"]:
                for index in controls_map["ipj"]["indices"]:
                    # Dynamically retrieve the data for each subform
                    ipj_data[int(index)] = {
                        'arom_estensione': form.ipj[int(index)].arom_estensione.data,
                        'arom_flessione': form.ipj[int(index)].arom_flessione.data,
                        'prom_estensione': form.ipj[int(index)].prom_estensione.data,
                        'prom_flessione': form.ipj[int(index)].prom_flessione.data
                    }

            print("IPJ")
            print(ipj_data)

            trapezio_metacarpale = {}

            if controls_map["trapezio_metacarpale"]["active"]:
                for index in controls_map["trapezio_metacarpale"]["indices"]:
                    trapezio_metacarpale[int(index)] = {
                        'anteposizione': form.trapezio_metacarpale[int(index)].anteposizione.data,
                        'abduzione': form.trapezio_metacarpale[int(index)].abduzione.data,
                        'kapandji': form.trapezio_metacarpale[int(index)].kapandji.data,
                    }
            
            print("TRAPEZIO METACARPALE")
            print(trapezio_metacarpale)


            polso={}
            if controls_map["polso"]["active"]:
                for index in controls_map["polso"]["indices"]:
                    polso[int(index)] = {
                        'arom_estensione': form.polso[int(index)].arom_estensione.data,
                        'arom_flessione': form.polso[int(index)].arom_flessione.data,
                        'prom_estensione': form.polso[int(index)].prom_estensione.data,
                        'prom_flessione': form.polso[int(index)].prom_flessione.data,
                        'arom_supinazione': form.polso[int(index)].arom_supinazione.data,
                        'arom_pronazione': form.polso[int(index)].arom_pronazione.data,
                        'prom_supinazione': form.polso[int(index)].prom_supinazione.data,
                        'prom_pronazione': form.polso[int(index)].prom_pronazione.data
                    }     

            print("POLSO")
            print(polso)

            print("VAS")
            vas_data= None
            if controls_map["vas"]["active"]:
                vas_data= form.vas.data
            print(vas_data)

            print("FORZA")
            forza={}

            if controls_map["forza"]["active"]:
                for index in controls_map["forza"]["indices"]:
                    forza[int(index)] = {
                        'key_pinch': form.forza[int(index)].key_pinch.data,
                        'tip_to_pinch': form.forza[int(index)].tip_to_pinch.data,
                        'misurazione_1_finger': form.forza[int(index)].misurazione_1_finger.data,
                        'misurazione_2_finger': form.forza[int(index)].misurazione_2_finger.data,
                        'misurazione_3_finger': form.forza[int(index)].misurazione_3_finger.data,
                        'three_fingers_pinch': form.forza[int(index)].three_fingers_pinch.data,
                        'misurazione_1_grip': form.forza[int(index)].misurazione_1_grip.data,
                        'misurazione_2_grip': form.forza[int(index)].misurazione_2_grip.data,
                        'misurazione_3_grip': form.forza[int(index)].misurazione_3_grip.data,
                        'grip': form.forza[int(index)].grip.data,
                        
                    }

            print(forza)


            print("Dash")
            dash_data= None
            if controls_map["dash"]["active"]:
                dash_data = {}
                
                for row, label in zip (form.dash.first_dash.rows,controls_map["dash"]["labels"]["labels_1"]):
                    dash_data[label[1]]=row.data["options"]
                for row, label in zip (form.dash.second_dash.rows,controls_map["dash"]["labels"]["labels_2"]):
                    dash_data[label[1]]=row.data["options"]
                for row, label in zip (form.dash.third_dash.rows,controls_map["dash"]["labels"]["labels_3"]):
                    dash_data[label[1]]=row.data["options"]
                for row, label in zip (form.dash.fourth_dash.rows,controls_map["dash"]["labels"]["labels_4"]):
                    dash_data[label[1]]=row.data["options"]
                for row, label in zip (form.dash.fifth_dash.rows,controls_map["dash"]["labels"]["labels_5"]):
                    dash_data[label[1]]=row.data["options"]
                for row, label in zip (form.dash.sixth_dash.rows,controls_map["dash"]["labels"]["labels_6"]):
                    dash_data[label[1]]=row.data["options"]
                    
                    
            print(dash_data)


            
            print("Prwhe")
            prwhe_data= None
            if controls_map["prwhe"]["active"]:
                prwhe_data = []
                for entry in form.prwhe.entries:  # Iterate over FieldList
                    prwhe_entry = {field.name: field.data for field in entry}
                    prwhe_data.append(prwhe_entry)
            print(prwhe_data)

            
            print("eaton littler")
            eaton_littler_data= None
            if controls_map["eaton_littler"]["active"]:
                eaton_littler_data= form.eaton_littler.data
            print(eaton_littler_data)


            print("edema")
            edema_data= None
            if controls_map["edema"]["active"]:
                edema_data= form.edema.data
            print(edema_data)



            print("Sensibilita volare")
            sensibilita_volare_data= None
            if controls_map["sensibilita_volare"]["active"]:
                sensibilita_volare_data= form.sensibilita_volare.data
            print(sensibilita_volare_data)


            print("Sensibilita dorsale")
            sensibilita_dorsale_data= None
            if controls_map["sensibilita_dorsale"]["active"]:
                sensibilita_dorsale_data= form.sensibilita_dorsale.data
            print(sensibilita_dorsale_data)


            cicatrice = {}

            if controls_map["cicatrice"]["active"]:
                for index in controls_map["cicatrice"]["indices"]:
                    cicatrice[int(index)] = {
                        'aderente': form.cicatrice[int(index)].aderente.data,
                        'distasi_ferita': form.cicatrice[int(index)].distasi_ferita.data,
                        'tinel': form.cicatrice[int(index)].tinel.data,
                    }
            
            print("cicatrice")
            print(cicatrice)


            print("tutore")
            tutore_data= None
            if controls_map["tutore"]["active"]:
                tutore_data= form.tutore.data
            print(tutore_data)

            print("altro")
            altro_data= {}
            if controls_map["altro"]["active"]:
                for index in controls_map["altro"]["indices"]:
                    altro_data[int(index)] = {
                        'complicanze': form.altro[int(index)].complicanze.data,
                        'note': form.altro[int(index)].note.data,

                    }
            print(altro_data)

        
        # #insert data into db
        # new_entry = PathologyData(
        #         id_doctor=1,  # Replace with the actual doctor ID
        #         id_pathology=1,  # Replace with the actual type ID
        #         id_pathology_type=1, #TODO da cambiare con id patologia
        #         id_patient=1,  # Replace with the actual patient ID
        #         id_pathology_status= PATHOLOGY_STATUS.DOPO.value[0],
        #         next_control_date=datetime.utcnow(),
        #         next_control_time= "12:00",
        #         is_date_accepted= 1,
        #         next_control_number=2, # il primo controllo ha sempre valore 0. Questo serve per recuperare il valore corretto dalla timeline
        #         id_control_status=CONTROL_STATUS.ACTIVE.value[0],  # Replace with the actual value
        #         surgery_date=datetime.utcnow(),
        #         mpcj=mpcj_data,
        #         pipj=pipj_data,
        #         dipj=dipj_data,
        #         ipj=ipj_data,
        #         polso=polso,
        #         vas=vas_data,
        #         trapezio_metacarpale=trapezio_metacarpale,
        #         forza=forza,
        #         dash=dash_data,
        #         prwhe=prwhe_data,
        #         eaton_littler=eaton_littler_data,
        #         edema=edema_data,
        #         cicatrice=cicatrice,
        #         tutore=tutore_data,
        #         altro=altro_data
        #         )
        #   # Replace with the actual value

        # db.session.add(new_entry)

        # # Commit the session to persist the changes to the database
        # db.session.commit()




    return render_template('doctor/test_controls.html',
                           form=form,
                           controls_map=controls_map) 

@doctor.route('/svg_test/',methods=["GET","POST"])
def svg_test():

    return render_template('doctor/svg_test.html')


@doctor.route('/dash_test/',methods=["GET","POST"])
def dash_test():

    form = DashFormTest()

    labels_1=[(label.value[1],label.value[0]) for label in DASH_ENUM_FIRST]
    labels_2=[(label.value[1],label.value[0]) for label in DASH_ENUM_SECOND]
    labels_3=[(label.value[1],label.value[0]) for label in DASH_ENUM_THIRD]
    labels_4=[(label.value[1],label.value[0]) for label in DASH_ENUM_FOURTH]
    labels_5=[(label.value[1],label.value[0]) for label in DASH_ENUM_FIFTH]
    labels_6=[(label.value[1],label.value[0]) for label in DASH_ENUM_SIXTH]

    results={}
    if form.validate_on_submit():
        
        for row, label in zip (form.dash.first_dash.rows,labels_1):
            print(label[1])
            print(row.data["options"])
            results[label[1]]=row.data["options"]
        
        for row, label in zip (form.dash.second_dash.rows,labels_2):
            results[label[1]]=row.data["options"]
        
        for row, label in zip (form.dash.third_dash.rows,labels_3):
            results[label[1]]=row.data["options"]

        for row, label in zip (form.dash.fourth_dash.rows,labels_4):
            results[label[1]]=row.data["options"]

        for row, label in zip (form.dash.fifth_dash.rows,labels_5):
            results[label[1]]=row.data["options"]

        for row, label in zip (form.dash.sixth_dash.rows,labels_6):
            results[label[1]]=row.data["options"]

        print(results)

    return render_template('doctor/test_dash.html',
                           form=form,
                           labels_1=labels_1,
                           labels_2=labels_2,
                           labels_3=labels_3,
                           labels_4=labels_4,
                           labels_5=labels_5,
                           labels_6=labels_6,
                           zip=zip)

