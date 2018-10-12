from django.shortcuts import render, redirect

def index(request):
    return render(request, "books_authors/index.html")