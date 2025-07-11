from django.urls import path #type: ignore
from . import views #aynı dizindeki views modülünü içe aktarıyoruz
# http://127.0.0.1:8000/client     => anasayfa
# http://127.0.0.1:8000/client/home  => anasayfa

#burdaki home kurslar views dosyasından erişilebilir hale gelir

urlpatterns = [
    path('', views.kurslar), #hiç bişy yazılmazsa anasayfa olarak kabul edilir
    path('list',views.kurslar),
    path('details',views.details),
    path('programlama',views.programlama),
    path('mobil-uygulama',views.mobiluygulamalar),

]
