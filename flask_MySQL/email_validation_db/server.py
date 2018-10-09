from flask import Flask, render_template, request, session, flash, redirect
from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'sooooosecretbro'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submitForm():
    mysql = connectToMySQL("email_validation")
    query = "INSERT INTO emails (email_address, created_on) VALUES (%(email_address)s, NOW());"
    data = {
             'email_address': request.form['email'],
           }
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'email')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        flash('The email address you entered (' + request.form["email"] + ') is a VALID email address! Thank you!', 'success')
    new_email_id = mysql.query_db(query, data)
    return redirect("/list")

@app.route("/list")
def listEmails():
    mysql = connectToMySQL("email_validation")
    emails = mysql.query_db("SELECT email_address,created_on FROM emails")
    flash('The email address you entered (' + request.form["email"] + ') is a VALID email address! Thank you!', 'success')
    print("Fetched all friends", emails)
    return render_template("success.html", emails=emails)


if __name__ == "__main__":
    app.run(debug=True)