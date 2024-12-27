from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField,IntegerField,TextAreaField
from wtforms.validators import DataRequired, Length,NumberRange
from wtforms.fields import DateField,TimeField,SelectField,HiddenField,FieldList,FormField,FloatField
from .internal_data_enum_pathologies import CONTROLS,OPTION_NULL



"""
Struttura di riferimento per i valori dei campi.
I numeri rappresentano il valore delle dita

mpcj={"mpcj":
      {1:{
    "Arom_Estensione": "Arom MCPJ",
    "Arom_Flessione": "Arom MCPJ",
    "Prom_Estensione": "Prom MCPJ",
    "Prom_Flessione": "Prom MCPJ"
    },
    2:{
    "Arom_Estensione": "Arom MCPJ",
    "Arom_Flessione": "Arom MCPJ",
    "Prom_Estensione": "Prom MCPJ",
    "Prom_Flessione": "Prom MCPJ"
    },
    3:{
    "Arom_Estensione": "Arom MCPJ",
    "Arom_Flessione": "Arom MCPJ",
    "Prom_Estensione": "Prom MCPJ",
    "Prom_Flessione": "Prom MCPJ"
    }
    
    }
    }

    
ATTENZIONE Affinchè il NumberRange funzioni correttamente bisogna inserire 'type': 'number', 'max': '120.0'
"""
#Form per gestire i valori
class AromPromForm(FlaskForm):
    #VALIDATORS
    # arom_estensione = FloatField("Arom Estensione",render_kw={'class': 'form-control','type': 'number', 'min':'-120.0', 'max': '120.0'}, validators=[DataRequired(),NumberRange(min=-120.0, max=120.0)])
    # arom_flessione = FloatField("Arom Flessione", render_kw={'class': 'form-control','type': 'number', 'min':'-120.0', 'max': '120.0'},validators=[DataRequired(),NumberRange(min=-120.0, max=120.0)])
    # prom_estensione = FloatField("Prom Estensione", render_kw={'class': 'form-control','type': 'number','min':'-120.0', 'max': '120.0'},validators=[DataRequired(),NumberRange(min=-120.0, max=120.0)])
    # prom_flessione = FloatField("Prom Flessione", render_kw={'class': 'form-control','type': 'number', 'min':'-120.0', 'max': '120.0'},validators=[DataRequired(),NumberRange(min=-120.0, max=120.0)])

    arom_estensione = FloatField("Arom Estensione",render_kw={'class': 'form-control','type': 'number', 'min':'-120.0', 'max': '120.0'})
    arom_flessione = FloatField("Arom Flessione", render_kw={'class': 'form-control','type': 'number', 'min':'-120.0', 'max': '120.0'})
    prom_estensione = FloatField("Prom Estensione", render_kw={'class': 'form-control','type': 'number','min':'-120.0', 'max': '120.0'})
    prom_flessione = FloatField("Prom Flessione", render_kw={'class': 'form-control','type': 'number', 'min':'-120.0', 'max': '120.0'})

class AromPromPolsoForm(AromPromForm):

    # arom_supinazione = FloatField("Arom Supinazione", render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '120.0'},validators=[DataRequired(),NumberRange(min=0.0, max=100.0)])
    # arom_pronazione = FloatField("Arom Pronazione", render_kw={'class': 'form-control','type': 'number','min':'0.0', 'max': '120.0'},validators=[DataRequired(),NumberRange(min=0.0, max=100.0)])
    # prom_supinazione = FloatField("Prom Supinazione", render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '120.0'},validators=[DataRequired(),NumberRange(min=0.0, max=100.0)])
    # prom_pronazione = FloatField("Prom Pronazione", render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '120.0'},validators=[DataRequired(),NumberRange(min=0.0, max=100.0)])

    arom_supinazione = FloatField("Arom Supinazione", render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '120.0'})
    arom_pronazione = FloatField("Arom Pronazione", render_kw={'class': 'form-control','type': 'number','min':'0.0', 'max': '120.0'})
    prom_supinazione = FloatField("Prom Supinazione", render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '120.0'})
    prom_pronazione = FloatField("Prom Pronazione", render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '120.0'})

