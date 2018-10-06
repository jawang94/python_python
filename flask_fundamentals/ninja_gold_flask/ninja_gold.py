from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route('/')         
def index():
    if 'message' not in session:
        session['message'] = ""
    if len(session['message']) > 200:
        session['message'] = ""
    return render_template("ninja_gold.html",message=session['message'],total=session['total'])


@app.route('/process_gold', methods=['POST'])         
def processgold():
    import random
    x = 0
    if request.form['building'] == 'farm':
        x = random.randrange(10,21)
        session['message'] += "Earned " + str(x) + " coins from the farm!<br>" 
    if request.form['building'] == 'cave':
        x = random.randrange(5,11)
        session['message'] += "Earned " + str(x) + " coins from the cave!<br>" 
    if request.form['building'] == 'house':
        x = random.randrange(2,6)
        session['message'] += "Earned " + str(x) + " coins from house!<br>" 
    if request.form['building'] == 'casino':
        x = random.randrange(-50,51)
        if x >= 0:
            session['message'] += "Entered a casino and earned " + str(x) + " coins! Lucky!<br>" 
        elif x < 0:
            session['message'] += "Entered a casino and lost " + str(x) + " coins! Uh oh!<br>" 
    if 'total' not in session:
        session['total'] = 0
    else:
        session['total'] = session.get('total') + x

    return redirect("/")


if __name__=="__main__":   
    app.run(debug=True)    