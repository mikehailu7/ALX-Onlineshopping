from django.shortcuts import render
from .models import *
def storage(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store/storage.html', context)



def carts(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)

		items = order.orderitem_set.all()
	else:
		items = []

	context = {'items' :items, 'order' :order}
	return render(request, 'store/carts.html', context)

def buy(request):
	context = {}
	return render(request, 'store/buy.html', context)

