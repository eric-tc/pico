# main.py

from flask import Blueprint, render_template,request,jsonify,redirect,url_for
from flask_login import login_required, current_user
from .internal_data import ROLE,CONTROL_STATUS,RizoartrosiControlsTimeline
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

    print("INDEX")
    if current_user.is_authenticated:
        print("INDEX")
        if(current_user.role == ROLE.DOCTOR.value):
            return redirect(url_for('doctor.profile'))
        if(current_user.role == ROLE.PATIENT.value):
            return redirect(url_for('patient.profile_patient'))

        return redirect(url_for('auth.login'))
    else:
        return redirect(url_for('auth.login'))


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

    return render_template("notification_list.html",sent_notifications=sent_notifications)


#pagina che mostra i valori del controllo per ogni singolo intervento
@main.route("/show_history_control_value/<control_value>/")
@login_required
def show_history_control_value(control_value):
    
    print(control_value)

    controls_map = RizoartrosiControlsTimeline.get_controls(control_number = int(control_value.next_control_number))

    return render_template("show_history_control_value.html",control_value=control_value,controls_map=controls_map)