from django.db.models import fields

from django import forms
from store.models import Product, Category
from .models import *
from orders.models import Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


