from django.shortcuts import render
from .models import Order

# Страница заказов
def orders(request):
    # Получаем все заказы для текущего пользователя
    user_orders = Order.objects.filter(user=request.user)  # Фильтруем заказы по текущему пользователю
    return render(request, 'orders.html', {'orders': user_orders})

