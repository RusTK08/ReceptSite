from django.contrib.auth.models import User
from django.db import models

# Create your models here.
def recept_preview_directory_path(instance: "Recept", filename: str) -> str:
    return "recepts/recepts_{pk}/preview/{filename}".format(
        pk=instance.pk,
        filename=filename
    )
class Recept(models.Model):
    name = models.CharField(max_length=50)
    count_ingredients = models.CharField(max_length=3, blank=True)
    ingredients = models.TextField(null=False, blank=True)
    weight_ingredients_gramm = models.TextField(null=False, blank=True)
    author = models.TextField() #User
    preview = models.ImageField(null=True, blank=True, upload_to=recept_preview_directory_path)
    def __str__(self):
        return f"Recept(pk={self.pk}, name={self.name!r})"