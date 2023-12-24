from flask import Blueprint, render_template,request,jsonify
from flask_login import login_required, current_user
from .internal_data import ROLE,NOTIFICATION_STATUS,PATHOLOGY,PATHOLOGY_TYPE
from .models import User,DoctorPatient,Notification
from . import db
from sqlalchemy import cast, Integer
from .doctor_forms import RizoartrosiForm

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

    patient_id = request.json.get('patient_id')
    
    new_link = Notification(id_doctor=current_user.id,
                            id_patient=patient_id,
                            status=NOTIFICATION_STATUS.SENT.value)
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

"""
Route to show all patient available

"""
@doctor.route('/patient_history/<patient_id>/<patient_name>',methods=["POST"])
@login_required
def patient_history(patient_id,patient_name):


    return render_template('patient_history.html')

# From used to setup pathology parameters
@doctor.route('/pathology/',methods=["POST"])
@login_required
def pathology():

    if request.method == 'POST':
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

      
        
    form= RizoartrosiForm()

    return render_template('doctor/patology.html',form=form)


@doctor.route('/medical_treatment/<patient_id>/<patient_name>',methods=["POST"])
@login_required
def medical_treatment(patient_id,patient_name):

    print(patient_id)

    for value in PATHOLOGY:
        print(value.value[0])
        print(value.value[1])
    return render_template('doctor/medical_treatment_selection.html',doctor_id=current_user.id,
                           patient_name=patient_name,
                           patient_id=patient_id,
                           pathology=PATHOLOGY,
                           pathology_type=PATHOLOGY_TYPE)
