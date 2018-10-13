from django.shortcuts import render, redirect
from apps.first_app.models import Users, UsersForm

def index(request):
    if request.method == "POST":
        return redirect("/users/create")
    data = Users.objects.all()
    datdict = {
        "datakey": data
    }
    return render(request, "first_app/result.html", datdict)

def process(request):
    form = UsersForm(request.POST)
    if form.is_valid():
        form.subject = request.POST['first_name'] + request.POST['last_name']
        form.email = request.POST['email']
        form.save()
    return redirect("/users")

def create(request):
    return render(request, "first_app/index.html")

def show(request):
    data = Users.objects.filter(id=request.POST['user_id'])
    datuser = {
        "user": data
    }
    return render(request, "first_app/user.html", datuser)

def destroy(request):
    Users.objects.filter(id=request.POST['destroyid']).delete()
    return redirect("/users")

def edit(request):
    request.session['x'] = request.POST['editid']
    return render(request, "first_app/edit.html")

def process_edit(request):
    tempid = request.session['x']
    Users.objects.filter(id=tempid).update(first_name=request.POST['edit1'], last_name=request.POST['edit2'],email=request.POST['edit3'])
    return redirect("/users")