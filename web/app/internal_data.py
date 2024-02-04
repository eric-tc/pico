#This file handles internal data of the application

from enum import Enum
import copy
# Define an enumeration class
class ROLE(Enum):
    DOCTOR = 1
    PATIENT = 2

# Define the notification status
class NOTIFICATION_STATUS(Enum):
    SENT = (1,"Sent")
    APPROVED = (2,"Approved")
    TOELIMINATE= (3,"To be Eliminated")

#Indica se i dati di un controllo sono stati inseriti
class CONTROL_STATUS(Enum):

    ACTIVE = (1,"Active")
    CLOSED = (2,"Closed")
    EXPIRED = (3,"Expired")

class EMAIL_STATUS(Enum):

    #Email inviata al paziente per il prossimo controllo
    ACTIVE = (1,"Sent")
    #il paziente ha confermato appuntamento
    CLOSED = (2,"Confirmed")


class PATHOLOGY(Enum):
    RIZOARTROSI= (1,"Rizoartrosi")
    FRATTURA_RADIO_DISTALE= (2,"Frattura Radio Distale")
    FRATTURE_METACARPALI = (3,"Frattura Metacarpale")
    
class PATHOLOGY_TYPE(Enum):
    RIZOARTROSI_TRAPEZIECTOMIA = (1,PATHOLOGY.RIZOARTROSI.value[0],"Trapeziectomia e artoplastica in sospensione con APL")
    RIZOARTROSI_PROTESI = (2,PATHOLOGY.RIZOARTROSI.value[0],"Protesi Touch")
    RIZOARTROSI_ALTRO = (3,PATHOLOGY.RIZOARTROSI.value[0],"Altre tipologie Rizoartrosi")
    FRATTURA_RADIO_DISTALE_GESSO = (4,PATHOLOGY.FRATTURA_RADIO_DISTALE.value[0],"Gesso Chiuso")
    FRATTURA_RADIO_DISTALE_PLACCA_VITI= (5,PATHOLOGY.FRATTURA_RADIO_DISTALE.value[0],"Placca Viti")
    FRATTURA_RADIO_DISTALE_PLACCA_ALTRO= (6,PATHOLOGY.FRATTURA_RADIO_DISTALE.value[0],"Altro Frattura radio distale")
    FRATTURE_METACARPALI_GESSO = (7,PATHOLOGY.FRATTURE_METACARPALI.value[0],"Gesso Chiuso")
    FRATTURE_METACARPALI_VALVA_GESSATA = (8,PATHOLOGY.FRATTURE_METACARPALI.value[0],"Valva Gessata")
    FRATTURE_METACARPALI_TUTORE_TERMOPLASTICA = (9,PATHOLOGY.FRATTURE_METACARPALI.value[0],"Tutore Termoplastica")

def get_pathology_type_dict():

    """
    Ritorna le patologie in formato json in modo da essere utilizzate in javascript
    Esempio
    {"1": 
        {
        "name": ["Trapeziectomia e artoplastica in sospensione con APL", "Protesi Touch", "Altre tipologie Rizoartrosi"],
        "id": ["1", "2", "3"]
        }
    "2":...
    }
    """
    name_dict = {}
    id_dict = {}
    # Iterate over enum values
    for pathology_type in PATHOLOGY_TYPE:
        category = str(pathology_type.value[1])
        #Questo id è lo stesso inserito a database
        id_type = str(pathology_type.value[0])
        name = pathology_type.value[2]

        # If category already exists, append the option, otherwise create a new list
        if category in name_dict:
            name_dict[category]["name"].append(name)
            name_dict[category]["id"].append(id_type)
        else:
            name_dict[category]={}            
            name_dict[category]["name"] = [name]
            name_dict[category]["id"] = [id_type]
            
    name_dict = str(name_dict).replace("'", '"')
    return name_dict


