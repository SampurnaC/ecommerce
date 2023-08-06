from django import forms
from store.models import Order, OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model=OrderItem
        fields=['quantity']

