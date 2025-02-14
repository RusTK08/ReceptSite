from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Recept(models.Model):
    name = models.CharField(max_length=50)
    count_ingredients = models.CharField(max_length=3, blank=True)
    ingredients = models.TextField(null=False, blank=True)
    weight_ingredients_gramm = models.CharField(max_length=3, blank=True)
    author = models.TextField() #User