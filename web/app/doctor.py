from flask import Blueprint, render_template,request,jsonify,redirect, url_for, flash,session
from flask_login import login_required, current_user
from .internal_data import ROLE,NOTIFICATION_STATUS,PATHOLOGY_KEY_SELECTION_FORM,PATHOLOGY,CONTROL_STATUS,EMAIL_STATUS,PATHOLOGY_TYPE,DoctorData,RizoartrosiControlsTimeline,CONTROLS,PATHOLOGY_STATUS
from .models import User,DoctorPatient,Notification,PathologyData,PathologyType,Pathology
from . import db,csrf
from sqlalchemy import cast, Integer,func
from .doctor_forms import RizoartrosiForm,MedicalTreatmentForm,PreTreamentForm,PostTreatmentForm
import datetime
from datetime import datetime, timedelta,time
from .mutils import get_date,get_date_from_datetime,get_pathology_enum,pathology_set_next_control,getDateInYMD
from werkzeug.security import generate_password_hash
import json
from .internal_data import get_pathology_type_dict
from .query_sql import select_next_treatments



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
    

    print(patients_list)

    #Ritorna tutti le patologie aggiunte dal dottore per le quali non è ancora stato fissato intervento
    #(pathology_row,patient_name,pathology_name)
    interventi_da_fissare= db.session.query(PathologyData,User.name,Pathology.name)\
    .join(User, PathologyData.id_patient == User.id)\
    .join(Pathology,PathologyData.id_pathology==Pathology.id)\
    .filter(PathologyData.id_doctor == current_user.id , PathologyData.id_pathology_status==PATHOLOGY_STATUS.PRIMA.value[0],PathologyData.id_control_status==CONTROL_STATUS.ACTIVE.value[0]).all()
    print("INTERVENTI DA FISSARE")
    print(interventi_da_fissare)


    # 2 recupero gli interventi di diversi pazienti più vicini alla data attuale
    next_treatments=[]
    # for patient_query in patients_list:
    #     #in base all'id paziente 
    #     print("value")
    #     doctorPatient, name = patient_query

    #     #recupero tutte le patologie a cui il paziente è associato il dottore
    #     select_next_treatments(doctorPatient.id_patient,next_treatments)


            
    return render_template('doctor/profile.html', 
                           name=current_user.name,
                           patients_list=patients_list,
                           interventi_da_fissare=interventi_da_fissare, 
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
    
    
    value_to_update= PathologyData.query.filter_by(id=pathology_id_row).first()
    
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


"""
Inserimento della patologia nella fase PRE INTERVENTO e ritorno in home

"""
@doctor.route('/parameters_pre_treatment_selection/<patient_id>/<patient_name>/<pathology_id>',methods=["GET","POST"])
@login_required
def parameters_pre_treatment_selection(patient_id,patient_name,pathology_id):

    
    print("PARAMETERS_PRE_TREATMENT_SELECTION")
    
    print(patient_id)
    print(patient_name)
    print(pathology_id)

    form= PreTreamentForm()

    controls_map=None
    
    #In base alla patologia selezionata ritorno le terapie associate a quella patologia
    for pathology in PATHOLOGY:
        if pathology.value[0] == int(pathology_id):
            controls_map= pathology.value[2].get_controls(control_number = 0)
            print("CONTROLS MAP")
            print(controls_map)
            break
    
    
    if request.method == 'POST':
        

        data_frattura = request.form.get(CONTROLS.DATA_FRATTURA.value)

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

        
        

        # Form was submitted
        # Access form data
        new_entry = PathologyData(
        id_doctor=current_user.id,
        id_pathology=pathology_id,  
        id_pathology_type=pathology_id, # Non conosco ancora il tipo di intervento che sceglierà il dottore
        id_pathology_status= PATHOLOGY_STATUS.PRIMA.value[0], 
        id_patient=patient_id,  
        next_control_date=datetime.utcnow() if data_frattura is None else data_frattura,
        next_control_time= "12:00",
        is_date_accepted= 0,
        next_control_number=0,
        id_control_status=CONTROL_STATUS.ACTIVE.value[0],  # Replace with the actual value
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
        modena=modena, # Replace with the actual value
        field1=  None,
        field2=  None,
        field3=  None,
        field4=  None,
        field5=  None,
        field6=  None,
        field7=  None
        )
        
        db.session.add(new_entry)

        # Commit the session to persist the changes to the database
        db.session.commit()

        return redirect(url_for('doctor.profile'))



    return render_template('doctor/trattamenti/parameters_pre_treatment_selection.html',doctor_id=current_user.id,
                            patient_name=patient_name,
                            patient_id=patient_id,
                            pathology=PATHOLOGY,
                            form_keys=PATHOLOGY_KEY_SELECTION_FORM,
                            form=form,
                            controls_map=controls_map
                          )



"""
Route che crea nella tabella patology data una riga con la patologia inserita

"""
@doctor.route('/insert_pre_medical_treatment/<patient_id>/<patient_name>/>',methods=["GET","POST"])
@login_required
def insert_pre_medical_treatment(patient_id,patient_name):

    print("INSERT_PRE_MEDICAL_TREATMENT")
    
    if request.method == 'POST':
        
        pathology_id = request.form.get("pathology")
        print(pathology_id)
        #in base alla patologia selezionata creo dei campi da compilare e alcuni vuoti
        # return render_template('doctor/pre_treatment/parameters_pre_treatment_selection.html',
        #                        doctor_id=current_user.id,
        #                        patient_id=patient_id,
        #                        patient_name=patient_name)

        return redirect(url_for('doctor.parameters_pre_treatment_selection', 
                        patient_id=patient_id, 
                        patient_name=patient_name, 
                        pathology_id=pathology_id))
    


    return render_template('doctor/insert_pre_medical_treatment.html',doctor_id=current_user.id,
                            patient_name=patient_name,
                            patient_id=patient_id,
                            pathology=PATHOLOGY,
                            form_keys=PATHOLOGY_KEY_SELECTION_FORM
                          )


@doctor.route('/medical_treatment/',methods=["POST"])
@login_required
def medical_treatment():


    #session.pop(DoctorData.OPTIONS_FIELD.value, None)

    medicalForm= MedicalTreatmentForm()

    # session[DoctorData.ID_PATIENT.value]=patient_id
    # #Quando crea un nuovo controllo l'appuntamento successivo è sempre il secondo
    # session[DoctorData.NUM_CONTROL.value]= 1

    # print("PATIENT ID")
    # print(session.get(DoctorData.ID_PATIENT.value))

    patient_id= request.form.get('patient_id')
    pathology_id = request.form.get('pathology_id')
    patient_name = request.form.get('patient_name')
    row_id_to_update = request.form.get('row_id')


    print(f"PATIENT ID {patient_id}")
    print(f"PATHOLOGY ID {pathology_id}")
    print(f"PATIENT NAME {patient_name}")
    print(f"ROW ID {row_id_to_update}")

    #ogni chiave rappresenta id patologia
    #pathology_names_id_options,timeline_pathology = get_pathology_type_dict()

    # ritorna la pathologia selezionata
    pathology_enum = get_pathology_enum(pathology_id)
    form= pathology_enum.value[3]()


    if form.validate_on_submit():

        
        surgery_date = getDateInYMD(request.form.get("data_intervento"))
        pathology_id_type =  request.form.get("treatment_options")

        #Aggiornamento riga patologia con la data dell'intervento
        pathology_row_to_update = PathologyData.query.get(row_id_to_update)
        #Id tipo patologia
        pathology_row_to_update.id_pathology_type= pathology_id_type        
        pathology_row_to_update.id_control_status=CONTROL_STATUS.CLOSED.value[0]
        pathology_row_to_update.surgery_date= surgery_date
        pathology_row_to_update.id_pathology_status= PATHOLOGY_STATUS.DURANTE.value[0]
        db.session.commit()

        # variabili comun a tutte le patologie
        data_prossimo_controllo=None
        orario_prossimo_controllo= None

        print(f"PATHOLOGY ID TYPE {pathology_id_type}")
        

        #Pathology_Enum è enum PATHOLOGY che contiene tutte le patologie. 
        # Il valore 2 ad esempio è RizoartrosiControlsTimeline.timeline che contiene le settimane dei controlli successivi 
        
        for control_number,weeks_to_add in enumerate(pathology_enum.value[2].getTimeline(pathology_id_type)):
            

            print(weeks_to_add)
            #indica se è stata concordata la data con il paziente
                    
            data_prossimo_controllo,orario_prossimo_controllo,is_date_accepted= pathology_set_next_control(request,control_number,weeks_to_add)

            # I valori dei parametri sono tutti a None perchè il dottore li dovrà inserire al momento del controllo
            new_entry = PathologyData(
                id_doctor=current_user.id,  # Replace with the actual doctor ID
                id_pathology=pathology_id,  # Replace with the actual type ID
                id_pathology_type=pathology_id_type, #TODO da cambiare con id patologia
                id_patient=patient_id,  # Replace with the actual patient ID
                id_pathology_status= PATHOLOGY_STATUS.DOPO.value[0],
                next_control_date=data_prossimo_controllo,
                next_control_time= orario_prossimo_controllo,
                is_date_accepted= is_date_accepted,
                next_control_number=control_number, # il primo controllo ha sempre valore 0. Questo serve per recuperare il valore corretto dalla timeline
                id_control_status=CONTROL_STATUS.ACTIVE.value[0],  # Replace with the actual value
                surgery_date=surgery_date,
                nprs_vas=None,  # Replace with the actual value
                prom_aprom_mcpj=None,  # Replace with the actual value
                prom_aprom_ipj=None,  # Replace with the actual value
                abduzione=None,  # Replace with the actual value
                anteposizione=None,  # Replace with the actual value
                kapandji=None,  # Replace with the actual value
                pinch=None,  # Replace with the actual value
                grip=None,  # Replace with the actual value
                dash=None,  # Replace with the actual value
                prwhe=None,  # Replace with the actual value
                eaton_littler=None,  # Replace with the actual value
                tipo_cicatrice=None,  # Replace with the actual value
                stato_cicatrice=None,  # Replace with the actual value
                modena=None, # Replace with the actual value
                field1= row_id_to_update,
                field2= None,
                field3= None,
                field4= None,
                field5= None,
                field6= None,
                field7= None
                )
        

                    # Add the instance to the session
            db.session.add(new_entry)

        # Commit the session to persist the changes to the database
        db.session.commit()

        flash('Inserimento terapia con successo')
        return redirect(url_for('doctor.profile'))
            

    


    return render_template(f'doctor/pathologies/{pathology_enum.value[1]}.html',
                           doctor_id=current_user.id,
                           patient_id=patient_id,
                           pathology_id=pathology_id,
                           patient_name=patient_name,
                           row_id=row_id_to_update,
                           form=form,
                           week_to_add=pathology_enum.value[2].weeks_to_first_control)

    # return render_template(f'doctor/{template_to_render}.html',doctor_id=current_user.id,
    #                         patient_name=patient_name,
    #                         pathology=PATHOLOGY,
    #                         pathology_type=PATHOLOGY_TYPE,
    #                         form_keys=PATHOLOGY_KEY_SELECTION_FORM,
    #                         form=medicalForm,
    #                         pathology_names_id_options=pathology_names_id_options,
    #                         timeline_pathology=timeline_pathology,
    #                         default_date= datetime.utcnow()
    #                       )



# From used to setup pathology parameters
@doctor.route('/pathology/',methods=["POST"])
@login_required
def pathology():

    form= RizoartrosiForm()
    print(f'Request Method: {request.method}')
    print(f'Form Data: {request.form}')
    print(f'Form Errors: {form.errors}')
    print(f'Form Errors: {form.validate_on_submit()}')

    session_value = session.get(DoctorData.ID_PATIENT.value, None)
    print(session_value)
    
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
            
            session_value = session.get(DoctorData.OPTIONS_FIELD.value, None)
            print("session Value")

           

            new_entry = PathologyData(
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
                modena=modena, # Replace with the actual value
                field1= json.dumps(session_value[0]) if 0 < len(session_value)  else None,
                field2= json.dumps(session_value[1]) if 1 < len(session_value)  else None,
                field3= json.dumps(session_value[2]) if 2 < len(session_value)  else None,
                field4= json.dumps(session_value[3]) if 3 < len(session_value)  else None,
                field5= json.dumps(session_value[4]) if 4 < len(session_value)  else None,
                field6= json.dumps(session_value[5]) if 5 < len(session_value)  else None,
                field7= json.dumps(session_value[6]) if 6 < len(session_value)  else None
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

    print("FRATTURE METACARPALI")

    for key in PATHOLOGY_KEY_SELECTION_FORM:
        
        if(request.form.get(key.value)):

            if(DoctorData.OPTIONS_FIELD.value in session):
                session[DoctorData.OPTIONS_FIELD.value].append({key.value : request.form.get(key.value)})
            else:
                session[DoctorData.OPTIONS_FIELD.value]=[{key.value : request.form.get(key.value)}]

    print("array valori opzionali")
    print (session[DoctorData.OPTIONS_FIELD.value])


    # print(request.form.get("fratture_metacarpali_step1_valore"))
    # print(request.form.get("fratture_metacarpali_classificazione_radiografica_value"))

    

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
        pathology_row_to_update = PathologyData.query.get(row_id_to_update)
        
        #se è ultimo controllo non aggiorno la data del controllo successivo
        if(not check_if_last):
            #per trovare unicamente una row trovo id_patient,id_pathology_type, e prossimo controllo = next_control_number + 1
            pathology_row_to_update_for_next_control= PathologyData.query.filter(PathologyData.id_patient == pathology_row_to_update.id_patient,PathologyData.id_pathology_type==pathology_row_to_update.id_pathology_type,PathologyData.next_control_number==int(next_control_number)+1).first()
       
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

    pathology_list=(db.session.query(PathologyData.id_patient,
                                     User.name,
                                     Pathology.id,
                                     Pathology.name,
                                     PathologyType.id,
                                     PathologyType.name)
    .join(Pathology, Pathology.id == PathologyData.id_pathology)
    .join(PathologyType, PathologyType.id == PathologyData.id_pathology_type)
    .join(User,User.id==patient_id)
    .filter(PathologyData.id_patient.in_(patients_id_list), 
            PathologyData.next_control_number==1).all()
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

    all_pathology_row = db.session.query(PathologyData).filter(PathologyData.id_patient == session.get(DoctorData.ID_PATIENT.value),
                                          PathologyData.id_pathology==id_pathology ,
                                          PathologyData.id_pathology_type== id_pathology_type).order_by(PathologyData.next_control_date.asc()).all()
    
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
@login_required
def create_patient():
    
    return render_template("doctor/create_new_patient.html")

"""
Il metodo post serve per gestire i dati derivati dal form
"""
@doctor.route('/create_new_patient',methods=["POST"])
@login_required
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


# CALENDARIO TRATTAMENTI POST OPERATORIO

@doctor.route('/calendar',methods=["GET"])
@login_required
def calendar():

    #Abilitano click su evento del calendario
    days_before=20
    days_after=20
    return render_template("doctor/trattamenti/calendar.html",
                           days_before=days_before,
                           days_after=days_after)


# Ritorna tutti i trattamenti di tutti i pazienti associati a quel dottore.
# Posso usare questi campi per popolare il calendario con diversi filtri
@doctor.route('/treatments_events')
def get_events():
    
    #Prendo solo gli eventi entro tot mesi. Per rendere la query più veloce

    today = datetime.today()

    # 3 Mesi
    months_to_retrieve=3
    date_after_x_months = today + timedelta(days=months_to_retrieve*30)

    treatments= db.session.query(PathologyData,User.name,Pathology.name)\
    .join(User,PathologyData.id_patient==User.id)\
    .join(Pathology,PathologyData.id_pathology==Pathology.id)\
    .filter(PathologyData.id_doctor == current_user.id,
            PathologyData.id_pathology_status==PATHOLOGY_STATUS.DOPO.value[0],
            PathologyData.next_control_date<date_after_x_months).all()
    
    events=[]

    #LEGENDA COLORI
    """
    isDateAccepted=0 -> colore grigio
    isDateAccepted=1 -> colore verde
    eventoPassato -> colore rosso

    """
    for treatment in treatments:
        event_dict={}

        pathology_row,patient_name,pathology_name = treatment
        #patient_name = "test"
        #pathology_name = "pathology_name"
        event_dict["title"]= f"{patient_name} - {pathology_name}- {pathology_row.next_control_number}° controllo - {pathology_row.next_control_time}"
        event_dict["start"]= pathology_row.next_control_date.strftime("%Y-%m-%d") + "T" + pathology_row.next_control_time
        event_dict["id"]= pathology_row.id
        

        if(pathology_row.is_date_accepted==0):
            event_dict["color"]= "#D3D3D3" 
        elif(pathology_row.is_date_accepted==1):
            event_dict["color"]= "#00FF00"

        events.append(event_dict)

    print(len(events))    

    return jsonify(events)

@doctor.route('/next_controls/<row_id>/<event_in_range>')
@login_required
def event_details(row_id,event_in_range):
    """
    row_id : id della riga della tabella patology_data
    event_in_range: indica se l'evento è nel range di compilazione
    """
    print(row_id)
    print("EVENT IN RANGE")
    print(event_in_range)

    form= PostTreatmentForm()

    controls_map=None
    week_to_add=None
    # Serve per impostare il valore di default per poi aggiungere le settimane
    data_intervento=None
    data_controllo=None
    pathology_db = db.session.query(PathologyData).filter(PathologyData.id==row_id).first()

    
    #In base alla patologia selezionata ritorno le terapie associate a quella patologia
    for pathology in PATHOLOGY:
        if pathology.value[0] == int(pathology_db.id_pathology):

            controls_map= pathology.value[2].get_next_control(control_number = pathology_db.next_control_number,
                                                          tipo_intervento=pathology_db.id_pathology_type)
            
            timeline= pathology.value[2].getTimeline(str(pathology_db.id_pathology_type))    
            
            print(f"TIMELINE {timeline}")

            week_to_add= timeline[pathology_db.next_control_number]
            
            
            data_intervento= pathology_db.surgery_date
            data_controllo= pathology_db.next_control_date
            print(controls_map)
            print(week_to_add)
            print(data_intervento)
            print(data_controllo)
            break
    
    # Siccome alcune patologie possono avere un decorso diverso devo tenere in considerazione anche il pathology type
    

    if form.is_submitted():

        #Verifico se utente ha cambiato data e ora del controllo successivo
        if form.submit_change_date.data:
            
            return redirect(url_for('doctor.calendar'))
        if form.submit_form.data:
            print("SUBMITTED")
            print(form.data)
            print(form.errors)

            return redirect(url_for('doctor.calendar'))

    return render_template('doctor/trattamenti/parameters_post_treatment_selection.html',
                           row_id=row_id,
                           form=form,
                           controls_map=controls_map,
                           week_to_add=week_to_add,
                           data_intervento=data_intervento,
                           data_controllo=data_controllo,
                           event_in_range=event_in_range)