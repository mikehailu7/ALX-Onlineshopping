from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True, blank=True) # a user can have one customer and a customer can have only one user
    name = models.CharField(max_length = 200, null = True) # charfield to say it is a string
    email= models.CharField(max_length = 200, null= True) # CASCADE is used to simultaneously delete or update an entry from both the child and parent table
    
    def __str__(self):  # this will be shown on the admin panel when we create the name
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length =200, null = True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null = True, blank=True)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    transaction_id = models.CharField(max_length=200, null=True)
    complete = models.BooleanField(default= False, null=True, blank=False )
    
    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    Product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True )
    data_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(max_length=200, null=True)
    
    def __str__(self):
        return self.address