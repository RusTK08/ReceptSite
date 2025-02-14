from django.urls import path

from recept.views import recept_index, groups_list, recept_list

app_name = "recept"
urlpatterns = [
    path("", recept_index, name="index"),
    path('groups/', groups_list, name="groups_list"),
    path('recepts/', recept_list, name="recept_list"),
]

