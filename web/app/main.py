# main.py

from flask import Blueprint, render_template,request,jsonify
from flask_login import login_required, current_user
from .internal_data import ROLE
from .models import User,Notification
from . import db,csrf
main = Blueprint('main', __name__)

"""
PROBLEMI

1) Quando seleziono il pulsante accetta o rimuovi, il pulsante dopo il click non si aggiorna in automatico
2) Verifica se un paziente può accedere agli URL del dottore e viceversa
NEW FEATURE
1) Quando il medico genera il primo trattaemento di default creare tutti i trattamenti successivi e controlli per il 
paziente OK
2) Creare una tabella lato dottore per visualizzare i prossimi trattamenti OK
3) Creare una cronistoria del paziente WORK IN PROGRESS -> Grafica OK manca la visualizzazione dei trattamenti
4) Qunado un dottore inserisce un trattamento, quelli successivi a quale dottore/fisioterapista sono assegnati. Sono assegnati in modo automatico?


Feature 12/01/2024

1) Finire la gestione dei diversi controlli tramite MAP. Manca da inserire i controlli 2,3 OK
2) Inserimento a Database del valore del controllo. Cambio di stato del controllo OK
3) Inserimento del controllo successivo a database con gestione dinamica delle chiavi tramite map OK
4) Visualizzazione nella dashboard del dottore nuovo controllo più vicinio non già chiuso.(il controllo si chiude quando inserisco i dati e non posso più modificarli)
    (Devo capire se una query può recuperare la data successiva verificando un campo)
"""

@main.route('/')
def index():
    if current_user.is_authenticated:
        if(current_user.role == ROLE.DOCTOR.value):
            return render_template('doctor/profile.html', name=current_user.name)
        if(current_user.role == ROLE.PATIENT.value):
            return render_template('patient/profile_patient.html', name=current_user.name)
        
        #TODO: Probabilmente devo rimuovere la sottoscrizione
        return render_template('auth/login.html')
    else:

        return render_template('auth/login.html')


@main.route('/anagrafica')
@login_required
def anagrafica():
    return render_template('anagrafica.html', id=current_user.id)


# Route to get the CSRF token for AJAX requests
@main.route('/get_csrf_token', methods=['GET'])
def get_csrf_token():
    token = csrf._get_csrf_token()
    return jsonify({'csrf_token': token})


@main.route("/show_notifications")
@login_required
def show_notifications():

    sent_notifications = (
    db.session.query(Notification, User.name)
    .join(User, Notification.id_patient == User.id)
    .filter(Notification.id_doctor == current_user.id)
    .all()
    )

    return render_template("notification.html",sent_notifications=sent_notifications)