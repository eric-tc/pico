from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length
from wtforms.fields import DateField,TimeField,SelectField,HiddenField
from .internal_data_enum_pathologies import FrattureMetaCarpaliEnum

#Questo file gestisce solo i form per l'intervento chirurgico. ATTENZIONE è incluso nel file internal:data.py
# Questi form sono legati all'enum Pathology


class ChirurgicoForm(FlaskForm):
    """
    Questi campi sono comuni a tutte le patologie
    
    ATTENZIONE TUTTI I FORM CHE DERIVANO DA QUESTO DEVONO AVERE LA PROPRIETA treatment_options.

    treatment_options è usata per gestire il decorso post operatorio in base alla 
    scelta fatta dall'utente
    
    """
    #il formato della data deve essere in questo modo altrimenti ho un errore
    data_intervento = StringField('Data Intervento', render_kw={'class': 'form-control-custom','readonly':True}, validators=None)
    
    #Questo valore è associato il campo datepicker
    data_primo_controllo = StringField('Data Primo Controllo', render_kw={'class': 'form-control-custom','readonly':True}, validators=None)
    orario_primo_controllo = StringField('Orario Primo Controllo', render_kw={'class': 'form-control'}, validators=None)


    # Hidden Input to handle variable
    pathology_id = HiddenField('Pathology ID', render_kw={'class': 'form-control'}, validators=None)
    patient_id = HiddenField('Patient ID', render_kw={'class': 'form-control'}, validators=None)
    row_id = HiddenField('Row ID', render_kw={'class': 'form-control'}, validators=None)
    patient_name = HiddenField('Patient Name', render_kw={'class': 'form-control'}, validators=None)

    
    submit_chirurgico_form = SubmitField("Submit", render_kw={'class': 'btn btn-primary'})


##------------------------------------------------------------------------------------------------------------------##
##                         RIZOARTROSI                                                                      ## 
##------------------------------------------------------------------------------------------------------------------##


