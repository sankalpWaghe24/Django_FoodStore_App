from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Cart, CartItem
from food.models import Food
from django.contrib import messages
from .filters import OrderFilter
# Create your views here.


def addtocart(request, foodId):
    cart, status = Cart.objects.get_or_create(user=request.user)
    food = Food.objects.get(foodId=foodId)
    item = CartItem.objects.create(food=food)
    item.save()
    cart.itemlist.add(item)
    item.save()
    print(f"{cart}, status : {status}")
    if status:
        messages.success(request, "Your cart is Created ")
    else:
        messages.success(request, "Your cart is Updated ")
    messages.success(request, f"{food.foodName} is Added in Your Cart...")
    return redirect("viewcart")


def viewcart(request):
    cart, status = Cart.objects.get_or_create(user=request.user)
    orders = cart.itemlist.all()
    myfilter = OrderFilter()
    context = {'orders': orders, 'cart': cart, 'myfilter': myfilter}
    return render(request, 'cart/viewcart.html', context)


def removeitem(request, pk):
    item = CartItem.objects.get(pk=pk)
    item.delete()
    messages.success(request, f"{item.food.foodName} is remove from Cart")
    return redirect("viewcart")

import json
def updatecart(request):
    id = int(request.GET['id'])
    quantity = int(request.GET['quantity'])
    item = CartItem.objects.filter(pk=id)
    item.update(quantity=quantity)
    totalprice = item[0].get_total
    print(totalprice)
    return HttpResponse(json.dumps({"totalprice": totalprice}),content_type='application/json')

def checkout(request):
    cart, status = Cart.objects.get_or_create(user=request.user)
    orders = cart.itemlist.all()
    context = {'orders': orders, 'cart': cart}
    return render(request, 'cart/checkout.html', context)

