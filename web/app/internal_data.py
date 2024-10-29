#This file handles internal data of the application

from enum import Enum
import copy
from .doctor_chirurgico_forms import RizoartrosiChirurgicoForm,FratturaRadioDistaleForm,FratturaMetaCarpaliForm
from .internal_data_enum_pathologies import FrattureMetaCarpaliEnum


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

class CONTROLS(Enum):

    DATA_FRATTURA= "data_frattura"
    MPCJ = "mpcj"
    PIPJ = "pipj"
    DIPJ = "dipj"
    IPJ = "ipj"
    POLSO = "polso"
    VAS = "vas"
    TRAPEZIO_METACARPALE = "trapezio_metacarpale"
    FORZA = "forza"
    DASH = "dash"
    PRWHE = "prwhe"
    EATON_LITTLER = "eaton_littler"
    EDEMA = "edema"
    CICATRICE = "cicatrice"
    TUTORE= "tutore"
    ALTRO = "altro"

class CONTROLSNUMBER(Enum):
    ONE = (1,"one")
    TWO = (2,"two")
    THREE = (3,"three")
    FOUR= (4,"four")
    FIVE= (5,"five")
    SIX= (6,"six")
    SEVEN= (7,"seven")
    EIGHT= (8,"eight")
    NINE= (9,"nine")
    TEN= (10,"ten")
    next= (11,"next")

#--------------------------------- DEFINIZIONE DELLE TIMELINE ---------------------------------

#Definizione Timelines per le diverse patologie
#Ad ogni patologia associo una classe dove definisco per ogni controllo quali campi devono essere visualizzati
#Ogni campo corrisponde ad un valore associato al database.
    


