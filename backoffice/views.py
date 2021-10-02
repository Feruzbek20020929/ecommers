from django.shortcuts import render,redirect
from store.models import Product, Category
from django.views.generic import CreateView
from .forms import *
from django.views.generic.edit import UpdateView,DeleteView
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from orders.models import Order

def home(request):
    return render(request,"home.html")

class Productcreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create/Productadd.html'
    success_url = '/'

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update/productupdate.html'
    success_url = '/'

class ProductDeleteView(DeleteView):
    model = Product
    form_class = ProductForm
    success_url = '/'
    template_name = 'delete/deleteproducts.html'

class ProductList(ListView):
    model = Product
    success_url='/'
    template_name = 'home.html'












class CategoryAddView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = '/'
    template_name='create/category_form.html'


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = '/'
    template_name="update/categoryupdate.html"

class CategoryDeleteView(DeleteView):
    model = Category
    form_class =CategoryForm
    success_url = '/'
    template_name="delete/categorydelete.html"
    

class CategoryList(ListView):
    model = Category
    template_name='categorylist.html'


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    success_url = '/'
    template_name="update/contactupdate.html"

    

class OrderList(ListView):
    model = Order
    template_name='order.html'