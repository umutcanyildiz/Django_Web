from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

data = {
    "progralamlama": "programlama kategorisindeki kurslar",
    "yazilim": "yazılım kategorisindeki kurslar",
    "veritabani": "veritabanı kategorisindeki kurslar",
    "web": "web kategorisindeki kurslar"
}


def kurslar(request):
    return HttpResponse('kurslar')

def details(request,kurs_adi):
    return HttpResponse(f'{kurs_adi} detay sayfası')

def getCoursesByCategory(request, category_name): #dinamik url parametresi
    # category parametresi URL'den alınır ve kullanılır
    try:
        courses = data[category_name]
        return HttpResponse(f'{category_name} kategorisindeki kurslar listesi')
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