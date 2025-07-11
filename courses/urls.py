from django.urls import path
from . import views #aynı dizindeki views modülünü içe aktarıyoruz
# http://127.0.0.1:8000/client     => anasayfa
# http://127.0.0.1:8000/client/home  => anasayfa

#burdaki home kurslar views dosyasından erişilebilir hale gelir

urlpatterns = [
    path('',views.home),
    path('anasayfa',views.home),
    path('kurslar',views.kurslar)
]
