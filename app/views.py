from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.messages import constants as messages_constant

# Create your views here.
message_levels = {
    "ERROR": messages_constant.ERROR,
}

def index (request):
    if not request.user.is_authenticated:
        return redirect(login)
    return render (request, 'index.html')

def shop (request):
    if not request.user.is_authenticated:
        return redirect(index)
    return render (request, 'shop.html')


def frieren (request):
    return render (request, 'frieren.html')

def naruto1 (request):
    return render (request, 'naruto1.html')

def naruto2 (request):
    return render (request, 'naruto2.html')

def jujutsu1 (request):
    return render (request, 'jujutsu1.html')


def signup (request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required")
            return redirect(signup)
        user_exist = User.objects.filter(username=username).exists()
        if user_exist:
            messages.error(request, "Username already taken")
            return redirect(signup)
        if password != confirm_password:
            messages.error(request, "Password does not match")
            return redirect(signup)
        if len(password) < 8:
            messages.error(request, "Password must have up to 8 characters")
            return redirect(signup)
        user = User.objects.create (username=username, email=email)
        user.set_password(password)
        user.save()
        # messages.success(request, "User created successfully")
        return redirect(login)
    return render (request, 'signup.html')

def login (request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not username or not password:
            messages.error(request, "All fields are required")
            return redirect(login)
        user = auth.authenticate(username=username, password=password)
        if not user:
            messages.error(request, "Invalid Login credentials")
            return redirect(login)
        auth.login(request, user)
        # messages.success(request, "Login successfully")
        return redirect(index)
    return render (request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect(login)

