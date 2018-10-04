from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<x>/<color>')
def play(x,color):
    return render_template("playground.html",times=int(x),box_color=color)

if __name__ == "__main__":
    app.run(debug=True)