class PathologyTimline:
    
    Controls_Map={
        CONTROLS.DATA_FRATTURA.value: {"active":False,
                           "indices":[0]
                           },
        CONTROLS.MPCJ.value: {"active":False,
                           "indices":[0]
                           },
        CONTROLS.PIPJ.value: {"active":False,
                           "indices":[0]
                           },
        CONTROLS.DIPJ.value: {"active":False,
                           "indices":[0]
                           },
        CONTROLS.IPJ.value: {"active":False,
                           "indices":[0]
                           },
        CONTROLS.POLSO.value: {"active":False,
                           "indices":[0]
                           },
        CONTROLS.VAS.value: {"active":False,
                           "indices":[0]
                           },
        CONTROLS.TRAPEZIO_METACARPALE.value: {"active":False,
                           "indices":[0]
                           },
        CONTROLS.FORZA.value: {"active":False,
                           "indices":[0]
                           },
        CONTROLS.DASH.value: {"active":False,
                           "indices":[0]
                           },
        CONTROLS.PRWHE.value: {"active":False,
                           "indices":[0]
                           },
        CONTROLS.EATON_LITTLER.value: {"active":False,
                           "indices":[0]
                           },
        CONTROLS.EDEMA.value: {"active":False,
                           "indices":[0]
                           },
        CONTROLS.CICATRICE.value: {"active":False,
                           "indices":[0]
                           },
        CONTROLS.TUTORE.value: {"active":False,
                           "indices":[0]
                           },
        CONTROLS.ALTRO.value: {"active":False,
                           "indices":[0]
                           }
    }

    pre_treatment_controls=None


    @classmethod
    def process_parameters(cls, controls_map,form):
        """
        Funzione usata per processare i parametri passati dal form e renderli nel formato adatto 
        per il database

        controls_map: mappa aggiornata con i valori attivi per il controllo specifico
        form: data del form passato
        """

        mpcj_data = {}
        if controls_map["mpcj"]["active"]:
            for index in controls_map["mpcj"]["indices"]:
                # Dynamically retrieve the data for each subform
                mpcj_data[int(index)] = {
                    'arom_estensione': form.mpcj_list[int(index)].arom_estensione.data,
                    'arom_flessione': form.mpcj_list[int(index)].arom_flessione.data,
                    'prom_estensione': form.mpcj_list[int(index)].prom_estensione.data,
                    'prom_flessione': form.mpcj_list[int(index)].prom_flessione.data
                }

        print("MPCJ")
        print(mpcj_data)

        
        dipj_data = {}
        if controls_map["dipj"]["active"]:
            for index in controls_map["dipj"]["indices"]:
                # Dynamically retrieve the data for each subform
                dipj_data[int(index)] = {
                    'arom_estensione': form.dipj_list[int(index)].arom_estensione.data,
                    'arom_flessione': form.dipj_list[int(index)].arom_flessione.data,
                    'prom_estensione': form.dipj_list[int(index)].prom_estensione.data,
                    'prom_flessione': form.dipj_list[int(index)].prom_flessione.data
                }
        print("DIPJ")
        print(dipj_data)

        
        pipj_data = {}
        if controls_map["pipj"]["active"]:
            for index in controls_map["pipj"]["indices"]:
                # Dynamically retrieve the data for each subform
                pipj_data[int(index)] = {
                    'arom_estensione': form.pipj_list[int(index)].arom_estensione.data,
                    'arom_flessione': form.pipj_list[int(index)].arom_flessione.data,
                    'prom_estensione': form.pipj_list[int(index)].prom_estensione.data,
                    'prom_flessione': form.pipj_list[int(index)].prom_flessione.data
                }

        print("PIPJ")
        print(pipj_data)
        
        ipj_data = {}
        if controls_map["ipj"]["active"]:
            for index in controls_map["ipj"]["indices"]:
                # Dynamically retrieve the data for each subform
                ipj_data[int(index)] = {
                    'arom_estensione': form.ipj_list[int(index)].arom_estensione.data,
                    'arom_flessione': form.ipj_list[int(index)].arom_flessione.data,
                    'prom_estensione': form.ipj_list[int(index)].prom_estensione.data,
                    'prom_flessione': form.ipj_list[int(index)].prom_flessione.data
                }

        print("IPJ")
        print(ipj_data)

        trapezio_metacarpale = {}

        if controls_map["trapezio_metacarpale"]["active"]:
            for index in controls_map["trapezio_metacarpale"]["indices"]:
                trapezio_metacarpale[int(index)] = {
                    'anteposizione': form.trapezio_metacarpale[int(index)].anteposizione.data,
                    'abduzione': form.trapezio_metacarpale[int(index)].abduzione.data,
                    'kapandji': form.trapezio_metacarpale[int(index)].kapandji.data,
                }
        
        print("TRAPEZIO METACARPALE")
        print(trapezio_metacarpale)


        polso={}
        if controls_map["polso"]["active"]:
            for index in controls_map["polso"]["indices"]:
                polso[int(index)] = {
                    'arom_estensione': form.polso[int(index)].arom_estensione.data,
                    'arom_flessione': form.polso[int(index)].arom_flessione.data,
                    'prom_estensione': form.polso[int(index)].prom_estensione.data,
                    'prom_flessione': form.polso[int(index)].prom_flessione.data,
                    'arom_supinazione': form.polso[int(index)].arom_supinazione.data,
                    'arom_pronazione': form.polso[int(index)].arom_pronazione.data,
                    'prom_supinazione': form.polso[int(index)].prom_supinazione.data,
                    'prom_pronazione': form.polso[int(index)].prom_pronazione.data
                }     

        print("POLSO")
        print(polso)

        print("VAS")
        vas_data= None
        if controls_map["vas"]["active"]:
            vas_data= form.vas.data
        print(vas_data)

        print("FORZA")
        forza={}

        if controls_map["forza"]["active"]:
            for index in controls_map["forza"]["indices"]:
                forza[int(index)] = {
                    'key_pinch': form.forza[int(index)].key_pinch.data,
                    'tip_to_pinch': form.forza[int(index)].tip_to_pinch.data,
                    'misurazione_1_finger': form.forza[int(index)].misurazione_1_finger.data,
                    'misurazione_2_finger': form.forza[int(index)].misurazione_2_finger.data,
                    'misurazione_3_finger': form.forza[int(index)].misurazione_3_finger.data,
                    'three_fingers_pinch': form.forza[int(index)].three_fingers_pinch.data,
                    'misurazione_1_grip': form.forza[int(index)].misurazione_1_grip.data,
                    'misurazione_2_grip': form.forza[int(index)].misurazione_2_grip.data,
                    'misurazione_3_grip': form.forza[int(index)].misurazione_3_grip.data,
                    'grip': form.forza[int(index)].grip.data,
                    
                }

        print(forza)


        print("Dash")
        dash_data= None
        if controls_map["dash"]["active"]:
            dash_data= form.dash.data
        print(dash_data)


        
        print("Prwhe")
        prwhe_data= None
        if controls_map["prwhe"]["active"]:
            prwhe_data= form.prwhe.data
        print(prwhe_data)

        
        print("eaton littler")
        eaton_littler_data= None
        if controls_map["eaton_littler"]["active"]:
            eaton_littler_data= form.eaton_littler.data
        print(eaton_littler_data)


        print("edema")
        edema_data= None
        if controls_map["edema"]["active"]:
            edema_data= form.edema.data
        print(edema_data)


        cicatrice = {}

        if controls_map["cicatrice"]["active"]:
            for index in controls_map["cicatrice"]["indices"]:
                cicatrice[int(index)] = {
                    'aderente': form.cicatrice[int(index)].aderente.data,
                    'distasi_ferita': form.cicatrice[int(index)].distasi_ferita.data,
                    'tinel': form.cicatrice[int(index)].tinel.data,
                }
        
        print("cicatrice")
        print(cicatrice)


        print("tutore")
        tutore_data= None
        if controls_map["tutore"]["active"]:
            tutore_data= form.tutore.data
        print(tutore_data)

        print("altro")
        altro_data= {}
        if controls_map["altro"]["active"]:
            for index in controls_map["altro"]["indices"]:
                altro_data[int(index)] = {
                    'complicanze': form.altro[int(index)].complicanze.data,
                    'note': form.altro[int(index)].note.data,

        }

        return mpcj_data,pipj_data,dipj_data,ipj_data,trapezio_metacarpale,polso,vas_data,forza,dash_data,prwhe_data,eaton_littler_data,edema_data,cicatrice,tutore_data,altro_data

   

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
    
    
class LesioneLigamentosaTimeline(PathologyTimline):
    
    #Settimane per il controllo
    timeline= [0,3,6,12,26,52,104,520,1040]

    first_control=[
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
    ]

    second_control = [
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value
        ]

    third_control = [
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.DASH.value,
        CONTROLS.PRWHE.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
    ]

