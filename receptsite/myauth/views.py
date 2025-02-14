from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest
from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy


# Create your views here.
def login_view(request: HttpRequest):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/admin/')
        return render(request, 'myauth/login.html')
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/admin/")
    return render(request, "myauth/login.html", {"error":"Ошибка авторизации"})
def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse("myauth:login"))
class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")