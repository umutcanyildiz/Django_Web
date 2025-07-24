from django.contrib import admin
from .models import Course,Category
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'isActive', 'slug',"category_list") #admin panelinde görüntülenecek alanlar
    list_display_links = ('title',"slug",) #admin panelinde tıklanabilir alanlar
    prepopulated_fields = {'slug': ('title',),} #slug alanı title alanına göre otomatik doldurulacak
    #readonly_fields = ('slug',) #slug alanı sadece okunabilir olacak, admin panelinde düzenlenemeyecek
    list_filter = ('isActive', 'date',) #admin panelinde filtreleme yapılabilecek alanlar
    list_editable = ('isActive',) #admin panelinde düzenlenebilir alanlar
    search_fields = ('title', 'description',) #admin panelinde arama yapılabilecek alanlar

    def category_list(self, obj):
        html  = ""
        for category in obj.categories.all():
            html += category.name + ", "
        return html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',"course_count")
    list_display_links = ('name',"slug",) #admin panelinde tıklanabilir alanlar
    prepopulated_fields = {'slug': ('name',),} #slug alanı name alanına göre otomatik doldurulacak
    
    def course_count(self, obj):
        return obj.course_set.count()
    course_count.short_description = 'Kurs Sayısı'


# admin.site.register(Course)  # Course modelini admin paneline kaydeder
# admin.site.register(Category)  # Category modelini admin paneline kaydeder