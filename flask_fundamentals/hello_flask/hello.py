from flask import Flask, render_template 
app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/dojo')
def dojo():
    return render_template('dojo.html')

@app.route('/jamaica')
def jamaica():
    return render_template('jamaica.html')

@app.route('/say/<name>')
def say(name):
    return "Hi "+name

@app.route('/repeat/<num>/<word>')
def hello(num,word):
    return word*int(num)

if __name__=="__main__":
    app.run(debug=True)



