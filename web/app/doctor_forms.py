from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField,IntegerField,TextAreaField
from wtforms.validators import DataRequired, Length,NumberRange
from wtforms.fields import DateField,TimeField,SelectField,HiddenField,FieldList,FormField,FloatField,RadioField,DecimalField
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
    kapandji = FloatField('Kapandji Score',render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '120.0'})

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

    misurazione_1_pinch = FloatField('Misurazione 1 pinch(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    misurazione_2_pinch = FloatField('Misurazione 1 pinch(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    misurazione_3_pinch = FloatField('Misurazione 1 pinch(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    key_pinch = FloatField('Key Pinch(Kg)', render_kw={'class': 'form-control','readonly': True,'type': 'number', 'min':'0.0', 'max': '100.0'})
    

    misurazione_1_tip = FloatField('Misurazione 1 tip(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    misurazione_2_tip = FloatField('Misurazione 1 tip(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    misurazione_3_tip = FloatField('Misurazione 1 tip(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    tip_to_pinch= FloatField('Tip to Pinch(Kg)', render_kw={'class': 'form-control','readonly': True,'type': 'number', 'min':'0.0', 'max': '100.0'})
    
    misurazione_1_finger = FloatField('Misurazione 1 Finger(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    misurazione_2_finger = FloatField('Misurazione 2 Finger(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    misurazione_3_finger = FloatField('Misurazione 3 Finger(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    three_fingers_pinch = FloatField('Three Fingers Pinch(Kg)', render_kw={'class': 'form-control','readonly': True,'type': 'number', 'min':'0.0', 'max': '100.0'})
    
    misurazione_1_grip= FloatField('Misurazione 1 Grip(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    misurazione_2_grip = FloatField('Misurazione 2 Grip(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    misurazione_3_grip = FloatField('Misurazione 3 Grip(Kg)', render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '100.0'})
    grip = FloatField('Grip(Kg)', render_kw={'class': 'form-control','readonly': True,'type': 'number', 'min':'0.0', 'max': '100.0'})
    

class CicatriceForm(FlaskForm):
    aderente = SelectField('Aderente', choices=[('', OPTION_NULL.NULL.value),(1, 'Si'), (0, 'No')], default=0, render_kw={'class': 'form-control'}, validators=None)
    distasi_ferita = SelectField('Distasi Ferita', choices=[('', OPTION_NULL.NULL.value),(1, 'Si'), (0, 'No')], default=0, render_kw={'class': 'form-control'}, validators=None)
    tinel = SelectField('Tinel', choices=[('', OPTION_NULL.NULL.value),(1, 'Si'), (0, 'No')], default=0, render_kw={'class': 'form-control'}, validators=None)

class AltroForm(FlaskForm):
    complicanze = SelectField('Complicanze', choices=[('CRPS', 'CRPS'), ('infenzione', 'infenzione'),("problematiche_nervose", 'problematiche nervose'),("problematiche tendinee", 'problematiche tendinee')], default="CRPS", render_kw={'class': 'form-control'}, validators=None)
    note= StringField('Note', render_kw={'class': 'form-control'}, validators=None)

class GuarigioneOsseaForm(FlaskForm):
    guarigione = SelectField('Guarigione Ossea', choices=[(1, 'Si'), (0, 'No')], default=0, render_kw={'class': 'form-control'}, validators=None)
    data_guarigione = StringField('Data Guarigione', render_kw={'class': 'form-control-custom','readonly':True}, validators=None)
    options = SelectField('Opzioni', choices=[("radiografia", 'radiografia'), ("tomogragia_computerizzata", 'tomogragia computerizzata'),("risonanza_magnetica", 'risonanza magnetica')], default="radiografia", render_kw={'class': 'form-control'}, validators=None) 



# Da aggiungere nel prwhe
# #ASPETTO ESTETICO
# aderente = SelectField('Quanto è importante l’aspetto estetico del suo polso o mano?', choices=[("molto", 'Molto'), ("per_nulla", 'Per Nulla'),("abbastanza", 'Abbastanza')], default="molto", render_kw={'class': 'form-control-grid'}, validators=None)
# aspetto_estetico = IntegerField('Aspetto Estetico [Minimo 0- Massimo 10]', render_kw={'class': 'form-control-grid','type': 'number', 'min':'1', 'max': '10'},)

# valore_prwhe =FloatField('Valore PRWHE', render_kw={'class': 'form-control-grid','readonly': True,'type': 'number', 'min':'0.0', 'max': '100.0'})

#ESEMPIO DASH

class RowFormDash(FlaskForm):
    options = RadioField(
        'Options',
        choices=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')
        ],
        default='1'
    )

class FirstDash(FlaskForm):
    rows = FieldList(FormField(RowFormDash), min_entries=21)  # 3 rows as an example
    

class SecondDash(FlaskForm):
    rows = FieldList(FormField(RowFormDash), min_entries=1)  # 3 rows as an example
    

class ThirdDash(FlaskForm):
    rows = FieldList(FormField(RowFormDash), min_entries=1)  # 3 rows as an example
    

class FourthDash(FlaskForm):
    rows = FieldList(FormField(RowFormDash), min_entries=5)  # 3 rows as an example

class FifthDash(FlaskForm):
    rows = FieldList(FormField(RowFormDash), min_entries=1)  # 3 rows as an example
RowFormDash
class Sixth(FlaskForm):
    rows = FieldList(FormField(RowFormDash), min_entries=1)  # 3 rows as an example
    


class DashForm(FlaskForm):


    first_dash= FormField(FirstDash)
    second_dash= FormField(SecondDash)
    third_dash= FormField(ThirdDash)
    fourth_dash= FormField(FourthDash)
    fifth_dash= FormField(FifthDash)
    sixth_dash= FormField(Sixth)

#PRWHE

class RowFormPrwhe(FlaskForm):
    options = RadioField(
        'Options',
        choices=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10'),
        ],
        default='1'
    )

class FirstPrwhe(FlaskForm):
    rows = FieldList(FormField(RowFormPrwhe), min_entries=4)  # 3 rows as an example
    

class SecondPrwhe(FlaskForm):
    rows = FieldList(FormField(RowFormPrwhe), min_entries=1)  # 3 rows as an example


class ThirdPrwhe(FlaskForm):
    rows = FieldList(FormField(RowFormPrwhe), min_entries=6)  # 3 rows as an example

class FourthPrwhe(FlaskForm):
    rows = FieldList(FormField(RowFormPrwhe), min_entries=4)  # 3 rows as an example

class PrwheForm(FlaskForm):
    first_prwhe= FormField(FirstPrwhe)
    second_prwhe= FormField(SecondPrwhe)
    third_prwhe= FormField(ThirdPrwhe)
    fourth_prwhe= FormField(FourthPrwhe)


class DashFormTest(FlaskForm):
    
    dash = FormField(DashForm)
    submit = SubmitField("Submit", render_kw={'class': 'btn btn-primary',"style":"max-width: 200px;"})


class TreatmentForm(FlaskForm):

    #1
    mpcj = FieldList(FormField(AromPromForm),label="MCPJ", min_entries=5, max_entries=5)
    
    pipj = FieldList(FormField(AromPromForm), render_kw={'class': 'form-control'},min_entries=5, max_entries=5)
    dipj = FieldList(FormField(AromPromForm), render_kw={'class': 'form-control'},min_entries=5, max_entries=5)
    ipj = FieldList(FormField(AromPromForm), render_kw={'class': 'form-control'},min_entries=5, max_entries=5)
    
    #2
    polso = FieldList(FormField(AromPromPolsoForm),render_kw={'class': 'form-control'}, min_entries=1, max_entries=1)

    #3
    vas = DecimalField(
        'Seleziona i valori:',
        validators=[
            NumberRange(min=0, max=10, message="Value must be between 0 and 100.")
        ]
        ,default=0.0,
        render_kw={'class': 'form-control','type': 'number', 'min':'0.0', 'max': '10.0'}
    )
    #
    trapezio_metacarpale= FieldList(FormField(TrapezioMetacarpicaForm),min_entries=1, max_entries=1)

    #5
    forza= FieldList(FormField(ForzaForm), min_entries=1, max_entries=1)
    
    #6
    #dash = FieldList(FormField(DashForm), min_entries=1, max_entries=1)
    dash = FormField(DashForm)
    #7
    prwhe=FormField(PrwheForm)
    #8
   
    eaton_littler= SelectField('Eaton Littler', choices=[ ('', OPTION_NULL.NULL.value),
                                                          ("0", 'Stadio 0- Nessun artrosi'),
                                                          ("1", "Stadio 1 - leggero aumento di ampiezza dell' articolazione trapezio-metacarpale (pre-artrite), contorni articolari normali, sublussazione <1/3."),
                                                          ("2", "Stadio 2 - restringimento dellarticolazione trapezio-metacarpale con sclerosi ossea, sublussazione dell' articolazione pari a 1/3, osteofiti <2 mm."),
                                                          ("3", "Stadio 3 - obliterazione dell'articolazione trapezio-metacarpale con geodi e sclerosi ossea, sublussazione dell'articolazione >1/3, osteofiti >2 mm"),
                                                          ("4", "Stadio 4 - deterioramento dell'articolazione trapezio-metacarpale con in aggiunta artrosi scafo-trapezio-trapezoidea con evidenti cambiamenti sclerotici e cistici")], 
                                                          default=0, render_kw={'class': 'form-control'}, validators=None)
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

    #18
    #utilizzato per passare tutto il form html per essere salvato come PDF
    hidden_html = HiddenField('hidden_html', render_kw={'class': 'form-control'}, validators=None)
    
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
            ('snac', 'SNAC'),
            ('slac', 'SLAC'),
            ('scac', 'SCAC'),
            ('kienbock', 'Kienbock'),
            ('lussazione_semilunare', 'Lussazione Inveterata Semilunare'),

        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    classificazione_watson = SelectField(
        'Classificazione Watson',
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
        'Classificazione Lichman',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3A', '3A'), 
            ('3B', '3B'),
            ('3C', '3C'), 
            ('4', '4'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    lussazione_lunare = SelectField(
        'Opzioni Lussazione Semilunare',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('volare', 'Volare'),
            ('dorsale', 'Dorsale'),
            ('altro', 'Altro'),
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
    



"""
Form utilizzato per gestire i campi del controllo
"""
class CustomControlForm(FlaskForm):
    
    note = TextAreaField('Inserisci le tue note',render_kw={'class': 'form-control'}
    )

    submit_custom_control = SubmitField("Inserisci", render_kw={'class': 'btn btn-success',"style":"max-width: 200px;"})
