from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def eightByEight():
    return render_template("checkerboard.html")


@app.route('/play/<x>/<y>')
def play(x,y):
    return render_template("checkerboard2.html",x=int(x),y=int(y))

if __name__ == "__main__":
    app.run(debug=True)