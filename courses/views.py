from django.shortcuts import render
from django.http import HttpResponse



def kurslar(request):
    return HttpResponse('kurslar')

def details(request,kurs_adi):
    return HttpResponse(f'{kurs_adi} detay sayfası')

def getCoursesByCategory(request, category_name): #dinamik url parametresi
    # category parametresi URL'den alınır ve kullanılır
    return HttpResponse(f'{category_name} kategorisindeki kurslar listesi')

def getCoursesByCategoryId(request, category_id): #dinamik
    return HttpResponse(category_id)