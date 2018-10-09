from flask import Flask, render_template, session, request, redirect, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
bcrypt = Bcrypt(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    mysql = connectToMySQL("login_and_registration")
    query = "SELECT * FROM users WHERE email = %(login_email)s;"
    data = {"login_email": request.form["login_email"]}
    result = mysql.query_db(query, data)
    if result:

        if bcrypt.check_password_hash(result[0]['password'], request.form['login_password']):

            session['userid'] = result[0]['id']

            return redirect('/loggedin')

    flash("You could not be logged in")
    return redirect("/")


@app.route("/register", methods=['POST'])
def register():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    mysql = connectToMySQL("login_and_registration")
    query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password_hash)s);"
    data = {"first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "password_hash": pw_hash
            }
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')
    if request.form['first_name'].isalpha() == False:
        flash("Name cannot contain numbers!", 'first_name')
    elif len(request.form['first_name']) <= 2:
        flash("Name must be 2+ characters", 'first_name')
    if request.form['last_name'].isalpha() == False:
        flash("Name cannot contain numbers!", 'last_name')
    elif len(request.form['last_name']) <= 2:
        flash("Name must be 2+ characters", 'last_name')
    if len(request.form['password']) < 1:
        flash("Password cannot be blank!", 'password')
    elif len(request.form['password']) < 8:
        flash("Password must be 8+ characters", 'password')
    if '_flashes' in session.keys():
        return redirect("/")
    new_user_id = mysql.query_db(query, data)
    return redirect("/success")

@app.route("/loggedin")
def loggedin():
    return render_template("loggedin.html")

@app.route("/success")
def success():
    mysql = connectToMySQL("login_and_registration")
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
