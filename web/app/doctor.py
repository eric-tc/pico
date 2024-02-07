from flask import Blueprint, render_template,request,jsonify,redirect, url_for, flash,session
from flask_login import login_required, current_user
from .internal_data import ROLE,NOTIFICATION_STATUS,PATHOLOGY,CONTROL_STATUS,EMAIL_STATUS,PATHOLOGY_TYPE,DoctorData,RizoartrosiControlsTimeline,CONTROLS
from .models import User,DoctorPatient,Notification,Rizoartrosi,PathologyType,Pathology
from . import db,csrf
from sqlalchemy import cast, Integer
from .doctor_forms import RizoartrosiForm,MedicalTreatmentForm
import datetime
from datetime import datetime, timedelta,time
from .mutils import get_date,get_date_from_datetime
from werkzeug.security import generate_password_hash

from .internal_data import get_pathology_type_dict

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

    #sent_notifications= Notification.query.filter_by(id_doctor=current_user.id)

    # 2 recupero gli interventi di diversi pazienti più vicini alla data attuale
    next_treatments=[]
    for patient_query in patients_list:
        #in base all'id paziente 
        print("value")
        doctorPatient, name = patient_query
        #TODO: Qui invece di ritornare la prima data ritorno tutte le date del paziente ordinate in modo ascendete
        patients_row = db.session.query(Rizoartrosi,User.name).join(User,Rizoartrosi.id_patient==User.id).filter(Rizoartrosi.id_patient == doctorPatient.id_patient,Rizoartrosi.next_control_date>= db.func.now()).order_by(Rizoartrosi.next_control_date).all()
        #successivamente creo un ciclo for su tutte le date
        # la prima volta che trovo un id < 2(Data chiusa) fermo il ciclo for e prendo quella data
        #faccio questo per tutti i pazienti associati al dottore

        #In questo modo mostro solo gli appuntamenti non ancora conclusi e successivi alla data attuale.

        #Verfico che la row recuperata della patologia non è None
        if patients_row is not None:
            for row in patients_row:
                #trovo il prossimo controllo in linea temporale non chiuso
                if(row[0].id_control_status == CONTROL_STATUS.ACTIVE.value[0]):
                    print(row)
                    time_object = datetime.strptime(row[0].next_control_time, "%H:%M").time()
                    # Create a datetime object with today's date and the extracted time
                    row[0].next_control_date = datetime.combine(row[0].next_control_date, time_object)
                    #TODO: Dovrò controllare per tipologia di patologia. La week serve per evidenziare i giorni
                    #corretti nella modal del cambio data
                    week_to_add , check_if_last = RizoartrosiControlsTimeline.get_week(control_number = int(row[0].next_control_number))
                    row_with_week=(row[0],row[1],week_to_add)
                    next_treatments.append(row_with_week)
                    #appena trovo un controllo non chiuso interrompo il ciclo di ricerca
                    break

            
    return render_template('doctor/profile.html', 
                           name=current_user.name,
                           patients_list=patients_list, 
                           next_treatments=next_treatments)
                          

"""
Route chimata dalla tabella nella sezione profile del prossimo intervento
permette di cambiare la data dell'intervento se neccessario
"""
@doctor.route('/change_date')
@login_required
def change_date():
    """
    pathology_id_row: Corrisponde alla riga della tabella patologia in cui devo cambiare la data
    pathology_type: id della patologia. Se per ogni patologia ho una tabella diversa devo sapere a in quale tabella andare

    """

    date= request.args.get("selected_date")
    time = request.args.get("selected_time")
    pathology_id_row= request.args.get("pathology_id_row")
    pathology_type= int(request.args.get("pathology_type"))

    
    print(date)
    print(time)
    print(pathology_id_row)
    print(pathology_type)
    
    if pathology_type == PATHOLOGY.RIZOARTROSI.value[0]:
        value_to_update= Rizoartrosi.query.filter_by(id=pathology_id_row).first()
        
        value_to_update.next_control_date= datetime.strptime(str(date),"%d-%m-%Y")
        value_to_update.next_control_time= str(time)

        try:
            # Commit the changes to the database
            db.session.commit()
            flash('DATA  AGGIORNATA CORRETTAMENTE')
            # If no exception is raised, the update was successful
            return redirect(url_for('doctor.profile'))
        

        except Exception as e:
            # Handle the exception (e.g., log the error, display an error message)
            print(f"Error updating record: {e}")
            flash('DATA NON AGGIORNATA CORRETTAMENTE')
            return redirect(url_for('doctor.profile'))


    flash('DATA NON AGGIORNATA CORRETTAMENTE')
    return redirect(url_for('doctor.profile'))



