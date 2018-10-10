from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "blog_app/index.html")

def new(request):
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def show(request, number):
    response = "Placeholder to display blog "
    return HttpResponse(response + number + ".")

def edit(request, number):
    response = "Placeholder to edit blog "
    return HttpResponse(response + number + ".")

def destroy(request, number):
    return redirect('/')

def create(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['counter'] = 100
        return redirect("/")
    else:
        return redirect("/")