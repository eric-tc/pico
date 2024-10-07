# questo file DEVE racchiudere solo gli Enum delle patologie che hanno un decorso post operatorio 
# diverso in base alle opzioni selezionate durante la fase di compilazione del form intervento
from enum import Enum

# In base a questi valori avrò un decorso post operatorio diverso
class FrattureMetaCarpaliEnum(Enum):
    CHIRURGICO = "1"
    NON_CHIRURGICO = "2"