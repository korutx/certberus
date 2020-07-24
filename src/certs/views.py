from django.shortcuts import render
from django.http import HttpResponse

from .services import list_certificates
# Create your views here.


def index(request):
    a, b = list_certificates()
    print(a, b)
    return HttpResponse("Hello, world. You're at the polls index.")