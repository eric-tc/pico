# main.py

from flask import Blueprint, render_template,request,jsonify
from flask_login import login_required, current_user
from .internal_data import ROLE
from .models import User,DoctorPatient
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        if(current_user.role == ROLE.DOCTOR.value):
            return render_template('profile.html', name=current_user.name)
        if(current_user.role == ROLE.PATIENT.value):
            return render_template('profile_patient.html', name=current_user.name)
    else:

        return render_template('login.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/profile_patient')
@login_required
def profile_patient():
    return render_template('profile_patient.html', name=current_user.name)


@main.route('/link_patient',methods=["POST"])
@login_required
def link_patient():

    patient_id = request.json.get('patient_id')
    
   

    new_link = DoctorPatient(id_doctor=current_user.id, id_patient=patient_id)
    db.session.add(new_link)
    db.session.commit()


    if True:
        return jsonify({"success":"associato"})
    else:
        return jsonify({'error': 'User not found'}), 404

@main.route('/patients_list')
@login_required
def patients_list():

    patients_list= User.query.filter_by(role=ROLE.PATIENT.value).all()

    return render_template('patients_list.html',patients_list=patients_list)


@main.route('/anagrafica')
@login_required
def anagrafica():
    return render_template('anagrafica.html', id=current_user.id)


@main.route('/pathology')
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

    return render_template('patology.html')