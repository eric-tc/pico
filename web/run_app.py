from app import my_app
from app.models import NotificationStatus,PathologyType,Pathology,EmailStatus

with my_app.app_context():
    NotificationStatus.insert_rows()
    PathologyType.insert_rows()
    Pathology.insert_rows()
    EmailStatus.insert_rows()

if __name__ == "__main__":

    #Create Default value to db before start app
    my_app.run(debug=True,host="0.0.0.0",port=4040)