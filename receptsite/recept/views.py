from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from recept.forms import ReceptForm
from recept.models import Recept



# Create your views here.

def recept_index(request: HttpRequest) -> HttpResponse:
    return render(request,'recept/recept-index.html')
def groups_list(request: HttpRequest) -> HttpResponse:
    context = {
        "groups": Group.objects.all(),
    }
    return render(request, 'recept/groups-list.html', context=context)

def recept_list(request: HttpRequest) -> HttpResponse:
    context = {
    "recepts": Recept.objects.all(),
    }
    return render(request, 'recept/recept-list.html', context=context)
@login_required
def create_recept_user(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ReceptForm(request.POST)
        if form.is_valid():
            Recept.objects.create(**form.cleaned_data)
            # url = reverse("recept:create_recept_user")
            # return redirect(url)

    else:
        form = ReceptForm() # or this block Recept.objects.create(**form.cleaned_data)
        context = {
            "form": form,
        }
    return render(request, "recept/create-user-recept.html", context=context)
class ReceptDetailsView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, pk:int):
        receptfind = Recept.objects.get(pk=pk)
        context = {
            "receptfind": receptfind,
        }
        return render(request,'recept/recept-details.html', context=context)
class ReceptUpdateView(LoginRequiredMixin, UpdateView):
    model = Recept
    fields = "name", "count_ingredients", "ingredients", "weight_ingredients_gramm", "author"
    template_name_suffix = "-update-form"
    def get_success_url(self):
        return reverse(
            "recept:recept_details",
            kwargs={
                "pk": self.object.pk
                    },
        )
class ReceptDeleteView(LoginRequiredMixin, DeleteView):
    model = Recept
    success_url = reverse_lazy("recept:recept_list")