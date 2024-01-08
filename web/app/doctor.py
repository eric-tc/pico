from flask import Blueprint, render_template,request,jsonify,redirect, url_for, flash,session
from flask_login import login_required, current_user
from .internal_data import ROLE,NOTIFICATION_STATUS,PATHOLOGY,CONTROL_STATUS,EMAIL_STATUS,PATHOLOGY_TYPE,DoctorData,RizoartrosiControlsTimeline
from .models import User,DoctorPatient,Notification,Rizoartrosi,PathologyType,Pathology
from . import db,csrf
from sqlalchemy import cast, Integer
from .doctor_forms import RizoartrosiForm,MedicalTreatmentForm
import datetime
from datetime import datetime, timedelta

doctor = Blueprint('doctor', __name__)


@doctor.route('/profile')
@login_required
def profile():

    patients_list=(
    db.session.query(DoctorPatient, User.name)
    .join(User, DoctorPatient.id_patient == User.id)
    .filter(DoctorPatient.id_doctor == current_user.id)
    .all()
    )

    print(patients_list)
    
    #sent_notifications= Notification.query.filter_by(id_doctor=current_user.id)

    sent_notifications = (
    db.session.query(Notification, User.name)
    .join(User, Notification.id_patient == User.id)
    .filter(Notification.id_doctor == current_user.id)
    .all()
    )

    print(sent_notifications)
    return render_template('doctor/profile.html', 
                           name=current_user.name,
                           patients_list=patients_list, 
                           sent_notifications=sent_notifications)
                          


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

@doctor.route('/medical_treatment/<patient_id>/<patient_name>',methods=["GET"])
@login_required
def medical_treatment(patient_id,patient_name):
    
    medicalForm= MedicalTreatmentForm()

    session[DoctorData.ID_PATIENT.value]=patient_id

    print("PATIENT ID")
    print(session.get(DoctorData.ID_PATIENT.value))

    
    for value in PATHOLOGY:
        print(value.value[0])
        print(value.value[1])
    return render_template('doctor/medical_treatment_selection.html',doctor_id=current_user.id,
                           patient_name=patient_name,
                           pathology=PATHOLOGY,
                           pathology_type=PATHOLOGY_TYPE,
                           form=medicalForm)

# From used to setup pathology parameters
@doctor.route('/pathology/',methods=["POST"])
@login_required
def pathology():

    form= RizoartrosiForm()
   
    
    print(f'Request Method: {request.method}')
    print(f'Form Data: {request.form}')
    print(f'Form Errors: {form.errors}')
    print(f'Form Errors: {form.validate_on_submit()}')

    if form.submit_rizoartrosi.data and form.validate_on_submit():
        print("SUBMIT RIZOARTROSI")
        # Extract form data from the request
        nprs_vas = request.form.get('nprs_vas')
        prom_arom_mcpj = request.form.get('prom_arom_mcpj')
        prom_arom_Ipj = request.form.get('prom_arom_Ipj')
        abduction = request.form.get('abduction')
        anterposition = request.form.get('anterposition')
        kapandji = request.form.get('kapandji')
        pinch = request.form.get('pinch')
        grip = request.form.get('grip')
        dash = request.form.get('dash')
        prwhe = request.form.get('prwhe')
        Eaton_littler = request.form.get('Eaton_littler')
        scar_status = request.form.get('scar_status')
        scar_type = request.form.get('scar_type')

        #Controllo quale tipologia di malattia ha selezionato il dottore
        #Per ogni patologia avrò un controllo specifico
        if(PATHOLOGY.RIZOARTROSI.value[0]== int(session.get(DoctorData.ID_PATHOLOGY.value))):
            #inserimento tabella rizoartrosi
            print("inserimento rizoartrosi")

            for control_number,weeks_to_add in enumerate(RizoartrosiControlsTimeline.timeline):
                new_entry = Rizoartrosi(
                    id_doctor=current_user.id,  # Replace with the actual doctor ID
                    id_pathology=session.get(DoctorData.ID_PATHOLOGY.value,"0"),  # Replace with the actual type ID
                    id_pathology_type=session.get(DoctorData.ID_PATHOLOGY.value,"0"), #TODO da cambiare con id patologia
                    id_patient=session.get(DoctorData.ID_PATIENT.value,"0"),  # Replace with the actual patient ID
                    next_control_date=datetime.utcnow() + timedelta(weeks=weeks_to_add),
                    next_control_number=control_number +1,
                    id_control_status=CONTROL_STATUS.CLOSED.value[0] if control_number==0 else CONTROL_STATUS.ACTIVE.value[0],  # Replace with the actual value
                    nprs_vas=nprs_vas,  # Replace with the actual value
                    prom_arom_mcpj=90,  # Replace with the actual value
                    prom_arom_Ipj=85,  # Replace with the actual value
                    abduction=75,  # Replace with the actual value
                    anterposition=70,  # Replace with the actual value
                    kapandji=95,  # Replace with the actual value
                    pinch=80,  # Replace with the actual value
                    grip=90,  # Replace with the actual value
                    dash=25,  # Replace with the actual value
                    prwhe=40,  # Replace with the actual value
                    Eaton_littler=60,  # Replace with the actual value
                    scar_status='Healed',  # Replace with the actual value
                    scar_type='Normal',  # Replace with the actual value
                    modena='Some Value'  # Replace with the actual value
                )

                        # Add the instance to the session
                db.session.add(new_entry)

            # Commit the session to persist the changes to the database
            db.session.commit()

            flash('Inserimento terapia con successo')
            return redirect(url_for('doctor.profile')) # if user doesn't exist or password is wrong, reload the page

        print(nprs_vas)
        print(nprs_vas)

    #Questi valori arrivano dal form della pagina precedente e non dovrebbero essere sovrascritti
    # A meno che la patologia non sia inserita correttamente
    session[DoctorData.ID_PATHOLOGY.value] = request.form.get('pathology')
    session[DoctorData.ID_PATHOLOGY_TYPE.value] = request.form.get('pathology_type')

    return render_template('doctor/patology.html',form=form)


