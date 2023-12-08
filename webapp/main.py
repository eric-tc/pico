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


@main.route('/anagrafica')
@login_required
def anagrafica():
    return render_template('anagrafica.html', id=current_user.id)


