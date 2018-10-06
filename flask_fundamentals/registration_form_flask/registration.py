from flask import Flask, render_template, request, redirect, flash, session
import re, time
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'supersecret'


@app.route("/", methods=["GET"])
def index():
    return render_template("registration.html")

@app.route("/process", methods=["POST"])
def submitform():
    if len(request.form['first_name']) < 1:
        flash("First name cannot be blank!", 'first_name')
    if not request.form['first_name'].isalpha():
        flash("First name cannot contain numbers!", 'first_name')
    if len(request.form['last_name']) < 1:
        flash("Last name cannot be blank!", 'last_name')
    if not request.form['last_name'].isalpha():
        flash("Last name cannot contain numbers!", 'last_name')
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')
    try: 
        time.strptime(request.form['bday'], "%m/%d/%Y")
    except ValueError:
        flash("Invalid birthdate format!")
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters!", 'password')
    if request.form['password'].isalpha():
        flash("Password must contain at least one number!")
    if request.form['password'].islower():
        flash("Password must contain at least one upper case letter!")
    if request.form['password_confirmation'] != request.form['password']:
        flash("Passwords don't match!", 'password')
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        flash('Success!')
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
