from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    telegram_id = models.CharField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=255)  # Django автоматически хеширует пароль

    # Указываем related_name для групп и прав доступа, чтобы избежать конфликта с моделью User из auth
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # измените название на нужное
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user_groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # измените название на нужное
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user_permissions',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
