from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import ProjectModel


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')

        return render(request, 'register.html', {'error': 'Passwords do not match.'})

    return render(request, 'register.html')


def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        dept = request.POST.get('dept')
        image = request.FILES.get('image')

        ProjectModel.objects.create(
            user_name=name,
            password=phone,
            created_by=request.user,
        )

        return redirect('home')

    return render(request, 'home.html')


def dashboard(request):
    return render(request, 'dashboard.html')

    