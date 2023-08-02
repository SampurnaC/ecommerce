from django.shortcuts import render
from .models import *

def products(request):
    products = Product.objects.all()
    context={'products': products}
    return render(request, 'store/products.html', context)

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context={'product': product}
    return render(request, 'store/product_detail.html', context)

def cart(request):
    return render(request, 'store/cart.html')



def order(request):
    return render(request, 'store/order.html')

def checkout(request):
    return render(request, 'store/checkout.html')
