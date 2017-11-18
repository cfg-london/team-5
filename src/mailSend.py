from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

mail=Mail(app)

app.config.update(
	DEBUG=True,
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'codeforgoodisgood@gmail.com',
	MAIL_PASSWORD = 'codeforgood'
	)

mail=Mail(app)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      name = request.form.getlist('Name')
      physics = request.form.getlist('Physics')
      chem = request.form.getlist('chemistry')
      math = request.form.getlist('Mathematics')

      msg = Message("Heck",
                    sender="codeforgoodisgood@gmail.com",
                    recipients=["2jaycarder5@gmail.com"])
      print(name[0] + " " + physics[0] + " " + chem[0] + " " + math[0])
      msg.body = str(name[0] + " " + physics[0] + " " + chem[0] + " " + math[0])
      mail.send(msg)
      return render_template("home.html")

if __name__ == '__main__':
   app.run(debug = True)
