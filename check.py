from firebase import firebase

firebase = firebase.FirebaseApplication("https://ec-major-apr-2022-default-rtdb.firebaseio.com/",None)
flow_json = firebase.get('/timepass/Flow/','')
turbidity_json = firebase.get('/timepass/Turbidity/','')
ph_json = firebase.get('/timepass/pH/','')
temperature_json = firebase.get('/timepass/Temperature/','')

print(flow_json)
print('#################################################################')
print(turbidity_json)
print('#################################################################')
print(temperature_json)
print('#################################################################')
print(ph_json)
print('#################################################################')