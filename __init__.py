import os
from flask import Flask,render_template,request,url_for,redirect
# from flask_mail import Mail,Message
# from firebase import firebase

# firebase = firebase.FirebaseApplication("https://ec-major-apr-2022-default-rtdb.firebaseio.com/",None)
# flow_json = firebase.get('/timepass/Flow/','')
# turbidity_json = firebase.get('/timepass/Turbidity/','')
# ph_json = firebase.get('/timepass/pH/','')
# temperature_json = firebase.get('/timepass/temperature/','')

app = Flask(__name__)

# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = '<mailid>'
# app.config['MAIL_PASSWORD'] = '<password>'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True

# mail = Mail(app)

@app.route('/')
def homepage():
    return render_template('index.html')

# @app.route('/mail/')
# def send_message():
#     if request.method == 'POST':
#         name = request.form['Name']
#         msg = request.form['Message']
#         email = request.form['Email']
#         subject = "Thanks for your interest to GoInsightful!"
#         message = Message(subject, sender='<mailid>',recipients=[email])
#         message.body = " ".join(["Hi", name, "\n", "This is what we got from you:", "\n", msg])

#         mail.send(message)

#         success = "Message Sent"
#         return render_template("success.html", success=success)

if __name__== "__main__":
    app.run(debug=True)