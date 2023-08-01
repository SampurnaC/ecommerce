from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'store/home.html')

def products(request):
    return render(request, 'store/product.html')

def order(request):
    return render(request, 'store/order.html')

def checkout(request):
    return render(request, 'store/checkout.html')
