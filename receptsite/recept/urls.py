from django.urls import path

from recept.views import (recept_index,
                          groups_list,
                          recept_list,
                          create_recept_user,
                          ReceptDetailsView,
                          ReceptUpdateView,
                          ReceptDeleteView)

app_name = "recept"
urlpatterns = [
    path("", recept_index, name="index"),
    path('groups/', groups_list, name="groups_list"),
    path('recepts/', recept_list, name="recept_list"),
    path('recepts/create/', create_recept_user, name="create_recept_user"),
    path('recepts/<int:pk>/', ReceptDetailsView.as_view(), name="recept_details"),
    path('recepts/<int:pk>/update/', ReceptUpdateView.as_view(), name="recept_update"),
    path('recepts/<int:pk>/delete/', ReceptDeleteView.as_view(), name="recept_delete"),

]

