from django.shortcuts import render
from .models import *
def storage(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store/storage.html', context)

def carts(request):
	context = {}
	return render(request, 'store/carts.html', context)

def buy(request):
	context = {}
	return render(request, 'store/buy.html', context)