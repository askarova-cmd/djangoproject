from django.contrib import admin
from .models import Dish, Category, ContactMessage, BlogPost, BlogImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('title', 'description')

class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')
    inlines = [BlogImageInline]  # подключаем возможность добавлять несколько изображений

from .models import ContactMessage

admin.site.register(ContactMessage)