class ScafoideTimeline(PathologyTimline):
    
    #Settimane per il controllo
    timeline= [0,2,6,26,52,520,1040]

    first_control=[
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
       
    ]

    second_control = [
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value
        ]

    third_control = [
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.DASH.value,
        CONTROLS.PRWHE.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
    ]


class LesioneNervosaTimeline(PathologyTimline):
    
    #Settimane per il controllo
    timeline= [0,4,12,26,52,104,520,1040]

    first_control=[
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        ]

    second_control = [
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value
        ]

    third_control = [
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.DASH.value,
        CONTROLS.PRWHE.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
    ]


class DupuytrenTimeline(PathologyTimline):
    
    #Settimane per il controllo
    timeline= [0,2,6,12,26,52,520,1040]

    first_control=[
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
    ]

    second_control = [
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value
        ]

    third_control = [
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.DASH.value,
        CONTROLS.PRWHE.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
    ]


class ResezioneFilieraTimeline(PathologyTimline):
    
    #Settimane per il controllo
    timeline= [0,2,6,12,26,52,520,1040]

    first_control=[
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.DASH.value,
        CONTROLS.PRWHE.value,
        CONTROLS.EATON_LITTLER.value,
        CONTROLS.PIPJ.value
    ]

    second_control = [
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value
        ]

    third_control = [
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.DASH.value,
        CONTROLS.PRWHE.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
    ]


class LesioneTendineaTimeline(PathologyTimline):
    
    #Questi sono i dati per ogni controllo
    timeline= [0,4,6,8,12,26,52,154,520,1040]

    first_control=[
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.DASH.value,
        CONTROLS.PRWHE.value,
        CONTROLS.EATON_LITTLER.value,
        CONTROLS.PIPJ.value
    ]

    second_control = [
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value
        ]

    third_control = [
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.DASH.value,
        CONTROLS.PRWHE.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
    ]

class FrattureFalangeProssimaleTimeline(PathologyTimline):
    
    #Questi sono i dati per ogni controllo
    timeline= [0,4,6,8,12,26,52,154,520,1040]

    first_control=[
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.DASH.value,
        CONTROLS.PRWHE.value,
        CONTROLS.EATON_LITTLER.value,
        CONTROLS.PIPJ.value
    ]

    second_control = [
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value
        ]

    third_control = [
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.DASH.value,
        CONTROLS.PRWHE.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
    ]




