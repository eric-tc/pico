#This file handles internal data of the application

from enum import Enum
import copy
from .doctor_chirurgico_forms import RizoartrosiChirurgicoForm,FratturaRadioDistaleChirurgicoForm,\
FratturaMetaCarpaliChirurgicoForm,\
FratturaFalangeProssimaleChirurgicoForm,\
ResezioneFilieraChirurgicoForm,\
ScafoideFratturaChirurgicoForm,\
ScafoidePseudoArtrosiChirurgicoForm,\
DupuytrenChirurgicoForm,\
LesioneLigamentosaChirurgicoForm,\
LesioneTendineaFlessoriChirurgicoForm

from .internal_data_enum_pathologies import FrattureMetaCarpaliEnum,\
    FrattureFalangeProssimaleEnum,\
    ScafoideFratturaEnum,\
    ResezioneFilieraEnum,\
    RizoartrosiEnum,\
    FratturaRadioDistaleEnum,\
    ScafoidePseudortrosiEnum,\
    LesioneTendineaFlessoriEnum,\
    DupuytrenEnum,\
    LesioneLigamentosaEnum,\
    CONTROLS,\
    CONTROLSNUMBER,\
    PATHOLOGY_LABEL

from .doctor_forms import PreResezioneFileraForm,PreDupuytrenForm,PreLesioneLigamentosaForm

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

