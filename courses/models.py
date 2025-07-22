from django.db import models
from django.utils.text import slugify

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50) #null = true demek boş bırakılabilir
    description = models.TextField()
    imageUrl = models.CharField(max_length=200)
    date = models.DateField()
    isActive = models.BooleanField(default=True)
    slug = models.SlugField(default="",null=False,unique=True,db_index=True) #bunun yerine migrations klasörünü silip tekrar makemigrations ve migrate komutlarını çalıştırabiliriz.
    #editable= False , #bu alanın admin panelinde düzenlenmesini engeller
    #blank=False, #bu alanın formda boş bırakılmasını engeller
    #slug alanı benzersiz olmalı ve boş olmamalı, ayrıca veritabanında indekslenmeli
    #db_index=True, bu alanın veritabanında indekslenmesini sağlar, bu da sorgu performansını artırır.

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # Başlık küçük harfe çevrilir ve boşluklar tireye dönüştürülür
        super().save(*args, **kwargs)

    def __str__(self): #burda 
        return f"{self.title}"
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True) #slug alanı benzersiz olmalı

    def __str__(self): #burda 
        return f"{self.name}"

#You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
#Run 'python manage.py migrate' to apply them -> bu kodu çalıştırdığımızda veritabanında tablolar oluşturulacak.

#kendi migrationlarımızı oluşturmak için
#python manage.py makemigrations -> kodunu çalıştıracağız
#bu kod çalıştırıldığında migrations klasöründe yeni bir dosya oluşturulacak.
#Migration dosyası, veritabanı şemasındaki değişiklikleri takip eder ve bu değişiklikleri uygulamak için kullanılır.
#bu oluşturduğumuz migration dosyası da migration için bekliyor o yüzden 
#python manage.py migrate -> komutunu çalıştıracağız.


#KAYIT EKLEME İÇİN sheel kullanacağız şimdilik:
# python manage.py shell
# from courses.models import Course
# #Kayıt eklemek için
# course = Course(title="Django Kursu", description="Django ile web geliştirme kursu", imageUrl="https://example.com/image.jpg", date="2023-10-01", isActive=True)
# course.save()  # Bu, veritabanına kaydı ekler. ya da
# Course.objects.create(title="Django Kursu", description="Django ile web geliştirme kursu", imageUrl="https://example.com/image.jpg", date="2023-10-01", isActive=True) yazarsak .save() metodunu çağırmadan da kayıt ekleyebiliriz.


#Kayıt sorgulama için:
# from courses.models import Course
# courses = Course.objects.all()  # Tüm kayıtları getirir
# course = Course.objects.get(pk=1)  # ID'si 1 olan kaydı getirir
# print(course.title, course.description, course.date)


#Kayıt Filtreleme için:
# from courses.models import Course
#exclude ise belirtilen koşula uymayan kayıtları getirir.
# courses = Course.objects.filter(isActive=True)  # Sadece aktif kursları getirir
# course = Course.objects.filter(title__icontains="Django")  # Başlığı "Django" içeren kursları getirir
#filter bize liste olarak sonuç döndürür, get ise tek bir kayıt döndürür.
#yani elemana ulaşmak için [0] yazabiliriz.
#Course.objects.filter(date__lte="2023-10-01")  # Tarihi 2023-10-01 veya daha önce olan kursları getirir
#Course.objects.filter(title_contains="Django")  # Başlığı "Django" içeren kursları getirir
#logical operatörler de kullanılabilir:
# Course.objects.filter(isActive=True, date__gte="2023-01-01")  # Aktif ve 2023'ten sonra olan kursları getirir
#or da kullanılabilir:
# from django.db.models import Q
# courses = Course.objects.filter(Q(isActive=True) | Q(date__gte="2023-01-01"))  # Aktif veya 2023'ten sonra olan kursları getirir
#courses = Course.objects.filter(Q(title__contains="kurs") | Q(date__gte="2023-01-01"), isActive=1) #  # Başlığı "kurs" içeren veya 2023'ten sonra olan ve aktif olan kursları getirir


##SLUG-FIELD
#SlugField, genellikle URL'lerde kullanılmak üzere metin alanlarını benzersiz ve okunabilir hale getirmek için kullanılır.
#SlugField, genellikle başlık gibi metin alanlarını URL dostu hale getirmek için kullanılır. Örneğin, "Django Kursu" başlığı "django-kursu" şeklinde bir slug'a dönüştürülebilir.
#shelde kullanarak slug alanını doldurabiliriz:
# from courses.models import Course
#Course.objects.get(pk=1).save()  


#Kayıt güncelleme
# from courses.models import Course
# course = Course.objects.get(pk=1)  # ID'si 1 olan kaydı al
# course.title = "Yeni Başlık"  # Başlığı güncelle
# course.save()  # Değişiklikleri kaydet
#veya çoklu güncelleme yapmak için
# Course.objects.filter(isActive=True).update(isActive=False)  # Aktif olan tüm kursları pasif yapar


#Kayıt Silme
# from courses.models import Course
# course = Course.objects.get(pk=1)  # ID'si 1 olan kaydı al
# course.delete()  # Kaydı sil
#ya da 
# Course.objects.filter(isActive=False).delete()  # Pasif olan tüm kursları siler

#Admin paneli için kullancı ekleme
#python manage.py createsuperuser
#Bu komut çalıştırıldığında kullanıcı adı, e-posta ve şifre istenir

