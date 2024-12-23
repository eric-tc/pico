from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField,IntegerField,widgets
from wtforms.validators import DataRequired, Length
from wtforms.fields import DateField,TimeField,SelectField,HiddenField,SelectMultipleField
from .internal_data_enum_pathologies import FrattureMetaCarpaliEnum,\
        ScafoideFratturaEnum,\
        RizoartrosiEnum,\
        FratturaRadioDistaleEnum,\
        FrattureFalangeProssimaleEnum,\
        LesioneTendineaFlessoriEnum,\
        LesioneTendineaEstensoriEnum,\
        ResezioneFilieraEnum,\
        ScafoidePseudortrosiEnum,\
        DupuytrenEnum,\
        LesioneNervosaEnum,\
        LesioneLigamentosaEnum,\
        OPTION_NULL

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
    data_intervento = StringField('Data Intervento', render_kw={'class': 'form-control-custom','readonly':True,'style':'max-width:80%;'}, validators=None)
    
    #Questo valore è associato il campo datepicker
    data_primo_controllo = StringField('Data Primo Controllo', render_kw={'class': 'form-control-custom','readonly':True,'style':'max-width:80%;'}, validators=None)
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
        choices=[(enum.value[0], enum.value[1]) for enum in RizoartrosiEnum],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    altro= StringField('Altro', render_kw={'class': 'form-control'}, validators=None)

    