class TrapezioMetacarpicaForm(FlaskForm):

    # anteposizione = FloatField('Anteposizione',render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '120.0'}, validators=[DataRequired(),NumberRange(min=0.0, max=120.0)])
    # abduzione = FloatField('Abduzione', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '120.0'}, validators=[DataRequired(),NumberRange(min=0.0, max=120.0)])
    # kapandji = FloatField('Pinch',render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '120.0'}, validators=[DataRequired(),NumberRange(min=0.0, max=10.0)])

    anteposizione = FloatField('Anteposizione',render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '120.0'})
    abduzione = FloatField('Abduzione', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '120.0'})
    kapandji = FloatField('Pinch',render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '120.0'})

class ForzaForm(FlaskForm):

    # key_pinch = FloatField('Key Pinch(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'}, validators=[DataRequired(),NumberRange(min=0.0, max=100.0)])
    # tip_to_pinch= FloatField('Tip to Pinch(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'}, validators=[DataRequired(),NumberRange(min=0.0, max=100.0)])
    # misurazione_1_finger = FloatField('Misurazione 1 Finger(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'}, validators=[DataRequired(),NumberRange(min=0.0, max=100.0)])
    # misurazione_2_finger = FloatField('Misurazione 2 Finger(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'}, validators=[DataRequired(),NumberRange(min=0.0, max=100.0)])
    # misurazione_3_finger = FloatField('Misurazione 3 Finger(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'}, validators=[DataRequired(),NumberRange(min=0.0, max=100.0)])
    # three_fingers_pinch = FloatField('Three Fingers Pinch(Kg)', render_kw={'class': 'form-control','readonly': True,'type': 'number', 'min':'0.0', 'max': '100.0'}, validators=[DataRequired(),NumberRange(min=0.0, max=100.0)])
    # misurazione_1_grip= FloatField('Misurazione 1 Grip(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'}, validators=[DataRequired(),NumberRange(min=0.0, max=100.0)])
    # misurazione_2_grip = FloatField('Misurazione 2 Grip(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'}, validators=[DataRequired(),NumberRange(min=0.0, max=100.0)])
    # misurazione_3_grip = FloatField('Misurazione 3 Grip(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'}, validators=[DataRequired(),NumberRange(min=0.0, max=100.0)])
    # grip = FloatField('Grip(Kg)', render_kw={'class': 'form-control','readonly': True,'type': 'number', 'min':'0.0', 'max': '100.0'}, validators=[DataRequired(),NumberRange(min=0.0, max=100.0)])


    key_pinch = FloatField('Key Pinch(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    tip_to_pinch= FloatField('Tip to Pinch(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    misurazione_1_finger = FloatField('Misurazione 1 Finger(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    misurazione_2_finger = FloatField('Misurazione 2 Finger(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    misurazione_3_finger = FloatField('Misurazione 3 Finger(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    three_fingers_pinch = FloatField('Three Fingers Pinch(Kg)', render_kw={'class': 'form-control','readonly': True,'type': 'number', 'min':'0.0', 'max': '100.0'})
    misurazione_1_grip= FloatField('Misurazione 1 Grip(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    misurazione_2_grip = FloatField('Misurazione 2 Grip(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    misurazione_3_grip = FloatField('Misurazione 3 Grip(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    grip = FloatField('Grip(Kg)', render_kw={'class': 'form-control','readonly': True,'type': 'number', 'min':'0.0', 'max': '100.0'})
    

class CicatriceForm(FlaskForm):
    aderente = SelectField('Aderente', choices=[(1, 'Si'), (0, 'No')], default=0, render_kw={'class': 'form-control'}, validators=None)
    distasi_ferita = SelectField('Distasi Ferita', choices=[(1, 'Si'), (0, 'No')], default=0, render_kw={'class': 'form-control'}, validators=None)
    tinel = SelectField('Tinel', choices=[(1, 'Si'), (0, 'No')], default=0, render_kw={'class': 'form-control'}, validators=None)

class AltroForm(FlaskForm):
    complicanze = SelectField('Complicanze', choices=[('CRPS', 'CRPS'), ('infenzione', 'infenzione'),("problematiche_nervose", 'problematiche nervose'),("problematiche tendinee", 'problematiche tendinee')], default="CRPS", render_kw={'class': 'form-control'}, validators=None)
    note= StringField('Note', render_kw={'class': 'form-control'}, validators=None)

class GuarigioneOsseaForm(FlaskForm):
    guarigione = SelectField('Guarigione Ossea', choices=[(1, 'Si'), (0, 'No')], default=0, render_kw={'class': 'form-control'}, validators=None)
    data_guarigione = StringField('Data Guarigione', render_kw={'class': 'form-control-custom','readonly':True}, validators=None)
    options = SelectField('Opzioni', choices=[("radiografia", 'radiografia'), ("tomogragia_computerizzata", 'tomogragia computerizzata'),("risonanza_magnetica", 'risonanza magnetica')], default="radiografia", render_kw={'class': 'form-control'}, validators=None) 


class PrwheForm(FlaskForm):

    #DOLORE
    # dolore_riposo = IntegerField('A riposo [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},validators=[DataRequired(),NumberRange(min=1, max=10)])
    # dolore_movimenti_ripetuti = IntegerField('Eseguendo Movimenti Ripetuti del polso Mano [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},validators=[DataRequired(),NumberRange(min=1, max=10)])
    # dolore_sollevando = IntegerField('Sollevando un oggetto pesante [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},validators=[DataRequired(),NumberRange(min=1, max=10)])
    # dolore_piu_male = IntegerField('Quando fa più male', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},validators=[DataRequired(),NumberRange(min=1, max=10)])
    # dolore_avverto_dolore = IntegerField('Quanto spesso avverte dolore', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},validators=[DataRequired(),NumberRange(min=1, max=10)])
    
    # #FUNZIONE. Le funzioni sono divise in a e b per il calcolo PRWHE
    # funzionea_maniglia = IntegerField('Girare la maniglia di una porta usando la mano malata [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},validators=[DataRequired(),NumberRange(min=1, max=10)])
    # funzionea_tagliare = IntegerField('Tagliare la carne tenendo il coltello con la mano malata [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},validators=[DataRequired(),NumberRange(min=1, max=10)])
    # funzionea_bottoni = IntegerField('Allacciare i bottoni della camicia [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},validators=[DataRequired(),NumberRange(min=1, max=10)])
    # funzionea_sedia = IntegerField('Sollevarsi da una sedia, spingendosi sulla mano malata [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},validators=[DataRequired(),NumberRange(min=1, max=10)])
    # funzionea_portare_oggetto = IntegerField('Portare un oggetto del peso di circa 5 kg con la mano malata [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},validators=[DataRequired(),NumberRange(min=1, max=10)])
    # funzionea_carta_igienica = IntegerField('Usare la carta igienica con la mano malata [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},validators=[DataRequired(),NumberRange(min=1, max=10)])

    # funzioneb_cura_persona = IntegerField('Attività di cura della propria persona (vestirsi, lavarsi, etc) [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},validators=[DataRequired(),NumberRange(min=1, max=10)])
    # funzioneb_lavori_domestici = IntegerField('Lavori domestici [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},validators=[DataRequired(),NumberRange(min=1, max=10)])
    # funzioneb_lavoro = IntegerField('Lavoro (occupazione o lavoro giornaliero) [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},validators=[DataRequired(),NumberRange(min=1, max=10)])
    # funzioneb_attivita_ricreative = IntegerField('Attività ricreative e del tempo libero [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},validators=[DataRequired(),NumberRange(min=1, max=10)])
    
    # #ASPETTO ESTETICO
    # aderente = SelectField('Quanto è importante l’aspetto estetico del suo polso o mano?', choices=[("molto", 'Molto'), ("per_nulla", 'Per Nulla'),("abbastanza", 'Abbastanza')], default=0, render_kw={'class': 'form-control-grid'}, validators=None)
    # aspetto_estetico = IntegerField('Aspetto Estetico [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},validators=[DataRequired(),NumberRange(min=1, max=10)])

    # valore_prwhe =FloatField('Valore PRWHE', render_kw={'class': 'form-control-grid','type': 'number', 'min':'0.0', 'max': '100.0'},validators=[DataRequired(),NumberRange(min=0.0, max=100.0)])


    dolore_riposo = IntegerField('A riposo [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'})
    dolore_movimenti_ripetuti = IntegerField('Eseguendo Movimenti Ripetuti del polso Mano [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'})
    dolore_sollevando = IntegerField('Sollevando un oggetto pesante [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'})
    dolore_piu_male = IntegerField('Quando fa più male', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'})
    dolore_avverto_dolore = IntegerField('Quanto spesso avverte dolore', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'})
    
    #FUNZIONE. Le funzioni sono divise in a e b per il calcolo PRWHE
    funzionea_maniglia = IntegerField('Girare la maniglia di una porta usando la mano malata [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'})
    funzionea_tagliare = IntegerField('Tagliare la carne tenendo il coltello con la mano malata [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'})
    funzionea_bottoni = IntegerField('Allacciare i bottoni della camicia [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'})
    funzionea_sedia = IntegerField('Sollevarsi da una sedia, spingendosi sulla mano malata [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'})
    funzionea_portare_oggetto = IntegerField('Portare un oggetto del peso di circa 5 kg con la mano malata [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'})
    funzionea_carta_igienica = IntegerField('Usare la carta igienica con la mano malata [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'})

    funzioneb_cura_persona = IntegerField('Attività di cura della propria persona (vestirsi, lavarsi, etc) [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'})
    funzioneb_lavori_domestici = IntegerField('Lavori domestici [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'})
    funzioneb_lavoro = IntegerField('Lavoro (occupazione o lavoro giornaliero) [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'})
    funzioneb_attivita_ricreative = IntegerField('Attività ricreative e del tempo libero [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'})
    
    #ASPETTO ESTETICO
    aderente = SelectField('Quanto è importante l’aspetto estetico del suo polso o mano?', choices=[("molto", 'Molto'), ("per_nulla", 'Per Nulla'),("abbastanza", 'Abbastanza')], default="molto", render_kw={'class': 'form-control-grid'}, validators=None)
    aspetto_estetico = IntegerField('Aspetto Estetico [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},)

    valore_prwhe =FloatField('Valore PRWHE', render_kw={'class': 'form-control-grid','type': 'number', 'min':'0.0', 'max': '100.0'})


class DashForm(FlaskForm):
    
    #0
    svitare_coperchio = IntegerField('Svitare il coperchio di un barattolo ben chiuso o nuovo. [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    scrivere = IntegerField('Scrivere [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    girare_chiave = IntegerField('Girare una chiave  [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    preparare_pasto = IntegerField('Preparare un pasto ', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    aprire_porta_pesante = IntegerField('Aprire spingendo una porta pesante ', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    
    #5    
    posare_oggetto = IntegerField('Posare un oggetto su uno scaffale al di sopra della propria testa  [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    fare_lavori_domestici = IntegerField('Fare lavori domestici pesanti (es. lavare i pavimenti o i vetri)  [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    fare_lavori_giardinaggio = IntegerField('Fare lavori di giardinaggio (es. lavare i pavimenti o i vetri)  [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    rifare_letto = IntegerField('Rifare il letto [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    portare_borsa = IntegerField('Portare la borsa della spesa o una ventiquattrore [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    
    #10
    portare_oggetto = IntegerField('Portare un oggetto pesante (oltre 5 Kg) [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    cambio_lampadina = IntegerField('Cambiare una lampadina posta al di sopra della propria testa [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    lavarsi_capelli = IntegerField('Lavarsi o asciugarsi i capelli (vestirsi, lavarsi, etc) [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    lavarsi_schiena = IntegerField('Lavarsi la schiena [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    Infilare_maglione = IntegerField('Infilarsi un maglione [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    
    #15
    usare_coltello = IntegerField('Usare un coltello per tagliare del cibo [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    attivita_ricreative = IntegerField('Attività ricreative che richiedono poco sforzo (es. giocare a carte,lavorare a maglia) [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    attivita_colpi_braccio = IntegerField('Attività ricreative nelle quali si fa forza o si prendono colpi sul braccio, sulla spalla o sulla mano (es. usare il martello, giocare atennis o a golf, ecc [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    attivita_mov_libero = IntegerField('Attività ricreative che richiedono un movimento libero del braccio(es. giocare a frisbee, a badminton, ecc.)  [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    necessita_spostamento = IntegerField('Far fronte alle necessità di spostamento (andare da un posto ad un altro) [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    
    #20
    att_sesso = IntegerField('Attività sessuale [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    sett_passata = IntegerField('Durante la settimana passata, in che misura il suo problema al braccio, alla spalla o alla mano ha interferito con le normali attività sociali con la famiglia, gli amici, i vicini di casa i gruppi di cui fa parte?  [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    durante_settimana = IntegerField('Durante la settimana passata è stato limitato nel suo lavoro o in altre attività quotidiane abituali a causa del suo problema al braccio, alla spalla o alla mano? [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    dolore_braccio = IntegerField('Dolore al braccio, alla spalla o alla mano [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    dolore_braccio_attivita = IntegerField('Dolore al braccio, alla spalla o alla mano nel compiere una qualsiasi attività specifica  [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    
    #25
    formicolio = IntegerField('Formicolio (sensazione di punture di spillo) al braccio, alla spalla o alla mano [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    debolezza_braccio = IntegerField('Debolezza al braccio, alla spalla o alla mano  [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    rigidita_braccio = IntegerField('Rigidità del braccio, della spalla o della mano [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    difficolta_dormire = IntegerField('Durante ultima settimana quanta difficoltà ha incontrato nel dormire a causa del dolore al braccio, alla spalla o alla mano? [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    meno_utile = IntegerField('Mi sento meno capace, meno fiducioso o meno utile a causa del mio problema al braccio, alla spalla o alla mano  [Minimo 0- Massimo 5]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '5'})
    

class TreatmentForm(FlaskForm):

    #1
    mpcj = FieldList(FormField(AromPromForm),label="MCPJ", min_entries=5, max_entries=5)
    
    pipj = FieldList(FormField(AromPromForm), render_kw={'class': 'form-control'},min_entries=5, max_entries=5)
    dipj = FieldList(FormField(AromPromForm), render_kw={'class': 'form-control'},min_entries=5, max_entries=5)
    ipj = FieldList(FormField(AromPromForm), render_kw={'class': 'form-control'},min_entries=5, max_entries=5)
    
    #2
    polso = FieldList(FormField(AromPromPolsoForm),render_kw={'class': 'form-control'}, min_entries=1, max_entries=1)

    #3
    vas = FloatField('vas', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '120.0'})

    #
    trapezio_metacarpale= FieldList(FormField(TrapezioMetacarpicaForm),min_entries=1, max_entries=1)

    #5
    forza= FieldList(FormField(ForzaForm), min_entries=1, max_entries=1)
    
    #6
    dash = FieldList(FormField(DashForm), min_entries=1, max_entries=1)
    
    #7
    prwhe = FieldList(FormField(PrwheForm), min_entries=1, max_entries=1)
    
    #8
    eaton_littler = IntegerField(CONTROLS.EATON_LITTLER.value + "Valori [0,4]", render_kw={'class': 'form-control','type': 'number', 'min':'0', 'max': '4'} )
    
    #9
    sensibilita_volare = HiddenField('sensibilita_volare', render_kw={'class': 'form-control'}, validators=None)
    
    sensibilita_dorsale = HiddenField('sensibilita_dorsale', render_kw={'class': 'form-control'}, validators=None)
    
    #10
    edema = SelectField('Edema', choices=[(1, 'Si'), (0, 'No')], default=0, render_kw={'class': 'form-control'}, validators=None)
    
    #11
    cicatrice =  FieldList(FormField(CicatriceForm),min_entries=1, max_entries=1)
    
    #12
    tutore = SelectField('Tutore', choices=[(1, 'SI'), (0, 'No'),(2,"Altro")], default=0, render_kw={'class': 'form-control'}, validators=None)
    #13
    altro = FieldList(FormField(AltroForm),min_entries=1, max_entries=1)

    #14
    guarigione_ossea = FieldList(FormField(GuarigioneOsseaForm),min_entries=1, max_entries=1)

    #15
    concesso_inizio_mobilizzazione = SelectField('Concesso Inizio Mobilizzazione', choices=[(1, 'Yes'), (0, 'No')], default=0, render_kw={'class': 'form-control'}, validators=None)

    #16
    articolazione_stabile = SelectField('Articolazione Stabile', choices=[(1, 'Yes'), (0, 'No')], default=0, render_kw={'class': 'form-control'}, validators=None)

    #17
    data_inizio_mobilizzazione = StringField('Data Inizio Mobilizzazione Attiva', render_kw={'class': 'form-control-custom','readonly':True}, validators=None)

    submit_form = SubmitField("Submit", render_kw={'class': 'btn btn-primary',"style":"max-width: 200px;"})

    def __init__(self, selected_indices=None,controls_map=None, *args, **kwargs):
        super(TreatmentForm, self).__init__(*args, **kwargs)
        self.controls_map = controls_map
        self.max_indeces = [] #indici non esclusi di default


    def validate_eaton_littler(self,value=None):
            
            self.eaton_littler.validators = []

    def validate_vas(self,value=None):

        self.vas.validators = []     

    def validate_trapezio_metacarpale(self,value=None):

         for index, subform in enumerate(self.trapezio_metacarpale):

            # Remove validators for fields that are not rendered (not visible)
            subform.anteposizione.validators = []
            subform.abduzione.validators = []
            subform.kapandji.validators = []

    #Metodo definito da flask_form per la validazione dei campi
    def validate_forza(self,value=None):
        
        for index, subform in enumerate(self.forza):

            # Remove validators for fields that are not rendered (not visible)
            subform.key_pinch.validators = []
            subform.tip_to_pinch.validators = []
            subform.misurazione_1_finger.validators = []
            subform.misurazione_2_finger.validators = []
            subform.misurazione_3_finger.validators = []
            subform.three_fingers_pinch.validators = []
            subform.misurazione_1_grip.validators = []
            subform.misurazione_2_grip.validators = []
            subform.misurazione_3_grip.validators = []
            subform.grip.validators = []

    def validate_polso(self,value=None):

        
        for index, subform in enumerate(self.polso):

            # Remove validators for fields that are not rendered (not visible)
            subform.form.arom_supinazione.validators = []
            subform.form.arom_pronazione.validators = []
            subform.form.prom_supinazione.validators = []
            subform.form.prom_pronazione.validators = []
            subform.form.arom_estensione.validators = []
            subform.form.arom_flessione.validators = []
            subform.form.prom_estensione.validators = []
            subform.form.prom_flessione.validators = []


    def validate_list(self, value_list,selected_indices):

         for index, subform in enumerate(value_list):
            """
            Quando eseguo la validazione gli indici non seguono i campi selezionati, ma partono sempre dallo 0
            per cui se ho selezionato gli indici selected_indices= [2,3] i campi a cui dovrò togliere la validazione saranno tutti quelli dopo la lunghezza dell'array
            cioè [2,3,4]. Infatti gli indici partono da 0 e contano il numero di elementi presenti.

            In pratica i valori di ritorno sono una lista che parte sempre da indice 0. Tutti gli altri significa che non sono stati visualizzati

            """

            print("selected_indices: ", selected_indices)
            print("len(selected_indices): ", len(selected_indices))
            if index not in range(0, len(selected_indices)):
                print("Index not in selected_indices: ", index)
                # Remove validators for fields that are not rendered (not visible)
                subform.arom_estensione.validators = []
                subform.arom_flessione.validators = []
                subform.prom_estensione.validators = []
                subform.prom_flessione.validators = []

    #Funzione di validazione sovrascritta per disabilitare i validatori in base alla lista degli indici selezionati
    # def validate(self, extra_validators=None):
    #     """
    #     Usato per rendere la validazione attiva solo sugli indici selezionati
    #     """
    #     valid = super(TreatmentForm, self).validate()

    #     #in base alla lista delle controls_map devo disabilitare i validatori

    #     for key, value in self.controls_map.items():
    #         if value["active"] == False:
    #             print("Disabilito il campo: ", key)
                
    #             if key == "mpcj":
    #                 self.validate_list(self.mpcj,self.max_indeces)   
    #             elif key == "dipj":
    #                 self.validate_list(self.dipj,self.max_indeces)
    #             elif key == "pipj":
    #                 self.validate_list(self.pipj,self.max_indeces)
    #             elif key == "ipj":
    #                 self.validate_list(self.ipj,self.max_indeces)
    #             elif key == "polso":
    #                 print("Disabilito il polso")
    #                 self.validate_polso()
    #             elif key == "trapezio_metacarpale":
    #                 print("Disabilito il trapezio_metacarpale")
    #                 self.validate_trapezio_metacarpale()
    #             elif key == "vas":
    #                 print("Disabilito il vas")
    #                 self.validate_vas()
    #             elif key == "forza":
    #                 print("Disabilito il forza")
    #                 self.validate_forza()
    #             elif key == "eaton_littler":
    #                 self.validate_eaton_littler()
            
    #         elif value:
    #             # Se true devo disabilitare gli indici non selezionati
    #             if key == "mpcj":
    #                 self.validate_list(self.mpcj,self.controls_map[key]["indices"])
    #             elif key == "dipj":
    #                 self.validate_list(self.dipj,self.controls_map[key]["indices"])
    #             elif key == "pipj":
    #                 self.validate_list(self.pipj,self.controls_map[key]["indices"])
    #             elif key == "ipj":
    #                 self.validate_list(self.ipj,self.controls_map[key]["indices"])
                
    #     # Perform another validation after updating the validators
    #     return super(TreatmentForm, self).validate()


# class TreatmentForm(FlaskForm):
#     nprs_vas = IntegerField(CONTROLS.NPRS_VAS.value, render_kw={'class': 'form-control'}, validators=None)
#     prom_aprom_mcpj = IntegerField(CONTROLS.PROM_APROM_MCPJ.value, render_kw={'class': 'form-control'}, validators=None)
#     prom_aprom_ipj = IntegerField(CONTROLS.PROM_APROM_IPJ.value, render_kw={'class': 'form-control'}, validators=None)
#     abduzione = IntegerField(CONTROLS.ABDUZIONE.value, render_kw={'class': 'form-control'},  validators=None)
#     anteposizione = IntegerField(CONTROLS.ANTEPOSIZIONE.value, render_kw={'class': 'form-control'},  validators=None)
#     kapandji = IntegerField(CONTROLS.KAPANDJI.value, render_kw={'class': 'form-control'},  validators=None)
#     pinch = IntegerField(CONTROLS.PINCH.value, render_kw={'class': 'form-control'},  validators=None)
#     grip = IntegerField(CONTROLS.GRIP.value, render_kw={'class': 'form-control'},  validators=None)
#     dash = IntegerField(CONTROLS.DASH.value, render_kw={'class': 'form-control'},  validators=None)
#     prwhe = IntegerField(CONTROLS.PRWHE.value, render_kw={'class': 'form-control'},  validators=None)
#     eaton_littler = IntegerField(CONTROLS.EATON_LITTLER.value, render_kw={'class': 'form-control'}, validators=None )
#     stato_cicatrice = StringField(CONTROLS.STATO_CICATRICE.value, render_kw={'class': 'form-control'},  validators=None)
#     tipo_cicatrice = StringField(CONTROLS.TIPO_CICATRICE.value, render_kw={'class': 'form-control'},  validators=None)
#     modena = StringField(CONTROLS.MODENA.value,render_kw={'class': 'form-control'},  validators=None)

#     submit_form = SubmitField("Submit", render_kw={'class': 'btn btn-primary'})

class PreTreamentForm(TreatmentForm):
    # I valori del campo del form devono avere lo stesso valore delle chiavi di CONTROLS
    #in questo modo nella UI posso verificare quando un campo è attivo o meno utilizzando una map dove la chiave
    # è la label:True,False. Vedere pagina next_control
    data_frattura = StringField('Data Frattura', render_kw={'class': 'form-control-custom','readonly':True}, validators=None)


# Per alcune patologie posso aggiungere dei parametri aggiuntivi nei dati pre operatori

class PreDupuytrenForm(FlaskForm):

    numero_interventi = IntegerField('Numero Interventi', render_kw={'class': 'form-control'}, validators=[DataRequired(message="Campo richiesto"),
            NumberRange(min=1, max=20, message="Value must be between 1 and 20.")])
    
    hidden_hand_selection = HiddenField('hidden_hand_selection', render_kw={'class': 'form-control'}, validators=None)

class PreLesioneLigamentosaForm(FlaskForm):
    
    hidden_lesione_selection = HiddenField('hidden_lesione_selection', render_kw={'class': 'form-control'}, validators=None)



class PreResezioneFileraForm(FlaskForm):

    surgery = SelectField(
        'Seleziona Intervento',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('1', 'SNAC'),
            ('2', 'SLAC'),
            ('3', 'SCAC'),
            ('4', 'Kienbock'),
            ('5', 'Lussazione Inveterata Semilunare'),

        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    classificazione_watson = SelectField(
        'classificazione radiografica',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    
    classificazione_lichman = SelectField(
        'Opzioni Classificazione Radiografica',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('1', '0'),
            ('2', '1'),
            ('3', '2'),
            ('4', '3A'), 
            ('5', '3B'),
            ('6', '3C'), 
            ('7', '4'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    lussazione_lunare = SelectField(
        'Opzioni Classificazione Radiografica',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('1', 'Volare'),
            ('2', 'Dorsale'),
            ('3', 'Altro'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

#Form vecchio probabilmente posso eliminarlo
class PostTreatmentForm(TreatmentForm):
    # I valori del campo del form devono avere lo stesso valore delle chiavi di CONTROLS
    #in questo modo nella UI posso verificare quando un campo è attivo o meno utilizzando una map dove la chiave
    # è la label:True,False. Vedere pagina next_control

     #Questo valore è associato il campo datepicker
    data_controllo = StringField('Data Controllo', render_kw={'class': 'form-control-custom','readonly':True}, validators=None)
    orario_controllo = StringField('Orario Controllo', render_kw={'class': 'form-control'}, validators=None)
    
    #Nei controlli posso anche cambiare solo la data
    submit_change_date = SubmitField("Cambia Data", render_kw={'class': 'btn btn-info'})


    # Hidden Input to handle variable
    pathology_id = HiddenField('Pathology ID', render_kw={'class': 'form-control'}, validators=None)
    patient_id = HiddenField('Patient ID', render_kw={'class': 'form-control'}, validators=None)
    row_id = HiddenField('Row ID', render_kw={'class': 'form-control'}, validators=None)
    patient_name = HiddenField('Patient Name', render_kw={'class': 'form-control'}, validators=None)


class PostScafoideForm(FlaskForm):
    
    guarigione = SelectField(
        'Seleziona Intervento',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('Si', 'Si'),
            ('No', 'No'),
            
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    data_controllo = StringField('Data Guarigione', render_kw={'class': 'form-control-custom','readonly':True}, validators=None)

    esame = SelectField(
        'Seleziona Intervento',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('radiografia', 'radiografia'),
            ('tomografia_computerizzata', 'tomografia_computerizzata'),
            ('risonanza_magnetica', 'risonanza_magnetica'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )



class MedicalTreatmentForm(FlaskForm):
    """
    Questo form gestisce
    """
    entrytime_1 = TimeField('Time',render_kw={'class': 'form-control-custom'})
    




class CustomControlForm(FlaskForm):
    
    note = TextAreaField('Inserisci le tue note',render_kw={'class': 'form-control'}
    )

    submit_custom_control = SubmitField("Inserisci", render_kw={'class': 'btn btn-success',"style":"max-width: 200px;"})
