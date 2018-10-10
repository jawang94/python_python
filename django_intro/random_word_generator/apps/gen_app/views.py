from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    return render(request, "gen_app/index.html")

def reset(request):
    if request.method == "POST":
        request.session['counter'] += 1
        request.session['word'] = get_random_string(length=14)
        return redirect(index)