# Indicano quanti giorni prima 
# e dopo è possibile compilare un evento schedulato
class EVENT_DAYS(Enum):

    DAYS_BEFORE = 5
    DAYS_AFTER = 80


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
        CONTROLS.SENSIBILITA_VOLARE.value: {"active":False,
                           "indices":[0]
                           },
        CONTROLS.SENSIBILITA_DORSALE.value: {"active":False,
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
                           },
        CONTROLS.GUARIGIONE_OSSEA.value: {"active":False,
                                            "indices":[0]
                                            },
        CONTROLS.CONCESSO_INIZIO_MOBILIZZAZIONE.value: {"active":False,
                                                        "indices":[0]
                                                        },
        CONTROLS.ARTICOLAZIONE_STABILE.value: {"active":False,
                                               "indices":[0]
                                                },
        CONTROLS.DATA_INIZIO_MOBILIZZAZIONE.value: {"active":False,
                                               "indices":[0]
                                                },                            
    }
    
    #Controlla i Form aggiuntivi per i controlli per operatori.
    #Ad esempio se devo aggiungere dei parametri oltre a quelli di default
    Controls_Map_Pre={
        PATHOLOGY_LABEL.RIZOARTROSI.value: {"active":False},                    
        PATHOLOGY_LABEL.FRATTURA_RADIO_DISTALE.value: {"active":False},  
        PATHOLOGY_LABEL.FRATTURE_METACARPALI.value : {"active":False},  
        PATHOLOGY_LABEL.FRATTURE_FALANGE_PROSSIMALE.value : {"active":False},  
        PATHOLOGY_LABEL.LESIONE_TENDINEA_FLESSORI.value : {"active":False},
        PATHOLOGY_LABEL.LESIONE_TENDINEA_ESTENSORI.value : {"active":False},  
        PATHOLOGY_LABEL.RESEZIONE_FILIERA.value: {"active":False},  
        PATHOLOGY_LABEL.DUPUYTREN.value: {"active":False},  
        PATHOLOGY_LABEL.LESIONE_NERVOSA.value:{"active":False},  
        PATHOLOGY_LABEL.SCAFOIDE_FRATTURA.value: {"active":False},
        PATHOLOGY_LABEL.SCAFOIDE_PSEUDOARTROSI.value: {"active":False},  
        PATHOLOGY_LABEL.LESIONE_LIGAMENTOSA.value: {"active":False},
        PATHOLOGY_LABEL.DUPUYTREN.value: {"active":False}  
    }


    @classmethod
    def process_parameters(cls, controls_map,form):
        """
        Funzione usata per processare i parametri passati dal form e renderli nel formato adatto 
        per il database

        controls_map: mappa aggiornata con i valori attivi per il controllo specifico
        form: data del form passato
        """

        mpcj_data = {}
        if controls_map[CONTROLS.MPCJ.value]["active"]:
            for index in controls_map[CONTROLS.MPCJ.value]["indices"]:
                # Dynamically retrieve the data for each subform
                mpcj_data[int(index)] = {
                    'arom_estensione': form.mpcj[int(index)].arom_estensione.data,
                    'arom_flessione': form.mpcj[int(index)].arom_flessione.data,
                    'prom_estensione': form.mpcj[int(index)].prom_estensione.data,
                    'prom_flessione': form.mpcj[int(index)].prom_flessione.data
                }

        print("MPCJ")
        print(mpcj_data)

        
        dipj_data = {}
        if controls_map[CONTROLS.DIPJ.value]["active"]:
            for index in controls_map[CONTROLS.DIPJ.value]["indices"]:
                # Dynamically retrieve the data for each subform
                dipj_data[int(index)] = {
                    'arom_estensione': form.dipj[int(index)].arom_estensione.data,
                    'arom_flessione': form.dipj[int(index)].arom_flessione.data,
                    'prom_estensione': form.dipj[int(index)].prom_estensione.data,
                    'prom_flessione': form.dipj[int(index)].prom_flessione.data
                }
        print("DIPJ")
        print(dipj_data)

        
        pipj_data = {}
        if controls_map[CONTROLS.PIPJ.value]["active"]:
            for index in controls_map[CONTROLS.PIPJ.value]["indices"]:
                # Dynamically retrieve the data for each subform
                pipj_data[int(index)] = {
                    'arom_estensione': form.pipj[int(index)].arom_estensione.data,
                    'arom_flessione': form.pipj[int(index)].arom_flessione.data,
                    'prom_estensione': form.pipj[int(index)].prom_estensione.data,
                    'prom_flessione': form.pipj[int(index)].prom_flessione.data
                }

        print("PIPJ")
        print(pipj_data)
        
        ipj_data = {}
        if controls_map[CONTROLS.IPJ.value]["active"]:
            for index in controls_map[CONTROLS.IPJ.value]["indices"]:
                # Dynamically retrieve the data for each subform
                ipj_data[int(index)] = {
                    'arom_estensione': form.ipj[int(index)].arom_estensione.data,
                    'arom_flessione': form.ipj[int(index)].arom_flessione.data,
                    'prom_estensione': form.ipj[int(index)].prom_estensione.data,
                    'prom_flessione': form.ipj[int(index)].prom_flessione.data
                }

        print("IPJ")
        print(ipj_data)

        trapezio_metacarpale = {}

        if controls_map[CONTROLS.TRAPEZIO_METACARPALE.value]["active"]:
            for index in controls_map[CONTROLS.TRAPEZIO_METACARPALE.value]["indices"]:
                trapezio_metacarpale[int(index)] = {
                    'anteposizione': form.trapezio_metacarpale[int(index)].anteposizione.data,
                    'abduzione': form.trapezio_metacarpale[int(index)].abduzione.data,
                    'kapandji': form.trapezio_metacarpale[int(index)].kapandji.data,
                }
        
        print("TRAPEZIO METACARPALE")
        print(trapezio_metacarpale)


        polso={}
        if controls_map[CONTROLS.POLSO.value]["active"]:
            for index in controls_map[CONTROLS.POLSO.value]["indices"]:
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
        if controls_map[CONTROLS.VAS.value]["active"]:
            vas_data= form.vas.data
        print(vas_data)

        print("FORZA")
        forza={}

        if controls_map[CONTROLS.FORZA.value]["active"]:
            for index in controls_map[CONTROLS.FORZA.value]["indices"]:
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
        if controls_map[CONTROLS.DASH.value]["active"]:
            dash_data = []
            for entry in form.dash.entries:  # Iterate over FieldList
                dash_entry = {field.name: field.data for field in entry}
                dash_data.append(dash_entry)
        print(dash_data)


        
        print("Prwhe")
        prwhe_data =[]
        if controls_map[CONTROLS.PRWHE.value]["active"]:
            for entry in form.prwhe.entries:  # Iterate over FieldList
                prwhe_entry = {field.name: field.data for field in entry}
                prwhe_data.append(prwhe_entry)
        print(prwhe_data)

        
        print("eaton littler")
        eaton_littler_data= None
        if controls_map[CONTROLS.EATON_LITTLER.value]["active"]:
            eaton_littler_data= form.eaton_littler.data
        print(eaton_littler_data)


        print("edema")
        edema_data= None
        if controls_map[CONTROLS.EDEMA.value]["active"]:
            edema_data= form.edema.data
        print(edema_data)

        print("Sensibilita_volare")
        sensibilita_volare_data= None
        if controls_map[CONTROLS.SENSIBILITA_VOLARE.value]["active"]:
            sensibilita_volare_data= form.sensibilita_volare.data
        print(sensibilita_volare_data)


        print("Sensibilita_dorsale")
        sensibilita_dorsale_data= None
        if controls_map[CONTROLS.SENSIBILITA_DORSALE.value]["active"]:
            sensibilita_dorsale_data= form.sensibilita_dorsale.data
        print(sensibilita_dorsale_data)

        cicatrice = {}

        if controls_map[CONTROLS.CICATRICE.value]["active"]:
            for index in controls_map[CONTROLS.CICATRICE.value]["indices"]:
                cicatrice[int(index)] = {
                    'aderente': form.cicatrice[int(index)].aderente.data,
                    'distasi_ferita': form.cicatrice[int(index)].distasi_ferita.data,
                    'tinel': form.cicatrice[int(index)].tinel.data,
                }
        
        print("cicatrice")
        print(cicatrice)


        print("tutore")
        tutore_data= None
        if controls_map[CONTROLS.TUTORE.value]["active"]:
            tutore_data= form.tutore.data
        print(tutore_data)

        print("altro")
        altro_data= {}
        if controls_map[CONTROLS.ALTRO.value]["active"]:
            for index in controls_map["altro"]["indices"]:
                altro_data[int(index)] = {
                    'complicanze': form.altro[int(index)].complicanze.data,
                    'note': form.altro[int(index)].note.data,

        }

        return mpcj_data,pipj_data,dipj_data,ipj_data,trapezio_metacarpale,polso,vas_data,forza,dash_data,prwhe_data,eaton_littler_data,edema_data,sensibilita_volare_data,sensibilita_dorsale_data,cicatrice,tutore_data,altro_data

   

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
    
    decorso_unico=True

    #Questi sono i dati per ogni controllo
    timeline= None

    last_control_number_before_next=1

    #Questa funzione serve perchè per alcune patologie il decorso post operatorio 
    # segue una timeline diversa per cui in base alle opzioni selezionate della patologia ritorna
    # un valore diverso
    # Gli indici della timeline corrispondono ai controlli ritornati da get_one,get_two,get_next
    # Se il valore è 0 significa che il controllo è saltato
    @classmethod
    def getTimeline(cls,tipo_intervento=None):
            
        timeline= [0,3,6,12,26,52,520,1040]
        return timeline

    #ATTENZIONE RICORDARSI di le weeks_to_first_control che corrispondono al primo numero della timeline !=0
    weeks_to_first_control={
        "1":3,
        
    }

    @classmethod
    def get_pre(cls):
        
        pre_controls_map = copy.deepcopy(cls.Controls_Map_Pre)
        pre_controls_map[PATHOLOGY_LABEL.LESIONE_LIGAMENTOSA.value]["active"]=True
        
        #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        tmp_ControlMap[CONTROLS.DATA_FRATTURA.value]["active"]=True

        return tmp_ControlMap,pre_controls_map

    
    @classmethod
    def get_one(cls,tipo_intervento,dito_rotto=1):
        tipo_intervento=str(tipo_intervento)

        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
           
        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.CONCESSO_INIZIO_MOBILIZZAZIONE.value]["active"]=True
        
        tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[0,1,2,3,4]

        tmp_ControlMap[CONTROLS.PIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.PIPJ.value]["indices"]= [0,1,2,3,4]

        tmp_ControlMap[CONTROLS.DIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.DIPJ.value]["indices"]= [1,2,3,4]
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True

        return tmp_ControlMap
    
    @classmethod
    def get_next(cls,tipo_intervento,dito_rotto=1):
        tipo_intervento=str(tipo_intervento)

        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
           
        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[0,1,2,3,4]

        tmp_ControlMap[CONTROLS.PIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.PIPJ.value]["indices"]= [0,1,2,3,4]

        tmp_ControlMap[CONTROLS.DIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.DIPJ.value]["indices"]= [1,2,3,4]
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True
        tmp_ControlMap[CONTROLS.CONCESSO_INIZIO_MOBILIZZAZIONE.value]["active"]=True
        return tmp_ControlMap



