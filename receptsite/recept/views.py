from django.contrib.auth.models import Group
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

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