"""
Ajax request to send notification to patient

"""
@doctor.route('/send_patient_notification',methods=["POST"])
@login_required
def send_patient_notification():

    print("DATA JSON")
    csrf.protect()

    print("DATA JSON")
    patient_id = request.json.get('patient_id')
    
    new_link = Notification(id_doctor=current_user.id,
                            id_patient=patient_id,
                            status=NOTIFICATION_STATUS.SENT.value[0])
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


# -------------------------ROUTE PER DEFINIRE un nuovo controllo paziente---------------------------------------------------

@doctor.route('/medical_treatment/<patient_id>/<patient_name>/',methods=["GET"])
@login_required
def medical_treatment(patient_id,patient_name):
    
    medicalForm= MedicalTreatmentForm()

    session[DoctorData.ID_PATIENT.value]=patient_id
    #Quando crea un nuovo controllo l'appuntamento successivo è sempre il secondo
    session[DoctorData.NUM_CONTROL.value]= 1

    print("PATIENT ID")
    print(session.get(DoctorData.ID_PATIENT.value))

   
    #ogni chiave rappresenta id patologia
    pathology_names_id_options,timeline_pathology = get_pathology_type_dict()

    return render_template('doctor/medical_treatment_selection.html',doctor_id=current_user.id,
                            patient_name=patient_name,
                            pathology=PATHOLOGY,
                            pathology_type=PATHOLOGY_TYPE,
                            form=medicalForm,
                            pathology_names_id_options=pathology_names_id_options,
                            timeline_pathology=timeline_pathology,
                            default_date= datetime.utcnow()
                          )

