from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request):
    return HttpResponse(
        '<h1>Rooms</h1>'
    )
def room_view(request, id):
    return HttpResponse(
        f'<h1>Rooms{id}</h1>'
    )