class FratturaMetaCarpaleTimeline(PathologyTimline):
    
    decorso_unico=False

    #Questi sono i dati per ogni controllo
    timeline= None

    last_control_number_before_next=2

    #Questa funzione serve perchè per alcune patologie il decorso post operatorio 
    # segue una timeline diversa per cui in base alle opzioni selezionate della patologia ritorna
    # un valore diverso
    # Gli indici della timeline corrispondono ai controlli ritornati da get_one,get_two,get_next
    # Se il valore è 0 significa che il controllo è saltato
    @classmethod
    def getTimeline(cls,tipo_intervento=None):
        print(tipo_intervento)
        print(tipo_intervento==FrattureMetaCarpaliEnum.CHIRURGICO.value)
        
        if(tipo_intervento==FrattureMetaCarpaliEnum.NON_CHIRURGICO.value):
            timeline= [0,0,4,8,12,26,52,154,520,1040]
            return timeline
        if (tipo_intervento==FrattureMetaCarpaliEnum.CHIRURGICO.value):
            timeline= [0,1,4,8,12,26,52,154,520,1040]
            return timeline

    #ATTENZIONE RICORDARSI di le weeks_to_first_control che corrispondono alla timeline[0]
    weeks_to_first_control={
        FrattureMetaCarpaliEnum.CHIRURGICO.value:1,
        FrattureMetaCarpaliEnum.NON_CHIRURGICO.value:4
    }

    @classmethod
    def get_pre(cls):
        
        #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        tmp_ControlMap[CONTROLS.DATA_FRATTURA.value]["active"]=True

        return tmp_ControlMap

    #Siccome il decorso è diverso per il primo intervento
    # get_one ritorna una mappa solo quando il tipo_intervento è chirurgico
    @classmethod
    def get_one(cls,tipo_intervento,metacarpo_rotto=1):
        tipo_intervento=str(tipo_intervento)

        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)

        if(tipo_intervento==FrattureMetaCarpaliEnum.CHIRURGICO.value):
            pip_j_indices=[]
            pip_j_indices.append(int(metacarpo_rotto))
            tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
            tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
            tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
            tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
            # In questo controllo sono attivii tutti i campi
            tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[1,2,3,4,5]
            tmp_ControlMap[CONTROLS.PIPJ.value]["active"]=True
            tmp_ControlMap[CONTROLS.PIPJ.value]["indices"]= pip_j_indices

            return tmp_ControlMap
    @classmethod
    def get_second(cls,tipo_intervento,metacarpo_rotto=1):

        tipo_intervento=str(tipo_intervento)
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        pip_j_indices=[]
        pip_j_indices.append(int(metacarpo_rotto))
        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
        tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        # In questo controllo sono attivii tutti i campi
        tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[1,2,3,4,5]
        tmp_ControlMap[CONTROLS.PIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.PIPJ.value]["indices"]= pip_j_indices
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True

        if(tipo_intervento==FrattureMetaCarpaliEnum.CHIRURGICO.value):
            tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True

        return tmp_ControlMap
    
    @classmethod
    def get_next(cls,tipo_intervento,metacarpo_rotto=1):

        tipo_intervento=str(tipo_intervento)
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        pip_j_indices=[]
        pip_j_indices.append(int(metacarpo_rotto))
        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        # In questo controllo sono attivii tutti i campi
        tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[1,2,3,4,5]
        tmp_ControlMap[CONTROLS.PIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.PIPJ.value]["indices"]= pip_j_indices
        tmp_ControlMap[CONTROLS.FORZA.value]["indices"]= pip_j_indices
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True

        if(tipo_intervento==FrattureMetaCarpaliEnum.CHIRURGICO.value):
            tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True

        return tmp_ControlMap




