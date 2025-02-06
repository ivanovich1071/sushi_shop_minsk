from django.shortcuts import render

# Страница профиля пользователя
def profile(request):
    # Здесь можно добавить логику получения данных пользователя
    # Например, если у пользователя уже есть профиль в базе данных,
    # можно передать эти данные в шаблон
    return render(request, 'profile.html')
