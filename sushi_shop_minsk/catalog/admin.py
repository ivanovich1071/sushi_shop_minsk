from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock_quantity', 'status', 'date_added')
    list_filter = ('category', 'status')
    search_fields = ('name', 'description')
    ordering = ('-date_added',)
    list_per_page = 20

admin.site.register(Product, ProductAdmin)
