from django.shortcuts import render, redirect

def index(request):
    return render(request, "dojo_app/index.html")