class FratturaRadioDistaleChirurgicoForm(ChirurgicoForm):

    treatment_options = SelectField(
        'Seleziona Intervento',
        choices=[(enum.value[0], enum.value[1]) for enum in FratturaRadioDistaleEnum],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    classificazione_radiografica_a = SelectField(
        'Classificazione Radiografica',
        choices=[
            ('', OPTION_NULL.NULL.value),
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
            ('', OPTION_NULL.NULL.value),
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

class FratturaMetaCarpaliChirurgicoForm(ChirurgicoForm):

    rottura_metacarpo = SelectField(
        'Seleziona Metacarpo rotto',
        choices=[
            ('', OPTION_NULL.NULL.value),
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
        choices=[ (enum.value[0], enum.value[1]) for enum in FrattureMetaCarpaliEnum],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    # Valori trattamento Non chirurgico

    tipologia = SelectField(
        'Tipologia',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('gesso_chiuso', 'Gesso Chiuso'),
            ('valva_gessata', 'Valva Gessata'),
            ('tutore_termoplastica', 'Tutore in Termoplastica'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    polso_incluso = SelectField(
        'Polso Incluso',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('1', 'No'),
            ('2', 'Si'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    mcpj_incluso = SelectField(
        'MCPj Incluso',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('1', 'No'),
            ('2', 'Si'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    mcpj_estese_incluso = SelectField(
        'MCPj Estese Incluso',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('flesse', 'Flesse'),
            ('estese', 'Estese'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    pipj_incluso = SelectField(
        'PIPj Incluso',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('1', 'No'),
            ('2', 'Si'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )
    
    pipj_estese_incluso = SelectField(
        'PIPj Estese Incluso',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('flesse', 'Flesse'),
            ('estese', 'Estese'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    #Valori chirurgici

    fili_kirschner = SelectField(
        'Fili di Kirschner',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('endomidollare', 'endomidoallre'),
            ('anterogradi', 'anterogradi'),
            ('endomidollare_retrogradi', 'endomidollare retrogradi'),
            ('trasversi', 'trasversi'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    viti = SelectField(
        'Viti',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('endomidollare', 'endomidoallre'),
            ('lag', 'lag'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    classificazione_radiografica = SelectField(
        'classificazione radiografica',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('prossimale', 'Prossimale'),
            ('diafisaria', 'Diafisarisa'),
            ('sottocapitata', 'Sottocapitata'),
             ('distale_articolare', 'Distale Articolare'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    diafisaria = SelectField(
        'classificazione radiografica',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('trasversa', 'Trasversa'),
            ('obliqua', 'Obliqua'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

##------------------------------------------------------------------------------------------------------------------##
##                          FALANGE PROSSIMALE                                                                      ## 
##------------------------------------------------------------------------------------------------------------------##
class FratturaFalangeProssimaleChirurgicoForm(ChirurgicoForm):
    
    treatment_options = SelectField(
        'Seleziona Intervento',
        choices=[ (enum.value[0], enum.value[1]) for enum in FrattureFalangeProssimaleEnum],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    rottura_falange = SelectField(
        'Seleziona Falange rotta',
        choices=[
            ('', OPTION_NULL.NULL.value),
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
            ('', OPTION_NULL.NULL.value),
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
            ('', OPTION_NULL.NULL.value),
            ('1', 'No'),
            ('2', 'Si'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    mcpj_incluso = SelectField(
        'MCPj Incluso',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('1', 'No'),
            ('2', 'Si'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    mcpj_estese_incluso = SelectField(
        'MCPj Estese Incluso',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('1', 'Flesse'),
            ('2', 'Estese'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    pipj_incluso = SelectField(
        'PIPj Incluso',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('1', 'No'),
            ('2', 'Si'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )
    
    pipj_estese_incluso = SelectField(
        'PIPj Estese Incluso',
        choices=[
            ('', OPTION_NULL.NULL.value),
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
            ('', OPTION_NULL.NULL.value),
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
            ('', OPTION_NULL.NULL.value),
            ('1', 'endomidoallre'),
            ('2', 'lag'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    classificazione_radiografica = SelectField(
        'classificazione radiografica',
        choices=[
            ('', OPTION_NULL.NULL.value),
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
            ('', OPTION_NULL.NULL.value),
            ('1', 'Frammento Singolo'),
            ('2', 'Multiframmentaria'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    diafisaria = SelectField(
        'Opzioni Classificazione Radiografica',
        choices=[
            ('', OPTION_NULL.NULL.value),
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
            ('', OPTION_NULL.NULL.value),
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
##                          LESIONE TENDINEA FLESSORI                                                               ## 
##------------------------------------------------------------------------------------------------------------------##
class LesioneTendineaFlessoriChirurgicoForm(ChirurgicoForm):
    
    treatment_options = SelectField(
        'Seleziona Intervento',
        choices=[ (enum.value[0], enum.value[1]) for enum in LesioneTendineaFlessoriEnum],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    tipologia = SelectField(
        'Tipologia',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('fds', 'FDS'),
            ('fdp', 'FDP'),
            ('fds_fdp', 'FDS e FDP'),
            ('fpl', 'fpl'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    #indica tutti i valori salvati dal disegno
    map_selected=HiddenField('map_selected', render_kw={'class': 'form-control'}, validators=None)

    #Se FDS Zona 2

    fds_2 = SelectField(
        'Fds Opzioni',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('completo', 'completo'),
            ('bandella_radiale', 'bandella radiale'),
            ('bandella_ulnare', 'Bandella ulnare'),
            ('4', 'trasversi'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    #fpl_zona 1

    fpl_1_leddy_packer = SelectField(
        'Classificazione Leddy Packer',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('leddy_1', '1'),
            ('leddy_2', '2'),
            ('leddy_3', '3'),
            ('leddy_4', '4'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    #zona 5 

    # tendini_5 = SelectMultipleField(
    # 'Fili di Kirschner',
    # choices=[
    #     ('fcr', 'FDS'),
    #     ('pl', 'FDP'),
    #     ('fcu', 'FDS e FDP'),
    #     ('fpl', 'FPL'),
    #     ('fds_II_III_IV_V', 'FDS_II_III_IV_V'),
    #     ('fdp_II_III_IV_V', 'FDP_II_III_IV_V'), 
    # ],
    # coerce=str,  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
    # render_kw={'class': 'form-control'},  # Add custom styling
    # option_widget=widgets.CheckboxInput(),  # Render each choice as a checkbox
    # widget=widgets.ListWidget(prefix_label=False)  # ListWidget to group checkboxes
    # )

    tendini_5=SelectMultipleField(
        'Tendini lesionati zona 5',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('fcr', 'FDS'),
            ('pl', 'FDP'),
            ('fcu', 'FDS e FDP'),
            ('fpl', 'FPL'),
            ('fds_II_III_IV_V', 'FDS_II_III_IV_V'),
            ('fdp_II_III_IV_V', 'FDP_II_III_IV_V'), 
        ],
        widget=widgets.ListWidget(prefix_label=False),  # List layout for checkboxes
        option_widget=widgets.CheckboxInput(),  # Render as checkboxes
    )

    #zona 1

    tipo_sutura_1 = SelectField(
        'Tipo Sutura',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('singolo_pull_out', 'Singolo pull out'),
            ('doppio_pull_out', 'Doppio pull out'),
            ('sutura_termino_terminale', 'Sutura termino terminale'),
            ('altro', 'Altro'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    tipo_filo_1 = SelectField(
        'Grandezza Filo',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('0', '0'),
            ('1_0', '1.0'),
            ('2_0', '2.0'),
            ('3_0', '3.0'),
            ('4_0', '4.0'),
            ('5_0', '5.0'),
            ('6_0', '6.0'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    materiale_filo_1 = SelectField(
        'Materiale Filo',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('nylon', 'Nylon'),
            ('prolene', 'Prolene'),
            ('vicryl', 'Vicryl'),
            ('ti_cron', 'Ti-Cron'),
            ('fiber_wire', 'Fiber wire'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    #Altre Zone

    tipo_sutura = SelectField(
        'Materiale Filo',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('2_passaggi', '2 passaggi'),
            ('4_passaggi', '4 passaggi'),
            ('6_passaggi', '6 passaggi'),
            ('altro', 'Altro'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    passaggio_2 = SelectField(
        'Tipologia Passaggio 2',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('kessler_modificata', 'Kessler Modificata'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    passaggio_4 = SelectField(
        'Tipologia Passaggio 4',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('doppia_kessler_modificata', 'Doppia Kessler Modificata'),
            ('adelaide', 'Adelaide'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    passaggio_6 = SelectField(
        'Tipologia Passaggio 6',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('tripla_kessler_modificata', 'Tripla Kessler Modificata'),
            ('m_tang', 'M-Tang'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    altro = SelectField(
        'Altro',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('punti_staccati', 'Punti Staccati'),
            ('punti_u', 'Punti a U'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    tipo_filo_zona_generica = SelectField(
        'Grandezza Filo',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('0', '0'),
            ('1_0', '1.0'),
            ('2_0', '2.0'),
            ('3_0', '3.0'),
            ('4_0', '4.0'),
            ('5_0', '5.0'),
            ('6_0', '6.0'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    materiale_filo_zona_generica = SelectField(
        'Materiale Filo',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('nylon', 'Nylon'),
            ('prolene', 'Prolene'),
            ('vicryl', 'Vicryl'),
            ('ti_cron', 'Ti-Cron'),
            ('fiber_wire', 'Fiber wire'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )


##------------------------------------------------------------------------------------------------------------------##
##                          LESIONE TENDINEA FLESSORI                                                               ## 
##------------------------------------------------------------------------------------------------------------------##
class LesioneTendineaEstensoriChirurgicoForm(ChirurgicoForm):
    
    treatment_options = SelectField(
        'Seleziona Intervento',
        choices=[ (enum.value[0], enum.value[1]) for enum in LesioneTendineaEstensoriEnum],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )


    #indica tutti i valori salvati dal disegno
    map_selected=HiddenField('map_selected', render_kw={'class': 'form-control'}, validators=None)


    #zona 2 3 dita lunghe

    struttura_lesionata=SelectMultipleField(
        'Selezionare la struttura lesionata',
        choices=[
         ('bandella_laterale_radiale', 'Bandella laterale radiale'),
            ('bandella_centrale', 'Bandella centrale'),
            ('bandella_ulnare', 'Bandella ulnare'),
        ],
        widget=widgets.ListWidget(prefix_label=False),  # List layout for checkboxes
        option_widget=widgets.CheckboxInput(),  # Render as checkboxes
    )


    #zona 4,5,6

    zona_4_5_6_tipologia = SelectField(
        'Tipologia',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('edc', 'EDC'),
           
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    zona_4_5_6_secondo_tipologia=SelectField(
        'Tipologia',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('edc', 'EDC'),
            ('eip', 'EIP'),
           
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    zona_4_5_6_quinto_tipologia=SelectField(
        'Tipologia',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('edc', 'EDC'),
            ('edm', 'EDM'),
           
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    #zona 1 e 2 pollice
    zona_1_2_pollice = SelectField(
        'Tipologia',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('epl', 'EPL'),
           
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    #zona 3 e 4 pollice

    zona_3_4_pollice = SelectField(
        'Tipologia',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('epl', 'EPL'),
            ('epb', 'EPB'),
           
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    #zona 7 8 9

    zona_7_8_9 = SelectField(
        'Selezionare i tendini in zona 7 8 9',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('apl', 'APL'),
            ('epb', 'EPB'),
            ('epl', 'EPL'),
            ('eip', 'EIP'),
            ('edc', 'EDC'),
            ('edm', 'EDM'),
            ('ecu', 'ECU'),
           
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )


    # zona 1 parametri generale

    raggio_zona_1 = SelectField(
        'Selezionare Raggio',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('I', 'I'),
            ('II', 'II'),
            ('III', 'III'),
            ('IV', 'IV'),
            ('V', 'V'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    doyle = SelectField(
        'Classificazione Doyle',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4a', '4a'),
            ('4b', '4b'),
            ('4c', '4c'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    swan_neck = SelectField(
        'Presente Swan neck',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('si', 'Si'),
            ('no', 'No'),
           
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    trattamento_zona_1 = SelectField(
        'Trattamento',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('splint', 'Splint'),
            ('sintesi', 'Riduzione e Sintesi'),
           
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    split = SelectField(
        'Split',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('6_settimane', '6 settimane'),
            ('8_settimane', '8 settimane'),
           
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    sintesi = SelectField(
        'Riduzione e Sintesi',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('fili_k_ishiguro', 'fili k ishiguro'),
            ('viti', 'viti'),
            ('ancoretta', 'ancoretta'),
            ('tenorrafia', 'tenorrafia'),
            ('altro', 'altro'),
           
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    complicanze = SelectField(
        'Complicanze',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('mobilizzazione_mezzi_sintesi', 'Mobilizzazione mezzi sintesi'),
            ('infezione', 'Infezione'),
            ('perdita_riduzione', 'perdita riduzione'),
           
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    


    # Generale tutte le zone

    tipo_sutura = SelectField(
        'Materiale Filo',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('2_passaggi', '2 passaggi'),
            ('4_passaggi', '4 passaggi'),
            ('6_passaggi', '6 passaggi'),
            ('altro', 'Altro'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    passaggio_2 = SelectField(
        'Tipologia Passaggio 2',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('kessler_modificata', 'Kessler Modificata'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    passaggio_4 = SelectField(
        'Tipologia Passaggio 4',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('doppia_kessler_modificata', 'Doppia Kessler Modificata'),
            ('adelaide', 'Adelaide'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    passaggio_6 = SelectField(
        'Tipologia Passaggio 6',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('tripla_kessler_modificata', 'Tripla Kessler Modificata'),
            ('m_tang', 'M-Tang'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    altro = SelectField(
        'Altro',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('punti_staccati', 'Punti Staccati'),
            ('punti_u', 'Punti a U'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    tipo_filo_zona_generica = SelectField(
        'Grandezza Filo',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('0', '0'),
            ('1_0', '1.0'),
            ('2_0', '2.0'),
            ('3_0', '3.0'),
            ('4_0', '4.0'),
            ('5_0', '5.0'),
            ('6_0', '6.0'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    materiale_filo_zona_generica = SelectField(
        'Materiale Filo',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('nylon', 'Nylon'),
            ('prolene', 'Prolene'),
            ('vicryl', 'Vicryl'),
            ('ti_cron', 'Ti-Cron'),
            ('fiber_wire', 'Fiber wire'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )


##------------------------------------------------------------------------------------------------------------------##
##                          RESEZIONE FILIERA                                                                       ## 
##------------------------------------------------------------------------------------------------------------------##
class ResezioneFilieraChirurgicoForm(ChirurgicoForm):

    treatment_options = SelectField(
        'Seleziona Intervento',
        choices=[
           (enum.value[0], enum.value[1]) for enum in ResezioneFilieraEnum
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    accesso = SelectField(
        'Accesso',
        choices=[
            ('', OPTION_NULL.NULL.value),   
            ('1', 'volare'),
            ('2', 'dorsale'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    
    tipologia = SelectField(
        'Tipologia',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('1', 'longitudinale'),
            ('2', 'trasversale'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

##------------------------------------------------------------------------------------------------------------------##
##                          DupuyTren                                                                      ## 
##------------------------------------------------------------------------------------------------------------------##
class DupuytrenChirurgicoForm(ChirurgicoForm):

    treatment_options = SelectField(
        'Seleziona Intervento',
        choices=[
           (enum.value[0], enum.value[1]) for enum in DupuytrenEnum
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    complicanze = SelectField(
        'Complicanze',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('1', 'Lesione Tendinea'),
            ('2', 'Lesione Nervosa'),
            ('3', 'Altro'),

        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )


##------------------------------------------------------------------------------------------------------------------##
##                          LesioneNervosa                                                                      ## 
##------------------------------------------------------------------------------------------------------------------##
class LesioneNervosaChirurgicoForm(ChirurgicoForm):

    treatment_options = SelectField(
        'Seleziona Intervento',
        choices=[
           (enum.value[0], enum.value[1]) for enum in LesioneNervosaEnum
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )


    tipo_lesione = SelectField(
        'Tipo Lesione',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('completa', 'completa'),
            ('parziale', 'parziale'),
            ('sintetico', 'Sintetico'),

        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    innesto = SelectField(
        'Innesto',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('innesto_nervoso', 'Innesto Nervoso'),
            ('muscolo_vena', 'Muscolo in vena'),
            ('sintetico', 'Sintetico'),

        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    innesto_nervoso = SelectField(
        'Innesto Nervoso',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('surale', 'Innesto Nervoso'),
            ('nervo_interosseo_posteriore', 'Nervo Interosso Posteriore'),
            ('nervo_interosseo_anteriore', 'Nervo Interosso Anteriore'),
            ('altro', 'Altro'),

        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )
    
    sensibilita_volare = HiddenField('sensibilita_volare', render_kw={'class': 'form-control'}, validators=None)
    
    sensibilita_dorsale = HiddenField('sensibilita_dorsale', render_kw={'class': 'form-control'}, validators=None)

##------------------------------------------------------------------------------------------------------------------##
##                          SCAFOIDE 
# Lo scafoide avrà 2 form perchè ci sono diversi decorsi post operatori in base alla frattura e pseudoartrosi       ## 
##------------------------------------------------------------------------------------------------------------------##

class ScafoideFratturaChirurgicoForm(ChirurgicoForm):
    
    treatment_options = SelectField(
        'Tipologia',
        choices=[
           (enum.value[0], enum.value[1]) for enum in ScafoideFratturaEnum   
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    area = SelectField(
        'Accesso',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('terzo_prossimale', 'volare'),
            ('terzo_medio', 'terzo_medio'),
            ('terzo_distale', 'terzo_distale'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )   
    
    #Se CONSERVATIVO

    conservativo = SelectField(
        'Conservativo',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('gesso_chiuso_pollice_incluso', 'gesso chiuso pollice incluso'),
            ('gesso_chiuso_pollice_escluso', 'gesso chiuso pollice escluso'),
            ('tutore_termoplastica_pollice_incluso', 'tutore termoplastica pollice incluso'),
            ('tutore_termoplastica_pollice_escluso', 'tutore termoplastica pollice escluso'),
            ('altro', 'altro'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )
    #CHIRURGICO
    chirurgico = SelectField(
        'Conservativo',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('vite_percutanea_anterograda', 'vite percutanea anterograda'),
            ('vite_percutanea_retrograda', 'vite percutanea retrograda'),
            ('vite_open_anterograda', 'vite open anterograda'),
            ('vite_open_retrograda', 'vite open retrograda'),
            ('altro', 'altro'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )


class ScafoidePseudoArtrosiChirurgicoForm(ChirurgicoForm):

    treatment_options = SelectField(
        'Seleziona Intervento',
        choices=[
              (enum.value[0], enum.value[1]) for enum in ScafoidePseudortrosiEnum
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    # SE OPEN o OPEN ASSISTENZA ARTROSCOPICA

    open = SelectField(
        'Accesso',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('accesso_volare', 'accesso_volare'),
            ('accesso_dorsale', 'accesso dorsale'),
            ('accesso_volare_accesso_dorsale', 'entrambi'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    #TUTTI
    innesto = SelectField(
        'Innesto',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('innesto_cresta_iliaca', 'innesto cresta iliaca'),
            ('innesto_da_radio', 'innesto da radio'),
            ('innesto_sintetico', 'innesto sintetico'),
            ('lembo_da_condilo_femorale mediale', 'lembo da condilo femorale mediale'),
            ('altro', 'altro'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    tipo_sintesi = SelectField(
        'Sintesi',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('fili_kirschner', 'fili kirschner'),
            ('vite_retrograda', 'vite retrograda'),
            ('vite_anterograda', 'vite anterograda'),
            ('placca', 'placca'),
            ('nessuna_sintesi', 'nessuna sintesi'),
            ('altro', 'altro'),
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

   
##------------------------------------------------------------------------------------------------------------------##
##                          LESIONE LIGAMENTOSA
## 
##------------------------------------------------------------------------------------------------------------------##


class LesioneLigamentosaChirurgicoForm(ChirurgicoForm):
      
    treatment_options = SelectField(
        'Seleziona Intervento',
        choices=[
              (enum.value[0], enum.value[1]) for enum in LesioneLigamentosaEnum
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    #Valori trattamento Non chirurgico
    conservativo = SelectField(
        'Tipologia',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('1', 'Valva Gessata'),
            ('2', 'Tutore Su misura'),
            ('3', 'Sindattalia'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )

    #chirurgico

    chirurgico = SelectField(
        'Tipologia',
        choices=[
            ('', OPTION_NULL.NULL.value),
            ('1', 'Reinserzione con ancoretta'),
            ('2', 'Pull out'),
            ('3', 'Sutura'),
            ('4', 'Altro'), 
        ],
        coerce=str  # Data type conversion, e.g., if you expect an integer you can use coerce=int.
        ,render_kw={'class': 'form-control'}
    )
