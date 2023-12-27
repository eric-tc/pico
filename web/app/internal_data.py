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
    timeline= [0,2,6,12,26,52,154,520.,1040]
    
    #quante settimane aspettare se il paziente non risponde alla mail
    waiting_weeks= 1
    
    first_control = [
        RIZOARTROSI_CONTROLS.NPRS_VAS,
        RIZOARTROSI_CONTROLS.PROM_APROM_MCPJ,
        RIZOARTROSI_CONTROLS.PROM_APROM_IPJ,
        RIZOARTROSI_CONTROLS.CICATRICE
        ]
    
    second_control = [
        RIZOARTROSI_CONTROLS.NPRS_VAS,
        RIZOARTROSI_CONTROLS.PROM_APROM_MCPJ,
        RIZOARTROSI_CONTROLS.PROM_APROM_IPJ,
        RIZOARTROSI_CONTROLS.ABDUZIONE,
        RIZOARTROSI_CONTROLS.ANTEPOSIZIONE,
        RIZOARTROSI_CONTROLS.KAPANDJI,
        RIZOARTROSI_CONTROLS.PINCH,
        RIZOARTROSI_CONTROLS.GRIP,
        RIZOARTROSI_CONTROLS.DASH,
        RIZOARTROSI_CONTROLS.PRWHE,
        RIZOARTROSI_CONTROLS.MODENA,
        RIZOARTROSI_CONTROLS.CICATRICE,

    ]

    third_control = [
        RIZOARTROSI_CONTROLS.NPRS_VAS,
        RIZOARTROSI_CONTROLS.PROM_APROM_MCPJ,
        RIZOARTROSI_CONTROLS.PROM_APROM_IPJ,
        RIZOARTROSI_CONTROLS.ABDUZIONE,
        RIZOARTROSI_CONTROLS.ANTEPOSIZIONE,
        RIZOARTROSI_CONTROLS.KAPANDJI,
        RIZOARTROSI_CONTROLS.PINCH,
        RIZOARTROSI_CONTROLS.GRIP,
        RIZOARTROSI_CONTROLS.DASH,
        RIZOARTROSI_CONTROLS.PRWHE,
        RIZOARTROSI_CONTROLS.MODENA,
        RIZOARTROSI_CONTROLS.CICATRICE,

    ]

    get_controls=[first_control,second_control,third_control]



"""
Chiavi utilizzate per salvare i dati nella sessione user dottore
"""

class DoctorData(Enum):
    ID_PATIENT= "id_patient"
    ID_PATHOLOGY= "id_pathology"
    ID_PATHOLOGY_TYPE= "id_pathology_type"
        
    


    

    