class FrattureRadioDistaliTimeline(PathologyTimline):
    
    decorso_unico=False

    #Questi sono i dati per ogni controllo
    timeline= [0,2,4,8,12,26,52,154,520,1040]

    # se non ho differenze nel post operatorio la timeline è la stessa
    @classmethod
    def getTimeline(cls,tipo_intervento=None):
        
        return cls.timeline
       

    weeks_to_first_control={
        "1":2
    }



    @classmethod
    def get_pre(cls):
        
        #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        tmp_ControlMap[CONTROLS.DATA_FRATTURA.value]["active"]=True

        return tmp_ControlMap
  

    first_control=[

        CONTROLS.DASH.value,
        CONTROLS.PRWHE.value,
        CONTROLS.EATON_LITTLER.value,
        CONTROLS.PIPJ.value
    ]

    second_control = [
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value
        ]

    third_control = [
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.DASH.value,
        CONTROLS.PRWHE.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
        CONTROLS.PIPJ.value,
    ]


class RizoartrosiControlsTimeline(PathologyTimline):

    #Variabile definita per ogni controllo. Indica se il percorso
    #post operatorio è unico o no
    decorso_unico=True
    #Il primo valore è sempre 0 perchè rispecchia il momento dell'intervento
    timeline= [0,3,6,12,26,52,154,520,1040]

    # Numero che corrisponde al numero di controlli implementati
    # dopo di che sono tutti uguali e sono chiamati con il methodo get_next
    last_control_number_before_next=2

    # se non ho differenze nel post operatorio la timeline è la stessa
    @classmethod
    def getTimeline(cls,tipo_intervento=None):
        print(cls.timeline)
        return cls.timeline
    
    #quante settimane aspettare se il paziente non risponde alla mail
    waiting_weeks= 1

    # Settimane per il primo controllo. Serve per quando devo gestire il calendario
    # per trattamenti che hanno un decorso post operatorio diverso. 
    # ATTENZIONE QUESTO VALORE DEVE ESSERE LO STESSO DI timeline[1]
    # Usato solo nella schermata medical_treatment per gestire il calendario del primo controllo
    weeks_to_first_control={
        "1":3
    }
    
    #Ultimo Controllo
    LAST_CONTROL=9

    @classmethod
    def get_pre(cls):
        
        #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)

        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.IPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.TRAPEZIO_METACARPALE.value]["active"]=True
        tmp_ControlMap[CONTROLS.FORZA.value]["active"]=True
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True
        tmp_ControlMap[CONTROLS.EATON_LITTLER.value]["active"]=True

        #Setto i valori per il primo controllo

        return tmp_ControlMap
    
    @classmethod
    def get_one(cls,pathology_type=None,param=None):
        """
        pathology_type serve perchè in alcuni controlli devo fare delle distinzioni
        Quando metto il valore di defautl None significa che non ho bisogno di fare distinzioni
        """
        #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)

        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.IPJ.value]["active"]=True

        return tmp_ControlMap

    @classmethod
    def get_two(cls,pathology_type=None,param=None):

          #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)

        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.IPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.TRAPEZIO_METACARPALE.value]["active"]=True
        tmp_ControlMap[CONTROLS.FORZA.value]["active"]=True
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True
    


    @classmethod
    def get_next(cls,pathology_type=None,param=None):
        """
        Se i controlli sucessivi sono tutti uguali uso una sola funzione
        """
        #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)

        tmp_ControlMap[CONTROLS.VAS]["active"]=True
        tmp_ControlMap[CONTROLS.EDEMA]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ]["active"]=True
        tmp_ControlMap[CONTROLS.IPJ]["active"]=True
        tmp_ControlMap[CONTROLS.TRAPEZIO_METACARPALE]["active"]=True
        tmp_ControlMap[CONTROLS.FORZA]["active"]=True
        tmp_ControlMap[CONTROLS.DASH]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE]["active"]=True
        tmp_ControlMap[CONTROLS.CICATRICE]["active"]=True

        return tmp_ControlMap
   

   

"""
Chiavi utilizzate per salvare i dati nella sessione user dottore
"""

class CacheDataDoctor(Enum):

    #utilizzati per salvare gli eventi del calendario in modo da non eseguire delle query inutili
    CALENDAR_EVENTS= "calendar_events"


"""
Chiavi Vecchie utilizzate nella sessione. VERIFICARE Se sono ancora utili
"""
class DoctorData(Enum):
    ID_PATIENT= "id_patient"
    ID_PATHOLOGY= "id_pathology"
    ID_PATHOLOGY_TYPE= "id_pathology_type"
    CONTROL_DATE = "first_control_date"
    CONTROL_TIME = "first_control_time"
    #questa chiave tiene traccia dell'appuntamento del controllo successivo
    NUM_CONTROL = "control_number"
    OPTIONS_FIELD= "options_field"
        

