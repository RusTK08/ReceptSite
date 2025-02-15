from django import forms
from django.contrib.auth.models import User

from recept.models import recept_preview_directory_path


class ReceptForm(forms.Form):
    name = forms.CharField(max_length=50)
    count_ingredients = forms.CharField(max_length=3)
    ingredients = forms.CharField(widget=forms.Textarea)
    weight_ingredients_gramm = forms.CharField(widget=forms.Textarea)
    author = forms.CharField(max_length=50)  # User
    preview = forms.ImageField()