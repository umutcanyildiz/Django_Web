from django.shortcuts import render
from django.http import HttpResponse

def home(request): #istege karsi bir de response donduruyoruz
    return HttpResponse('anasayfa')

def iletisim(request):
    return HttpResponse('iletişim sayfası')

def hakkimizda(request):
    return HttpResponse('hakkımızda sayfası')