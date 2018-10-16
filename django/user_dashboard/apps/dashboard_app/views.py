from django.shortcuts import render, redirect
from django.contrib import messages
from apps.dashboard_app.models import User, Message, Comment
import bcrypt

def index(request):
    return render(request, "dashboard_app/index.html")

def dashboard(request):
    if 'id' not in request.session:
        return redirect("/home/register")
    if request.method == "POST":
        return redirect("/home/register")
    data = User.objects.all()
    user_data = User.objects.get(id=request.session['id'])
    datdict = {
        "datakey": data,
        "pk": user_data
    }
    return render(request, "dashboard_app/dashboard_admin.html", datdict)

def destroy(request):
    User.objects.filter(id=request.POST['destroyid']).delete()
    return redirect("/home/dashboard")

def edit(request):
    request.session['x'] = request.POST['editid']
    user_data = User.objects.get(id=request.session['id'])
    datdict = {
        "pk": user_data
    }
    return render(request, "dashboard_app/edit.html", datdict)

def process_edit(request):
    tempid = request.session['x']
    User.objects.filter(id=tempid).update(first_name=request.POST['edit1'], last_name=request.POST['edit2'],email=request.POST['edit3'])
    return redirect("/home/dashboard")

def register(request):
    return render(request, "dashboard_app/register.html")

def validate_register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/home/register')
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

def add_new(request):
    user_data = User.objects.get(id=request.session['id'])
    datdict = {
        "pk": user_data
    }
    return render(request, "dashboard_app/add_user.html", datdict)

def validate_add_new(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/home/add_user')
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
        request.session['message'] = "added"
        return redirect("/home/success")

def login(request):
    return render(request, "dashboard_app/login.html")

def validate_login(request):
    request.session['error'] = ""
    try:
        User.objects.get(email=request.POST['login_email'])
    except:
        request.session['error'] += "Incorrect Email"
        return redirect("/home/register")
    user = User.objects.get(email=request.POST['login_email'])
    if user:
        if bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode()):
            request.session['message'] = "logged in"
            request.session['id'] = user.id
            return redirect("/home/dashboard")
        else:
            request.session['error'] += "Incorrect Password"
            return redirect("/home/register")

def success(request):
    data = User.objects.get(id=request.session['id'])
    userdict = {
        "datakey": data
    }
    return render(request, "dashboard_app/success.html", userdict)

def logoff(request):
    request.session['id'] = None
    return redirect('/home/login')

def wall(request):
    user_data = User.objects.get(id=request.session['id'])
    message_data = Message.objects.all()
    comment_data = Comment.objects.all()
    master_dict = {
        "datakey": user_data,
        "datakey2": message_data,
        "datakey3": comment_data,
    }
    return render(request, "wall_app/wall.html", master_dict)

def post_message(request):
    my_message = Message.objects.create(message=request.POST['new_message'], poster=User.objects.get(id=request.session['id']))
    return redirect("/home/wall")

def post_comment(request):
    if request.method == "POST":
        this_user = User.objects.get(id=request.session['id'])
        this_message = Message.objects.get(id=request.POST['message_id'])
        my_comment = Comment.objects.create(commenter=this_user, commented=this_message, comment=request.POST['new_comment'])
        return redirect("/home/wall")
    return redirect("/home/wall")