from django.shortcuts import render
from .models import Product

# Главная страница
def home(request):
    products = Product.objects.all()  # Получаем все товары
    return render(request, 'home.html', {'products': products})

# Страница каталога товаров
def catalog(request):
    products = Product.objects.all()  # Получаем все товары
    return render(request, 'catalog.html', {'products': products})