"""
Enum utilizzato per associare ad ogni patologia la propria timeline di decorso operatorio
Le lables sono utilizzate per caricare il file html corrispondente in doctor/patologie/

Descrizione parameteri

value[0]: id della patologia
value[1]: nome della patologia
value[2]: classe della timeline
value[3]: form chirurgico
value[4]: enum per le opzioni chirurgiche

"""

class PATHOLOGY(Enum):
    RIZOARTROSI= (1,"rizoartrosi",RizoartrosiControlsTimeline,RizoartrosiChirurgicoForm,None)
    FRATTURA_RADIO_DISTALE= (2,"frattura_radio_distale",FrattureRadioDistaliTimeline,FratturaRadioDistaleForm,None)
    FRATTURE_METACARPALI = (3,"fratture_metacarpali",FratturaMetaCarpaleTimeline,FratturaMetaCarpaliForm,FrattureMetaCarpaliEnum)
    FRATTURE_FALANGE_PROSSIMALE = (4, "fratture_falange_prossimale",FrattureFalangeProssimaleTimeline,None,None)
    FERITA_LESIONE_TENDINEA = (5, "ferita_lesione_tendinea",LesioneTendineaTimeline,None,None)
    RESEZIONE_FILIERA= (6, "resezione_filiera",ResezioneFilieraTimeline,None,None)
    DUPUYTREN= (7, "dupuytren",DupuytrenTimeline,None,None)
    LESIONE_NERVOSA=(8, "lesione_nervosa",LesioneNervosaTimeline,None,None)
    SCAFOIDE= (9, "scafoide",ScafoideTimeline,None,None)
    LESIONE_LIGAMENTOSA= (10, "lesione_ligamentosa",LesioneLigamentosaTimeline,None,None)
        


class PATHOLOGY_STATUS(Enum):
    PRIMA= (1,"Prima del Trattamento")
    DURANTE= (2,"Trattamento")
    DOPO = (3,"Post Trattamento")
    
class PATHOLOGY_TYPE(Enum):
    RIZOARTROSI_TRAPEZIECTOMIA = (1,PATHOLOGY.RIZOARTROSI,"Trapeziectomia e artoplastica in sospensione con APL")
    RIZOARTROSI_PROTESI = (2,PATHOLOGY.RIZOARTROSI,"Protesi Touch")
    RIZOARTROSI_ALTRO = (3,PATHOLOGY.RIZOARTROSI,"Altre tipologie Rizoartrosi")
    FRATTURA_RADIO_DISTALE_GESSO = (4,PATHOLOGY.FRATTURA_RADIO_DISTALE,"Gesso Chiuso")
    FRATTURA_RADIO_DISTALE_PLACCA_VITI= (5,PATHOLOGY.FRATTURA_RADIO_DISTALE,"Placca Viti")
    FRATTURA_RADIO_DISTALE_PLACCA_ALTRO= (6,PATHOLOGY.FRATTURA_RADIO_DISTALE,"Altro Frattura radio distale")
    FRATTURE_METACARPALI_CHIRURGICO = (7,PATHOLOGY.FRATTURE_METACARPALI,"Chirurgico")
    FRATTURE_METACARPALI_NON_CHIRURGICO = (8,PATHOLOGY.FRATTURE_METACARPALI,"Non Chirurgico")
    FRATTURE_FALANGE_PROSSIMALE_CHIRURGICO=(9,PATHOLOGY.FRATTURE_FALANGE_PROSSIMALE,"Chirurgico")
    FRATTURE_FALANGE_PROSSIMALE_NON_CHIRURGICO=(10,PATHOLOGY.FRATTURE_FALANGE_PROSSIMALE,"Non Chirurgico")
    FERITA_LESIONE_TENDINEA_TENDINE_FLESSORE = (11,PATHOLOGY.FERITA_LESIONE_TENDINEA, "Tendine Flessore")
    FERITA_LESIONE_TENDINEA_TENDINE_ESTENSORE = (12,PATHOLOGY.FERITA_LESIONE_TENDINEA, "Tendine Estensore")




