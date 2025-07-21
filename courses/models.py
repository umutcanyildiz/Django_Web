from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50) #null = true demek boş bırakılabilir
    description = models.TextField()
    imageUrl = models.CharField(max_length=200),
    date = models.DateField(),
    isActive = models.BooleanField(default=True)

#You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
#Run 'python manage.py migrate' to apply them -> bu kodu çalıştırdığımızda veritabanında tablolar oluşturulacak.

#kendi migrationlarımızı oluşturmak için
#python manage.py makemigrations -> kodunu çalıştıracağız
#bu kod çalıştırıldığında migrations klasöründe yeni bir dosya oluşturulacak.
#Migration dosyası, veritabanı şemasındaki değişiklikleri takip eder ve bu değişiklikleri uygulamak için kullanılır.
#bu oluşturduğumuz migration dosyası da migration için bekliyor o yüzden 
#python manage.py migrate -> komutunu çalıştıracağız.