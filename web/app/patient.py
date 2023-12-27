from flask import Blueprint, render_template,request,jsonify
from flask_login import login_required, current_user
from .internal_data import ROLE,NOTIFICATION_STATUS
from .models import User,DoctorPatient,Notification
from sqlalchemy import or_, and_
from . import db

patient = Blueprint('patient', __name__)


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

    print(len(current_notifications_list))

    return render_template('patient/profile_patient.html', name=current_user.name,current_notifications_list=current_notifications_list)


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