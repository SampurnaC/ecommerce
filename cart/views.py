from django.shortcuts import render
from store.models import *
from django.db.models import Count
from django.contrib.auth.decorators import login_required



@login_required(login_url='login/')
def cart(request):
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.order_items.all().order_by('-date_added')
    # items = items.last()
    # items = order.orderitem_set.all()
    # breakpoint()
    # for it in items:
    #     print(it.product.name)
    # dups = order.order_items.values(product.name).annotate(Count('id')).order_by('-date_added').filter(id__count__gt=1)

    context = {'items':items, 'order':order}
    return render(request, 'cart/cart.html', context)
