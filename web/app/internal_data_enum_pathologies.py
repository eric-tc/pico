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


class FratturaRadioDistaleEnum(Enum):
    GESSO_CHIUSO= ('1', 'gesso chiuso')
    PLACCA_VITI= ('2', 'placca e viti')
    FISSATORE_ESTERNO= ('3', 'fissatore esterno con fili di Kirschner')
    VITI = ('4', 'viti')
    VALVA_GESSATA = ('5', 'valva gessata')

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

class LesioneTendineaFlessoriEnum(Enum):
    """
    [0]= Valore salvato a db nel campo pathology_data.id_pathology_type
    [1]= Visualizzato nel form
    """       
    FLESSORI = ("1","Flessori")

class LesioneTendineaEstensoriEnum(Enum):
    """
    [0]= Valore salvato a db nel campo pathology_data.id_pathology_type
    [1]= Visualizzato nel form
    """       
    FLESSORI = ("1","Estensori")

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
    CHIRURGICO = ("1","Chirurgico")
    CONSERVATIVO = ("2","Conservativo")

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

class LesioneNervosaEnum(Enum):
    """
    [0]= Valore salvato a db nel campo pathology_data.id_pathology_type
    [1]= Visualizzato nel form
    """        
    NEURORRAFIA = ("1","neurorraffia termino-terminale")
    INNESTO = ("2","innesto")
    ALTRO = ("3","Altro")

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
    SENSIBILITA_VOLARE = "sensibilita_volare"
    SENSIBILITA_DORSALE = "sensibilita_dorsale"
    CICATRICE = "cicatrice"
    TUTORE= "tutore"
    ALTRO = "altro"
    GUARIGIONE_OSSEA = "guarigione_ossea"
    CONCESSO_INIZIO_MOBILIZZAZIONE = "concesso_inizio_mobilizzazione"
    ARTICOLAZIONE_STABILE = "articolazione_stabile"
    DATA_INIZIO_MOBILIZZAZIONE = "data_inizio_mobilizzazione"
   

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
    LESIONE_TENDINEA_FLESSORI = "lesione_tendinea_flessori"
    LESIONE_TENDINEA_ESTENSORI = "lesione_tendinea_estensori"
    RESEZIONE_FILIERA= "resezione_filiera"
    DUPUYTREN= "dupuytren"
    LESIONE_NERVOSA="lesione_nervosa"
    SCAFOIDE_FRATTURA= "scafoide_frattura"
    SCAFOIDE_PSEUDOARTROSI= "scafoide_pseudoartrosi"
    LESIONE_LIGAMENTOSA= "lesione_ligamentosa"

class OPTION_NULL(Enum):
    NULL = "Seleziona un'opzione"


# DASH ENUM

class DASH_ENUM(Enum):
    SVITARE_COPERICHIO = "Svitare coperchio"
    SCRIVERE = "Scrivere"
    GIRARE_CHIAVE = "Girare una chiave"
    PREPARARE_PASTO = "Preparare un pasto"
    APRIRE_PORTA_PESANTE = "Aprire spingendo una porta pesante"
    
    #5
    POSARE_OGGETTO= "Posare un oggetto su uno scaffale al di sopra della propria testa"
    FARE_LAVORI_DOMESTICI= "Fare lavori domestici pesanti (es. lavare i pavimenti o i vetri)"
    LAVORI_GIARDINAGGIO="Fare lavori di giardinaggio"
    RIFARE_LETTO= "Rifare il letto"
    PORTARE_BORSA= "Portare la borsa della spesa o una ventiquattrore"

    #10
    PORTARE_OGGETTO= "Portare un oggetto pesante (oltre 5 Kg)"
    CAMBIO_LAMPADINA = "Cambiare una lampadina posta al di sopra della propria testa"
    LAVARSI_CAPELLI = "Lavarsi o asciugarsi i capelli"
    LAVARSI_SCHIENA = "Lavarsi la schiena"
    INFILARSI_MAGILIONE= "Infilarsi un maglione"

    #15
    USARE_COLTELLO= "Usare un coltello per tagliare del cibo"
    ATTIVITA_RICREATIVE ="Attività ricreative che richiedono poco sforzo (es. giocare a carte,lavorare a maglia "
    ATTIVITA_COLPI_BRACCIO= "Attività ricreative nelle quali si fa forza o si prendono colpi sul braccio, sulla spalla o sulla mano (es. usare il martello, giocare a tennis o a golf, ecc.)"
    ATTIVITA_MOV_LIBERO="Attività ricreative che richiedono un movimento libero del braccio (es. giocare a frisbee, a badminton, ecc.)"
    NECESSITA_SPOSTAMENTO= "Far fronte alle necessità di spostamento (andare da un posto ad un altro)"

    #20

    ATTIVITA_SESSUALE= "Attività sessuale"