from flask import Flask, render_template, request, redirect
app = Flask(__name__)

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
    return render_template("dojo_survey_results.html")
    

# @app.route("/result")
# def showresults():
#     print(request.form)
#     return render_template("dojo_survey_results.html")

if __name__ == "__main__":
    app.run(debug=True)