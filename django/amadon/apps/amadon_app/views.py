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
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'quantity' not in request.session:
        request.session['quantity'] = 0
    quantity = request.POST['quantity']
    item = Item.objects.get(id=request.POST['itemid'])
    total = int(quantity) * float(item.item_price)
    order_form = OrderForm(request.POST)
    if order_form.is_valid():
        order_form.order_total = total
        order_form.description = str(f'Purchased {quantity} {item}s for ${total}.')
        order_form.save()
    request.session['currenttotal'] = round(float(total),4)
    request.session['total'] += round(float(total),4)
    request.session['quantity'] += int(quantity)
    return redirect("/amadon/checkout")

def checkout(request):
    return render(request, "amadon_app/checkout.html")

