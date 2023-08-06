from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=90, db_index=True)
    slug=models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural="categories"

    def __str(self):
        return self.name

# class Customer(models.Model):
#     user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    digital=models.BooleanField(default=False, null=True, blank=True)
    image=models.ImageField(upload_to='uploads/', default='default.jpg')

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=90, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems=self.order_items.all()
        sum=0
        for item in orderitems:
            item_new=item.get_total
            sum=sum+item_new
        return sum
        
class OrderItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order=models.ForeignKey(Order, related_name="order_items", on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        total = self.product.price * self.quantity

        # if self.product.name > str(1):
        #     breakpoint()
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
