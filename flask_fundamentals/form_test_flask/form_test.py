from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("form_test.html")
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    name = request.form['name']
    email = request.form['email']
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True) 

