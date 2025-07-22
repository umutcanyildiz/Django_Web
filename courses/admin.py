from django.contrib import admin
from .models import Course,Category
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'isActive', 'slug',) #admin panelinde görüntülenecek alanlar
    list_display_links = ('title',"slug",) #admin panelinde tıklanabilir alanlar
    readonly_fields = ('slug',) #slug alanı sadece okunabilir olacak, admin panelinde düzenlenemeyecek
    list_filter = ('isActive', 'date',) #admin panelinde filtreleme yapılabilecek alanlar
    list_editable = ('isActive',) #admin panelinde düzenlenebilir alanlar
    search_fields = ('title', 'description',) #admin panelinde arama yapılabilecek alanlar

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)



# admin.site.register(Course)  # Course modelini admin paneline kaydeder
# admin.site.register(Category)  # Category modelini admin paneline kaydeder