#questi form sono usati sia per il paziente che per il dottore

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length,NumberRange
from wtforms.fields import DateField,TimeField,SelectField,HiddenField,FieldList,FormField,FloatField,PasswordField


# Create a flask form for email password phone and name
class SettingsFormDoctor(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=35)],render_kw={'class': 'form-control','readonly': True})
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=35)],render_kw={'class': 'form-control'})
    password = PasswordField('Password',render_kw={'class': 'form-control'})
    phone = StringField('Phone', validators=[DataRequired(), Length(min=6, max=35)],render_kw={'class': 'form-control'})
    submit_doctor_settings = SubmitField('Aggiorna',render_kw={'class': 'btn btn-success',"style":"max-width: 200px;"})

class SettingsFormPatient(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=35)],render_kw={'class': 'form-control'})
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=35)],render_kw={'class': 'form-control'})
    birth_date = StringField('Data Di Nascita', render_kw={'class': 'form-control-custom','readonly':True}, validators=None)
    phone = StringField('Phone', validators=[DataRequired(), Length(min=6, max=35)],render_kw={'class': 'form-control'})
    password = PasswordField('Password',render_kw={'class': 'form-control'})
    sx_dx_hand= SelectField('Mano Dominante', choices=[('sx', 'Sinistro'), ('dx', 'Destro')],render_kw={'class': 'form-control'})
    submit_patient_settings = SubmitField('Aggiorna',render_kw={'class': 'btn btn-success',"style":"max-width: 200px;"})


