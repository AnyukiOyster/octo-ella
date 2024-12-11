from django.shortcuts import render, redirect
from .models import Category, Product, Cart
from .forms import RegForm
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


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

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form': RegForm}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegForm(request.POST)

        #Проверка корректности данных
        if form.is_valid():
            username = form.clean_username()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            #Авторизация пользователя
            login(request, user)
            return redirect('/')

        # Если данные некорректны
        context = {'form': RegForm, 'message': 'Неверный адрес электронной почты или пароль'}
        return render(request, self.template_name, context)

def search(request):
    if request.method == 'POST':
        get_product = request.POST.get('search')

        if Product.objects.get(product_name__iregex=get_product):
            search_product = Product.objects.get(product_name__iregex=get_product)
            return redirect(f'/product/{search_product.id}')
        else:
            return redirect('/')