class CONTROLS(Enum):

    NPRS_VAS = "nprs_vas"
    PROM_APROM_MCPJ = "prom_aprom_mcpj"
    PROM_APROM_IPJ = "prom_aprom_ipj"
    ABDUZIONE = "abduzione"
    ANTEPOSIZIONE = "anteposizione"
    KAPANDJI = "kapandji"
    PINCH = "pinch"
    GRIP = "grip"
    DASH = "dash"
    PRWHE = "prwhe"
    EATON_LITTLER = "eaton_littler"
    TIPO_CICATRICE = "tipo_cicatrice"
    STATO_CICATRICE= "stato_cicatrice"
    MODENA = "modena"


#--------------------------------- DEFINIZIONE DELLE TIMELINE ---------------------------------

#Definizione Timelines per le diverse patologie
#Ad ogni patologia associo una classe dove definisco per ogni controllo quali campi devono essere visualizzati
#Ogni campo corrisponde ad un valore associato al database.
    


class PathologyTimline:
    
    Controls_Map={

        CONTROLS.NPRS_VAS.value: False,
        CONTROLS.PROM_APROM_MCPJ.value: False,
        CONTROLS.PROM_APROM_IPJ.value: False,
        CONTROLS.ABDUZIONE.value: False,
        CONTROLS.ANTEPOSIZIONE.value: False,
        CONTROLS.KAPANDJI.value: False,
        CONTROLS.PINCH.value: False,
        CONTROLS.GRIP.value: False,
        CONTROLS.DASH.value: False,
        CONTROLS.PRWHE.value: False,
        CONTROLS.EATON_LITTLER.value: False,
        CONTROLS.STATO_CICATRICE.value: False,
        CONTROLS.TIPO_CICATRICE.value: False,
        CONTROLS.MODENA.value: False
    }

    @classmethod
    def setup_map_key_value(cls,control_map,control_array:list[str])->dict:

        for key in control_map.keys():
            # Check if the value of the key is present in the array
            if key in control_array:
                # Change the value in the map to True
                control_map[key] = True
        
        return control_map

    @classmethod
    def get_week(cls,control_number):
        """
        control_number: numero controllo

        ritorna il numero di settimana successive rispetto al numeroù
        di controllo richiesto
        """
        last_control_check = False
        if(control_number==0):
            return cls.timeline[0],last_control_check

        # non ho nessun controllo successivo
        if(control_number==len(cls.timeline)):
            return cls.timeline[control_number-1],True
        
        return cls.timeline[control_number-1],False

    @classmethod
    def get_controls(cls,control_number)->dict:
        """
        Ritorna la mappa per il controllo indicato in control_number
        Questa mappa serve per visualizzare nell'interfaccia grafica solo i campi
        specifici per il numero di controllo selezionato
        """
        #TODO: Da aggiungere per ogni controllo previsto dalla terapia

        
        #Non posso modificare i dati interni della mappa altrimenti per ogni utente
        #avrei una stessa struttura dati condivisa e questo non andrebbe bene
        # copio i dati in una mappa temporanera
        tmp_ControlMap = copy.deepcopy(RizoartrosiControlsTimeline.Controls_Map)

        if(int(control_number)==1):
            tmp_ControlMap= RizoartrosiControlsTimeline.setup_map_key_value(tmp_ControlMap,
                                                                            RizoartrosiControlsTimeline.first_control)
        if(int(control_number)==2):
            tmp_ControlMap= RizoartrosiControlsTimeline.setup_map_key_value(tmp_ControlMap,
                                                                            RizoartrosiControlsTimeline.second_control)
        if(int(control_number)==3):
            tmp_ControlMap= RizoartrosiControlsTimeline.setup_map_key_value(tmp_ControlMap,
                                                                            RizoartrosiControlsTimeline.third_control)

        if(int(control_number)>3):
            tmp_ControlMap= RizoartrosiControlsTimeline.setup_map_key_value(tmp_ControlMap,
                                                                            RizoartrosiControlsTimeline.third_control)
        
        return tmp_ControlMap

