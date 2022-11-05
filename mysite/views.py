from .forms import InputForm
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    context['form'] = InputForm()
    return render(request, "index.html", context)


def from_submit(request):
    return render(request, "from_submit.html")
