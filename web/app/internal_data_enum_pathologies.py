# questo file DEVE racchiudere solo gli Enum delle patologie che hanno un decorso post operatorio 
# diverso in base alle opzioni selezionate durante la fase di compilazione del form intervento
from enum import Enum


class RizoartrosiEnum(Enum):
    """
    [0]= Valore salvato a db nel campo pathology_data.id_pathology_type
    [1]= Visualizzato nel form
    """        
    TRAPEZIECTOMIA_ARTOPLASTICA=('1', 'Trapeziectomia più artroplastica in sospensione con abduttore lungo del pollice')
    PROTESI=('2', 'Protesi Touch')
    TRAPEZIECTOMIA = ('3', 'trapeziectomia')
    TRAPEZIECTOMIA_FLESSORE= ('4', 'trapeziectomia più artroplastica con flessore radiale del carpo')
    TRAPEZIECTOMIA_TIGHT =('5', 'trapeziectomia più tight rope')
    EMITRAPEZIECOTIMA = ('6', 'emitrapeziectomia,')
    
# In base a questi valori avrò un decorso post operatorio diverso
class FrattureMetaCarpaliEnum(Enum):
    """
    [0]= Valore salvato a db nel campo pathology_data.id_pathology_type
    [1]= Visualizzato nel form
    """       
    CHIRURGICO = ("1","chirurgico")
    NON_CHIRURGICO = ("2","non chirugico")

class FrattureFalangeProssimaleEnum(Enum):
    """
    [0]= Valore salvato a db nel campo pathology_data.id_pathology_type
    [1]= Visualizzato nel form
    """       
    CHIRURGICO = ("1","chirurgico")
    NON_CHIRURGICO = ("2","non chirugico")

class ResezioneFilieraEnum(Enum):
    """
    [0]= Valore salvato a db nel campo pathology_data.id_pathology_type
    [1]= Visualizzato nel form
    """       
    CHIRURGICO = ("1","chirurgico")
    CONSERVATIVO = ("2","conservativo")

# In base a questi valori avrò un decorso post operatorio diverso
class ScafoideFratturaEnum(Enum):
    """
    [0]= Valore salvato a db nel campo pathology_data.id_pathology_type
    [1]= Visualizzato nel form
    """        
    CHIRURGICO = ("1","chirurgico")
    CONSERVATIVO = ("2","conservativo")

# In base a questi valori avrò un decorso post operatorio diverso
class ScafoidePseudortrosiEnum(Enum):
    """
    [0]= Valore salvato a db nel campo pathology_data.id_pathology_type
    [1]= Visualizzato nel form
    """        
    OPEN = ("1","open")
    OPEN_ASSISTENZA = ("2","open assistenza artroscopica")
    ARTROSCOPICO = ("3","artroscopico")

class DupuytrenEnum(Enum):
    """
    [0]= Valore salvato a db nel campo pathology_data.id_pathology_type
    [1]= Visualizzato nel form
    """        
    APONEVRECTOMIA_OPEN = ("1","aponevrectomia segmentale open")
    APONEVRECTOMIA_INNESTO = ("2","aponevrectomia con innesto cutaneo")
    CORDOTOMIA = ("3","Cordotomia")
    ALTRO = ("4","Altro")

class LesioneLigamentosaEnum(Enum):
    """
    [0]= Valore salvato a db nel campo pathology_data.id_pathology_type
    [1]= Visualizzato nel form
    """        
    CHIRURGICO = ("1","chirurgico")
    CONSERVATIVO = ("2","conservativo")

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
    GUARIGIONE_OSSEA = "guarigione_ossea"
    CONCESSO_INIZIO_MOBILIZZAZIONE = "concesso_inizio_mobilizzazione"
    ARTICOLAZIONE_STABILE = "articolazione_stabile"
   

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

class PATHOLOGY_LABEL(Enum):
    RIZOARTROSI= "rizoartrosi"    
    FRATTURA_RADIO_DISTALE= "frattura_radio_distale"
    FRATTURE_METACARPALI = "fratture_metacarpali"
    FRATTURE_FALANGE_PROSSIMALE = "fratture_falange_prossimale"
    FERITA_LESIONE_TENDINEA = "ferita_lesione_tendinea"
    RESEZIONE_FILIERA= "resezione_filiera"
    DUPUYTREN= "dupuytren"
    LESIONE_NERVOSA="lesione_nervosa"
    SCAFOIDE_FRATTURA= "scafoide_frattura"
    SCAFOIDE_PSEUDOARTROSI= "scafoide_pseudoartrosi"
    LESIONE_LIGAMENTOSA= "lesione_ligamentosa"