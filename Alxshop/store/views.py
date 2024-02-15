from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
import datetime


def storage(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_carts_items
    else:
        items = []
        order = {"get_carts_total": 0, "get_carts_items": 0, "shipping": False}
        cartItems = order["get_carts_items"]

    products = Product.objects.all()
    context = {"products": products, "cartItems": cartItems}
    return render(request, "store/storage.html", context)


def carts(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_carts_items
    else:
        items = []
        order = {"get_carts_total": 0, "get_carts_items": 0, "shipping": False}
        cartItems = order["get_carts_items"]

    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, "store/carts.html", context)


def buy(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_carts_items
    else:
        items = []
        order = {"get_carts_total": 0, "get_carts_items": 0, "shipping": False}
        cartItems = order["get_carts_items"]
    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, "store/buy.html", context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    print("Action:", action)
    print("productId:", productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderItem.quantity = orderItem.quantity + 1
    elif action == "remove":
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)
from django.views.decorators.csrf import csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        if total == order.get_carts_total:
            order.complete = True
        order.save()
        if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address=data['shipping']['address'],
                city = data['shipping']['address'],
                state = data['shipping']['city'],
                zipcode = data['shipping']['zipcode'],
            )

    else:
        print('user is not logged in')
    return JsonResponse("payment complete", safe=False)