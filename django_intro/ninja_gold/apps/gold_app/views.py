from django.shortcuts import render, redirect
import random

def index(request):
    # if 'total' not in request.session:
    #     request.session['total'] = 0
    # if 'message' not in request.session:
    #     request.session['message'] = ""
    # if len(session['message']) > 250:
    #     request.session['message'] = ""
    return render(request, "gold_app/index.html")

def process(request):
    x = 0
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'message' not in request.session:
        request.session['message'] = ""
    if len(request.session['message']) > 250:
        request.session['message'] = ""
    if request.POST['building'] == 'farm':
        x = random.randrange(10,21)
        request.session['message'] += "Earned " + str(x) + " coins from the farm!<br>" 
    if request.POST['building'] == 'cave':
        x = random.randrange(5,11)
        request.session['message'] += "Earned " + str(x) + " coins from the cave!<br>" 
    if request.POST['building'] == 'house':
        x = random.randrange(2,6)
        request.session['message'] += "Earned " + str(x) + " coins from house!<br>" 
    if request.POST['building'] == 'casino':
        x = random.randrange(-50,51)
        if x >= 0:
            request.session['message'] += "Entered a casino and earned " + str(x) + " coins! Lucky!<br>" 
        elif x < 0:
            request.session['message'] += "Entered a casino and lost " + str(abs(x)) + " coins! Uh oh!<br>" 
    if 'total' not in request.session:
        request.session['total'] = 0
    else:
        request.session['total'] = request.session['total'] + x
    return redirect("/")