# From used to setup pathology parameters
@doctor.route('/pathology/',methods=["POST"])
@login_required
def pathology():

    form= RizoartrosiForm()
    print(f'Request Method: {request.method}')
    print(f'Form Data: {request.form}')
    print(f'Form Errors: {form.errors}')
    print(f'Form Errors: {form.validate_on_submit()}')

    if form.submit_rizoartrosi.data and form.validate_on_submit():
        print("SUBMIT RIZOARTROSI")
        # Extract form data from the request
        nprs_vas = request.form.get(CONTROLS.NPRS_VAS.value)
        prom_arom_mcpj = request.form.get(CONTROLS.PROM_APROM_MCPJ.value)
        prom_arom_Ipj = request.form.get(CONTROLS.PROM_APROM_IPJ.value)
        abduzione = request.form.get(CONTROLS.ABDUZIONE.value)
        anteposizione = request.form.get(CONTROLS.ANTEPOSIZIONE.value)
        kapandji = request.form.get(CONTROLS.KAPANDJI.value)
        pinch = request.form.get(CONTROLS.PINCH.value)
        grip = request.form.get(CONTROLS.GRIP.value)
        dash = request.form.get(CONTROLS.DASH.value)
        prwhe = request.form.get(CONTROLS.PRWHE.value)
        eaton_littler = request.form.get(CONTROLS.EATON_LITTLER.value)
        stato_cicatrice = request.form.get(CONTROLS.STATO_CICATRICE.value)
        tipo_cicatrice = request.form.get(CONTROLS.TIPO_CICATRICE.value)
        modena = request.form.get(CONTROLS.MODENA.value)

        #Controllo quale tipologia di malattia ha selezionato il dottore
        #Per ogni patologia avrò un controllo specifico
        if(PATHOLOGY.RIZOARTROSI.value[0]== int(session.get(DoctorData.ID_PATHOLOGY.value))):
            #inserimento tabella rizoartrosi
            print("inserimento rizoartrosi")

            for control_number,weeks_to_add in enumerate(RizoartrosiControlsTimeline.timeline):

                next_control_date= datetime.utcnow() + timedelta(weeks=weeks_to_add)
                next_control_time = "12:00"
                
                is_date_accepted= 0
                
                #Se il numero del controllo corrisponde al controllo successivo verifico
                # se la data del prossimo incontro è stata accettata dal paziente
                print("CONTROL NUMBER")
                print(control_number)
                if(control_number == int(session.get(DoctorData.NUM_CONTROL.value))):
                    print(control_number)

                    if(session.get(DoctorData.CONTROL_DATE.value)!=""):
                        print(session.get(DoctorData.CONTROL_DATE.value))
                        next_control_date= datetime.strptime(str(session.get(DoctorData.CONTROL_DATE.value)),"%d-%m-%Y")
                        print("DATE ACCEPTED")
                        print(next_control_date)
                        is_date_accepted=1
                        

                    if(session.get(DoctorData.CONTROL_TIME.value)!=""):
                        next_control_time= session.get(DoctorData.CONTROL_TIME.value)
                        is_date_accepted=1

                new_entry = Rizoartrosi(
                    id_doctor=current_user.id,  # Replace with the actual doctor ID
                    id_pathology=session.get(DoctorData.ID_PATHOLOGY.value,"0"),  # Replace with the actual type ID
                    id_pathology_type=session.get(DoctorData.ID_PATHOLOGY_TYPE.value,"0"), #TODO da cambiare con id patologia
                    id_patient=session.get(DoctorData.ID_PATIENT.value,"0"),  # Replace with the actual patient ID
                    next_control_date=next_control_date,
                    next_control_time= next_control_time,
                    is_date_accepted= is_date_accepted,
                    next_control_number=control_number +1,
                    id_control_status=CONTROL_STATUS.CLOSED.value[0] if control_number==0 else CONTROL_STATUS.ACTIVE.value[0],  # Replace with the actual value
                    nprs_vas=nprs_vas,  # Replace with the actual value
                    prom_aprom_mcpj=prom_arom_mcpj,  # Replace with the actual value
                    prom_aprom_ipj=prom_arom_Ipj,  # Replace with the actual value
                    abduzione=abduzione,  # Replace with the actual value
                    anteposizione=anteposizione,  # Replace with the actual value
                    kapandji=kapandji,  # Replace with the actual value
                    pinch=pinch,  # Replace with the actual value
                    grip=grip,  # Replace with the actual value
                    dash=dash,  # Replace with the actual value
                    prwhe=prwhe,  # Replace with the actual value
                    eaton_littler=eaton_littler,  # Replace with the actual value
                    tipo_cicatrice=tipo_cicatrice,  # Replace with the actual value
                    stato_cicatrice=stato_cicatrice,  # Replace with the actual value
                    modena=modena # Replace with the actual value
                )

                        # Add the instance to the session
                db.session.add(new_entry)

            # Commit the session to persist the changes to the database
            db.session.commit()

            flash('Inserimento terapia con successo')
            return redirect(url_for('doctor.profile'))


    #Questi valori arrivano dal form della pagina precedente e non dovrebbero essere sovrascritti
    # A meno che la patologia non sia inserita correttamente
    session[DoctorData.ID_PATHOLOGY.value] = request.form.get('pathology')
    session[DoctorData.ID_PATHOLOGY_TYPE.value] = request.form.get('pathology_type')
    session[DoctorData.CONTROL_DATE.value] = request.form.get("selected_date")
    session[DoctorData.CONTROL_TIME.value] = request.form.get("selected_time")

    print(request.form.get('pathology'))
    print(request.form.get('pathology_type'))

    print(request.form.get("selected_date"))
    print(request.form.get("selected_time"))
    print(f"PRIMO INTERVENTO DATA SELEZIONATA {session.get(DoctorData.CONTROL_DATE.value)}")
    print(f"PRIMO INTERVENTO TEMPO SELEZIONATA {session.get(DoctorData.CONTROL_TIME.value)}")
    
    #Quando il dottore crea il primo intervento il numero del controllo è sempre 1
    controls_map = RizoartrosiControlsTimeline.get_controls(control_number = 1)

    print(controls_map)
    
    return render_template('doctor/patology.html',form=form,controls_map=controls_map)


