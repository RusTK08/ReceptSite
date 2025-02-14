from django import forms
from django.contrib.auth.models import User


class ReceptForm(forms.Form):
    name = forms.CharField(max_length=50)
    count_ingredients = forms.CharField(max_length=3)
    ingredients = forms.CharField(widget=forms.Textarea)
    weight_ingredients_gramm = forms.CharField(max_length=3)
    author = forms.CharField(max_length=50)  # User