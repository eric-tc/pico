#Questo file contiente le querySql comuni tra paziente e dottore

from .models import PathologyData,PathologyType,Pathology,User
from .internal_data import CONTROL_STATUS, CONTROLS,RizoartrosiControlsTimeline
from . import db
from datetime import datetime

def select_next_treatments(id_patient:int, next_treatment_list):
    """
    La query passando un id paziente ritorna tutti i prossimi controlli per tipologia di intervento non chiusi
    oridinati rispetto alla data del primo controllo 
    
    """
    
    pathology_ids = [value for (value,) in db.session.query(PathologyData.id_pathology_type).filter(PathologyData.id_patient == id_patient).distinct().all()]
    
    for pathology_id_type in pathology_ids:

        print(pathology_id_type)
    
        #TODO: Qui invece di ritornare la prima data ritorno tutte le date del paziente ordinate in modo ascendete
        patients_row = db.session.query(PathologyData,User.name,PathologyType.name).join(User,PathologyData.id_patient==User.id).join(PathologyType,PathologyType.id==pathology_id_type).filter(PathologyData.id_patient == id_patient,PathologyData.id_pathology_type==pathology_id_type,PathologyData.next_control_date>= db.func.now()).order_by(PathologyData.next_control_date).all()
        
    #successivamente creo un ciclo for su tutte le date
        # la prima volta che trovo un id < 2(Data chiusa) fermo il ciclo for e prendo quella data
        #faccio questo per tutti i pazienti associati al dottore

        #In questo modo mostro solo gli appuntamenti non ancora conclusi e successivi alla data attuale.
        print(patients_row)

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
                    row_with_week=(row[0],row[1],row[2],week_to_add)
                    next_treatment_list.append(row_with_week)
                    #appena trovo un controllo non chiuso interrompo il ciclo di ricerca
                    break
    