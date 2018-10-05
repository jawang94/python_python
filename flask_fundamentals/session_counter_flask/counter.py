from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'notsosecret' 

@app.route("/")
def main():
    if session['visits'] != 0:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return render_template("counter.html",total_visits=session.get('visits'))

@app.route('/plustwo')
def plustwo():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    return redirect("/")

@app.route('/clear')
def clear():
    if 'visits' in session:
        session['visits'] = 0
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)