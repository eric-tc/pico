from flask import Blueprint, render_template,request,jsonify
from flask_login import login_required, current_user
from .internal_data import ROLE
from .models import User,DoctorPatient
from . import db

patient = Blueprint('patient', __name__)


@patient.route('/profile_patient')
@login_required
def profile_patient():
    return render_template('profile_patient.html', name=current_user.name)