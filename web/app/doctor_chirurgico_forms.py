from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length
from wtforms.fields import DateField,TimeField,SelectField,HiddenField



#Questo file gestisce solo i form per l'intervento chirurgico. ATTENZIONE è incluso nel file internal:data.py
# Questi form sono legati all'enum Pathology

class RizoartrosiChirurgicoForm(FlaskForm):
    #il formato della data deve essere in questo modo altrimenti ho un errore
    data_intervento = StringField('Data Intervento', render_kw={'class': 'form-control-custom'}, validators=None)
    
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

    #Questo valore è associato il campo datepicker
    data_primo_controllo = StringField('Data Primo Controllo', render_kw={'class': 'form-control-custom'}, validators=None)
    orario_primo_controllo = StringField('Orario Primo Controllo', render_kw={'class': 'form-control'}, validators=None)

    # Hidden Input to handle variable

    pathology_id = HiddenField('Pathology ID', render_kw={'class': 'form-control'}, validators=None)
    patient_id = HiddenField('Patient ID', render_kw={'class': 'form-control'}, validators=None)
    row_id = HiddenField('Row ID', render_kw={'class': 'form-control'}, validators=None)
    patient_name = HiddenField('Patient Name', render_kw={'class': 'form-control'}, validators=None)


    submit_rizoartrosi_chirurgico = SubmitField("Submit", render_kw={'class': 'btn btn-primary'})
