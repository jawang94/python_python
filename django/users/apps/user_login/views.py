from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, "user_login/index.html")