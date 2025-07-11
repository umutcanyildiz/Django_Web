from django.urls import path  # type: ignore
from . import views  # aynı dizindeki views modülünü içe aktarıyoruz

urlpatterns = [
    path('',views.home),
    path('anasayfa',views.home),
    path('iletisim',views.iletisim),
    path('hakkimizda',views.hakkimizda),
]