#---------------------------------ROUTE PER GESTIRE I CONTROLLI SUCCESSIVI DEL PAZIENTE-----------------------------
"""
row_id_to_update= rappresenta il numero della riga della colonna da aggiornare.
deafult_date= rappresenta la data di creazione del controllo. Serve per quando programmare il controllo successivo rispetto alla data
in cui è stato creato
"""
@doctor.route('/next_control/<patient_id>/<patient_name>/<next_control_number>/<row_id_to_update>/<default_date>',methods=["GET","POST"])
@login_required
def next_control(patient_id,patient_name,next_control_number,row_id_to_update,default_date):

    print(next_control_number)

    form= RizoartrosiForm()
    controls_map = RizoartrosiControlsTimeline.get_controls(control_number = next_control_number)
    #devo prendere le settimana del controllo successivo rispetto a quello che sto compilando
    week_to_add , check_if_last = RizoartrosiControlsTimeline.get_week(control_number = int(next_control_number) + 1)

    if form.submit_rizoartrosi.data and form.validate_on_submit():

        print(row_id_to_update)
        pathology_row_to_update = Rizoartrosi.query.get(row_id_to_update)
        
        #se è ultimo controllo non aggiorno la data del controllo successivo
        if(not check_if_last):
            #per trovare unicamente una row trovo id_patient,id_pathology_type, e prossimo controllo = next_control_number + 1
            pathology_row_to_update_for_next_control= Rizoartrosi.query.filter(Rizoartrosi.id_patient == pathology_row_to_update.id_patient,Rizoartrosi.id_pathology_type==pathology_row_to_update.id_pathology_type,Rizoartrosi.next_control_number==int(next_control_number)+1).first()
       
            #TODO: Per qualche motivo la data non è formattata secondo la regola del javascript
            next_date= get_date(request.form.get("selected_date"))
            next_time=request.form.get("selected_time") 
            print("NEXT DATE")
            print(next_date)
            # se la data o il tempo sono selezionati cambio rispettivamente
            # la data e l'ora del controllo successivo a quello compilato
            is_date_accepted=0
            if(next_date != ""):
                pathology_row_to_update_for_next_control.next_control_date= get_date_from_datetime(next_date)
                is_date_accepted = 1

            if(next_time != ""):
                pathology_row_to_update_for_next_control.next_control_time= request.form.get("selected_time")

            #Se la data è non null la data concordata con il paziente
            pathology_row_to_update_for_next_control.is_date_accepted = is_date_accepted

        
        #Ciclo su tutte le chiavi della controls_map e tramite sett_attr assegno i nuovi valori
        #Con questo metodo in base ai valori ritornati nella map aggiorno i campi a database
        for key in controls_map.keys():
            setattr(pathology_row_to_update, key, request.form.get(key=key))
            
        # una volta inserito i valori il controllo si chiude e non può essere modificato
        pathology_row_to_update.id_control_status= int(CONTROL_STATUS.CLOSED.value[0])
        #Aggiornamento della row
        db.session.commit()
        
        flash('Inserimento terapia con successo')
        return redirect(url_for('doctor.profile')) # if user doesn't exist or password is wrong, reload the page

    print(controls_map)

    return render_template('doctor/next_control.html',
                           controls_map=controls_map,
                           form=form,
                           patient_id=patient_id,
                           week_to_add=week_to_add, #usato per fare highlight nel calendario delle date disponibili
                           check_if_last=check_if_last,
                           default_date=default_date
                             # se è ultimo controllo devo nascondere inserimento della data e tempo. Il controllo successivo non esiste
                           )



