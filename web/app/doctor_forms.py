from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length

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
    nprs_vas = IntegerField('NPRS VAS', render_kw={'class': 'form-control'}, validators=None)
    prom_arom_mcpj = IntegerField('PROM AROM MCPJ', render_kw={'class': 'form-control'}, validators=None)
    prom_arom_Ipj = IntegerField('PROM AROM IPJ', render_kw={'class': 'form-control'}, validators=None)
    abduction = IntegerField('Abduction', render_kw={'class': 'form-control'},  validators=None)
    anterposition = IntegerField('Anterposition', render_kw={'class': 'form-control'},  validators=None)
    kapandji = IntegerField('Kapandji', render_kw={'class': 'form-control'},  validators=None)
    pinch = IntegerField('Pinch', render_kw={'class': 'form-control'},  validators=None)
    grip = IntegerField('Grip', render_kw={'class': 'form-control'},  validators=None)
    dash = IntegerField('DASH', render_kw={'class': 'form-control'},  validators=None)
    prwhe = IntegerField('PRWHE', render_kw={'class': 'form-control'},  validators=None)
    Eaton_littler = IntegerField('Eaton Littler', render_kw={'class': 'form-control'}, validators=None )
    scar_status = StringField('Scar Status', render_kw={'class': 'form-control'},  validators=None)
    scar_type = StringField('Scar Type', render_kw={'class': 'form-control'},  validators=None)