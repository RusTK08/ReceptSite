from django.contrib import admin

from recept.models import Recept

class ReceptAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "count_ingredients", "ingredients", "weight_ingredients_gramm", "author", "preview"

# Register your models here.
admin.site.register(Recept, ReceptAdmin)