from django.shortcuts import render, redirect
from django.contrib import messages
from apps.logreg_app.models import User
import bcrypt


def index(request):
    return render(request, "logreg_app/index.html")


def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/home')
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash,
        )
        user = User.objects.get(email=request.POST['email'])
        request.session['id'] = user.id
        request.session['message'] = "registered"
        return redirect("/home/success")


def validate_login(request):
    request.session['error'] = ""
    try:
        User.objects.get(email=request.POST['login_email'])
    except:
        request.session['error'] += "Incorrect Email"
        return redirect("/home")
    user = User.objects.get(email=request.POST['login_email'])
    if user:
        if bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode()):
            request.session['message'] = "logged in"
            request.session['id'] = user.id
            return redirect("/home/success")
        else:
            request.session['error'] += "Incorrect Password"
            return redirect("/home")



def success(request):
    data = User.objects.get(id=request.session['id'])
    userdict = {
        "datakey": data
    }
    return render(request, "logreg_app/success.html", userdict)
