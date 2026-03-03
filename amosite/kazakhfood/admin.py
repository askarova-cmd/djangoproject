from django.contrib import admin
from .models import Category, Dish


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('title', 'description')


from .models import ContactMessage

admin.site.register(ContactMessage)
