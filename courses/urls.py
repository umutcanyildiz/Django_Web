from django.urls import path #type: ignore
from . import views #aynı dizindeki views modülünü içe aktarıyoruz
# http://127.0.0.1:8000/client     => anasayfa
# http://127.0.0.1:8000/client/home  => anasayfa

#burdaki home kurslar views dosyasından erişilebilir hale gelir

urlpatterns = [
    path('', views.index), #hiç bişy yazılmazsa anasayfa olarak kabul edilir
    path('<kurs_adi>',views.details),
    path('kategori/<int:category_id>',views.getCoursesByCategoryId),
    path('kategori/<str:category_name>',views.getCoursesByCategory,name="courses_by_category"), #kategori/ adı sabit olarak gelir ve str bir veri geldiğinde bu path ile eşleşir
    
    
    #kategori/ adı sabit olarak gelir ve int bir veri geldiğinde üstteki #path ile eşleşir, str bir veri geldiğinde ise alttaki path ile eşleşir
    
    
    
    # dinamik url, category değişkeni views fonksiyonuna parametre olarak gönderilir
    #ve birde yukardan aşağıya doğru kontrol edilir, eğer yukarıdaki path'ler ile eşleşmezse bu dinamik url'e yönlendirilir
    #yani sırayla kontrol edilir, ilk eşleşen bulunur ve o yönlendirilir
]
