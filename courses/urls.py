from django.urls import path #type: ignore
from . import views #aynı dizindeki views modülünü içe aktarıyoruz
# http://127.0.0.1:8000/client     => anasayfa
# http://127.0.0.1:8000/client/home  => anasayfa

#burdaki home kurslar views dosyasından erişilebilir hale gelir

urlpatterns = [
    path('', views.kurslar), #hiç bişy yazılmazsa anasayfa olarak kabul edilir
    path('list',views.kurslar),
    path('details',views.details),
    path('<category>',views.getCoursesByCategory) # dinamik url, category değişkeni views fonksiyonuna parametre olarak gönderilir
    #ve birde yukardan aşağıya doğru kontrol edilir, eğer yukarıdaki path'ler ile eşleşmezse bu dinamik url'e yönlendirilir
    #yani sırayla kontrol edilir, ilk eşleşen bulunur ve o yönlendirilir
]