# ------------------------------ROUTE PER MOSTRARE LA STORIA DEL PAZIENTE-------------------------------
# In ogni route devo salvare id paziente selezionato e la pathology type nella sessione
# Non passo nessun parametro nella path. passo tutti i valori in Post con il form

"""
Route per mostrare tutti i pazienti e i rispettivi trattamenti eseguiti

"""
@doctor.route('/patient_treatment_list/<patient_id>/<patient_name>',methods=["GET"])
@login_required
def patient_treatment_list(patient_id,patient_name):

    #prendo tutti i pazienti associati al dottore e mi faccio ritornare le malattie
    
    session[DoctorData.ID_PATIENT.value]= patient_id


    patients_ids = db.session.query(DoctorPatient.id_patient).filter(DoctorPatient.id_doctor == current_user.id).all()
    
    patients_id_list= [patient_id[0] for patient_id in patients_ids ]

    print(patients_id_list)

    #ciclo su tutte le tabelle delle malattie per farmi ritornare tutti gli interventi. Versione 1
    # Nella tabella doctor patient pathology recupero solo le tabelle che devo ciclare per recuperare la storia paziente

    pathology_list=(db.session.query(Rizoartrosi.id_patient,
                                     User.name,
                                     Pathology.id,
                                     Pathology.name,
                                     PathologyType.id,
                                     PathologyType.name)
    .join(Pathology, Pathology.id == Rizoartrosi.id_pathology)
    .join(PathologyType, PathologyType.id == Rizoartrosi.id_pathology_type)
    .join(User,User.id==patient_id)
    .filter(Rizoartrosi.id_patient.in_(patients_id_list), 
            Rizoartrosi.next_control_number==1).all()
    )
    
    
    print(pathology_list)


    return render_template('doctor/patient_treatment_list.html',pathology_list=pathology_list)


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

    timeline = db.session.query(Rizoartrosi).filter(Rizoartrosi.id_patient == session.get(DoctorData.ID_PATIENT.value),
                                          Rizoartrosi.id_pathology==id_pathology ,
                                          Rizoartrosi.id_pathology_type== id_pathology_type).order_by(Rizoartrosi.next_control_date.asc()).all()

    print(timeline)
    return render_template('patient_history.html',timeline=timeline)


