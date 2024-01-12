from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length
from wtforms.fields import DateField,TimeField
from .internal_data import RIZOARTROSI_CONTROLS

# class RizoartrosiForm(FlaskForm):
#     nprs_vas = IntegerField('NPRS VAS', render_kw={'class': 'form-control'}, validators=[DataRequired()])
#     prom_arom_mcpj = IntegerField('PROM AROM MCPJ', render_kw={'class': 'form-control'}, validators=[DataRequired()])
#     prom_arom_Ipj = IntegerField('PROM AROM IPJ', render_kw={'class': 'form-control'}, validators=[DataRequired()])
#     abduction = IntegerField('Abduction', render_kw={'class': 'form-control'}, validators=[DataRequired()])
#     anterposition = IntegerField('Anterposition', render_kw={'class': 'form-control'}, validators=[DataRequired()])
#     kapandji = IntegerField('Kapandji', render_kw={'class': 'form-control'}, validators=[DataRequired()])
#     pinch = IntegerField('Pinch', render_kw={'class': 'form-control'}, validators=[DataRequired()])
#     grip = IntegerField('Grip', render_kw={'class': 'form-control'}, validators=[DataRequired()])
#     dash = IntegerField('DASH', render_kw={'class': 'form-control'}, validators=[DataRequired()])
#     prwhe = IntegerField('PRWHE', render_kw={'class': 'form-control'}, validators=[DataRequired()])
#     Eaton_littler = IntegerField('Eaton Littler', render_kw={'class': 'form-control'}, validators=[DataRequired()])
#     scar_status = StringField('Scar Status', render_kw={'class': 'form-control'}, validators=[DataRequired()])
#     scar_type = StringField('Scar Type', render_kw={'class': 'form-control'}, validators=[DataRequired()])


class RizoartrosiForm(FlaskForm):
    # I valori del campo del form devono avere lo stesso valore delle chiavi di RIZOARTROSI_CONTROLS
    #in questo modo nella UI posso verificare quando un campo è attivo o meno utilizzando una map dove la chiave
    # è la label:True,False. Vedere pagina next_control
    nprs_vas = IntegerField(RIZOARTROSI_CONTROLS.NPRS_VAS.value, render_kw={'class': 'form-control'}, validators=None)
    prom_aprom_mcpj = IntegerField(RIZOARTROSI_CONTROLS.PROM_APROM_MCPJ.value, render_kw={'class': 'form-control'}, validators=None)
    prom_aprom_ipj = IntegerField(RIZOARTROSI_CONTROLS.PROM_APROM_IPJ.value, render_kw={'class': 'form-control'}, validators=None)
    abduzione = IntegerField(RIZOARTROSI_CONTROLS.ABDUZIONE.value, render_kw={'class': 'form-control'},  validators=None)
    anteposizione = IntegerField(RIZOARTROSI_CONTROLS.ANTEPOSIZIONE.value, render_kw={'class': 'form-control'},  validators=None)
    kapandji = IntegerField(RIZOARTROSI_CONTROLS.KAPANDJI.value, render_kw={'class': 'form-control'},  validators=None)
    pinch = IntegerField(RIZOARTROSI_CONTROLS.PINCH.value, render_kw={'class': 'form-control'},  validators=None)
    grip = IntegerField(RIZOARTROSI_CONTROLS.GRIP.value, render_kw={'class': 'form-control'},  validators=None)
    dash = IntegerField(RIZOARTROSI_CONTROLS.DASH.value, render_kw={'class': 'form-control'},  validators=None)
    prwhe = IntegerField(RIZOARTROSI_CONTROLS.PRWHE.value, render_kw={'class': 'form-control'},  validators=None)
    eaton_littler = IntegerField(RIZOARTROSI_CONTROLS.EATON_LITTLER.value, render_kw={'class': 'form-control'}, validators=None )
    stato_cicatrice = StringField(RIZOARTROSI_CONTROLS.STATO_CICATRICE.value, render_kw={'class': 'form-control'},  validators=None)
    tipo_cicatrice = StringField(RIZOARTROSI_CONTROLS.TIPO_CICATRICE.value, render_kw={'class': 'form-control'},  validators=None)
    modena = StringField(RIZOARTROSI_CONTROLS.MODENA.value,render_kw={'class': 'form-control'},  validators=None)
    submit_rizoartrosi = SubmitField("Submit", render_kw={'class': 'btn btn-primary'})



class MedicalTreatmentForm(FlaskForm):
    """
    Questo form gestisce
    """
    entrytime_1 = TimeField('Time',render_kw={'class': 'form-control-custom'})
    
