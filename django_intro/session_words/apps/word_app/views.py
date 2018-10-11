from django.shortcuts import render, redirect
from time import gmtime, strftime

def index(request):
    return render(request, "word_app/index.html")

def process(request):
    if 'words' not in request.session:
        request.session['words'] = []
    temp_list = request.session['words']
    temp_list.append({"word": request.POST['word'], "color": request.POST['color'],
                     "show_big": request.POST['big_font'], 
                     "created_on": strftime("%Y-%m-%d %H:%M:%S", gmtime())})
    request.session['words'] = temp_list
    return redirect("/session_words")

def clear(request):
    request.session['words'] = ""
    return redirect("/session_words")