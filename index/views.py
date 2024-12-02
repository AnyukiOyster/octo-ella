from itertools import product

from django.shortcuts import render
from unicodedata import category

from .models import Category, Product, Cart

# Create your views here.
#Главная страница
def home_page(request):
    #Достаём данные из БД
    products = Product.objects.all
    categories = Category.objects.all
    #Передаём данные фронт-энду
    context = {'products': products, 'categories': categories}

    return render(request, 'home.html', context)
