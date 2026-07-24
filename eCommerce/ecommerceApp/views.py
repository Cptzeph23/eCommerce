from urllib import request

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def chefs(request):
    return render(request, 'chefs.html')

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')

def orders(request):
    return render(request, 'orders.html')

def reservation(request):
    return render(request, 'reservation.html')

def reviews(request):
    return render(request, 'about.html')

def starter_page(request):
    return render(request, 'starter-page.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')


