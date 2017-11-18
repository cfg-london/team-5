from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('home.html')

@app.route('/form', methods=['POST'])
def my_form_post():
    test = request.form['test']
    processed_text = test.upper()
    print(processed_text)
    return processed_text

if __name__ == '__main__':
   app.run(debug = True)
