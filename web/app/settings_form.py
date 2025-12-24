#questi form sono usati sia per il paziente che per il dottore

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length,NumberRange
from wtforms.fields import DateField,TimeField,SelectField,HiddenField,FieldList,FormField,FloatField,PasswordField,TextAreaField
from .internal_data_enum_pathologies import CONTROLS,OPTION_NULL

# Create a flask form for email password phone and name
class SettingsFormDoctor(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=35)],render_kw={'class': 'form-control','readonly': True})
    name = StringField('Nome', validators=[DataRequired(), Length(min=2, max=35)],render_kw={'class': 'form-control'})
    password = PasswordField('Password',render_kw={'class': 'form-control'})
    phone = StringField('Phone', validators=[DataRequired(), Length(min=6, max=35)],render_kw={'class': 'form-control'})
    submit_doctor_settings = SubmitField('Aggiorna',render_kw={'class': 'btn btn-success',"style":"max-width: 200px;"})

class SettingsFormPatient(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=35)],render_kw={'class': 'form-control'})
    name = StringField('Nome', validators=[DataRequired(), Length(min=2, max=35)],render_kw={'class': 'form-control'})
    surname = StringField('Cognome', validators=[DataRequired(), Length(min=2, max=35)],render_kw={'class': 'form-control'})
    birth_date = StringField('Data Di Nascita', render_kw={'class': 'form-control-custom','readonly':True}, validators=None)
    phone = StringField('Telefono', validators=[ Length(min=0, max=35)],render_kw={'class': 'form-control'})
    password = PasswordField('Password',render_kw={'class': 'form-control'})
    sx_dx_hand= SelectField('Mano Dominante', choices=[('', OPTION_NULL.NULL.value),('sx', 'Sinistro'), ('dx', 'Destro')],render_kw={'class': 'form-control'})
    manual_job = SelectField('Lavoro Manuale', choices=[('', OPTION_NULL.NULL.value),('no', 'No'), ('si', 'Si')],render_kw={'class': 'form-control'})
    sex = SelectField('Sesso', choices=[('', OPTION_NULL.NULL.value),('M', 'Maschio'), ('F', 'Femmina')],render_kw={'class': 'form-control'})
    job = StringField('Lavoro', validators=[Length(min=0, max=35)],render_kw={'class': 'form-control'})
    note = TextAreaField('Note',render_kw={'class': 'form-control'})
    submit_patient_settings = SubmitField('Aggiorna',render_kw={'class': 'btn btn-success',"style":"max-width: 200px;"})


