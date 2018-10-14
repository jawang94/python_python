from django.shortcuts import render, redirect
from apps.logreg_app.models import User, UserForm
import bcrypt 

def index(request):
    return render(request, "logreg_app/index.html")

def create(request):
    form = UserForm(request.POST)
    if form.is_valid():
        form.first_name = request.POST['first_name']
        form.last_name = request.POST['last_name']
        form.email = request.POST['email']
        form.password = request.POST['password']
        form.save()
    return redirect("/home")

# def login(request):
#     if 'total' not in request.session:
#         request.session['total'] = 0
#     if 'quantity' not in request.session:
#         request.session['quantity'] = 0
#     quantity = request.POST['quantity']
#     item = Item.objects.get(id=request.POST['itemid'])
#     total = int(quantity) * float(item.item_price)
#     order_form = OrderForm(request.POST)
#     if order_form.is_valid():
#         order_form.order_total = total
#         order_form.description = str(f'Purchased {quantity} {item}s for ${total}.')
#         order_form.save()
#     request.session['currenttotal'] = round(float(total),4)
#     request.session['total'] += round(float(total),4)
#     request.session['quantity'] += int(quantity)
#     return redirect("/home/success")

def success(request):
    return render(request, "logreg_app/success.html")

