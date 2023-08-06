
from django.shortcuts import render
from store.models import *

def cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items1 = order.order_items.all()
    return {
        'item':  items1.last()
    }
  