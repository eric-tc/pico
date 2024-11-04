# questo file DEVE racchiudere solo gli Enum delle patologie che hanno un decorso post operatorio 
# diverso in base alle opzioni selezionate durante la fase di compilazione del form intervento
from enum import Enum

# In base a questi valori avrò un decorso post operatorio diverso
class FrattureMetaCarpaliEnum(Enum):
    CHIRURGICO = "1"
    NON_CHIRURGICO = "2"

class FrattureFalangeProssimaleEnum(Enum):
    CHIRURGICO = "1"
    NON_CHIRURGICO = "2"

# In base a questi valori avrò un decorso post operatorio diverso
class ScafoideFratturaEnum(Enum):
    """
    [0]= Nome usato per selezionare il controllo
    [1]= Valore usato per salvare a db il numero nella tabella pathology_data.id_pathology_type
    """        
    CHIRURGICO = ("chirurgico","1")
    CONSERVATIVO = ("conservativo","2")

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