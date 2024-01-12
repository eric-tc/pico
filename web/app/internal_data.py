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


class PATHOLOGY_TYPE(Enum):
    RIZOARTROSI_TRAPEZIECTOMIA = (1,"Trapeziectomia e artoplastica in sospensione con APL")
    RIZOARTROSI_PROTESI = (2,"Protesi Touch")
    RIZOARTROSI_ALTRO = (3,"Altro")

class RIZOARTROSI_CONTROLS(Enum):

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


class RizoartrosiControlsTimeline:

    #The values set number of weeks after first meeting
    #0 serve perchè al primo incontro paziente/dottore la data è quella corrente
    timeline= [0,2,6,12,26,52,154,520,1040]
    
    #quante settimane aspettare se il paziente non risponde alla mail
    waiting_weeks= 1

    #Mappa che tiente traccia di tutti i controlli da mostrare.
    #Questa mappa attiva o disattiva i campi nella UI in base ai controlli
    #selezionati negli array first_control, second_control ecc...

    Controls_Map={

        RIZOARTROSI_CONTROLS.NPRS_VAS.value: False,
        RIZOARTROSI_CONTROLS.PROM_APROM_MCPJ.value: False,
        RIZOARTROSI_CONTROLS.PROM_APROM_IPJ.value: False,
        RIZOARTROSI_CONTROLS.ABDUZIONE.value: False,
        RIZOARTROSI_CONTROLS.ANTEPOSIZIONE.value: False,
        RIZOARTROSI_CONTROLS.KAPANDJI.value: False,
        RIZOARTROSI_CONTROLS.PINCH.value: False,
        RIZOARTROSI_CONTROLS.GRIP.value: False,
        RIZOARTROSI_CONTROLS.DASH.value: False,
        RIZOARTROSI_CONTROLS.PRWHE.value: False,
        RIZOARTROSI_CONTROLS.EATON_LITTLER.value: False,
        RIZOARTROSI_CONTROLS.STATO_CICATRICE.value: False,
        RIZOARTROSI_CONTROLS.TIPO_CICATRICE.value: False,
        RIZOARTROSI_CONTROLS.MODENA.value: False
    }

    first_control={

        RIZOARTROSI_CONTROLS.NPRS_VAS.value: False,
        RIZOARTROSI_CONTROLS.PROM_APROM_MCPJ.value: False,
        RIZOARTROSI_CONTROLS.PROM_APROM_IPJ.value: False,
        RIZOARTROSI_CONTROLS.ABDUZIONE.value: False,
        RIZOARTROSI_CONTROLS.ANTEPOSIZIONE.value: False,
        RIZOARTROSI_CONTROLS.KAPANDJI.value: False,
        RIZOARTROSI_CONTROLS.PINCH.value: False,
        RIZOARTROSI_CONTROLS.GRIP.value: False,
        RIZOARTROSI_CONTROLS.DASH.value: False,
        RIZOARTROSI_CONTROLS.PRWHE.value: False,
        RIZOARTROSI_CONTROLS.EATON_LITTLER.value: False,
        RIZOARTROSI_CONTROLS.MODENA.value: False
    }


    second_control = [
        RIZOARTROSI_CONTROLS.NPRS_VAS.value,
        RIZOARTROSI_CONTROLS.PROM_APROM_MCPJ.value,
        RIZOARTROSI_CONTROLS.PROM_APROM_IPJ.value,
        RIZOARTROSI_CONTROLS.STATO_CICATRICE.value,
        RIZOARTROSI_CONTROLS.TIPO_CICATRICE.value
        ]
    
    first_control = [
        RIZOARTROSI_CONTROLS.NPRS_VAS.value,
        RIZOARTROSI_CONTROLS.PROM_APROM_MCPJ.value,
        RIZOARTROSI_CONTROLS.PROM_APROM_IPJ.value,
        RIZOARTROSI_CONTROLS.ABDUZIONE.value,
        RIZOARTROSI_CONTROLS.ANTEPOSIZIONE.value,
        RIZOARTROSI_CONTROLS.KAPANDJI.value,
        RIZOARTROSI_CONTROLS.PINCH.value,
        RIZOARTROSI_CONTROLS.GRIP.value,
        RIZOARTROSI_CONTROLS.DASH.value,
        RIZOARTROSI_CONTROLS.PRWHE.value,
        RIZOARTROSI_CONTROLS.MODENA.value,
        RIZOARTROSI_CONTROLS.STATO_CICATRICE.value,
        RIZOARTROSI_CONTROLS.TIPO_CICATRICE.value,

    ]

    third_control = [
        RIZOARTROSI_CONTROLS.NPRS_VAS.value,
        RIZOARTROSI_CONTROLS.PROM_APROM_MCPJ.value,
        RIZOARTROSI_CONTROLS.PROM_APROM_IPJ.value,
        RIZOARTROSI_CONTROLS.ABDUZIONE.value,
        RIZOARTROSI_CONTROLS.ANTEPOSIZIONE.value,
        RIZOARTROSI_CONTROLS.KAPANDJI.value,
        RIZOARTROSI_CONTROLS.PINCH.value,
        RIZOARTROSI_CONTROLS.GRIP.value,
        RIZOARTROSI_CONTROLS.DASH.value,
        RIZOARTROSI_CONTROLS.PRWHE.value,
        RIZOARTROSI_CONTROLS.MODENA.value,
        RIZOARTROSI_CONTROLS.STATO_CICATRICE.value,
        RIZOARTROSI_CONTROLS.TIPO_CICATRICE.value,
    ]

    get_controls=[first_control,second_control,third_control]
    

    @classmethod
    def setup_map_key_value(cls,control_map,control_array:list[str])->dict:

        for key in control_map.keys():
            # Check if the value of the key is present in the array
            if key in control_array:
                # Change the value in the map to True
                print("SET TRUE")
                control_map[key] = True
        
        return control_map


    @classmethod
    def get_controls(cls,control_number)->dict:
        #TODO: Da aggiungere per ogni controllo previsto dalla terapia
        
        #Non posso modificare i dati interni della mappa altrimenti per ogni utente
        #avrei uno stessa struttura dati condivisa e questo non andrebbe bene
        # copio i dati in una mappa temporanera
        tmp_ControlMap = copy.deepcopy(RizoartrosiControlsTimeline.Controls_Map)

        if(int(control_number)==2):
            tmp_ControlMap= RizoartrosiControlsTimeline.setup_map_key_value(tmp_ControlMap,
                                                                            RizoartrosiControlsTimeline.second_control)
        if(int(control_number)==3):
            tmp_ControlMap= RizoartrosiControlsTimeline.setup_map_key_value(tmp_ControlMap,
                                                                            RizoartrosiControlsTimeline.third_control)

        return tmp_ControlMap



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
        
    


    

    