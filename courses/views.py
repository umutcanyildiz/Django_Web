from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request): #istege karsi bir de response donduruyoruz
    return HttpResponse('anasayfa')

def kurslar(request):
    return HttpResponse('kurslar')