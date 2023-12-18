#This file handles internal data of the application

from enum import Enum

# Define an enumeration class
class ROLE(Enum):
    DOCTOR = 1
    PATIENT = 2

# Define the notification status
class NOTIFICATION_STATUS(Enum):
    SENT = 1
    APPROVED = 2
    TOELIMINATE= 3