class ScafoidePseudoartrosiTimeline(PathologyTimline):
    
    decorso_unico=False

    #Questi sono i dati per ogni controllo
    timeline= None

    last_control_number_before_next=3

    #Questa funzione serve perchè per alcune patologie il decorso post operatorio 
    # segue una timeline diversa per cui in base alle opzioni selezionate della patologia ritorna
    # un valore diverso
    # Gli indici della timeline corrispondono ai controlli ritornati da get_one,get_two,get_next
    # Se il valore è 0 significa che il controllo è saltato
    @classmethod
    def getTimeline(cls,tipo_intervento=None):
        
        timeline= [0,6,12,26,52,520,1040]
        return timeline
        

    #ATTENZIONE RICORDARSI di le weeks_to_first_control che corrispondono al primo numero della timeline !=0
    weeks_to_first_control={
        "1":6,
    }

    @classmethod
    def get_pre(cls):
        
        pre_controls_map = copy.deepcopy(cls.Controls_Map_Pre)

        #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        tmp_ControlMap[CONTROLS.DATA_FRATTURA.value]["active"]=True

        return tmp_ControlMap,pre_controls_map

    #Siccome il decorso è diverso per il primo intervento
    # get_one ritorna una mappa solo quando il tipo_intervento è chirurgico
    @classmethod
    def get_one(cls,tipo_intervento,dito_rotto=1):
        tipo_intervento=str(tipo_intervento)

        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        
        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
        tmp_ControlMap[CONTROLS.CONCESSO_INIZIO_MOBILIZZAZIONE.value]["active"]=True
        tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.IPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.TRAPEZIO_METACARPALE.value]["active"]=True
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True
    
        return tmp_ControlMap

    @classmethod
    def get_two(cls,tipo_intervento,metacarpo_rotto=1):

        
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        
        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.CONCESSO_INIZIO_MOBILIZZAZIONE.value]["active"]=True
        tmp_ControlMap[CONTROLS.POLSO.value]["active"]=False # Diventa true se concesso_inizio_mobilizzazione è true
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.IPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.TRAPEZIO_METACARPALE.value]["active"]=True
        tmp_ControlMap[CONTROLS.FORZA.value]["active"]=True
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True
    
        return tmp_ControlMap
    
    @classmethod
    def get_three(cls,tipo_intervento,metacarpo_rotto=1):

        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        
        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.CONCESSO_INIZIO_MOBILIZZAZIONE.value]["active"]=True
        tmp_ControlMap[CONTROLS.POLSO.value]["active"]=False # Diventa true se concesso_inizio_mobilizzazione è true
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.IPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.TRAPEZIO_METACARPALE.value]["active"]=True
        tmp_ControlMap[CONTROLS.FORZA.value]["active"]=True
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True

        tmp_ControlMap[CONTROLS.GUARIGIONE_OSSEA.value]["active"]=True
    
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
        tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[0,1,2,3,4]
        tmp_ControlMap[CONTROLS.PIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.PIPJ.value]["indices"]= pip_j_indices
        tmp_ControlMap[CONTROLS.FORZA.value]["indices"]= pip_j_indices
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True

        if(tipo_intervento==FrattureMetaCarpaliEnum.CHIRURGICO.value[0]):
            tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True

        return tmp_ControlMap


