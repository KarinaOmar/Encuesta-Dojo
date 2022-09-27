from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

app.secret_key = "llave super secreta"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comentarios']=request.form['comentarios']
    return redirect('/result')


@app.route('/result')
def result():
    return render_template('result.html')









if __name__ == "__main__":
    app.run(debug=True)