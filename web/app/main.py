# main.py

from flask import Blueprint, render_template,request,jsonify
from flask_login import login_required, current_user
from .internal_data import ROLE
from .models import User,DoctorPatient
from . import db

main = Blueprint('main', __name__)

"""
PROBLEMI

1) Quando seleziono il pulsante accetta o rimuovi, il pulsante dopo il click non si aggiorna in automatico
2) Verifica se un paziente può accedere agli URL del dottore e viceversa
NEW FEATURE
1) Quando il medico genera il primo trattaemento di default creare tutti i trattamenti successivi e controlli per il 
paziente
2) Creare una tabella lato dottore per visualizzare i prossimi trattamenti
3) Creare una cronistoria del paziente

"""

@main.route('/')
def index():
    if current_user.is_authenticated:
        if(current_user.role == ROLE.DOCTOR.value):
            return render_template('doctor/profile.html', name=current_user.name)
        if(current_user.role == ROLE.PATIENT.value):
            return render_template('patient/profile_patient.html', name=current_user.name)
    else:

        return render_template('auth/login.html')


@main.route('/anagrafica')
@login_required
def anagrafica():
    return render_template('anagrafica.html', id=current_user.id)