class ScafoideFratturaTimeline(PathologyTimline):
    
    decorso_unico=False

    #Questi sono i dati per ogni controllo
    timeline= None

    last_control_number_before_next=4

    #Questa funzione serve perchè per alcune patologie il decorso post operatorio 
    # segue una timeline diversa per cui in base alle opzioni selezionate della patologia ritorna
    # un valore diverso
    # Gli indici della timeline corrispondono ai controlli ritornati da get_one,get_two,get_next
    # Se il valore è 0 significa che il controllo è saltato
    @classmethod
    def getTimeline(cls,tipo_intervento=None):
        
        if(tipo_intervento==ScafoideFratturaEnum.CONSERVATIVO.value[0]):
            timeline= [0,0,6,12,26,52,520,1040]
            return timeline
        if (tipo_intervento==ScafoideFratturaEnum.CHIRURGICO.value[0]):
            timeline= [0,2,6,12,26,52,520,1040]
            return timeline

    #ATTENZIONE RICORDARSI di le weeks_to_first_control che corrispondono al primo numero della timeline !=0
    weeks_to_first_control={
        "1":2,
        "2":6
    }

    @classmethod
    def get_pre(cls):
        
        pre_controls_map = copy.deepcopy(cls.Controls_Map_Pre)

        #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        tmp_ControlMap[CONTROLS.DATA_FRATTURA.value]["active"]=True

        return tmp_ControlMap,pre_controls_map

    #Siccome il decorso è diverso per il primo intervento
    # get_one ritorna una mappa solo quando il tipo_intervento è chirurgico
    @classmethod
    def get_one(cls,tipo_intervento,dito_rotto=1):
        tipo_intervento=str(tipo_intervento)

        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        
        if(tipo_intervento==ScafoideFratturaEnum.CHIRURGICO.value[0]):
           
            tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
            tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
            tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
            tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True

            return tmp_ControlMap
    
    @classmethod
    def get_two(cls,tipo_intervento,metacarpo_rotto=1):

        tipo_intervento=str(tipo_intervento)
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        pip_j_indices=[]
        pip_j_indices.append(int(metacarpo_rotto))
        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
        tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
        tmp_ControlMap[CONTROLS.FORZA.value]["active"]=True
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True
        
        return tmp_ControlMap
    
    @classmethod
    def get_three(cls,tipo_intervento,metacarpo_rotto=1):

        tipo_intervento=str(tipo_intervento)
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        pip_j_indices=[]
        pip_j_indices.append(int(metacarpo_rotto))
        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
        tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
        tmp_ControlMap[CONTROLS.FORZA.value]["active"]=True
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True
        
        return tmp_ControlMap
    
    @classmethod
    def get_four(cls,tipo_intervento,metacarpo_rotto=1):

        tipo_intervento=str(tipo_intervento)
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        pip_j_indices=[]
        pip_j_indices.append(int(metacarpo_rotto))
        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
        tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
        tmp_ControlMap[CONTROLS.FORZA.value]["active"]=True
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True
        tmp_ControlMap[CONTROLS.GUARIGIONE_OSSEA.value]["active"]=True
        
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
        tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[0,1,2,3,4]
        tmp_ControlMap[CONTROLS.PIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.PIPJ.value]["indices"]= pip_j_indices
        tmp_ControlMap[CONTROLS.FORZA.value]["indices"]= pip_j_indices
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True

        if(tipo_intervento==FrattureMetaCarpaliEnum.CHIRURGICO.value[0]):
            tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True

        return tmp_ControlMap


