from flask import Flask, render_template, session, redirect, request, flash
app = Flask(__name__)
app.secret_key = 'datsecret' 

@app.route("/")
def main():
    return render_template("number_game.html")

@app.route('/submit', methods=["post"])
def submit():
    import random
    x = random.randrange(0, 101) 
    guess = request.form['guess']
    session['result'] = ""
    session['bgrcolor'] = ""
    if len(guess) == 0:
        flash("Please enter a number!")
        return redirect("/")
    if x == int(guess):
        return redirect("/correct")
    elif x > int(guess):
        return redirect("/toolow")
    else:
        return redirect("/toohigh")

@app.route('/correct')
def correct():
    session['result'] = "Correct"
    session['bgrcolor'] = "Green"
    return render_template("number_game_result.html", result=session['result'],bgrcolor=session['bgrcolor'])

@app.route('/toolow')
def toolow():
    session['result'] = "Too Low!"
    session['bgrcolor'] = "lightblue"
    return render_template("number_game_result.html", result=session['result'],bgrcolor=session['bgrcolor'])

@app.route('/toohigh')
def toohigh():
    session['result'] = "Too High!"
    session['bgrcolor'] = "Red"
    return render_template("number_game_result.html", result=session['result'],bgrcolor=session['bgrcolor'])

if __name__ == "__main__":
    app.run(debug=True)