'''
Questa classe contiene tutte le chiavi 
del form utilizzato per la selezione delle patologie
'''
class PATHOLOGY_KEY_SELECTION_FORM(Enum):
    #RADIO DISTALE
    
    radio_distale_giorni_value= "radio_distale_giorni_value"
    classificazione_radiografica_tipo_valore= "classificazione_radiografica_tipo_valore"
    classificazione_radiografica_numero_valore= "classificazione_radiografica_numero_valore"
    #METACARPALI
    fratture_metacarpali_non_chirurgico_type= "fratture_metacarpali_non_chirurgico_type"
    fratture_metacarpali_non_chirirgico_polso= "fratture_metacarpali_non_chirirgico_polso"
    fratture_metacarpali_non_chirirgico_mcpj = "fratture_metacarpali_non_chirirgico_mcpj"
    fratture_metacarpali_non_chirirgico_mcpj_yes_value="fratture_metacarpali_non_chirirgico_mcpj_yes_value"
    fratture_metacarpali_non_chirirgico_pipj="fratture_metacarpali_non_chirirgico_pipj"
    fratture_metacarpali_non_chirirgico_pipj_yes="fratture_metacarpali_non_chirirgico_pipj_yes"
    fratture_metacarpali_non_chirirgico_pipj_yes_value="fratture_metacarpali_non_chirirgico_pipj_yes_value"
    fratture_metacarpali_chirurgico_data="fratture_metacarpali_chirurgico_data"
    fratture_metacarpali_fili_kirschner="fratture_metacarpali_fili_kirschner"
    fratture_metacarpali_viti="fratture_metacarpali_viti"
    fratture_metacarpali_step1_valore="fratture_metacarpali_step1_valore"
    fratture_metacarpali_classificazione_radiografica_value="fratture_metacarpali_classificazione_radiografica_value"
    fratture_metacarpali_diafisaria_value="fratture_metacarpali_diafisaria_value"

    #FALANGE_PROSSIMALE

    fratture_falange_prossimale_non_chirurgico_type= "fratture_falange_prossimale_non_chirurgico_type"
    fratture_falange_prossimale_non_chirirgico_polso= "fratture_falange_prossimale_non_chirirgico_polso"
    fratture_falange_prossimale_non_chirirgico_mcpj = "fratture_falange_prossimale_non_chirirgico_mcpj"
    fratture_falange_prossimale_non_chirirgico_mcpj_yes_value="fratture_falange_prossimale_non_chirirgico_mcpj_yes_value"
    fratture_falange_prossimale_non_chirirgico_pipj="fratture_falange_prossimale_non_chirirgico_pipj"
    fratture_falange_prossimale_non_chirirgico_pipj_yes="fratture_falange_prossimale_non_chirirgico_pipj_yes"
    fratture_falange_prossimale_non_chirirgico_pipj_yes_value="fratture_falange_prossimale_non_chirirgico_pipj_yes_value"
    fratture_falange_prossimale_chirurgico_data="fratture_falange_prossimale_chirurgico_data"
    fratture_falange_prossimale_fili_kirschner="fratture_falange_prossimale_fili_kirschner"
    fratture_falange_prossimale_viti="fratture_falange_prossimale_viti"
    fratture_falange_prossimale_step1_valore="fratture_falange_prossimale_step1_valore"
    fratture_falange_prossimale_classificazione_radiografica_value="fratture_falange_prossimale_classificazione_radiografica_value"
    fratture_falange_prossimale_diafisaria_value="fratture_falange_prossimale_diafisaria_value" 

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
    #Per ogni controllo devo ritornare il numero di settimane del controllo successivo.
    #Questo serve nell'interfaccia grafica per selezionare i giorni del calendario in cui è possibile selzionare la data

    timeline_dict = {}
    # Iterate over enum values
    for pathology_type in PATHOLOGY_TYPE:
        category = str(pathology_type.value[1].value[0])
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
            #per ogni PATHOLOGY prendo dopo quante settimane c'è il primo controllo
            timeline_dict[category]= pathology_type.value[1].value[2].timeline[1]
            
            
    name_dict = str(name_dict).replace("'", '"')
    timeline_dict = str(timeline_dict).replace("'", '"')
    return name_dict,timeline_dict