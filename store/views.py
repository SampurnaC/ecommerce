from django.shortcuts import render, redirect
from .models import *
from cart.forms import OrderForm
from store.forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login/')
def products(request):
    products = Product.objects.all()
    context={'products': products}
    return render(request, 'store/products.html', context)

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    customer = request.user
    order = Order.objects.get(customer=customer)

    # items = order.order_items.all()
    # context={'product': product, 'order': order, 'items': items}
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            orderitem=form.save()
            # product = Product.objects.get(id=pk)
            orderitem.product=product
            product_name=orderitem.product.name

            # customer = request.user.customer
            # order=Order.objects.get(customer=customer)

            orderitem.order=order
            order1=order

            orderitem.save()
            return redirect('cart:cart')
    else:
        form=OrderForm()
    name=OrderItem.objects.filter(product=product)
    context={'product': product, 'form': form, 'name': name, 'customer': customer, 'order': order}

    return render(request, 'store/product_detail.html', context)

def delete_order_item(request, id):
    product = Product.objects.get(id=id)
    customer = request.user
    orderitem=OrderItem.objects.filter(product=product)
    orderitem.delete()
    return redirect('cart:cart')

def order(request):
    return render(request, 'store/order.html')

def checkout(request):
    return render(request, 'store/checkout.html')

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'store/register.html', {
        'form': form
    })
