from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    time = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }

    return render(request,'time_app/index.html', time)