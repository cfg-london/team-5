from flask import Flask, request, render_template #, Mail

app = Flask(__name__)
mail=Mail(app)

 app.config['MAIL_SERVER']='smtp.gmail.com'
 app.config['MAIL_PORT'] = 465
 app.config['MAIL_USERNAME'] = 'codeforgoodisgood@hotmail.com'
 app.config['MAIL_PASSWORD'] = 'Codeforgood'
 app.config['MAIL_USE_TLS'] = False
 app.config['MAIL_USE_SSL'] = True

@app.route('/', methods=['GET'])
def my_form():
    return 'a'

@app.route('/healthcheck')
def healthcheck():
    return "Healthy"

@app.route('/form', methods=['GET','POST'])
def my_form_post():
   test = request.form['test']
   processed_text = test.upper()
    msg = Message("hello",
                  sender="codeforgoodisgood@hotmail.com",
                  recipients=["jontinator@hotmail.co.uk"])
    msg.body = processed_text
    mail.send(msg)
   print (processed_text)
   return processed_text

if __name__ == '__main__':
   app.run()
