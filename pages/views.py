from django.shortcuts import render
from django.http import HttpResponse

def index(request): #istege karsi bir de response donduruyoruz
    return render(request,"pages/index.html") #html sayfası döndürür (templates klasöründeki index.html dosyasını render eder)

def contact(request):
    return render(request,"pages/contact.html") #html sayfası döndürür (templates klasöründeki contact.html dosyasını render eder)

def about(request):
    return render(request,"pages/about.html") #html sayfası döndürür (templates klasöründeki about.html dosyasını render eder)