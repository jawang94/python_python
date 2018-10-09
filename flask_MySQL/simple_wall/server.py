from flask import Flask, render_template, session, request, redirect, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "secretwall!"
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("testindex.html")

@app.route("/register", methods=['POST'])
def register():
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
    if request.form['password'] != request.form['confirm_password']:
        flash("Passwords don't match!", 'password')
    if '_flashes' in session.keys():
        return redirect("/")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    mysql = connectToMySQL("simple_wall")
    query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password_hash)s);"
    query2 = "SELECT email FROM users WHERE email = %(email)s;"
    data = {"first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "password_hash": pw_hash
            }
    result2 = mysql.query_db(query2, data)
    if result2 != False:
        flash("This email is already in use!")
    if '_flashes' in session.keys():
        return redirect("/")
    new_user_id = mysql.query_db(query, data)
    return redirect("/success")

@app.route("/success")
def success():
    mysql = connectToMySQL("simple_wall")
    return render_template("success.html")

@app.route('/login', methods=['POST'])
def login():
    mysql = connectToMySQL("simple_wall")
    query = "SELECT * FROM users WHERE email = %(login_email)s;"
    data = {"login_email": request.form["login_email"]}
    result = mysql.query_db(query, data)
    if result:
    
        if bcrypt.check_password_hash(result[0]['password'], request.form['login_password']):
    
            session['userid'] = result[0]['user_id']

            return redirect('/loggedin')

    flash("You could not be logged in")
    return redirect("/")

@app.route("/loggedin")
def loggedin():
    mysql = connectToMySQL("simple_wall")
    query = "SELECT * FROM users WHERE user_id = %(userid)s;"
    data = {"userid": session['userid']}
    result = mysql.query_db(query, data)
    session['username'] = result[0]['first_name']
    query2 = "SELECT messages.user_id as sent_from_id,users2.first_name,messages.recipient_id as sent_to_id,users.first_name,messages.message,messages.created_on FROM users JOIN messages ON users.user_id = messages.recipient_id JOIN users as users2 ON messages.user_id = users2.user_id WHERE messages.recipient_id = %(userid)s;"
    result2 = mysql.query_db(query2, data)
    query3 = "SELECT count(message) as messages_received FROM messages WHERE messages.recipient_id = %(userid)s;"
    result3 = mysql.query_db(query3, data)
    query4 = "SELECT count(message) as messages_sent FROM messages WHERE messages.user_id = %(userid)s;"
    result4 = mysql.query_db(query4, data)
    query5 = "SELECT * FROM users;"
    result5 = mysql.query_db(query5, data)
    return render_template("loggedin.html",name=session['username'],all_messages=result2,count=result3[0]['messages_received'],sent=result4[0]['messages_sent'],all_users=result5)

@app.route("/sendmessage", methods=['POST'])
def sendmessage():
    mysql = connectToMySQL("simple_wall")
    query = "INSERT INTO messages (message, user_id, recipient_id, created_on) VALUES (%(message)s, %(user_id)s, %(recipient_id)s, NOW());"
    data = {"message": request.form['message'],
            "user_id": session['userid'],
            "recipient_id": request.form['recipient_id']
            }
    new_message_id = mysql.query_db(query, data)
    if new_message_id:
        flash('Message sent!')
        return redirect("/loggedin")
    flash('Message not sent.')
    return redirect("/loggedin")

if __name__ == "__main__":
    app.run(debug=True)
