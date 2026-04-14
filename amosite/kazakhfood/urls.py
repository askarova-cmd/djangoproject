from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('contacts/', views.contacts, name='contacts'),
    path('reserve/', views.reserve, name='reserve'),
    path('category/<slug:category_slug>/', views.menu, name='menu_by_category'),
    path('dish/<int:pk>/', views.dish_detail, name='dish_detail'),
    path('delivery/', views.delivery, name='delivery'),
    path('', views.home_ru, name='home_ru'),
    path('kk/', views.home_kk, name='home_kk'),
    path('en/', views.home_en, name='home_en'),
]




