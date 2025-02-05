from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Регистрируем модель User в админке
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active')

    # Настроим поля для редактирования в админке
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone', 'address', 'telegram_id')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')}
         ),
    )

    # Задаем порядок сортировки
    ordering = ('username',)


# Регистрируем нашего кастомного пользователя в админке
admin.site.register(User, CustomUserAdmin)
