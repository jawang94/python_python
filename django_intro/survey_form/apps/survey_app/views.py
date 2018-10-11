from django.shortcuts import render, redirect

def index(request):
    return render(request, "survey_app/index.html")

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect("/result")

def result(request):
    if request.method == "POST":
        return redirect("/")
    return render(request, "survey_app/result.html")
