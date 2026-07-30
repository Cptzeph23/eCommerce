from django.shortcuts import render, redirect
from .models import NewUser, Contact

# Create your views here.

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if NewUser.objects.filter(email=email, password=password).exists():
            request.session['logged_in'] = True
            request.session['user_email'] = email
            return redirect('index')

        return redirect('login')
    if request.session.get('logged_in'):
        return render(request, 'index.html')

    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def chefs(request):
    return render(request, 'chefs.html')

def contact(request):
    if request.method == 'POST':
        message = Contact(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        message.save()
        return redirect('/contact/')
    else:
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
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if NewUser.objects.filter(email=email, password=password).exists():
            request.session['logged_in'] = True
            request.session['user_email'] = email
            return redirect('index')

        return redirect('login')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        users = NewUser(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )
        users.save()
        return redirect('/')
    else:
        return render(request, 'register.html')
