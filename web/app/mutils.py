from datetime import datetime

from .internal_data import PATHOLOGY
from datetime import datetime, timedelta,time

def get_date(date,)->datetime:
    return datetime.strptime(str(date),"%d-%m-%Y")

"""
Recupera solo la data quando la stringa è in formato
format_string = '%Y-%m-%d %H:%M:%S' e la trasforma in "%d-%m-%Y"
"""
def get_date_from_datetime(datetime:datetime,)->datetime:
    
    formatted_date = datetime.strftime('%d-%m-%Y')
    return datetime.strptime(formatted_date,'%d-%m-%Y')

"""
date: è in formato %d-%m-%Y
return: è in formato %Y-%m-%d
"""
def getDateInYMD(date:datetime):
    return datetime.strptime(date, "%d-%m-%Y").strftime("%Y-%m-%d")

def get_pathology_enum(pathology_id):
    for pathology in PATHOLOGY:
        if pathology.value[0] == int(pathology_id):
            return pathology
        

"""
Utilizzata per settare la data del prossimo controllo
"""
def pathology_set_next_control(request,control_number:int,weeks_to_add:int):

    is_date_accepted= 0
    #Solo il primo controllo ha la data dell'intervento
    if control_number==0:
        data_prossimo_controllo= request.form.get("data_primo_controllo")
        orario_prossimo_controllo= request.form.get("orario_primo_controllo")

        if(data_prossimo_controllo is not None):
            data_prossimo_controllo= get_date(data_prossimo_controllo)
            is_date_accepted=1
        else:
            data_prossimo_controllo= datetime.utcnow() + timedelta(weeks=weeks_to_add)

    else:
        data_prossimo_controllo= datetime.utcnow() + timedelta(weeks=weeks_to_add)
        orario_prossimo_controllo= "12:00"  

    return data_prossimo_controllo,orario_prossimo_controllo,is_date_accepted