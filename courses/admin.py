from django.contrib import admin
from .models import Course,Category
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'isActive', 'slug',"category",) #admin panelinde görüntülenecek alanlar
    list_display_links = ('title',"slug",) #admin panelinde tıklanabilir alanlar
    prepopulated_fields = {'slug': ('title',),} #slug alanı title alanına göre otomatik doldurulacak
    #readonly_fields = ('slug',) #slug alanı sadece okunabilir olacak, admin panelinde düzenlenemeyecek
    list_filter = ('isActive', 'date',"category",) #admin panelinde filtreleme yapılabilecek alanlar
    list_editable = ('isActive',) #admin panelinde düzenlenebilir alanlar
    search_fields = ('title', 'description',) #admin panelinde arama yapılabilecek alanlar

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    list_display_links = ('name',"slug",) #admin panelinde tıklanabilir alanlar
    prepopulated_fields = {'slug': ('name',),} #slug alanı name alanına göre otomatik doldurulacak



# admin.site.register(Course)  # Course modelini admin paneline kaydeder
# admin.site.register(Category)  # Category modelini admin paneline kaydeder