from django.shortcuts import render, redirect
from .models import NewUser, Contact
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            messages.success(request, "Account created successfully.")
            return redirect("index")
        messages.error(request, "Please Correct the errors below")
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        messages.error(request, "Invalid username or password")
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("index")

@login_required
def profile_view(request):
    return render(request, "profile.html", {"profile":request.user.profile})




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
