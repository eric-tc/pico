from flask import Blueprint, render_template,request,jsonify,flash,redirect,url_for
from flask_login import login_required, current_user
from .internal_data import ROLE,NOTIFICATION_STATUS,CONTROL_STATUS,RizoartrosiControlsTimeline
from .models import User,DoctorPatient,Notification,PathologyData,PathologyType
from sqlalchemy import or_, and_
from . import db
from datetime import datetime
from .query_sql import select_next_treatments
from .settings_form import SettingsFormPatient
from werkzeug.security import generate_password_hash, check_password_hash

patient = Blueprint('patient', __name__)


"""
Route Utilizzata dal dottore per cambiare i settings del paziente
"""
@patient.route('/settings_patient_doctor/<patient_id>',methods=["GET","POST"])
@login_required
def settings_patient_doctor(patient_id):

    print("PATIENT DOCTOR SETTINGS")
    form = SettingsFormPatient()
    user_data = User.query.get(patient_id)
    
    if form.validate_on_submit():
        print(form.email.data)
        user_data.name = form.name.data
        #check if form.password.data is not empty
        if form.password.data:
            print("Password Aggiornata")
            user_data.password = generate_password_hash(form.password.data)
        user_data.phone = form.phone.data
        db.session.commit()
        flash('Cambio Dati effettuato con successo')

        return redirect(url_for('doctor.profile'))
        

    form.email.data= user_data.email
    form.name.data= user_data.name
    form.phone.data= user_data.phone
    #retrieve data from db and assign to form
    
    return render_template('patient/settings_patient.html',form=form ,name=current_user.name)
"""
Route Utilizzata dal dottore per cambiare i settings del paziente

"""

@patient.route('/settings_patient')
@login_required
def settings_patient():

    form = SettingsFormPatient()

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

        return redirect(url_for('patient.profile_patient'))
        

    form.email.data= user_data.email
    form.name.data= user_data.name
    form.phone.data= user_data.phone
    #retrieve data from db and assign to form

    return render_template('patient/settings_patient.html', name=current_user.name)


@patient.route('/profile_patient')
@login_required
def profile_patient():

    #get all notification
    current_notifications_list= db.session.query(Notification, User.name).join(User, Notification.id_doctor == User.id).filter(
        and_(
            Notification.id_patient==current_user.id,
            or_(
                Notification.status==NOTIFICATION_STATUS.SENT.value[0],
                Notification.status==NOTIFICATION_STATUS.APPROVED.value[0]
            )
        )
    ).all()

    #recupero la lista degli interventi successivi associati al paziente
    next_treatments=[]
    select_next_treatments(current_user.id,next_treatments)

    return render_template('patient/profile_patient.html', 
                           name=current_user.name,
                           current_notifications_list=current_notifications_list,
                           next_treatments=next_treatments)


"""
Ajax request to link doctor and patient
"""
@patient.route('/accept_doctor_request',methods=["POST"])
@login_required
def accept_doctor_request():

    id_doctor = request.json.get('id_doctor')
    id_notification= request.json.get('id_notification')

    try:
        # Create a new link when patient confirm doctor requests
        #update notification status
        notification_to_update= Notification.query.get(id_notification)

        if notification_to_update:

            notification_to_update.status= NOTIFICATION_STATUS.APPROVED.value[0]

            new_link = DoctorPatient(id_doctor=id_doctor, id_patient=current_user.id)
            db.session.add(new_link)
            db.session.commit()
            
            return jsonify({"success":"associato"})

        else:
            
            return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({'error': str(e)}), 500
    finally:
        db.session.close()


"""
Ajax request to link doctor and patient
"""
@patient.route('/remove_doctor_request',methods=["POST"])
@login_required
def remove_doctor_request():

    
    id_notification= request.json.get('id_notification')
    id_doctor = request.json.get('id_doctor')

    try:
        # Create a new link when patient confirm doctor requests
        #update notification status
        notification_to_update= Notification.query.get(id_notification)
        removeLinkPatientDoctor = DoctorPatient.query.filter_by(id_doctor=id_doctor, id_patient=current_user.id).first()

        if notification_to_update:

            notification_to_update.status= NOTIFICATION_STATUS.TOELIMINATE.value[0]
            db.session.delete(removeLinkPatientDoctor)
            db.session.commit()
            
            return jsonify({"success":"rimosso"})

        else:
            
            return jsonify({'error': 'notification not found'}), 404
    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({'error': str(e)}), 500
    finally:
        db.session.close()