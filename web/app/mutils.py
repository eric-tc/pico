from datetime import datetime

from .internal_data import PATHOLOGY

def get_date(date,)->datetime:
    return datetime.strptime(str(date),"%d-%m-%Y")

"""
Recupera solo la data quando la stringa è in formato
format_string = '%Y-%m-%d %H:%M:%S' e la trasforma in "%d-%m-%Y"
"""
def get_date_from_datetime(datetime:datetime,)->datetime:
    
    formatted_date = datetime.strftime('%d-%m-%Y')
    return datetime.strptime(formatted_date,'%d-%m-%Y')


def get_pathology_enum(pathology_id):
    for pathology in PATHOLOGY:
        if pathology.value[0] == int(pathology_id):
            return pathology