from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length
from wtforms.fields import DateField,TimeField
from .internal_data import CONTROLS




class PreTreamentForm(FlaskForm):
    # I valori del campo del form devono avere lo stesso valore delle chiavi di CONTROLS
    #in questo modo nella UI posso verificare quando un campo è attivo o meno utilizzando una map dove la chiave
    # è la label:True,False. Vedere pagina next_control
    selected_date = DateField(CONTROLS.DATA_FRATTURA.value, format='%d-%m-%Y', render_kw={'class': 'form-control'}, validators=None)
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



class MedicalTreatmentForm(FlaskForm):
    """
    Questo form gestisce
    """
    entrytime_1 = TimeField('Time',render_kw={'class': 'form-control-custom'})
    
