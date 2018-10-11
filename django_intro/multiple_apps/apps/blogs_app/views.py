from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

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
    return redirect('/blogs')

def create(request):
    return redirect("/blogs")