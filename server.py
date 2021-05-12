import random
from flask import Flask, render_template, redirect, request, session 
app = Flask(__name__)
app.secret_key = "this the secret key"

@app.route('/')
def index():
    if 'randomNum' not in session:
        session['randomNum'] = random.randint(1,100)
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    session['userGuess'] = request.form['userGuess']
    if session['randomNum'] > int(session['userGuess']):
        session['answer'] = "Too Low!"
        session['color'] = "#CF2A27"
    if session['randomNum'] < int(session['userGuess']):
        session['answer'] = "Too High!"
        session['color'] = "#CF2A27"
    if session['randomNum'] == int(session['userGuess']):
        session['answer'] = "You got it!"
        session['color'] = "green"
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)