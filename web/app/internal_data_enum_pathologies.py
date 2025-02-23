# questo file DEVE racchiudere solo gli Enum delle patologie che hanno un decorso post operatorio 
# diverso in base alle opzioni selezionate durante la fase di compilazione del form intervento
from enum import Enum


class RizoartrosiEnum(Enum):
    """
    [0]= Valore salvato a db nel campo pathology_data.id_pathology_type
    [1]= Visualizzato nel form
    """        
    TRAPEZIECTOMIA_ARTOPLASTICA=('1', 'Trapeziectomia e artroplastica in sospensione con abduttore lungo del pollice')
    PROTESI=('2', 'Protesi Touch')
    TRAPEZIECTOMIA = ('3', 'Trapeziectomia')
    TRAPEZIECTOMIA_FLESSORE= ('4', 'Trapeziectomia più artroplastica con flessore radiale del carpo')
    TRAPEZIECTOMIA_TIGHT =('5', 'Trapeziectomia più tight rope')
    EMITRAPEZIECOTIMA = ('6', 'Emitrapeziectomia,')


class FratturaRadioDistaleEnum(Enum):
    GESSO_CHIUSO= ('1', 'Gesso chiuso')
    PLACCA_VITI= ('2', 'Placca e viti')
    FISSATORE_ESTERNO= ('3', 'Fissatore esterno con fili di Kirschner')
    VITI = ('4', 'Viti')
    VALVA_GESSATA = ('5', 'Valva gessata')

# In base a questi valori avrò un decorso post operatorio diverso
class FrattureMetaCarpaliEnum(Enum):
    """
    [0]= Valore salvato a db nel campo pathology_data.id_pathology_type
    [1]= Visualizzato nel form
    """       
    CHIRURGICO = ("1","Chirurgico")
    NON_CHIRURGICO = ("2","Non chirugico")

class FrattureFalangeProssimaleEnum(Enum):
    """
    [0]= Valore salvato a db nel campo pathology_data.id_pathology_type
    [1]= Visualizzato nel form
    """       
    CHIRURGICO = ("1","Chirurgico")
    NON_CHIRURGICO = ("2","Non chirugico")

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
    CHIRURGICO = ("1","Chirurgico")
    CONSERVATIVO = ("2","Conservativo")

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
    OPEN = ("1","Open")
    OPEN_ASSISTENZA = ("2","Open con assistenza artroscopica")
    ARTROSCOPICO = ("3","interamente artroscopico")

class DupuytrenEnum(Enum):
    """
    [0]= Valore salvato a db nel campo pathology_data.id_pathology_type
    [1]= Visualizzato nel form
    """        
    APONEVRECTOMIA_OPEN = ("1","Aponevrectomia segmentale open")
    APONEVRECTOMIA_INNESTO = ("2","Aponevrectomia con innesto cutaneo")
    CORDOTOMIA = ("3","Cordotomia")
    ALTRO = ("4","Altro")

class LesioneNervosaEnum(Enum):
    """
    [0]= Valore salvato a db nel campo pathology_data.id_pathology_type
    [1]= Visualizzato nel form
    """        
    NEURORRAFIA = ("1","Neurorraffia termino-terminale")
    INNESTO = ("2","Innesto")
    ALTRO = ("3","Altro")

class LesioneLigamentosaEnum(Enum):
    """
    [0]= Valore salvato a db nel campo pathology_data.id_pathology_type
    [1]= Visualizzato nel form
    """        
    CHIRURGICO = ("1","Chirurgico")
    CONSERVATIVO = ("2","Conservativo")

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

