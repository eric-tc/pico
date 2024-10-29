from datetime import datetime

from .internal_data import PATHOLOGY
from datetime import datetime, timedelta,time

def get_date(date,)->datetime:
    return datetime.strptime(str(date),"%d-%m-%Y")


def get_date_YMD(date,)->datetime:
    return datetime.strptime(str(date),"%Y-%m-%d")
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
control_check: Verifica se è il primo controllo dopo aver skippato i controlli dove la timeline ha come
valore di settimane 0. Significa che il controllo è stato skippato e quindi non è stato effettuato
"""
def pathology_set_next_control(data_primo_controllo,
                               orario_primo_controllo,
                               control_check:int,
                               weeks_to_add:int,
                               surgery_date:str):

    is_date_accepted= 0
    orario_prossimo_controllo= "12:00"
    #Le date dei controllo sono in base alla surgery_date
    #Nel primo controllo se presente la data metto controllo come accettato
    if control_check:
        
        if(data_primo_controllo is not None):
            data_prossimo_controllo= get_date(data_primo_controllo)
            orario_prossimo_controllo= orario_primo_controllo
            is_date_accepted=1
        else:
            data_prossimo_controllo= get_date_YMD(surgery_date) + timedelta(weeks=weeks_to_add)
            orario_prossimo_controllo= "12:00"

    else:
        data_prossimo_controllo= get_date_YMD(surgery_date) + timedelta(weeks=weeks_to_add)
        orario_prossimo_controllo= "12:00"  

    if orario_prossimo_controllo is None:
        orario_prossimo_controllo= "12:00"
    

    return data_prossimo_controllo,orario_prossimo_controllo,is_date_accepted