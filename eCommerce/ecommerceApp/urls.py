
from django.contrib import admin
from django.urls import path
from ecommerceApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name = 'about'),
    path('chefs/', views.chefs, name='chefs'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name = 'menu'),
    path('orders/', views.orders, name='orders'),
    path('reservation/', views.reservation, name='reservation'),
    path('reviews/', views.reviews, name='reviews'),
    path('starter-page/', views.starter_page, name='starter_page')
]
