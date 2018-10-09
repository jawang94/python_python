from flask import Flask, render_template, request, session, flash, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():)
    return render_template('index.html', friends=all_friends)
    
@app.route("/submit", methods=["POST"])
def submit():
    mysql = connectToMySQL("friendsdb")
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    if len(request.form['first_name']) < 1:
        flash('Please enter a first name.')
    if len(request.form['first_name']) < 1:
        flash('Please enter a first name.')
    if len(request.form['last_name']) < 1:
        flash('Please enter a last name.')
    if len(request.form['occupation']) < 1:
        flash('Please enter an occupation.')
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        flash('Success!')
    new_friend_id = mysql.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)



