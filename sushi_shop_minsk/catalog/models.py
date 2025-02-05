from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=200)
    category = models.CharField(max_length=100)
    stock_quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('available', 'Available'), ('unavailable', 'Unavailable')])

    def __str__(self):
        return self.name
