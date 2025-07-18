from django.urls import path  # type: ignore
from . import views  # aynı dizindeki views modülünü içe aktarıyoruz

urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path('contact',views.contact),
    path('about',views.about),
]