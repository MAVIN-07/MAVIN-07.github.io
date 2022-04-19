import firebase_admin
from firebase_admin import credentials,db

# Initialisation of SDK class
cred = credentials.Certificate("/home/mavin/ec-major-apr-2022-firebase-adminsdk-s2y7g-3fe8149a7b.json")
my_app_name = 'major_project_app'
xyz = {'databaseURL': 'https://ec-major-apr-2022-default-rtdb.firebaseio.com'}
obj = firebase_admin.initialize_app(cred,xyz,name=my_app_name)

class ListenerClass:
    def __init__(self,appname):
        self.appname = appname
    
    def listener(self,event):
        # Make a list of these values and pass as parameter to flask function to update the table
        print(event.event_type)
        print(event.path)
        print(event.data)
        print(self.appname)

#Temperature Listener
temperature_object = ListenerClass(my_app_name+'_1')
db.reference('timepass/Temperature', app=obj).listen(temperature_object.listener)

#pH Listener
ph_object = ListenerClass(my_app_name+'_2')
db.reference('timepass/pH', app=obj).listen(ph_object.listener)

#Turbidity Listener
turbidity_object = ListenerClass(my_app_name+'_3')
db.reference('timepass/Turbidity', app=obj).listen(turbidity_object.listener)

#Flow Listener
flow_object = ListenerClass(my_app_name+'_4')
db.reference('timepass/Flow', app=obj).listen(flow_object.listener)