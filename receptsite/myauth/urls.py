from django.contrib.auth.views import LoginView
from django.urls import path

from myauth.views import login_view, logout_view, MyLogoutView

app_name = "myauth"
urlpatterns = [
    # path('login/',
    #      LoginView.as_view(template_name="myauth:login.html", redirect_authenticated_user=True),
    #      name="login"),
        path('login/',login_view, name="login"),
        path('logout/', logout_view, name="logout"),
    #     path('logout/', MyLogoutView.as_view(), name="logout"),
        ]