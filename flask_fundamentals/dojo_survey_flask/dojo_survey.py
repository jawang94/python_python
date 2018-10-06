from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route("/")
def surveyhome():
    return render_template("dojo_survey.html")

@app.route("/users", methods=['POST'])
def submitform():
    print("Form successfully submitted.")
    print(request.form)
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    if len(name) == 0:
        flash("Please enter a name!")
        return redirect('/')
    if len(name) < 121:
        flash("Name is too long!")
        return redirect('/')
    return render_template("dojo_survey_results.html")


if __name__ == "__main__":
    app.run(debug=True)