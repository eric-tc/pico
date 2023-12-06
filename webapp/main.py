# main.py

from flask import Blueprint, render_template,request
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('profile.html', name=current_user.name)
    else:

        return render_template('login.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/anagrafica')
@login_required
def anagrafica():
    return render_template('anagrafica.html', id=current_user.id)


@main.route('/pathology')
@login_required
def patology():

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