# ------------------------------ROUTE PER MOSTRARE LA STORIA DEL PAZIENTE-------------------------------
# In ogni route devo salvare id paziente selezionato e la pathology type nella sessione
# Non passo nessun parametro nella path. passo tutti i valori in Post con il form

"""
Route per mostrare tutti i pazienti e i rispettivi trattamenti eseguiti

"""
@doctor.route('/patient_treatment_list/<patient_id>/<patient_name>',methods=["GET"])
@login_required
def patient_treatment_list(patient_id,patient_name):

    #prendo tutti i pazienti associati al dottore e mi faccio ritornare le malattie
    
    session[DoctorData.ID_PATIENT.value]= patient_id


    patients_ids = db.session.query(DoctorPatient.id_patient).filter(DoctorPatient.id_doctor == current_user.id).all()
    
    patients_id_list= [patient_id[0] for patient_id in patients_ids ]

    print(patients_id_list)

    #ciclo su tutte le tabelle delle malattie per farmi ritornare tutti gli interventi. Versione 1
    # Nella tabella doctor patient pathology recupero solo le tabelle che devo ciclare per recuperare la storia paziente

    pathology_list=(db.session.query(Rizoartrosi.id_patient,
                                     User.name,
                                     Pathology.id,
                                     Pathology.name,
                                     PathologyType.id,
                                     PathologyType.name)
    .join(Pathology, Pathology.id == Rizoartrosi.id_pathology)
    .join(PathologyType, PathologyType.id == Rizoartrosi.id_pathology_type)
    .join(User,User.id==patient_id)
    .filter(Rizoartrosi.id_patient.in_(patients_id_list), 
            Rizoartrosi.next_control_number==1).all()
    )
    
    return render_template('doctor/patient_treatment_list.html',pathology_list=pathology_list)


"""
Route to show patient history
"""
@doctor.route('/patient_history/<id_pathology>/<id_pathology_type>/',methods=["GET"])
@login_required
def patient_history(id_pathology,id_pathology_type):
    
    print(session.get(DoctorData.ID_PATIENT.value))
    
   

    print("HISTORY PATIENT")
    print(id_pathology)
    print(id_pathology_type)

    all_pathology_row = db.session.query(Rizoartrosi).filter(Rizoartrosi.id_patient == session.get(DoctorData.ID_PATIENT.value),
                                          Rizoartrosi.id_pathology==id_pathology ,
                                          Rizoartrosi.id_pathology_type== id_pathology_type).order_by(Rizoartrosi.next_control_date.asc()).all()
    
    #Associa ad ogni controllo la propria lista di controlli attivi 
    pathology_and_control_maps=[]

    for pathology_raw in all_pathology_row:

        control_map = RizoartrosiControlsTimeline.get_controls(pathology_raw.next_control_number)
        pathology_and_control_maps.append((pathology_raw,control_map))

    return render_template('patient_history.html',pathology_and_control_maps=pathology_and_control_maps,control_status_enum=CONTROL_STATUS)


"""
Questa route permette al dottore di creare istantaneamente il paziente e
associarlo senza passare dalle notifiche

"""

@doctor.route('/create_new_patient',methods=["GET"])
def create_patient():
    
    return render_template("doctor/create_new_patient.html")

"""
Il metodo post serve per gestire i dati derivati dal form
"""
@doctor.route('/create_new_patient',methods=["POST"])
def create_patient_post():

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again  
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_patient = User(email=email, name=name, password=generate_password_hash(password),role=ROLE.PATIENT.value)

    # add the new user to the database
    db.session.add(new_patient)
    db.session.commit()

    if(new_patient):
            new_link = DoctorPatient(id_doctor=current_user.id, id_patient=new_patient.id)
            db.session.add(new_link)
            db.session.commit()

    return redirect(url_for('doctor.profile'))