from django.shortcuts import render
from .models import Category, Product, Cart

#Главная страница
def home_page(request):
    #Достаём данные из БД
    products = Product.objects.all
    categories = Category.objects.all
    #Передаём данные фронт-энду
    context = {'products': products, 'categories': categories}

    return render(request, 'home.html', context)

#Вывод товаров по выбранной категории
def category_page(request, pk):
    #выводим нужную категорию
    category = Category.objects.get(id=pk)
    #Фильтруем товары по категории
    products = Product.objects.filter(product_category=category)
    #Передаём данные на FE
    context = {'category': category, 'products': products}

    return render(request, 'category.html', context)

#Вывод определённого товара
def product_page(request,pk):
    #Вывод выбранного товара
    product = Product.objects.get(id=pk)
    # Передаём данные на FE
    context = {'product': product}

    return render(request, 'product.html', context)