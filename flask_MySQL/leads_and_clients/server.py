from flask import Flask, render_template, request, session, flash, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'supersecretkey'


@app.route('/')
def index():
    mysql = connectToMySQL("lead_gen_business")
    all_customers = mysql.query_db("SELECT clients.first_name,clients.last_name,count(leads.leads_id) as leads FROM clients JOIN sites ON clients.client_id = sites.client_id JOIN leads ON sites.site_id = leads.site_id GROUP BY clients.first_name,clients.last_name ORDER BY leads desc;")
    print("Fetched all customers", all_customers)
    return render_template('index.html', customers=all_customers)


@app.route("/submit", methods=["POST"])
def submit():
    mysql = connectToMySQL("lead_gen_business")
    query = "INSERT INTO leads (updated_at) VALUES (NOW());"
    data = {
        'updated_at': request.form['date'],
    }
    if len(request.form['date']) < 1:
        flash('Please enter a valid date.')
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        flash('Success!')
    new_friend_id = mysql.query_db(query, data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
