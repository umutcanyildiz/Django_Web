from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50) #null = true demek boş bırakılabilir
    description = models.TextField()
    imageUrl = models.CharField(max_length=200),
    date = models.DateField(),
    isActive = models.BooleanField(default=True)