class LesioneNervosaTimeline(PathologyTimline):
    
    decorso_unico=True

    #Questi sono i dati per ogni controllo
    timeline= None

    last_control_number_before_next=1

    #Questa funzione serve perchè per alcune patologie il decorso post operatorio 
    # segue una timeline diversa per cui in base alle opzioni selezionate della patologia ritorna
    # un valore diverso
    # Gli indici della timeline corrispondono ai controlli ritornati da get_one,get_two,get_next
    # Se il valore è 0 significa che il controllo è saltato
    @classmethod
    def getTimeline(cls,tipo_intervento=None):
            
        timeline= [0,2,6,12,26,52,520,1040]
        return timeline

    #ATTENZIONE RICORDARSI di le weeks_to_first_control che corrispondono al primo numero della timeline !=0
    weeks_to_first_control={
        "1":2,
        
    }

    @classmethod
    def get_pre(cls):
        
        pre_controls_map = copy.deepcopy(cls.Controls_Map_Pre)
        pre_controls_map[PATHOLOGY_LABEL.DUPUYTREN.value]["active"]=True
        
        #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        tmp_ControlMap[CONTROLS.DATA_FRATTURA.value]["active"]=True

        return tmp_ControlMap,pre_controls_map

    
    @classmethod
    def get_one(cls,tipo_intervento,dito_rotto=1):
        tipo_intervento=str(tipo_intervento)

        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
           
        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[0,1,2,3,4]

        tmp_ControlMap[CONTROLS.PIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.PIPJ.value]["indices"]= [0,1,2,3,4]

        tmp_ControlMap[CONTROLS.DIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.DIPJ.value]["indices"]= [1,2,3,4]
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True

        return tmp_ControlMap
    
    
    @classmethod
    def get_next(cls,tipo_intervento,metacarpo_rotto=1):

        tipo_intervento=str(tipo_intervento)
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        pip_j_indices=[]
        pip_j_indices.append(int(metacarpo_rotto))
        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[0,1,2,3,4]

        tmp_ControlMap[CONTROLS.PIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.PIPJ.value]["indices"]= [0,1,2,3,4]

        tmp_ControlMap[CONTROLS.DIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.DIPJ.value]["indices"]= [1,2,3,4] #non Ho il pollice       
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True

        return tmp_ControlMap


class DupuytrenTimeline(PathologyTimline):
    
    decorso_unico=True

    #Questi sono i dati per ogni controllo
    timeline= None

    last_control_number_before_next=1

    #Questa funzione serve perchè per alcune patologie il decorso post operatorio 
    # segue una timeline diversa per cui in base alle opzioni selezionate della patologia ritorna
    # un valore diverso
    # Gli indici della timeline corrispondono ai controlli ritornati da get_one,get_two,get_next
    # Se il valore è 0 significa che il controllo è saltato
    @classmethod
    def getTimeline(cls,tipo_intervento=None):
            
        timeline= [0,2,6,12,26,52,520,1040]
        return timeline

    #ATTENZIONE RICORDARSI di le weeks_to_first_control che corrispondono al primo numero della timeline !=0
    weeks_to_first_control={
        "1":2,
        
    }

    @classmethod
    def get_pre(cls):
        
        pre_controls_map = copy.deepcopy(cls.Controls_Map_Pre)
        pre_controls_map[PATHOLOGY_LABEL.DUPUYTREN.value]["active"]=True
        
        #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        tmp_ControlMap[CONTROLS.DATA_FRATTURA.value]["active"]=True

        return tmp_ControlMap,pre_controls_map

    
    @classmethod
    def get_one(cls,tipo_intervento,dito_rotto=1):
        tipo_intervento=str(tipo_intervento)

        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
           
        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[0,1,2,3,4]

        tmp_ControlMap[CONTROLS.PIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.PIPJ.value]["indices"]= [0,1,2,3,4]

        tmp_ControlMap[CONTROLS.DIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.DIPJ.value]["indices"]= [1,2,3,4]
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True

        return tmp_ControlMap
    
    
    @classmethod
    def get_next(cls,tipo_intervento,metacarpo_rotto=1):

        tipo_intervento=str(tipo_intervento)
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        pip_j_indices=[]
        pip_j_indices.append(int(metacarpo_rotto))
        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[0,1,2,3,4]

        tmp_ControlMap[CONTROLS.PIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.PIPJ.value]["indices"]= [0,1,2,3,4]

        tmp_ControlMap[CONTROLS.DIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.DIPJ.value]["indices"]= [1,2,3,4] #non Ho il pollice       
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True

        return tmp_ControlMap