class FrattureRadioDistaliTimeline(PathologyTimline):
    
    #Questi sono i dati per ogni controllo
    timeline= [0,2,4,8,12,26,52,154,520,1040]

    first_control={
        CONTROLS.NPRS_VAS.value: False,
        CONTROLS.PROM_APROM_MCPJ.value: False,
        CONTROLS.PROM_APROM_IPJ.value: False,
        CONTROLS.ABDUZIONE.value: False,
        CONTROLS.ANTEPOSIZIONE.value: False,
        CONTROLS.KAPANDJI.value: False,
        CONTROLS.PINCH.value: False,
        CONTROLS.GRIP.value: False,
        CONTROLS.DASH.value: False,
        CONTROLS.PRWHE.value: False,
        CONTROLS.EATON_LITTLER.value: False,
        CONTROLS.MODENA.value: False
    }

    second_control = [
        CONTROLS.NPRS_VAS.value,
        CONTROLS.PROM_APROM_MCPJ.value,
        CONTROLS.PROM_APROM_IPJ.value,
        CONTROLS.STATO_CICATRICE.value,
        CONTROLS.TIPO_CICATRICE.value
        ]

    third_control = [
        CONTROLS.NPRS_VAS.value,
        CONTROLS.PROM_APROM_MCPJ.value,
        CONTROLS.PROM_APROM_IPJ.value,
        CONTROLS.ABDUZIONE.value,
        CONTROLS.ANTEPOSIZIONE.value,
        CONTROLS.KAPANDJI.value,
        CONTROLS.PINCH.value,
        CONTROLS.GRIP.value,
        CONTROLS.DASH.value,
        CONTROLS.PRWHE.value,
        CONTROLS.MODENA.value,
        CONTROLS.STATO_CICATRICE.value,
        CONTROLS.TIPO_CICATRICE.value,
    ]


class RizoartrosiControlsTimeline(PathologyTimline):

    #The values set number of weeks after first meeting
    #0 serve perchè al primo incontro paziente/dottore la data è quella corrente
    timeline= [0,2,6,12,26,52,154,520,1040]
    
    #quante settimane aspettare se il paziente non risponde alla mail
    waiting_weeks= 1
    
    #Ultimo Controllo
    LAST_CONTROL=9

    first_control=[
        CONTROLS.NPRS_VAS.value,
        CONTROLS.PROM_APROM_MCPJ.value,
        CONTROLS.PROM_APROM_IPJ.value,
        CONTROLS.ABDUZIONE.value,
        CONTROLS.ANTEPOSIZIONE.value,
        CONTROLS.KAPANDJI.value,
        CONTROLS.PINCH.value,
        CONTROLS.GRIP.value,
        CONTROLS.DASH.value,
        CONTROLS.PRWHE.value,
        CONTROLS.EATON_LITTLER.value,
        CONTROLS.MODENA.value
    ]


    #Questi valori rappresentano le chiavi che saranno attivate nella control MAP
    second_control = [
        CONTROLS.NPRS_VAS.value,
        CONTROLS.PROM_APROM_MCPJ.value,
        CONTROLS.PROM_APROM_IPJ.value,
        CONTROLS.STATO_CICATRICE.value,
        CONTROLS.TIPO_CICATRICE.value
    ]

    third_control = [
        CONTROLS.NPRS_VAS.value,
        CONTROLS.PROM_APROM_MCPJ.value,
        CONTROLS.PROM_APROM_IPJ.value,
        CONTROLS.ABDUZIONE.value,
        CONTROLS.ANTEPOSIZIONE.value,
        CONTROLS.KAPANDJI.value,
        CONTROLS.PINCH.value,
        CONTROLS.GRIP.value,
        CONTROLS.DASH.value,
        CONTROLS.PRWHE.value,
        CONTROLS.MODENA.value,
        CONTROLS.STATO_CICATRICE.value,
        CONTROLS.TIPO_CICATRICE.value,
    ]
    

   

"""
Chiavi utilizzate per salvare i dati nella sessione user dottore
"""

class DoctorData(Enum):
    ID_PATIENT= "id_patient"
    ID_PATHOLOGY= "id_pathology"
    ID_PATHOLOGY_TYPE= "id_pathology_type"
    CONTROL_DATE = "first_control_date"
    CONTROL_TIME = "first_control_time"
    #questa chiave tiene traccia dell'appuntamento del controllo successivo
    NUM_CONTROL = "control_number"
        
    


    

    