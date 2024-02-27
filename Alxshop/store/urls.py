"""URL for our views"""

from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path("", views.storage, name="storage"),
    path("carts/", views.carts, name="carts"),
    path("buy/", views.buy, name="buy"),
    path("update_item/", views.updateItem, name="update_item"),
    path("update_item/", views.processOrder, name="update_item"),
]