class DASH_ENUM_FIRST(Enum):
    SVITARE_COPERICHIO = (1,"Svitare coperchio")
    SCRIVERE = (2,"Scrivere")
    GIRARE_CHIAVE = (3,"Girare una chiave")
    PREPARARE_PASTO = (4,"Preparare un pasto")
    APRIRE_PORTA_PESANTE = (5,"Aprire spingendo una porta pesante")
    
    #5
    POSARE_OGGETTO= (6,"Posare un oggetto su uno scaffale al di sopra della propria testa")
    FARE_LAVORI_DOMESTICI= (7,"Fare lavori domestici pesanti (es. lavare i pavimenti o i vetri)")
    LAVORI_GIARDINAGGIO=(8,"Fare lavori di giardinaggio")
    RIFARE_LETTO= (9,"Rifare il letto")
    PORTARE_BORSA= (10,"Portare la borsa della spesa o una ventiquattrore")

    #10
    PORTARE_OGGETTO= (11,"Portare un oggetto pesante (oltre 5 Kg)")
    CAMBIO_LAMPADINA = (12,"Cambiare una lampadina posta al di sopra della propria testa")
    LAVARSI_CAPELLI = (13,"Lavarsi o asciugarsi i capelli")
    LAVARSI_SCHIENA = (14,"Lavarsi la schiena")
    INFILARSI_MAGILIONE= (15,"Infilarsi un maglione")

    #15
    USARE_COLTELLO= (16,"Usare un coltello per tagliare del cibo")
    ATTIVITA_RICREATIVE =(17,"Attività ricreative che richiedono poco sforzo (es. giocare a carte,lavorare a maglia ")
    ATTIVITA_COLPI_BRACCIO= (18,"Attività ricreative nelle quali si fa forza o si prendono colpi sul braccio, sulla spalla o sulla mano (es. usare il martello, giocare a tennis o a golf, ecc.)")
    ATTIVITA_MOV_LIBERO=(19,"Attività ricreative che richiedono un movimento libero del braccio (es. giocare a frisbee, a badminton, ecc.)")
    NECESSITA_SPOSTAMENTO= (20,"Far fronte alle necessità di spostamento (andare da un posto ad un altro)")

    #20

    ATTIVITA_SESSUALE= (21,"Attività sessuale")

class DASH_ENUM_SECOND(Enum):
    PROBLEMA_BRACCIO= (22,"Durante la settimana passata, in che misura il suo problema al braccio, alla spalla o alla mano ha interferito con le normali attività sociali con la famiglia, gli amici, i vicini di casa i gruppi di cui fa parte?")

class DASH_ENUM_THIRD(Enum):
    PROBLEMA_LAVORO= (23,"Durante la settimana passata è stato limitato nel suo lavoro o in altre attività quotidiane abituali a causa del suo problema al braccio, alla spalla o alla mano?")

class DASH_ENUM_FOURTH(Enum):
    DOLORE_BRACCIO= (24,"Dolore al braccio, alla spalla o alla mano")
    DOLORE_BRACCIO_ATT=(25,"Dolore al braccio, alla spalla o alla mano nel compiere una qualsiasi attività specifica")
    FORMICOLIO=(26,"Formicolio (sensazione di punture di spillo) al braccio, alla spalla o alla mano")
    DEBOLEZZA_BRACCIO = (27,"Debolezza al braccio, alla spalla o alla mano")
    RIGIDITA_BRACCIO = (28,"Rigidità del braccio, della spalla o della mano")

class DASH_ENUM_FIFTH(Enum):
    PROBLEMA_DORMIRE= (29,"Durante l'ultima settimana quanta difficoltà ha incontrato nel dormire a causa del dolore al braccio, alla spalla o alla mano? ")

class DASH_ENUM_SIXTH(Enum):
    MENO_CAPACA= (30,"Mi sento meno capace, meno fiducioso o meno utile a causa del mio problema al braccio, alla spalla o alla mano ")


class PWRHE_ENUM_FIRST(Enum):
    DOLORE_RIPOSO= (1,"A riposo")
    DOLORE_MOV_RIPETUTI= (2,"Eseguendo movimenti ripetuti del polso /mano")
    DOLORE_SOLLVEVARE= (3," Sollevando un oggetto pesante")
    QUANTO_MALE= (4,"Quando fa più male")

class PWRHE_ENUM_SECOND(Enum):
    AVVERTO_DOLORE= (5,"Quando avverte dolore")

class PWRHE_ENUM_THIRD(Enum):
    GIRARE_MANIGLIA= (6,"Girare la maniglia di una porta usando la mano malata")
    TAGLIARE_CARNE= (7,"Tagliare la carne tenendo il coltello con la mano malata")
    ALLACCIARE_BOTTONE= (8,"Allacciare i bottoni della camicia")
    SOLLEVARE_SEDIA= (9,"Sollevarsi da una sedia, spingendosi sulla mano malata")
    PORTARE_OGGETTO= (10,"Portare un oggetto del peso di circa 5 kg con la mano malata")
    USARE_CARTA_IGIENICA= (11,"Usare la carta igienica con la mano malata")

class PWRHE_ENUM_FOURTH(Enum):
    CURA_PERSONALE= (12,"Attività di cura della propria persona (vestirsi, lavarsi, etc)")
    LAVORO_DOMESTICO= (13,"Lavori domestici (pulire, sbrigare le faccende)")
    LAVORO= (14,"Lavoro (occupazione o lavoro giornaliero)")
    ATTIVITA_RICREATIVE= (15,"Attività ricreative e del tempo libero")