class ResezioneFilieraTimeline(PathologyTimline):
    
    #Variabile definita per ogni controllo. Indica se il percorso
    #post operatorio è unico o no
    decorso_unico=True
    #Il primo valore è sempre 0 perchè rispecchia il momento dell'intervento
    timeline= [0,2,6,48,52,520,1040]

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
        "1":2
    }
    
    #Ultimo Controllo
    LAST_CONTROL=9

    @classmethod
    def get_pre(cls):
        
        #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)

        pre_controls_map = copy.deepcopy(cls.Controls_Map_Pre)
        #indica che ci sono dei parametri da inserire oltre a quelli classici
        pre_controls_map[PATHOLOGY_LABEL.RESEZIONE_FILIERA.value]["active"]=True

        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
        tmp_ControlMap[CONTROLS.FORZA.value]["active"]=True
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True
        
        #Setto i valori per il primo controllo

        return tmp_ControlMap,pre_controls_map
    
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
        tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True

        return tmp_ControlMap

    @classmethod
    def get_two(cls,pathology_type=None,param=None):

          #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)

        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
        tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
        tmp_ControlMap[CONTROLS.FORZA.value]["active"]=True
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True

        return tmp_ControlMap


    @classmethod
    def get_next(cls,pathology_type=None,param=None):
        """
        Se i controlli sucessivi sono tutti uguali uso una sola funzione
        """
        #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)

        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
        tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
        tmp_ControlMap[CONTROLS.FORZA.value]["active"]=True
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True

        return tmp_ControlMap

class LesioneTendineaEstensoriTimeline(PathologyTimline):
    
    #Variabile definita per ogni controllo. Indica se il percorso
    #post operatorio è unico o no
    decorso_unico=True
    #Il primo valore è sempre 0 perchè rispecchia il momento dell'intervento
    timeline= [0,3,6,12,26,52,154,520,1040]

    # Numero che corrisponde al numero di controlli implementati
    # dopo di che sono tutti uguali e sono chiamati con il methodo get_next
    last_control_number_before_next=1

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
        
        pre_controls_map = copy.deepcopy(cls.Controls_Map_Pre)

        #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)

        tmp_ControlMap[CONTROLS.DATA_FRATTURA.value]["active"]=True

        #Setto i valori per il primo controllo

        return tmp_ControlMap,pre_controls_map

class LesioneTendineaFlessoriTimeline(PathologyTimline):
    
    #Variabile definita per ogni controllo. Indica se il percorso
    #post operatorio è unico o no
    decorso_unico=True
    #Il primo valore è sempre 0 perchè rispecchia il momento dell'intervento
    timeline= [0,3,6,12,26,52,154,520,1040]

    # Numero che corrisponde al numero di controlli implementati
    # dopo di che sono tutti uguali e sono chiamati con il methodo get_next
    last_control_number_before_next=1

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
        
        pre_controls_map = copy.deepcopy(cls.Controls_Map_Pre)

        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        tmp_ControlMap[CONTROLS.DATA_FRATTURA.value]["active"]=True


        return tmp_ControlMap,pre_controls_map

