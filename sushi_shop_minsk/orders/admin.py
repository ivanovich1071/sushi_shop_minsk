from django.contrib import admin
from .models import Order, OrderItem

# Модель для отображения позиций заказа в админке
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Количество пустых строк для добавления новых позиций

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_amount', 'order_date', 'updated_at')  # Отображаемые поля
    list_filter = ('status', 'user')  # Фильтрация по статусу и пользователю
    search_fields = ('id', 'user__username')  # Поиск по ID заказа и имени пользователя
    inlines = [OrderItemInline]  # Встраиваем инлайн для позиций заказа

    # Настройка полей для редактирования
    fieldsets = (
        (None, {
            'fields': ('user', 'status', 'total_amount')
        }),
        ('Dates', {
            'fields': ('order_date', 'updated_at')
        }),
    )

    # Сортировка по дате заказа (order_date)
    ordering = ('-order_date',)

# Регистрируем модели в админке
admin.site.register(Order, OrderAdmin)
