from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length,NumberRange
from wtforms.fields import DateField,TimeField,SelectField,HiddenField,FieldList,FormField,FloatField
from .internal_data import CONTROLS



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

"""
#Form per gestire i valori
class AromPromForm(FlaskForm):
    arom_estensione = FloatField("Arom Estensione",render_kw={'class': 'form-control','type': 'number', 'max': '120.0'}, validators=[NumberRange(min=-120.0, max=120.0)])
    arom_flessione = FloatField("Arom Flessione", render_kw={'class': 'form-control','type': 'number', 'max': '120.0'},validators=[NumberRange(min=-120.0, max=120.0)])
    prom_estensione = FloatField("Prom Estensione", render_kw={'class': 'form-control','type': 'number', 'max': '120.0'},validators=[NumberRange(min=-120.0, max=120.0)])
    prom_flessione = FloatField("Prom Flessione", render_kw={'class': 'form-control','type': 'number', 'max': '120.0'},validators=[NumberRange(min=-120.0, max=120.0)])

class AromPromPolsoForm(AromPromForm):

    arom_supinazione = FloatField("Arom Supinazione", render_kw={'class': 'form-control'},validators=[NumberRange(min=0.0, max=100.0)])
    arom_pronazione = FloatField("Arom Pronazione", render_kw={'class': 'form-control'},validators=[NumberRange(min=0.0, max=100.0)])
    prom_supinazione = FloatField("Prom Supinazione", render_kw={'class': 'form-control'},validators=[NumberRange(min=0.0, max=100.0)])
    prom_pronazione = FloatField("Prom Pronazione", render_kw={'class': 'form-control'},validators=[NumberRange(min=0.0, max=100.0)])

class TrapezioMetacarpicaForm(FlaskForm):

    anteposizione = FloatField('Anteposizione',render_kw={'class': 'form-control'}, validators=[NumberRange(min=0.0, max=120.0)])
    abduzione = FloatField('Abduzione', render_kw={'class': 'form-control'}, validators=[NumberRange(min=0.0, max=120.0)])
    kapandji = FloatField('Pinch',render_kw={'class': 'form-control'}, validators=[NumberRange(min=0.0, max=10.0)])

class ForzaForm(FlaskForm):

    key_pinch = FloatField('Key Pinch(Kg)', render_kw={'class': 'form-control'}, validators=[NumberRange(min=0.0, max=100.0)])
    tip_to_pinch= FloatField('Tip to Pinch(Kg)', render_kw={'class': 'form-control'}, validators=[NumberRange(min=0.0, max=100.0)])
    three_fingers_pinch = FloatField('Three Fingers Pinch(Kg)', render_kw={'class': 'form-control'}, validators=[NumberRange(min=0.0, max=100.0)])
    grip = FloatField('Grip(Kg)', render_kw={'class': 'form-control'}, validators=[NumberRange(min=0.0, max=100.0)])
    

class CicatriceForm(FlaskForm):
    aderente = SelectField('Aderente', choices=[(1, 'Yes'), (0, 'No')], default=0, render_kw={'class': 'form-control'}, validators=None)
    distasi_ferita = SelectField('Distasi Ferita', choices=[(1, 'Yes'), (0, 'No')], default=0, render_kw={'class': 'form-control'}, validators=None)
    tinel = SelectField('Tinel', choices=[(1, 'Yes'), (0, 'No')], default=0, render_kw={'class': 'form-control'}, validators=None)

class AltroForm(FlaskForm):
    complicanze = SelectField('Complicanze', choices=[(0, 'CRPS'), (1, 'infenzione'),(2, 'problematiche nervose'),(3, 'problematiche tendinee')], default=0, render_kw={'class': 'form-control'}, validators=None)
    note= StringField('Note', render_kw={'class': 'form-control'}, validators=None)


class TreatmentForm(FlaskForm):

    #1
    mpcj_list = FieldList(FormField(AromPromForm),label="MCPJ", min_entries=5, max_entries=5)
    
    dipj_list = FieldList(FormField(AromPromForm), render_kw={'class': 'form-control'},min_entries=5, max_entries=5)
    pipj_list = FieldList(FormField(AromPromForm), render_kw={'class': 'form-control'},min_entries=5, max_entries=5)
    ipj_list = FieldList(FormField(AromPromForm), render_kw={'class': 'form-control'},min_entries=5, max_entries=5)
    
    #2
    polso = FieldList(FormField(AromPromPolsoForm),render_kw={'class': 'form-control'}, min_entries=1, max_entries=1)

    #3
    vas = FloatField('vas', render_kw={'class': 'form-control'}, validators=[NumberRange(min=0.0, max=10.0)])

    #
    trapezio_metacarpale= FieldList(FormField(TrapezioMetacarpicaForm),min_entries=1, max_entries=1)

    #5
    #forza= FieldList(FormField(ForzaForm), min_entries=1, max_entries=1)
    #6
    #dash = FloatField(CONTROLS.DASH.value, render_kw={'class': 'form-control'},  validators=None)
    

    #6
    # prwhe = IntegerField(CONTROLS.PRWHE.value, render_kw={'class': 'form-control'},  validators=None)
    # #7
    # eaton_littler = IntegerField(CONTROLS.EATON_LITTLER.value, render_kw={'class': 'form-control'}, validators=None )
    # #8
    # #sensibilty = Gestita attraverso un canvas e salvata direttamente a database. Vedere il file sensibilitu.html
    # #9
    # edema = SelectField('Edema', choices=[(1, 'Yes'), (0, 'No')], default=0, render_kw={'class': 'form-control'}, validators=None)
    # #10
    # cicatrice = FormField(CicatriceForm)
    # # #11
    # tutore = SelectField('Tutore', choices=[(1, 'Yes'), (0, 'No'),(2,"Altro")], default=0, render_kw={'class': 'form-control'}, validators=None)
    # # #12
    # altro = FormField(AltroForm)

    submit_form = SubmitField("Submit", render_kw={'class': 'btn btn-primary'})

    def __init__(self, selected_indices=None,controls_map=None, *args, **kwargs):
        super(TreatmentForm, self).__init__(*args, **kwargs)
        self.controls_map = controls_map
        self.max_indeces = [] #indici non esclusi di default

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
            subform.three_fingers_pinch.validators = []
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

    def validate(self, extra_validators=None):
        """
        Usato per rendere la validazione attiva solo sugli indici selezionati
        """
        valid = super(TreatmentForm, self).validate()

        #in base alla lista delle controls_map devo disabilitare i validatori

        for key, value in self.controls_map.items():
            if value["active"] == False:
                print("Disabilito il campo: ", key)
                
                if key == "mpcj":
                    self.validate_list(self.mpcj_list,self.max_indeces)   
                elif key == "dipj":
                    self.validate_list(self.dipj_list,self.max_indeces)
                elif key == "pipj":
                    self.validate_list(self.pipj_list,self.max_indeces)
                elif key == "ipj":
                    self.validate_list(self.ipj_list,self.max_indeces)
                elif key == "polso":
                    print("Disabilito il polso")
                    self.validate_polso()
                elif key == "trapezio_metacarpale":
                    print("Disabilito il trapezio_metacarpale")
                    self.validate_trapezio_metacarpale()
                elif key == "vas":
                    print("Disabilito il vas")
                    self.validate_vas()
                elif key == "forza":
                    print("Disabilito il forza")
                    #self.validate_forza()
            
            elif value:
                # Se true devo disabilitare gli indici non selezionati
                if key == "mpcj":
                    self.validate_list(self.mpcj_list,self.controls_map[key]["indices"])
                elif key == "dipj":
                    self.validate_list(self.dipj_list,self.controls_map[key]["indices"])
                elif key == "pipj":
                    self.validate_list(self.pipj_list,self.controls_map[key]["indices"])
                elif key == "ipj":
                    self.validate_list(self.ipj_list,self.controls_map[key]["indices"])
                
        # Perform another validation after updating the validators
        return super(TreatmentForm, self).validate()


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

class MedicalTreatmentForm(FlaskForm):
    """
    Questo form gestisce
    """
    entrytime_1 = TimeField('Time',render_kw={'class': 'form-control-custom'})
    

#------------------------------- DA ELIMINARE ----------------------------------

#Form vecchio probabilmente posso eliminarlo
class RizoartrosiForm(FlaskForm):
    # I valori del campo del form devono avere lo stesso valore delle chiavi di CONTROLS
    #in questo modo nella UI posso verificare quando un campo è attivo o meno utilizzando una map dove la chiave
    # è la label:True,False. Vedere pagina next_control
    nprs_vas = IntegerField(CONTROLS.NPRS_VAS.value, render_kw={'class': 'form-control'}, validators=None)
    prom_aprom_mcpj = IntegerField(CONTROLS.PROM_APROM_MCPJ.value, render_kw={'class': 'form-control'}, validators=None)
    prom_aprom_ipj = IntegerField(CONTROLS.PROM_APROM_IPJ.value, render_kw={'class': 'form-control'}, validators=None)
    abduzione = IntegerField(CONTROLS.ABDUZIONE.value, render_kw={'class': 'form-control'},  validators=None)
    anteposizione = IntegerField(CONTROLS.ANTEPOSIZIONE.value, render_kw={'class': 'form-control'},  validators=None)
    kapandji = IntegerField(CONTROLS.KAPANDJI.value, render_kw={'class': 'form-control'},  validators=None)
    pinch = IntegerField(CONTROLS.PINCH.value, render_kw={'class': 'form-control'},  validators=None)
    grip = IntegerField(CONTROLS.GRIP.value, render_kw={'class': 'form-control'},  validators=None)
    dash = IntegerField(CONTROLS.DASH.value, render_kw={'class': 'form-control'},  validators=None)
    prwhe = IntegerField(CONTROLS.PRWHE.value, render_kw={'class': 'form-control'},  validators=None)
    eaton_littler = IntegerField(CONTROLS.EATON_LITTLER.value, render_kw={'class': 'form-control'}, validators=None )
    stato_cicatrice = StringField(CONTROLS.STATO_CICATRICE.value, render_kw={'class': 'form-control'},  validators=None)
    tipo_cicatrice = StringField(CONTROLS.TIPO_CICATRICE.value, render_kw={'class': 'form-control'},  validators=None)
    modena = StringField(CONTROLS.MODENA.value,render_kw={'class': 'form-control'},  validators=None)
    submit_rizoartrosi = SubmitField("Submit", render_kw={'class': 'btn btn-primary'})


    