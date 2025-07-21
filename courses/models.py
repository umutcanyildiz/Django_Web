from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50) #null = true demek boş bırakılabilir
    description = models.TextField()
    imageUrl = models.CharField(max_length=200)
    date = models.DateField()
    isActive = models.BooleanField(default=True)

    def __str__(self): #burda 
        return f"{self.title} - {self.date} - {self.isActive}"
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True) #slug alanı benzersiz olmalı



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