class RizoartrosiChirurgicoForm(ChirurgicoForm):
    
    treatment_options = SelectField(
        'Seleziona Intervento',
        choices=[
            ('1', 'Trapeziectomia più artroplastica in sospensione con abduttore lungo del pollice'),
            ('2', 'Protesi Touch'),
            ('3', 'trapeziectomia'),
            ('4', 'rapeziectomia più artroplastica con flessore radiale del carpo'),
            ('5', 'rapeziectomia più tight rope'),
            ('6', 'emitrapeziectomia,'),

        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    altro= StringField('Altro', render_kw={'class': 'form-control'}, validators=None)

    


class FratturaRadioDistaleForm(ChirurgicoForm):

    treatment_options = SelectField(
        'Seleziona Intervento',
        choices=[
            ('1', 'Gesso Chiuso'),
            ('2', 'Placca a viti'),
            ('3', 'Fissatore esterno fili K'),
            ('4', 'Viti'),
            ('5', 'Valva Gessata'),
            
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    classificazione_radiografica_a = SelectField(
        'Classificazione Radiografica',
        choices=[
            ('1', 'A'),
            ('2', 'B'),
            ('3', 'C'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    classificazione_radiografica_numero = SelectField(
        'Classificazione Radiografica Numero',
        choices=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

##------------------------------------------------------------------------------------------------------------------##
##                         FRATTURE METACARPALI                                                                     ## 
##------------------------------------------------------------------------------------------------------------------##

class FratturaMetaCarpaliForm(ChirurgicoForm):

    rottura_metacarpo = SelectField(
        'Seleziona Metacarpo rotto',
        choices=[
            ('1', 'I'),
            ('2', 'II'),
            ('3', 'III'),
            ('4', 'IV'),
            ('5', 'V'),
            
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    treatment_options = SelectField(
        'Seleziona Intervento',
        choices=[
            (FrattureMetaCarpaliEnum.CHIRURGICO.value, 'Chirurgico'),
            (FrattureMetaCarpaliEnum.NON_CHIRURGICO.value, 'Non Chirurgico'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    # Valori trattamento Non chirurgico

    tipologia = SelectField(
        'Tipologia',
        choices=[
            ('1', 'Gesso Chiuso'),
            ('2', 'Valva Gessata'),
            ('3', 'Tutore in Termoplastica'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    polso_incluso = SelectField(
        'Polso Incluso',
        choices=[
            ('1', 'No'),
            ('2', 'Si'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    mcpj_incluso = SelectField(
        'MCPj Incluso',
        choices=[
            ('1', 'No'),
            ('2', 'Si'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    mcpj_estese_incluso = SelectField(
        'MCPj Estese Incluso',
        choices=[
            ('1', 'Flesse'),
            ('2', 'Estese'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    pipj_incluso = SelectField(
        'PIPj Incluso',
        choices=[
            ('1', 'No'),
            ('2', 'Si'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )
    
    pipj_estese_incluso = SelectField(
        'PIPj Estese Incluso',
        choices=[
            ('1', 'Flesse'),
            ('2', 'Estese'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    #Valori chirurgici

    fili_kirschner = SelectField(
        'Fili di Kirschner',
        choices=[
            ('1', 'endomidoallre'),
            ('2', 'anterogradi'),
            ('3', 'endomidollare retrogradi'),
            ('4', 'trasversi'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    viti = SelectField(
        'Viti',
        choices=[
            ('1', 'endomidoallre'),
            ('2', 'lag'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    classificazione_radiografica = SelectField(
        'classificazione radiografica',
        choices=[
            ('1', 'Prossimale'),
            ('2', 'Diafisarisa'),
            ('3', 'Sottocapitata'),
             ('4', 'Distale Articolare'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    diafisaria = SelectField(
        'classificazione radiografica',
        choices=[
            ('1', 'Trasversa'),
            ('2', 'Obliqua'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

##------------------------------------------------------------------------------------------------------------------##
##                          FALANGE PROSSIMALE                                                                      ## 
##------------------------------------------------------------------------------------------------------------------##
class FratturaFalangeProssimaleForm(ChirurgicoForm):
    
    treatment_options = SelectField(
        'Seleziona Intervento',
        choices=[
            (FrattureMetaCarpaliEnum.CHIRURGICO.value, 'Chirurgico'),
            (FrattureMetaCarpaliEnum.NON_CHIRURGICO.value, 'Non Chirurgico'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    rottura_falange = SelectField(
        'Seleziona Falange rotta',
        choices=[
            ('1', 'I'),
            ('2', 'II'),
            ('3', 'III'),
            ('4', 'IV'),
            ('5', 'V'),
            
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

      # Valori trattamento Non chirurgico

    tipologia = SelectField(
        'Tipologia',
        choices=[
            ('1', 'Gesso Chiuso'),
            ('2', 'Valva Gessata'),
            ('3', 'Tutore in Termoplastica'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    polso_incluso = SelectField(
        'Polso Incluso',
        choices=[
            ('1', 'No'),
            ('2', 'Si'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    mcpj_incluso = SelectField(
        'MCPj Incluso',
        choices=[
            ('1', 'No'),
            ('2', 'Si'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    mcpj_estese_incluso = SelectField(
        'MCPj Estese Incluso',
        choices=[
            ('1', 'Flesse'),
            ('2', 'Estese'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    pipj_incluso = SelectField(
        'PIPj Incluso',
        choices=[
            ('1', 'No'),
            ('2', 'Si'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )
    
    pipj_estese_incluso = SelectField(
        'PIPj Estese Incluso',
        choices=[
            ('1', 'Flesse'),
            ('2', 'Estese'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    #Valori chirurgici

    fili_kirschner = SelectField(
        'Fili di Kirschner',
        choices=[
            ('1', 'endomidoallre'),
            ('2', 'anterogradi'),
            ('3', 'endomidollare retrogradi'),
            ('4', 'trasversi'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    viti = SelectField(
        'Viti',
        choices=[
            ('1', 'endomidoallre'),
            ('2', 'lag'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    classificazione_radiografica = SelectField(
        'classificazione radiografica',
        choices=[
            ('1', 'Prossimale Articolare'),
            ('2', 'Diafisara'),
            ('3', 'Distale Articolare'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    prossimale = SelectField(
        'Opzioni Classificazione Radiografica',
        choices=[
            ('1', 'Frammento Singolo'),
            ('2', 'Multiframmentaria'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    diafisaria = SelectField(
        'Opzioni Classificazione Radiografica',
        choices=[
            ('1', 'Trasversa'),
            ('2', 'Obliqua'), 
            ('3', 'Multiframmentaria'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    distale = SelectField(
        'Opzioni Classificazione Radiografica',
        choices=[
            ('1', 'Weiss 1'),
            ('2', 'Weiss 2'), 
            ('3', 'Weiss 3'),
            ('4', 'Weiss 3'), 
            ('5', 'Weiss 5'),  
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )



##------------------------------------------------------------------------------------------------------------------##
##                          RESEZIONE FILIERA                                                                       ## 
##------------------------------------------------------------------------------------------------------------------##
class ResezioneFilieraForm(ChirurgicoForm):

    treatment_options = SelectField(
        'Seleziona Intervento',
        choices=[
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