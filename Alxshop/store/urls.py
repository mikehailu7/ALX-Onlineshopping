from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.storage, name="storage"),
	path('carts/', views.carts, name="carts"),
	path('buy/', views.buy, name="buy"),
]