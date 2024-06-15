from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)


class contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, related_name='contacts', on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    postaladress = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.first_name
    