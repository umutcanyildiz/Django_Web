from django.shortcuts import render
from django.http import HttpResponse



def kurslar(request):
    return HttpResponse('kurslar')

def details(request):
    return HttpResponse('kurs detay sayfası')

def getCoursesByCategory(request, category): #dinamik url parametresi
    # category parametresi URL'den alınır ve kullanılır
    return HttpResponse(f'{category} kategorisindeki kurslar listesi')