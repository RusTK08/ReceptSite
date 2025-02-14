from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest
from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView


# Create your views here.
class AboutMeView(TemplateView):
    template_name = "myauth/about-me.html"
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:about_me")
#     log:sam
#     pas:zzxxccvv11Z

    # user = User.objects.exclude(pk=1)
    # group, created = Group.objects.get_or_create(name='user_group')
    # user.groups.add(group)
    # user.save()
    # group.save()



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
