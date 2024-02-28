import json
from .models import *


def cookieCart(request):
    try:
        carts = json.loads(request.COOKIES["carts"])
    except:
        carts = {}

    print("Carts:", carts)
    items = []
    order = {"get_carts_total": 0, "get_carts_items": 0, "shipping": False}
    cartItems = order["get_carts_items"]

    for i in carts:
        try:
            cartItems += carts[i]["quantity"]

            product = Product.objects.get(id=i)
            total = product.price * carts[i]["quantity"]

            order["get_carts_total"] += total
            order["get_carts_items"] += carts[i]["quantity"]

            item = {
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "imageURL": product.imageURL,
                },
                "quantity": carts[i]["quantity"],
                "get_total": total,
                }
            items.append(item)

            if product.digital == False:
                order["shipping"] = True
        except:
            pass

    return {"cartItems": cartItems, "order": order, "items": items}


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_carts_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData["cartItems"] 
        order = cookieData["order"]
        items = cookieData["items"]
    return {"cartItems": cartItems, "order": order, "items": items}


def gustOrder(request, data):
    print("user is not logged in")

    print("COOKIES:", request.COOKIES)
    name = data["form"]["name"]
    email = data["form"]["email"]
    cookieData = cookieCart(request)
    items = cookieData["items"]

    customer, created = Customer.objects.get_or_create(
        email=email,
    )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )

    for item in items:
        product = Product.objects.get(id=item["product"]["id"])
        orderItem = OrderItem.objects.create(
            product=product, order=order, quantity=item["quantity"]
        )

    return customer, order
