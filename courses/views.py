from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from datetime import date, datetime
from .models import Course,Category #artık veri tabanındaki verileri kullanarak kurs listeleme sayfasını oluşturacağız.


db = {
    "courses" : [
        {
            "title": "Python Programlama",
            "description": "Python programlama dili ile ilgili kurs",
            "imageUrl": "1.jpeg",
            "slug": "python-programlama",
            "date": datetime.now(),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title": "Django Web Geliştirme",
            "description": "Django web geliştirme çerçevesi ile ilgili kurs",
            "imageUrl": "2.png",
            "slug": "django-web-gelistirme",
            "date": date.today(),
            "isActive": True,
            "isUpdated": True
        },
        {
            "title": "Veritabanı Yönetimi",
            "description": "Veritabanı yönetimi ve SQL ile ilgili kurs",
            "imageUrl": "3.jpg",
            "slug": "veritabani-yonetimi",
            "date": date.today(),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title": "Web Tasarımı",
            "description": "Web tasarımı ve HTML/CSS ile ilgili kurs",
            "imageUrl": "4.jpg",
            "slug": "web-tasarimi",
            "date": date.today(),
            "isActive": True,
            "isUpdated": False
        }
    ],
    "categories": [{"id": 1, "name" : "programlama","slug": "programlama"}, 
                   {"id": 2, "name" : "yazılım","slug": "yazilim"}, 
                   {"id": 3, "name" : "veritabanı","slug": "veritabani"}, 
                   {"id": 4, "name" : "web","slug": "web"}]
}



# http://127.0.0.1:8000/kurslar


def index(request):
    kurslar = Course.objects.all() #Course modelinden tüm kursları alıyoruz
    kategoriler = Category.objects.all() #Category modelinden tüm kategorileri alıyoruz
    return render(request, 'courses/index.html'
                  , {'categories': kategoriler, 'courses': kurslar}) #render ile index.html dosyasını render ediyoruz ve kategorileri ve kursları gönderiyoruz

def details(request,kurs_adi):
    return HttpResponse(f'{kurs_adi} detay sayfası')

def getCoursesByCategory(request, category_name): #dinamik url parametresi
    # category parametresi URL'den alınır ve kullanılır
    try:
        category_text = data[category_name]
        return render(request, 'courses/kurslar.html', {
            'category_name': category_name,
            'category_text': category_text 
            })
    except :
        return HttpResponseNotFound('Kategori bulunamadı')
    
def getCoursesByCategoryId(request, category_id): #dinamik
    try:
        categoriy_list = list(data.keys()) #kategorilerin anahtarlarını listeye al (programlama, yazılım, veritabanı, web)
        category = categoriy_list[category_id-1] #category_id 1'den başladığı için -1 yapıyoruz
        #category_id 1 ise programlama, 2 ise yazılım, 3 ise veritabanı, 4 ise web kategorisine yönlendir
        redirect_url = reverse('courses_by_category', args=[category]) #reverse ile url'yi alıyoruz
        return redirect(redirect_url) #redirect ile yönlendiriyoruz
    except :
        return HttpResponseNotFound('Kategori bulunamadı')