class FrattureFalangeProssimaleTimeline(PathologyTimline):
    
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
        print(tipo_intervento==FrattureMetaCarpaliEnum.CHIRURGICO.value[0])
        
        if(tipo_intervento==FrattureMetaCarpaliEnum.NON_CHIRURGICO.value[0]):
            timeline= [0,0,4,8,12,26,52,154,520,1040]
            return timeline
        if (tipo_intervento==FrattureMetaCarpaliEnum.CHIRURGICO.value[0]):
            timeline= [0,1,4,8,12,26,52,154,520,1040]
            return timeline

    #ATTENZIONE RICORDARSI di le weeks_to_first_control che corrispondono alla timeline[0]
    weeks_to_first_control={
        "1":1,
        "2":4
    }

    @classmethod
    def get_pre(cls):
        
        pre_controls_map = copy.deepcopy(cls.Controls_Map_Pre)
        
        #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        tmp_ControlMap[CONTROLS.DATA_FRATTURA.value]["active"]=True

        return tmp_ControlMap,pre_controls_map

    #Siccome il decorso è diverso per il primo intervento
    # get_one ritorna una mappa solo quando il tipo_intervento è chirurgico
    @classmethod
    def get_one(cls,tipo_intervento,metacarpo_rotto=1):
        tipo_intervento=str(tipo_intervento)

        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)

        if(tipo_intervento==FrattureMetaCarpaliEnum.CHIRURGICO.value[0]):
            pip_j_indices=[]
            pip_j_indices.append(int(metacarpo_rotto))
            tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
            tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
            tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
            tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
            # In questo controllo sono attivii tutti i campi
            tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[0,1,2,3,4]
            tmp_ControlMap[CONTROLS.PIPJ.value]["active"]=True
            tmp_ControlMap[CONTROLS.PIPJ.value]["indices"]= pip_j_indices

            return tmp_ControlMap
    @classmethod
    def get_two(cls,tipo_intervento,metacarpo_rotto=1):

        tipo_intervento=str(tipo_intervento)
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        pip_j_indices=[]
        pip_j_indices.append(int(metacarpo_rotto))
        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
        tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        # In questo controllo sono attivii tutti i campi
        tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[0,1,2,3,4]
        tmp_ControlMap[CONTROLS.PIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.PIPJ.value]["indices"]= pip_j_indices
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True

        if(tipo_intervento==FrattureMetaCarpaliEnum.CHIRURGICO.value[0]):
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
        tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[0,1,2,3,4]
        tmp_ControlMap[CONTROLS.PIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.PIPJ.value]["indices"]= pip_j_indices
        tmp_ControlMap[CONTROLS.FORZA.value]["indices"]= pip_j_indices
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True

        if(tipo_intervento==FrattureMetaCarpaliEnum.CHIRURGICO.value[0]):
            tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True

        return tmp_ControlMap





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
        print(tipo_intervento==FrattureMetaCarpaliEnum.CHIRURGICO.value[0])
        
        if(tipo_intervento==FrattureMetaCarpaliEnum.NON_CHIRURGICO.value[0]):
            timeline= [0,0,4,8,12,26,52,154,520,1040]
            return timeline
        if (tipo_intervento==FrattureMetaCarpaliEnum.CHIRURGICO.value[0]):
            timeline= [0,1,4,8,12,26,52,154,520,1040]
            return timeline

    #ATTENZIONE RICORDARSI  che weeks_to_first_control che corrispondono alla timeline[0]
    weeks_to_first_control={
        "1":1,
        "2":4
    }

    @classmethod
    def get_pre(cls):
        
        pre_controls_map = copy.deepcopy(cls.Controls_Map_Pre)

        #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        tmp_ControlMap[CONTROLS.DATA_FRATTURA.value]["active"]=True

        return tmp_ControlMap,pre_controls_map

    #Siccome il decorso è diverso per il primo intervento
    # get_one ritorna una mappa solo quando il tipo_intervento è chirurgico
    @classmethod
    def get_one(cls,tipo_intervento,metacarpo_rotto=1):
        tipo_intervento=str(tipo_intervento)

        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)

        if(tipo_intervento==FrattureMetaCarpaliEnum.CHIRURGICO.value[0]):
            pip_j_indices=[]
            pip_j_indices.append(int(metacarpo_rotto))
            tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
            tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
            tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
            tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
            # In questo controllo sono attivii tutti i campi
            tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[0,1,2,3,4]
            tmp_ControlMap[CONTROLS.PIPJ.value]["active"]=True
            tmp_ControlMap[CONTROLS.PIPJ.value]["indices"]= pip_j_indices

            return tmp_ControlMap
    @classmethod
    def get_two(cls,tipo_intervento,metacarpo_rotto=1):

        tipo_intervento=str(tipo_intervento)
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        pip_j_indices=[]
        pip_j_indices.append(int(metacarpo_rotto))
        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
        tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        # In questo controllo sono attivii tutti i campi
        tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[0,1,2,3,4]
        tmp_ControlMap[CONTROLS.PIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.PIPJ.value]["indices"]= pip_j_indices
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True

        if(tipo_intervento==FrattureMetaCarpaliEnum.CHIRURGICO.value[0]):
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
        tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[0,1,2,3,4]
        tmp_ControlMap[CONTROLS.PIPJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.PIPJ.value]["indices"]= pip_j_indices
        tmp_ControlMap[CONTROLS.FORZA.value]["indices"]= pip_j_indices
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True

        if(tipo_intervento==FrattureMetaCarpaliEnum.CHIRURGICO.value[0]):
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

    last_control_number_before_next=2

    @classmethod
    def get_pre(cls):
        
        pre_controls_map = copy.deepcopy(cls.Controls_Map_Pre)
        #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)
        tmp_ControlMap[CONTROLS.DATA_FRATTURA.value]["active"]=True

        return tmp_ControlMap,pre_controls_map
  
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
        tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["indices"]=[1,2,3,4]
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True

        return tmp_ControlMap

     
    @classmethod
    def get_two(cls,pathology_type=None,param=None):

          #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)

        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.EDEMA.value]["active"]=True
        tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["indeces"]=[1,2,3,4]
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True

        return tmp_ControlMap
    
       

    @classmethod
    def get_next(cls,pathology_type=None,param=None):
        """
        Se i controlli sucessivi sono tutti uguali uso una sola funzione
        """
        #deepCopy ctrl_map
        tmp_ControlMap = copy.deepcopy(cls.Controls_Map)

        tmp_ControlMap[CONTROLS.VAS.value]["active"]=True
        tmp_ControlMap[CONTROLS.POLSO.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["active"]=True
        tmp_ControlMap[CONTROLS.MPCJ.value]["indeces"]=[1,2,3,4]
        tmp_ControlMap[CONTROLS.FORZA.value]["active"]=True
        tmp_ControlMap[CONTROLS.DASH.value]["active"]=True
        tmp_ControlMap[CONTROLS.PRWHE.value]["active"]=True
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True
        
        return tmp_ControlMap


class RizoartrosiControlsTimeline(PathologyTimline):

    #Variabile definita per ogni controllo. Indica se il percorso
    #post operatorio è unico o no
    decorso_unico=True
    #Il primo valore è sempre 0 perchè rispecchia il momento dell'intervento
    timeline= [0,3,6,12,26,52,154,520,1040]

    # Numero che corrisponde al numero di controlli implementati
    # dopo di che sono tutti uguali e sono chiamati con il methodo get_next
    last_control_number_before_next=1

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
        
        pre_controls_map = copy.deepcopy(cls.Controls_Map_Pre)

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

        return tmp_ControlMap,pre_controls_map
    
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
    def get_next(cls,pathology_type=None,param=None):

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
        tmp_ControlMap[CONTROLS.SENSIBILITA_VOLARE.value]["active"]=True
        tmp_ControlMap[CONTROLS.CICATRICE.value]["active"]=True
    
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
value[5]: enum per le opzioni pre intervento. Se None non devo salvare nessun dato

PATHOLOGY_LABEL serve per tenere traccia delle label. In questo modo posso usare un enum
per generare il dict delle patologie pre in modo da avere dei parameteri diversi rispetto
a quelli generali che posso salvare a seconda della patologia
"""

class PATHOLOGY(Enum):
    
    RIZOARTROSI= (1,
                  PATHOLOGY_LABEL.RIZOARTROSI.value,
                  RizoartrosiControlsTimeline,
                  RizoartrosiChirurgicoForm,
                  RizoartrosiEnum,
                  None)
    FRATTURA_RADIO_DISTALE= (2,
                             PATHOLOGY_LABEL.FRATTURA_RADIO_DISTALE.value,
                             FrattureRadioDistaliTimeline,
                             FratturaRadioDistaleChirurgicoForm,
                             FratturaRadioDistaleEnum,
                             None)
    FRATTURE_METACARPALI = (3,
                            PATHOLOGY_LABEL.FRATTURE_METACARPALI.value,
                            FratturaMetaCarpaleTimeline,
                            FratturaMetaCarpaliChirurgicoForm,
                            FrattureMetaCarpaliEnum,
                            None)
    FRATTURE_FALANGE_PROSSIMALE = (4,
                                    PATHOLOGY_LABEL.FRATTURE_FALANGE_PROSSIMALE.value,
                                    FrattureFalangeProssimaleTimeline,
                                    FratturaFalangeProssimaleChirurgicoForm,
                                    FrattureFalangeProssimaleEnum,
                                    None)
    LESIONE_TENDINEA_FLESSORI = (5,
                                PATHOLOGY_LABEL.LESIONE_TENDINEA_FLESSORI.value,
                                LesioneTendineaFlessoriTimeline,
                                LesioneTendineaFlessoriChirurgicoForm,
                                LesioneTendineaFlessoriEnum,
                                None)
    RESEZIONE_FILIERA= (6,
                         PATHOLOGY_LABEL.RESEZIONE_FILIERA.value,
                         ResezioneFilieraTimeline,
                         ResezioneFilieraChirurgicoForm,
                         ResezioneFilieraEnum,
                         PreResezioneFileraForm)
    DUPUYTREN= (7,
                 PATHOLOGY_LABEL.DUPUYTREN.value,
                 DupuytrenTimeline,
                 DupuytrenChirurgicoForm,
                 DupuytrenEnum,
                 PreDupuytrenForm)
    LESIONE_NERVOSA=(8,
                      PATHOLOGY_LABEL.LESIONE_NERVOSA.value,
                      LesioneNervosaTimeline,
                      None,
                      None,
                      None)
    SCAFOIDE_FRATTURA= (9,
                         PATHOLOGY_LABEL.SCAFOIDE_FRATTURA.value,
                         ScafoideFratturaTimeline,
                         ScafoideFratturaChirurgicoForm,
                         ScafoideFratturaEnum,
                        None)
    SCAFOIDE_PSEUDOARTROSI= (10,
                              PATHOLOGY_LABEL.SCAFOIDE_PSEUDOARTROSI.value,
                              ScafoidePseudoartrosiTimeline,
                              ScafoidePseudoArtrosiChirurgicoForm,
                              ScafoidePseudortrosiEnum,
                              None)
    LESIONE_LIGAMENTOSA= (11,
                           PATHOLOGY_LABEL.LESIONE_LIGAMENTOSA.value,
                           LesioneLigamentosaTimeline,
                           LesioneLigamentosaChirurgicoForm,
                           LesioneLigamentosaEnum,
                           PreLesioneLigamentosaForm)
    LESIONE_TENDINEA_ESTENSORI = (12,
                                PATHOLOGY_LABEL.LESIONE_TENDINEA_ESTENSORI.value,
                                LesioneTendineaEstensoriTimeline,
                                None,
                                None,
                                None)
        


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
    FERITA_TENDINEA_TENDINE_FLESSORE = (11,PATHOLOGY.LESIONE_TENDINEA_FLESSORI, "Tendine Flessore")
    FERITA_TENDINEA_TENDINE_ESTENSORE = (12,PATHOLOGY.LESIONE_TENDINEA_ESTENSORI, "Tendine Estensore")




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