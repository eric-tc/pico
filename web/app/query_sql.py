#Questo file contiente le querySql comuni tra paziente e dottore

from .models import PathologyData,PathologyType,Pathology,User
from .internal_data import CONTROL_STATUS, CONTROLS,RizoartrosiControlsTimeline,PATHOLOGY_STATUS
from . import db
from datetime import datetime

