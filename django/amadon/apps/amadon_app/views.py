from django.shortcuts import render, redirect
from apps.amadon_app.models import Item, Order, OrderForm, ItemForm

def index(request):
    data = Item.objects.all()
    itemdict = {
        "datakey": data
    }
    return render(request, "amadon_app/index.html", itemdict)

def create(request):
    form = ItemForm(request.POST)
    if form.is_valid():
        form.item_name = request.POST['item_name']
        form.item_price = request.POST['item_price']
        form.save()
    return redirect("/amadon")

def process(request):
    return redirect("/amadon/checkout")

def checkout(request):
    return render(request, "amadon_app/checkout.html")

