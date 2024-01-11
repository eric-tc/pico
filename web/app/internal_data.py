#This file handles internal data of the application

from enum import Enum

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
    CICATRICE = "cicatrice"
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
        RIZOARTROSI_CONTROLS.CICATRICE.value: False,
        RIZOARTROSI_CONTROLS.MODENA.value: False
    }


    
    first_control = [
        RIZOARTROSI_CONTROLS.NPRS_VAS.value,
        RIZOARTROSI_CONTROLS.PROM_APROM_MCPJ.value,
        RIZOARTROSI_CONTROLS.PROM_APROM_IPJ.value,
        RIZOARTROSI_CONTROLS.CICATRICE.value
        ]
    
    second_control = [
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
        RIZOARTROSI_CONTROLS.CICATRICE.value,

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
        RIZOARTROSI_CONTROLS.CICATRICE.value,

    ]

    get_controls=[first_control,second_control,third_control]

    def __init__(self) -> None:
        pass
    
    def get_controls(self,control_number)->dict:
        #TODO: Da aggiungere per ogni controllo previsto dalla terapia
        if(control_number==1):
            for key in RizoartrosiControlsTimeline.Controls_Map:
            # Check if the value of the key is present in the array
                if key in RizoartrosiControlsTimeline.first_control:
                    # Change the value in the map to True
                    RizoartrosiControlsTimeline.Controls_Map[key] = True
                     
            return RizoartrosiControlsTimeline.Controls_Map[key]



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
        
    


    

    