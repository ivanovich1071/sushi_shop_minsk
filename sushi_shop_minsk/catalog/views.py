# catalog/views.py
from django.shortcuts import render

# Представление для главной страницы
def home(request):
    return render(request, 'home.html')
