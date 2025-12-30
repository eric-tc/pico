# In questo file sono calcolate le statistiche non è detto che tutti i parametri abbiano delle statistiche associate



def mpcj_statistics(data_list, indices):
    """
    Calcola le statistiche per i valori MPCJ
    :param data_list: Lista di dizionari contenenti i dati MPCJ
    :param indices: Indici delle dita da considerare
    :return: Dizionario con le statistiche calcolate
    """
    statistics = {}
    for index in indices:
        values = [data[index]['prom_flessione'] for data in data_list if index in data]
        if values:
            statistics[index] = {
                'min': min(values),
                'max': max(values),
                'average': sum(values) / len(values)
            }
    return statistics

def pipj_statistics(data_list, indices):
    """
    Calcola le statistiche per i valori PIPJ
    :param data_list: Lista di dizionari contenenti i dati PIPJ
    :param indices: Indici delle dita da considerare
    :return: Dizionario con le statistiche calcolate
    """
    statistics = {}
    for index in indices:
        values = [data[index]['prom_flessione'] for data in data_list if index in data]
        if values:
            statistics[index] = {
                'min': min(values),
                'max': max(values),
                'average': sum(values) / len(values)
            }
    return statistics

def dipj_statistics(data_list, indices):
    """
    Calcola le statistiche per i valori DIPJ
    :param data_list: Lista di dizionari contenenti i dati DIPJ
    :param indices: Indici delle dita da considerare
    :return: Dizionario con le statistiche calcolate
    """
    statistics = {}
    for index in indices:
        values = [data[index]['prom_flessione'] for data in data_list if index in data]
        if values:
            statistics[index] = {
                'min': min(values),
                'max': max(values),
                'average': sum(values) / len(values)
            }
    return statistics


def ipj_statistics(data_list, indices):
    """
    Calcola le statistiche per i valori IPJ
    :param data_list: Lista di dizionari contenenti i dati IPJ
    :param indices: Indici delle dita da considerare
    :return: Dizionario con le statistiche calcolate
    """
    statistics = {}
    for index in indices:
        values = [data[index]['prom_flessione'] for data in data_list if index in data]
        if values:
            statistics[index] = {
                'min': min(values),
                'max': max(values),
                'average': sum(values) / len(values)
            }
    return statistics

def polso_statistics(data_list):
    """
    Calcola le statistiche per i valori del polso
    :param data_list: Lista di valori del polso
    :return: Dizionario con le statistiche calcolate
    """
    if not data_list:
        return {}
    
    return {
        'min': min(data_list),
        'max': max(data_list),
        'average': sum(data_list) / len(data_list)
    }

def trapezio_metacarpale_statistics(data_list):
    """
    Calcola le statistiche per i valori trapezio-metacarpale
    :param data_list: Lista di valori trapezio-metacarpale
    :return: Dizionario con le statistiche calcolate
    """
    if not data_list:
        return {}
    
    return {
        'min': min(data_list),
        'max': max(data_list),
        'average': sum(data_list) / len(data_list)
    }
def forza_statistics(data_list):
    """
    Calcola le statistiche per i valori di forza
    :param data_list: Lista di valori di forza
    :return: Dizionario con le statistiche calcolate
    """
    if not data_list:
        return {}
    
    return {
        'min': min(data_list),
        'max': max(data_list),
        'average': sum(data_list) / len(data_list)
    }

def dash_statistics(data_list):
    """
    Calcola le statistiche per i valori DASH
    :param data_list: Lista di valori DASH
    :return: Dizionario con le statistiche calcolate
    """
    if not data_list:
        return {}
    
    return {
        'min': min(data_list),
        'max': max(data_list),
        'average': sum(data_list) / len(data_list)
    }

def prwhe_statistics(data_list):
    """
    Calcola le statistiche per i valori PRW
    :param data_list: Lista di valori PRW
    :return: Dizionario con le statistiche calcolate
    """
    if not data_list:
        return {}
    
    return {
        'min': min(data_list),
        'max': max(data_list),
        'average': sum(data_list) / len(data_list)
    }
def vas_statistics(data_list):
    """
    Calcola le statistiche per i valori VAS
    :param data_list: Lista di valori VAS
    :return: Dizionario con le statistiche calcolate
    """
    if not data_list:
        return {}
    
    return {
        'min': min(data_list),
        'max': max(data_list),
        'average': sum(data_list) / len(data_list)
    }


