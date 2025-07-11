
from django.contrib import admin
from django.urls import path, include # include fonksiyonunu ekliyoruz böylece uygulamaların urls.py dosyalarını kullanabileceğiz


urlpatterns = [
    path('kurs/', include('courses.urls')), # courses uygulamasının urls.py dosyasını dahil ediyoruz
    path('', include('pages.urls')), # pages uygulamasının urls.py dosyasını dahil ediyoruz
    path('admin/', admin.site.urls)
]
# Bu kod, Django projesinin URL yönlendirmelerini tanımlar. 'kurs/' ile başlayan URL'ler courses uygulamasına yönlendirilirken, anasayfa ve diğer sayfalar pages uygulamasına yönlendirilir. Admin paneli ise 'admin/' ile erişilebilir. 

#Django_Kursu
#courses
#pages
