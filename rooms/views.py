from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request):
    return HttpResponse(
        '<h1>Rooms</h1>'
    )